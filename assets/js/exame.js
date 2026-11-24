/* Simulador do examshell, sem tempo limite.
   Fluxo como na 42: login -> exercício do level 0 -> escrever o ficheiro -> git add / commit / push
   -> grademe (verificações automáticas + testes que corres no teu terminal) -> SUCCESS sobe de level,
   FAILURE dá outro exercício do mesmo level. O estado fica no localStorage (chave <store>:exam). */
(function () {
  "use strict";
  var app = document.querySelector("[data-exam-app]");
  if (!app || !window.P42 || !window.P42.makeShell) return;
  var P42 = window.P42, store = P42.store;
  var DATA = {};
  try { DATA = JSON.parse(document.getElementById("exam-data").textContent); } catch (e) { return; }
  var EXAMS = DATA.exams, LEVELS = DATA.levels;

  function $(s) { return app.querySelector(s); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function pad(n) { return ("0" + n).slice(-2); }
  function clock(ms) { var s = Math.max(0, Math.floor(ms / 1000)); return pad(Math.floor(s / 3600)) + ":" + pad(Math.floor(s / 60) % 60) + ":" + pad(s % 60); }
  function dur(ms) { var m = Math.round(ms / 60000); return m >= 60 ? Math.floor(m / 60) + " h " + pad(m % 60) + " min" : m + " min"; }

  var setup = $("[data-setup]"), runEl = $("[data-xrun]"), endEl = $("[data-end]"), gradeEl = $("[data-x-grade]");
  var state = store.get("exam", null);
  if (state && !state.git) state = null; /* estado de uma versão antiga do simulador */
  var timer = null;

  function save() { store.set("exam", state); }
  function examById(id) { return EXAMS.filter(function (x) { return x.id === id; })[0] || EXAMS[0]; }
  function cur() { return (LEVELS[String(state.cur.level)] || []).filter(function (e) { return e.nome === state.cur.nome; })[0]; }
  function fileName(e) { var f = e.ficheiros.split(",")[0].trim(); return f.indexOf("*") >= 0 ? e.nome + ".c" : f; }
  function path() { var e = cur(); return e.nome + "/" + fileName(e); }

  var sh = P42.makeShell(app, function () { return (state ? state.login : "piscine") + "@examshell:~/rendu$"; }, command);

  function pick(level) {
    var pool = LEVELS[String(level)] || [];
    var seen = state.seen[level] || [];
    var fresh = pool.filter(function (e) { return seen.indexOf(e.nome) < 0; });
    if (!fresh.length) fresh = pool.filter(function (e) { return !state.cur || e.nome !== state.cur.nome; });
    if (!fresh.length) fresh = pool;
    var e = fresh[Math.floor(Math.random() * fresh.length)];
    state.seen[level] = seen.concat([e.nome]);
    state.cur = { level: level, nome: e.nome, try: (state.tries[level] || 0) + 1 };
    state.code = "";
    state.git = { staged: {}, commits: [], pushed: null };
    state.phase = "work";
    save();
  }

  function show(which) {
    setup.hidden = which !== "setup";
    runEl.hidden = which !== "run";
    endEl.hidden = which !== "end";
    document.body.classList.toggle("in-exam", which === "run");
  }

  function announce() {
    var e = cur();
    sh.print('<span class="ok">assignment:</span> <b>' + esc(e.nome) + "</b> (level " + state.cur.level + ", tentativa " + state.cur.try + ")\n" +
      "enunciado: subjects/" + esc(e.nome) + "/subject.pt.txt\n" +
      "entrega:   ~/rendu/" + esc(path()) + "\n" +
      '<span class="mute">escreve o ficheiro, testa-o no teu terminal e entrega: git add . ; git commit -m "…" ; git push ; grademe</span>');
  }

  function renderRun() {
    var x = examById(state.id), e = cur();
    if (!e) { finish("erro"); return; }
    $("[data-x-name]").textContent = x.nome;
    $("[data-x-level]").textContent = state.cur.level + " / " + state.max;
    $("[data-x-done]").textContent = state.passed.length;
    $("[data-x-subject]").textContent = "subjects/" + e.nome + "/subject.pt.txt";
    $("[data-x-try]").textContent = "tentativa " + state.cur.try;
    $("[data-x-lvtag]").textContent = "level " + state.cur.level;
    $("[data-x-title]").textContent = e.nome;
    $("[data-x-files]").innerHTML = e.ficheiros.split(",").map(function (f) { return "<code>" + esc(f.trim()) + "</code>"; }).join(", ");
    $("[data-x-funcs]").innerHTML = e.funcoes ? e.funcoes.split(",").map(function (f) { return "<code>" + esc(f.trim()) + "</code>"; }).join(", ") : "Nenhuma";
    $("[data-x-type]").textContent = e.tipo;
    $("[data-x-text]").innerHTML = e.texto;
    $("[data-x-proto]").innerHTML = e.proto || "";
    $("[data-x-example]").innerHTML = e.exemplo || "";
    $("[data-x-file]").textContent = "~/rendu/" + path();
    $("[data-x-code]").value = state.code || "";
    $("[data-x-saved]").textContent = "";
    $("[data-x-prompt]").textContent = state.login + "@examshell:~/rendu$";
    renderGrade();
    tick();
  }

  function renderGrade() {
    var e = cur();
    gradeEl.hidden = state.phase !== "grading";
    if (state.phase === "grading") {
      $("[data-x-tests]").innerHTML = e.tests.map(function (t) { return "<li>" + t + "</li>"; }).join("");
    }
  }

  function tick() {
    if (!state || state.status !== "running") return;
    $("[data-x-time]").textContent = clock(Date.now() - state.start);
  }

  function begin() {
    var sel = app.querySelector('input[name="exam"]:checked');
    var x = examById(sel ? sel.value : EXAMS[0].id);
    var login = ($("[data-login]").value || "piscine").replace(/[^a-z0-9_-]/gi, "").toLowerCase() || "piscine";
    state = { id: x.id, login: login, status: "running", start: Date.now(), max: x.max_nivel,
              seen: {}, tries: {}, passed: [], trail: [], cur: null, code: "", git: null, phase: "work" };
    pick(0);
    show("run");
    sh.clear();
    sh.print("examshell: sessão aberta para <b>" + esc(login) + "</b> · " + esc(x.nome) + " · sem limite de tempo\nescreve <b>help</b> para ver os comandos.");
    announce();
    renderRun();
    window.clearInterval(timer);
    timer = window.setInterval(tick, 1000);
    window.scrollTo({ top: app.getBoundingClientRect().top + window.pageYOffset - 80 });
  }

  function nextAfter(ok) {
    var c = state.cur, e = cur();
    state.trail.push({ level: c.level, nome: c.nome, ok: ok, at: Date.now() - state.start });
    if (ok) {
      sh.print(">>>>>>>>>> SUCCESS <<<<<<<<<<\n" + esc(e.nome) + " aprovado. A subir de level.", "ok");
      if (state.passed.indexOf(c.level) < 0) state.passed.push(c.level);
      if (c.level >= state.max) { finish("fim"); return; }
      pick(c.level + 1);
    } else {
      sh.print(">>>>>>>>>> FAILURE <<<<<<<<<<\nNovo exercício do mesmo level.", "ko");
      state.tries[c.level] = (state.tries[c.level] || 0) + 1;
      pick(c.level);
    }
    announce();
    renderRun();
    window.scrollTo({ top: app.getBoundingClientRect().top + window.pageYOffset - 80 });
  }

  function grademe() {
    var e = cur(), p = path();
    if (state.phase === "grading") { sh.print("A correção já está a decorrer: responde aos testes em baixo."); gradeEl.scrollIntoView({ behavior: "smooth" }); return; }
    if (!state.git.pushed || state.git.pushed.snap[p] === undefined) {
      sh.print("grademe: nada para corrigir em rendu/" + esc(e.nome) + "/. Fizeste git add, git commit e git push?", "ko");
      return;
    }
    var code = state.git.pushed.snap[p];
    state.code = $("[data-x-code]").value;
    if (state.code !== code) sh.print("atenção: há alterações que não entregaste. Vou corrigir o último push.", "ko");
    sh.print("=> a corrigir " + esc(e.nome) + " (commit " + state.git.pushed.id + ")…");
    var r = P42.checkSubmission(code, e.spec, { norm: false });
    if (!r.ok) {
      sh.print(r.errs.map(function (x) { return "   " + esc(x); }).join("\n"), "ko");
      nextAfter(false);
      return;
    }
    sh.print("   verificações automáticas: OK\n   faltam os testes de execução: vê em baixo.", "ok");
    state.phase = "grading";
    save();
    renderGrade();
    gradeEl.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function command(line) {
    var w = line.split(/\s+/)[0];
    if (!line) return;
    if (state.status !== "running") { sh.print("O exame terminou.", "ko"); return; }
    if (w === "help") {
      sh.print("status              exercício, level, tentativa e tempo\nsubject             mostra o enunciado\ngit status          o que mudou desde o último push\ngit add .           prepara o ficheiro\ngit commit -m \"…\"   regista\ngit push            entrega\ngit log             commits\ngrademe             pede a correção\nfinish              termina o exame\nclear               limpa o terminal");
    } else if (w === "status") {
      sh.print("exercício: " + esc(state.cur.nome) + " · level " + state.cur.level + "/" + state.max + " · tentativa " + state.cur.try +
        "\nníveis feitos: " + state.passed.length + " · tempo: " + clock(Date.now() - state.start) + " (sem limite)" +
        "\nrepositório: " + (state.git.pushed ? "último push " + state.git.pushed.id : "ainda sem push"));
    } else if (w === "subject" || w === "cat") {
      $("[data-x-title]").scrollIntoView({ behavior: "smooth", block: "center" });
    } else if (w === "git") {
      var files = {};
      state.code = $("[data-x-code]").value;
      files[path()] = state.code;
      P42.gitCmd(line, state.git, files, sh, "exam-" + state.login + "/rendu");
      save();
    } else if (w === "grademe") {
      grademe();
    } else if (w === "finish" || w === "exit") {
      finish("parou");
    } else if (w === "clear") {
      sh.clear();
    } else if (w === "ls") {
      sh.print(esc(cur().nome) + "/\n  " + esc(fileName(cur())) + (state.code ? "" : " (vazio)"));
    } else {
      sh.print(esc(w) + ": comando não encontrado. Escreve help.", "ko");
    }
  }

  function finish(why) {
    window.clearInterval(timer);
    if (!state) return;
    state.status = "ended";
    state.why = why;
    state.used = Date.now() - state.start;
    var x = examById(state.id);
    var hist = store.get("exam-hist", []) || [];
    hist.unshift({ nome: x.nome, quando: Date.now(), feitos: state.passed.length, total: state.max + 1, usado: state.used });
    store.set("exam-hist", hist.slice(0, 30));
    save();
    renderEnd();
  }

  function renderEnd() {
    var x = examById(state.id), total = state.max + 1, done = state.passed.length;
    $("[data-end-title]").textContent = state.why === "fim" ? "Todos os levels feitos" : "Exame terminado";
    $("[data-end-text]").innerHTML = "<p><b>" + esc(x.nome) + "</b>: " + done + " de " + total + " levels feitos em " + dur(state.used || 0) + ".</p>" +
      '<p class="muted">A nota oficial do examshell não está nas fontes usadas, por isso aqui contam os levels. Na Piscine este exame teria ' + (x.duracao / 60) + " horas. Revê depois, na área de respostas, as soluções dos exercícios que te saíram.</p>";
    $("[data-end-list]").innerHTML = state.trail.length ? state.trail.map(function (t) {
      return '<li><span class="' + (t.ok ? "ok" : "ko") + '">' + (t.ok ? "✓ SUCCESS" : "✗ FAILURE") + "</span><b>level " + t.level + "</b> " + esc(t.nome) + ' <span class="mute">aos ' + dur(t.at) + "</span></li>";
    }).join("") : '<li class="mute">Nenhum exercício corrigido.</li>';
    show("end");
    renderHist();
  }

  function renderHist() {
    var hist = store.get("exam-hist", []) || [];
    if (!hist.length) return;
    $("[data-hist]").innerHTML = hist.map(function (h) {
      var d = new Date(h.quando);
      return "<li><b>" + esc(h.nome) + "</b><span>" + h.feitos + "/" + h.total + " levels</span><span class=\"mute\">" + dur(h.usado || 0) + "</span><span class=\"mute\">" + d.toLocaleDateString("pt-PT") + " " + pad(d.getHours()) + ":" + pad(d.getMinutes()) + "</span></li>";
    }).join("");
  }

  /* botões */
  $("[data-begin]").addEventListener("click", begin);
  app.querySelectorAll("[data-xs]").forEach(function (b) { b.addEventListener("click", function () { sh.run(b.getAttribute("data-xs")); }); });
  $("[data-x-pass]").addEventListener("click", function () { if (state && state.phase === "grading") { sh.print("testes de execução: todos passam."); nextAfter(true); } });
  $("[data-x-fail]").addEventListener("click", function () { if (state && state.phase === "grading") { sh.print("testes de execução: pelo menos um falha.", "ko"); nextAfter(false); } });
  var stop = $("[data-x-stop]"), armed = null;
  stop.addEventListener("click", function () {
    if (!armed) {
      stop.textContent = "confirmar: terminar agora";
      armed = window.setTimeout(function () { stop.textContent = "terminar exame"; armed = null; }, 3500);
      return;
    }
    window.clearTimeout(armed); armed = null; stop.textContent = "terminar exame";
    finish("parou");
  });
  $("[data-again]").addEventListener("click", function () { state = null; store.del("exam"); show("setup"); });

  var ta = $("[data-x-code]"), t = null;
  P42.bindEditor(ta, function () {
    window.clearTimeout(t);
    t = window.setTimeout(function () {
      if (!state) return;
      state.code = ta.value; save();
      $("[data-x-saved]").textContent = "guardado (por entregar)";
    }, 400);
  });

  /* arranque */
  renderHist();
  if (state && state.status === "running" && state.cur && cur()) {
    show("run");
    sh.print("examshell: sessão retomada para <b>" + esc(state.login) + "</b>.");
    announce();
    renderRun();
    timer = window.setInterval(tick, 1000);
  } else if (state && state.status === "ended") {
    renderEnd();
  } else {
    show("setup");
  }
})();
