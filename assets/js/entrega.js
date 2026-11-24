/* Entrega como na 42: git add / commit / push, moulinette e avaliação.
   - P42.checkSubmission(código, spec): verificações automáticas (como a moulinette, sem compilar):
     ficheiro entregue, main só quando é pedida, nomes das funções, funções proibidas e Norma.
   - Página de módulo: inscrição, repositório simulado, moulinette (por ordem, pára no primeiro KO)
     e folha de avaliação. Sem prazos.
   Tudo fica no localStorage, com try/catch (o site funciona sem ele). */
(function () {
  "use strict";
  if (!window.P42) return;
  var P42 = window.P42, store = P42.store;

  /* ------------------------------------------------------------ verificação estática */
  var KW = { "if": 1, "while": 1, "for": 1, "return": 1, "sizeof": 1, "switch": 1, "else": 1, "do": 1, "int": 1, "char": 1,
    "void": 1, "long": 1, "short": 1, "unsigned": 1, "signed": 1, "float": 1, "double": 1, "struct": 1, "const": 1,
    "static": 1, "defined": 1, "size_t": 1, "ssize_t": 1, "main": 1, "case": 1, "goto": 1, "typedef": 1, "union": 1, "enum": 1 };

  function strip(code) {
    /* uma só passagem: assim um "/*" dentro de uma string não abre um comentário */
    return code.replace(/\/\*[\s\S]*?\*\/|\/\/[^\n]*|"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])+'/g, function (m) {
      if (m.charAt(0) === '"') return '""';
      if (m.charAt(0) === "'") return "''";
      return m.charAt(1) === "*" ? m.replace(/[^\n]/g, " ") : " ";
    });
  }
  function definedNames(s) {
    var set = {}, m;
    var re = /\b([A-Za-z_]\w*)\s*\(([^;{}]*)\)\s*\{/g;
    while ((m = re.exec(s))) set[m[1]] = 1;
    var re2 = /\(\s*\*\s*([A-Za-z_]\w*)\s*\)/g;
    while ((m = re2.exec(s))) set[m[1]] = 1;
    var re3 = /#\s*define\s+([A-Za-z_]\w*)\s*\(/g;
    while ((m = re3.exec(s))) set[m[1]] = 1;
    return set;
  }
  function forbidden(s, spec) {
    var defs = definedNames(s), allowed = {}, bad = {}, m;
    (spec.funcs || []).concat(spec.names || []).forEach(function (f) { allowed[f] = 1; });
    var re = /\b([A-Za-z_]\w*)\s*\(/g;
    var body = s.replace(/^[ \t]*#[^\n]*/gm, " ");
    while ((m = re.exec(body))) {
      var n = m[1];
      if (KW[n] || defs[n] || allowed[n]) continue;
      bad[n] = 1;
    }
    return Object.keys(bad);
  }

  function checkSubmission(code, spec, opts) {
    opts = opts || {};
    var errs = [], notes = [];
    if (!code || !code.trim()) return { ok: false, errs: ["nada entregue: o ficheiro está vazio"], notes: [] };
    if (spec.kind === "script") {
      notes.push("scripts e Makefiles são corrigidos ao serem executados: confirma na folha de avaliação");
      return { ok: true, errs: errs, notes: notes };
    }
    var s = strip(code);
    var hasMain = /\bmain\s*\(/.test(s);
    if (spec.kind === "programa" && !hasMain) errs.push("é um programa: falta a função main");
    if ((spec.kind === "funcao" || spec.kind === "header") && /\bmain\s*\([^;{}]*\)\s*\{/.test(s))
      errs.push("entregaste uma main, mas o enunciado só pede a função (a moulinette usa a main dela)");
    (spec.names || []).forEach(function (n) {
      var def = new RegExp("\\b" + n + "\\s*\\([^;{}]*\\)\\s*" + (spec.kind === "header" ? ";" : "\\{"));
      if (!def.test(s)) errs.push((spec.kind === "header" ? "falta o protótipo de " : "falta a função ") + n + " (com o nome exato do enunciado)");
    });
    var bad = forbidden(s, spec);
    if (bad.length) errs.push("funções que não estão nas permitidas: " + bad.join(", ") + " (na 42, uma função proibida vale -42)");
    if (opts.norm && P42.normCheck) {
      var n = P42.normCheck(code).filter(function (r) { return r.kind === "er"; });
      if (n.length) errs.push("Norma: " + n.length + " erro(s); o primeiro na linha " + n[0].n + ": " + n[0].msg);
    }
    return { ok: errs.length === 0, errs: errs, notes: notes };
  }
  P42.checkSubmission = checkSubmission;
  P42.forbidden = function (code, spec) { return forbidden(strip(code), spec); };

  /* ------------------------------------------------------------ utilitários de UI */
  function $(s, c) { return (c || document).querySelector(s); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function hash(str) {
    var h = 2166136261;
    for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
    return ("0000000" + h.toString(16)).slice(-8);
  }
  function now() { return new Date().toLocaleString("pt-PT"); }
  P42.hash = hash;

  /* Terminal simples reutilizável: imprime linhas e lê comandos. */
  function makeShell(root, prompt, onCmd) {
    var out = $("[data-shell-out]", root), form = $("[data-shell-form]", root), input = $("[data-shell-in]", root);
    var hist = [], hpos = -1;
    function print(html, cls) {
      var d = document.createElement("div");
      if (cls) d.className = cls;
      d.innerHTML = html;
      out.appendChild(d);
      out.scrollTop = out.scrollHeight;
    }
    function run(line) {
      print('<span class="sh-p">' + esc(prompt()) + "</span> " + esc(line), "sh-cmd");
      if (line.trim()) { hist.unshift(line); hpos = -1; }
      onCmd(line.trim());
    }
    form.addEventListener("submit", function (ev) { ev.preventDefault(); var v = input.value; input.value = ""; run(v); });
    input.addEventListener("keydown", function (ev) {
      if (ev.key === "ArrowUp" && hist.length) { ev.preventDefault(); hpos = Math.min(hist.length - 1, hpos + 1); input.value = hist[hpos]; }
      else if (ev.key === "ArrowDown") { ev.preventDefault(); hpos = Math.max(-1, hpos - 1); input.value = hpos >= 0 ? hist[hpos] : ""; }
      else if (ev.key === "Escape") input.blur();
    });
    return { print: print, run: run, clear: function () { out.innerHTML = ""; }, input: input };
  }
  P42.makeShell = makeShell;

  /* Comandos git simulados sobre um conjunto de ficheiros {caminho: código}.
     state: {staged:{}, commits:[{id,msg,at,snap}], pushed:{id,snap}|null} */
  function gitCmd(line, state, files, sh, label) {
    var parts = line.match(/(?:[^\s"']+|"[^"]*"|'[^']*')+/g) || [];
    var sub = parts[1];
    var head = state.commits.length ? state.commits[state.commits.length - 1].snap : (state.pushed ? state.pushed.snap : {});
    if (sub === "status") {
      var lines = [], paths = Object.keys(files);
      var staged = paths.filter(function (p) { return state.staged[p] !== undefined && state.staged[p] !== head[p]; });
      var changed = paths.filter(function (p) { return files[p] && files[p] !== (state.staged[p] !== undefined ? state.staged[p] : head[p]); });
      lines.push("On branch master");
      var ahead = state.commits.length;
      if (ahead) lines.push("Your branch is ahead of 'origin/master' by " + ahead + " commit" + (ahead > 1 ? "s" : "") + ". (usa git push)");
      if (staged.length) lines.push("Changes to be committed:\n" + staged.map(function (p) { return '\t<span class="ok">' + (head[p] === undefined ? "new file:   " : "modified:   ") + esc(p) + "</span>"; }).join("\n"));
      if (changed.length) lines.push("Changes not staged for commit / untracked:\n" + changed.map(function (p) { return '\t<span class="ko">' + esc(p) + "</span>"; }).join("\n"));
      if (!staged.length && !changed.length) lines.push("nothing to commit, working tree clean");
      sh.print(lines.join("\n"));
    } else if (sub === "add") {
      var target = parts.slice(2).join(" ");
      if (!target) { sh.print("Nothing specified, nothing added. (experimenta: git add .)", "ko"); return; }
      var n = 0;
      Object.keys(files).forEach(function (p) {
        if ((target === "." || target === "-A" || target === "--all" || p.indexOf(target.replace(/\/$/, "")) === 0) && files[p]) { state.staged[p] = files[p]; n++; }
      });
      sh.print(n ? "" : "fatal: pathspec '" + esc(target) + "' did not match any files", n ? "" : "ko");
    } else if (sub === "commit") {
      var m = line.match(/-m\s+(?:"([^"]*)"|'([^']*)'|(\S+))/);
      if (!m) { sh.print('falta a mensagem: git commit -m "mensagem"', "ko"); return; }
      var msg = m[1] || m[2] || m[3];
      var snap = {}, diff = 0;
      Object.keys(head).forEach(function (p) { snap[p] = head[p]; });
      Object.keys(state.staged).forEach(function (p) { if (snap[p] !== state.staged[p]) diff++; snap[p] = state.staged[p]; });
      if (!diff) { sh.print("nothing to commit, working tree clean (fizeste git add?)", "ko"); return; }
      var id = hash(msg + JSON.stringify(snap) + Date.now()).slice(0, 7);
      state.commits.push({ id: id, msg: msg, at: Date.now(), snap: snap });
      state.staged = {};
      sh.print("[master " + id + "] " + esc(msg) + "\n " + diff + " file" + (diff > 1 ? "s" : "") + " changed");
    } else if (sub === "push") {
      if (!state.commits.length) { sh.print("Everything up-to-date (não há commits novos para enviar)", "ko"); return; }
      var last = state.commits[state.commits.length - 1];
      state.pushed = { id: last.id, snap: last.snap, at: Date.now() };
      var nc = state.commits.length;
      state.commits = [];
      sh.print("Enumerating objects: " + (nc * 3 + 2) + ", done.\nWriting objects: 100% (" + (nc * 3) + "/" + (nc * 3) + "), done.\nTo vogsphere:" + esc(label) + "\n   " + last.id + "  master -> master", "ok");
    } else if (sub === "log") {
      var all = state.commits.slice().reverse();
      if (state.pushed) all.push({ id: state.pushed.id, msg: "(no repositório)", at: state.pushed.at });
      sh.print(all.length ? all.map(function (c) { return '<span class="ok">commit ' + c.id + "</span>  " + esc(c.msg); }).join("\n") : "ainda não há commits");
    } else if (sub === "clone") {
      sh.print("Cloning into '" + esc(label.split("/").pop()) + "'...\nwarning: You appear to have cloned an empty repository.");
      state.cloned = true;
    } else {
      sh.print("git: '" + esc(sub || "") + "' não está simulado. Usa: git clone, status, add, commit -m, push, log", "ko");
    }
  }
  P42.gitCmd = gitCmd;

  /* ------------------------------------------------------------ entrega de um módulo */
  var box = $("[data-deliver]");
  if (!box) return;
  var DD;
  try { DD = JSON.parse(document.getElementById("deliver-data").textContent); } catch (e) { return; }
  var KEY = "deliv:" + DD.mod;
  var S = store.get(KEY, null);
  if (!S || typeof S !== "object") S = {};
  S.staged = S.staged || {}; S.commits = S.commits || []; S.pushed = S.pushed || null; S.aval = S.aval || {};
  function save() { store.set(KEY, S); }
  var repo = "vogsphere/intra-" + hash("repo" + DD.mod) + "-" + DD.mod;

  function filesNow() {
    var f = {};
    DD.exs.forEach(function (e) {
      var ta = document.getElementById("code-" + e.id);
      var code = ta ? ta.value : (store.get("code:" + e.id, "") || "");
      if (e.spec.kind === "none") return;
      f[e.num + "/" + e.spec.files[0]] = code;
    });
    return f;
  }

  var shell = makeShell(box, function () { return "piscine@42lisboa:~/" + DD.mod + "$"; }, command);
  var flow = box.querySelectorAll("[data-step]");
  function renderFlow() {
    var done = { inscricao: !!S.inscrito, push: !!S.pushed, moulinette: !!S.moul, avaliacao: !!S.avalDone };
    Array.prototype.forEach.call(flow, function (li) { li.classList.toggle("is-done", !!done[li.getAttribute("data-step")]); });
    var sum = $("[data-deliver-sum]", box);
    if (sum) {
      var parts = [];
      if (S.pushed) parts.push("último push: " + new Date(S.pushed.at).toLocaleString("pt-PT"));
      if (S.moul) parts.push("moulinette: <b>" + S.moul.grade + "/100</b>");
      if (S.avalDone) parts.push("avaliação: <b>" + S.avalGrade + "/100</b>");
      sum.innerHTML = parts.join(" · ");
    }
  }

  function moulinette() {
    if (!S.pushed) { shell.print("A moulinette só corrige o que está no repositório. Faz git add, git commit e git push primeiro.", "ko"); return; }
    shell.print("moulinette: a corrigir o commit " + S.pushed.id + " de " + DD.nome + "…");
    var res = [], stop = false, okCount = 0;
    DD.exs.forEach(function (e) {
      var path = e.num + "/" + e.spec.files[0];
      if (e.spec.kind === "none") { res.push({ num: e.num, nome: e.nome, st: "ok", why: ["não há nada para entregar"] }); if (!stop) okCount++; return; }
      var code = S.pushed.snap[path] || "";
      var r = checkSubmission(code, e.spec, { norm: true });
      if (stop) { res.push({ num: e.num, nome: e.nome, st: "skip", why: ["não conta: um exercício anterior falhou"] }); return; }
      if (r.ok) { okCount++; res.push({ num: e.num, nome: e.nome, st: "ok", why: r.notes }); }
      else { stop = true; res.push({ num: e.num, nome: e.nome, st: "ko", why: r.errs }); }
    });
    var grade = Math.round(okCount / DD.exs.length * 100);
    S.moul = { at: Date.now(), grade: grade, res: res, commit: S.pushed.id };
    save();
    res.forEach(function (r) {
      var tag = r.st === "ok" ? '<span class="ok">OK</span>' : r.st === "ko" ? '<span class="ko">KO</span>' : '<span class="mute">--</span>';
      shell.print(tag + "  " + esc(r.num) + "  " + esc(r.nome) + (r.why.length ? '\n      <span class="mute">' + r.why.map(esc).join("\n      ") + "</span>" : ""));
    });
    shell.print("nota da moulinette: <b>" + grade + "/100</b>  (por ordem: depois do primeiro KO, nada conta)", grade ? "ok" : "ko");
    shell.print('<span class="mute">A moulinette deste simulador não compila o código: verifica a entrega, a Norma, os nomes e as funções proibidas. O comportamento confirma-se na avaliação (escreve avaliacao).</span>');
    renderFlow(); renderEval();
  }

  /* Folha de avaliação: cada exercício tem testes para correres no teu terminal. */
  var evalBox = $("[data-eval]", box);
  function renderEval() {
    if (!S.moul) { evalBox.hidden = true; return; }
    evalBox.hidden = false;
    var html = '<h3 class="h3">folha de avaliação</h3><p class="muted">Como numa avaliação por pares: corre cada teste no teu terminal e marca os que passam. Um exercício só conta se passar em todos, e só contam os exercícios seguidos a partir do ex00.</p><ol class="esheet">';
    DD.exs.forEach(function (e) {
      var marks = S.aval[e.id] || [];
      var tests = e.tests.length ? e.tests : ["compila sem avisos com gcc -Wall -Wextra -Werror e faz o que o enunciado pede"];
      html += '<li class="esheet__ex"><p class="esheet__h"><b>' + esc(e.num) + "</b> " + esc(e.nome) + "</p><ul>" +
        tests.map(function (t, i) {
          return '<li><label><input type="checkbox" data-ev="' + e.id + '" data-ti="' + i + '"' + (marks[i] ? " checked" : "") + "> <span>" + t + "</span></label></li>";
        }).join("") + "</ul></li>";
    });
    html += '</ol><div class="esheet__end"><button type="button" class="btn btn--go" data-ev-close><span class="br">[</span> fechar a avaliação <span class="br">]</span></button><span data-ev-res></span></div>';
    evalBox.innerHTML = html;
    evalBox.querySelectorAll("[data-ev]").forEach(function (cb) {
      cb.addEventListener("change", function () {
        var id = cb.getAttribute("data-ev"), i = +cb.getAttribute("data-ti");
        S.aval[id] = S.aval[id] || [];
        S.aval[id][i] = cb.checked;
        save();
      });
    });
    $("[data-ev-close]", evalBox).addEventListener("click", function () {
      var ok = 0, stop = false;
      DD.exs.forEach(function (e) {
        var n = e.tests.length || 1, marks = S.aval[e.id] || [], all = true;
        for (var i = 0; i < n; i++) if (!marks[i]) all = false;
        if (!stop && all) ok++; else stop = true;
      });
      S.avalDone = true;
      S.avalGrade = Math.round(ok / DD.exs.length * 100);
      save();
      $("[data-ev-res]", evalBox).innerHTML = "nota da avaliação: <b>" + S.avalGrade + "/100</b> (" + ok + " de " + DD.exs.length + " exercícios seguidos)";
      shell.print("avaliação fechada: <b>" + S.avalGrade + "/100</b>", S.avalGrade ? "ok" : "ko");
      renderFlow();
    });
  }

  function command(line) {
    var w = line.split(/\s+/)[0];
    if (!line) return;
    if (w === "help" || w === "ajuda") {
      shell.print("inscrever            inscreve-te no projeto (como na intra)\ngit clone            clona o repositório\ngit status           o que mudou desde o último push\ngit add .            prepara todos os exercícios com código\ngit commit -m \"…\"    regista as alterações\ngit push             entrega (envia para o repositório)\ngit log              commits\nmoulinette           corrige o que está no repositório\navaliacao            abre a folha de avaliação\nls                   ficheiros do repositório\nclear                limpa o terminal");
    } else if (w === "inscrever") {
      if (S.inscrito) { shell.print("Já estás inscrito em " + esc(DD.nome) + "."); return; }
      S.inscrito = true; S.inscritoEm = Date.now(); save();
      shell.print("Inscrito em " + esc(DD.nome) + ". Repositório criado:\n  git@vogsphere.42lisboa.com:" + repo + "\nPróximo passo: git clone (sem prazo de entrega neste simulador)", "ok");
      renderFlow();
    } else if (w === "git") {
      if (!S.inscrito) { shell.print("Primeiro inscreve-te no projeto: escreve inscrever.", "ko"); return; }
      gitCmd(line, S, filesNow(), shell, repo);
      save(); renderFlow();
    } else if (w === "moulinette" || w === "grademe") {
      moulinette();
    } else if (w === "avaliacao" || w === "avaliação") {
      if (!S.moul) { shell.print("A avaliação só abre depois da moulinette.", "ko"); return; }
      renderEval(); evalBox.scrollIntoView({ behavior: "smooth", block: "start" });
    } else if (w === "ls") {
      var f = filesNow();
      shell.print(Object.keys(f).map(function (p) { return (f[p] ? "" : '<span class="mute">') + esc(p) + (f[p] ? "" : " (vazio)</span>"); }).join("\n"));
    } else if (w === "clear") {
      shell.clear();
    } else {
      shell.print(esc(w) + ": comando não encontrado. Escreve help.", "ko");
    }
  }

  box.querySelectorAll("[data-sh]").forEach(function (b) {
    b.addEventListener("click", function () { shell.run(b.getAttribute("data-sh")); });
  });
  shell.print('Entrega de <b>' + esc(DD.nome) + '</b>. Escreve <b>help</b> ou usa os botões. ' + (S.inscrito ? "Já estás inscrito." : "Começa por <b>inscrever</b>."));
  renderFlow();
  renderEval();
})();
