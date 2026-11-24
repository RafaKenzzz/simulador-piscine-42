/* Simulador da Piscine: comportamento comum a todas as páginas.
   - progresso e código guardados no localStorage (com try/catch: o site funciona sem ele)
   - efeito de digitação nos títulos, entradas suaves, botões de copiar
   - linha de comandos (tecla /) e atalhos de teclado
   - verificação básica da Norma no campo de código */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  var DATA = {};
  try { DATA = JSON.parse(document.getElementById("site-data").textContent); } catch (e) { DATA = { mods: [], pages: {} }; }
  var ROOT = document.body.getAttribute("data-root") || "";
  var KEY = DATA.store || "p42";
  var REDUCE = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------ armazenamento */
  var store = {
    get: function (k, d) {
      try { var v = window.localStorage.getItem(KEY + ":" + k); return v === null ? d : JSON.parse(v); } catch (e) { return d; }
    },
    set: function (k, v) {
      try { window.localStorage.setItem(KEY + ":" + k, JSON.stringify(v)); return true; } catch (e) { return false; }
    },
    del: function (k) { try { window.localStorage.removeItem(KEY + ":" + k); } catch (e) { /* sem armazenamento */ } },
    keys: function () {
      try { return Object.keys(window.localStorage).filter(function (k) { return k.indexOf(KEY + ":") === 0; }); } catch (e) { return []; }
    }
  };
  window.P42 = { store: store, data: DATA };

  function prog() { var p = store.get("prog", {}); return p && typeof p === "object" ? p : {}; }
  function setStatus(id, st) {
    var p = prog();
    if (st === "todo") delete p[id]; else p[id] = st;
    store.set("prog", p);
    store.set("last", id);
    renderProgress();
  }
  function allIds() { var a = []; (DATA.mods || []).forEach(function (m) { a = a.concat(m.exs); }); return a; }
  function modById(id) { return (DATA.mods || []).filter(function (m) { return m.id === id; })[0]; }
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function hhmm(d) { d = d || new Date(); return ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2); }

  /* ------------------------------------------------------------ progresso */
  var LABEL = { todo: "por fazer", doing: "em curso", done: "feito" };
  function renderProgress() {
    var p = prog();
    $$("[data-bar]").forEach(function (bar) {
      var key = bar.getAttribute("data-bar");
      var ids = key === "all" ? allIds() : ((modById(key) || {}).exs || []);
      var done = ids.filter(function (i) { return p[i] === "done"; }).length;
      var pct = ids.length ? Math.round(done / ids.length * 100) : 0;
      var fill = bar.firstElementChild;
      if (fill) fill.style.width = pct + "%";
      bar.setAttribute("aria-valuenow", pct);
    });
    $$("[data-bar-text]").forEach(function (t) {
      var key = t.getAttribute("data-bar-text");
      var ids = key === "all" ? allIds() : ((modById(key) || {}).exs || []);
      var done = ids.filter(function (i) { return p[i] === "done"; }).length;
      var doing = ids.filter(function (i) { return p[i] === "doing"; }).length;
      if (t.hasAttribute("data-short")) t.textContent = done + "/" + ids.length;
      else t.textContent = done + " de " + ids.length + " feitos" + (doing ? " · " + doing + " em curso" : "");
      var card = t.closest(".mcard");
      if (card) card.classList.toggle("is-done", ids.length > 0 && done === ids.length);
    });
    $$("[data-ex]").forEach(function (art) {
      var id = art.getAttribute("data-ex");
      var st = p[id] || "todo";
      art.classList.toggle("is-done", st === "done");
      art.classList.toggle("is-doing", st === "doing");
      var pill = $("[data-pill]", art);
      if (pill) { pill.textContent = LABEL[st]; pill.className = "pill" + (st === "todo" ? "" : " is-" + st); }
      $$("[data-st]", art).forEach(function (r) { r.checked = r.value === st; });
      var dot = $('[data-idx="' + id + '"] .dot');
      if (dot) dot.className = "dot" + (st === "todo" ? "" : " is-" + st);
    });
  }

  /* ------------------------------------------------------------ títulos e entradas */
  function typeIn(el) {
    var text = el.textContent.trim();
    var sr = document.createElement("span"); sr.className = "sr"; sr.textContent = text;
    var vis = document.createElement("span"); vis.setAttribute("aria-hidden", "true");
    var cur = document.createElement("span"); cur.className = "cur"; cur.setAttribute("aria-hidden", "true");
    el.textContent = "";
    el.appendChild(sr); el.appendChild(vis); el.appendChild(cur);
    if (REDUCE) { vis.textContent = text; return; }
    var i = 0;
    var speed = Math.max(22, Math.min(60, 1100 / Math.max(text.length, 1)));
    (function step() {
      i += 1;
      vis.textContent = text.slice(0, i);
      if (i < text.length) window.setTimeout(step, speed + Math.random() * 25);
    })();
  }
  $$("[data-type]").forEach(typeIn);

  var boot = $$("[data-boot]");
  boot.forEach(function (li, i) { window.setTimeout(function () { li.classList.add("is-in"); }, REDUCE ? 0 : 120 + i * 140); });

  if ("IntersectionObserver" in window && !REDUCE) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.04 });
    $$("[data-rv]").forEach(function (el) { io.observe(el); });
  } else {
    $$("[data-rv]").forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ------------------------------------------------------------ copiar */
  function copyText(text, done) {
    function fallback() {
      var ta = document.createElement("textarea");
      ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      done(ok);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, fallback);
    } else fallback();
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest("[data-copy]");
    if (!b) return;
    var pre = b.closest(".code").querySelector("pre");
    copyText(pre.textContent, function (ok) {
      b.textContent = ok ? "copiado ✓" : "falhou";
      b.classList.toggle("is-ok", ok);
      window.setTimeout(function () { b.textContent = "copiar"; b.classList.remove("is-ok"); }, 1600);
    });
  });

  /* ------------------------------------------------------------ verificação básica da Norma */
  function visualLen(line) {
    var n = 0;
    for (var i = 0; i < line.length; i++) n = line[i] === "\t" ? n + 4 - (n % 4) : n + 1;
    return n;
  }
  function stripLits(line) {
    return line.replace(/"(?:\\.|[^"\\])*"/g, '""').replace(/'(?:\\.|[^'\\])+'/g, "''");
  }
  var TYPES = "(?:unsigned\\s+|signed\\s+|const\\s+|static\\s+|long\\s+)*(?:struct\\s+\\w+|int|char|long|short|size_t|ssize_t|void|float|double|t_\\w+)";
  var DECL = new RegExp("^\\t" + TYPES + "\\s+\\**\\s*\\w+(?:\\[[^\\]]*\\])*\\s*(=.*)?;\\s*$");
  function normCheck(src) {
    var out = [];
    var lines = src.replace(/\r\n?/g, "\n").split("\n");
    if (lines.length && lines[lines.length - 1] === "") lines.pop();
    function add(n, kind, msg) { out.push({ n: n, kind: kind, msg: msg }); }
    if (!/^\/\* \*{74} \*\/$/.test(lines[0] || "")) add(1, "wa", "falta o cabeçalho da 42 (a norminette dá INVALID_HEADER)");
    var inFn = false, fnStart = 0, fnName = "", bodyLines = 0, vars = 0, declZone = false, funcs = 0, prevEmpty = false, inComment = false;
    lines.forEach(function (raw, i) {
      var n = i + 1;
      var line = stripLits(raw);
      var trimmed = line.trim();
      if (inComment) { if (line.indexOf("*/") >= 0) inComment = false; prevEmpty = false; return; }
      if (/^\s*\/\*/.test(line) && line.indexOf("*/") < 0) inComment = true;
      if (visualLen(raw) > 80) add(n, "er", "linha com " + visualLen(raw) + " colunas (máximo 80)");
      if (/[ \t]+$/.test(raw) && trimmed !== "") add(n, "er", "espaço ou tab no fim da linha");
      if (/^ +\S/.test(raw) && !/^\s*\*/.test(raw)) add(n, "er", "indentação com espaços (usa tabs)");
      if (/\bfor\s*\(/.test(line)) add(n, "er", "«for» é proibido: usa while");
      if (/\bdo\s*($|\{)/.test(line)) add(n, "er", "«do … while» é proibido");
      if (/\b(switch|case)\b/.test(line)) add(n, "er", "«switch/case» é proibido");
      if (/\bgoto\b/.test(line)) add(n, "er", "«goto» é proibido");
      if (/\?[^:]*:/.test(line.replace(/\/\*.*\*\//, ""))) add(n, "er", "operador ternário (? :) é proibido");
      if (/\b(if|while|return)\(/.test(line)) add(n, "er", "falta um espaço depois de «" + line.match(/\b(if|while|return)\(/)[1] + "»");
      if (/\breturn\s+[^(;\s]/.test(line)) add(n, "er", "o valor de return tem de estar entre parênteses: return (x);");
      if (/,\S/.test(line) && !/^\s*\/?\*/.test(line)) add(n, "er", "falta um espaço depois da vírgula");
      if (trimmed === "") {
        if (prevEmpty) add(n, "er", "duas linhas vazias seguidas");
        if (inFn && !declZone) add(n, "er", "linha vazia dentro da função (só é permitida depois das declarações)");
        if (inFn && declZone) declZone = false;
        prevEmpty = true;
      } else prevEmpty = false;
      if (!inFn && /^[a-zA-Z_].*\(.*\)\s*$/.test(raw) && !/;\s*$/.test(raw) && (lines[i + 1] || "") === "{") {
        fnName = (raw.match(/(\w+)\s*\(/) || [, "?"])[1];
        var params = (raw.match(/\((.*)\)/) || [, ""])[1].trim();
        if (params === "") add(n, "er", "função sem parâmetros tem de usar (void)");
        else if (params !== "void" && params.split(",").length > 4) add(n, "er", "mais de 4 parâmetros em " + fnName);
        if (!/\t\**\w+\s*\(/.test(raw)) add(n, "wa", "separa o tipo do nome da função com um tab");
        funcs += 1;
        return;
      }
      if (raw === "{" && !inFn && i > 0 && /\)\s*$/.test(lines[i - 1])) { inFn = true; fnStart = n; bodyLines = 0; vars = 0; declZone = true; return; }
      if (raw === "}" && inFn) {
        if (bodyLines > 25) add(fnStart, "er", "a função " + fnName + " tem " + bodyLines + " linhas (máximo 25)");
        if (vars > 5) add(fnStart, "er", "a função " + fnName + " declara " + vars + " variáveis (máximo 5)");
        inFn = false;
        return;
      }
      if (inFn) {
        bodyLines += 1;
        if (/\/\*|\/\//.test(line)) add(n, "er", "comentário dentro de uma função");
        if (DECL.test(raw)) {
          if (!declZone) add(n, "er", "declaração de variável fora do início da função");
          vars += 1;
          if (/=/.test(raw.replace(/==/g, ""))) add(n, "er", "declaração com atribuição na mesma linha");
        } else if (trimmed !== "" && declZone && bodyLines > 1 && vars > 0) {
          add(n, "er", "as declarações têm de ser seguidas de uma linha vazia");
          declZone = false;
        } else if (trimmed !== "") declZone = false;
        if ((line.match(/;/g) || []).length > 1 && !/^\s*while/.test(line)) add(n, "er", "mais de uma instrução na mesma linha");
      }
    });
    if (funcs > 5) add(1, "er", funcs + " funções no ficheiro (máximo 5)");
    if (lines.length && lines[lines.length - 1].trim() === "") add(lines.length, "er", "linha vazia no fim do ficheiro");
    return out.sort(function (a, b) { return a.n - b.n; });
  }

  /* ------------------------------------------------------------ campos de código */
  function bindEditor(ta, onChange) {
    ta.addEventListener("keydown", function (ev) {
      if (ev.key === "Tab" && !ev.shiftKey && !ev.ctrlKey && !ev.altKey && !ev.metaKey) {
        ev.preventDefault();
        var s = ta.selectionStart, e = ta.selectionEnd;
        ta.value = ta.value.slice(0, s) + "\t" + ta.value.slice(e);
        ta.selectionStart = ta.selectionEnd = s + 1;
        onChange();
      } else if (ev.key === "Escape") {
        ta.blur();
      }
    });
    ta.addEventListener("input", onChange);
  }
  window.P42.bindEditor = bindEditor;

  $$("[data-ex]").forEach(function (art) {
    var id = art.getAttribute("data-ex");
    $$("[data-st]", art).forEach(function (r) {
      r.addEventListener("change", function () { if (r.checked) setStatus(id, r.value); });
    });
    var ta = $("[data-code]", art);
    if (!ta) return;
    var saved = $("[data-saved]", art), count = $("[data-count]", art), outEl = $("[data-check-out]", art);
    ta.value = store.get("code:" + id, "") || "";
    function lines() { var n = ta.value ? ta.value.split("\n").length : 0; count.textContent = n + (n === 1 ? " linha" : " linhas"); }
    lines();
    var t = null;
    bindEditor(ta, function () {
      lines();
      window.clearTimeout(t);
      t = window.setTimeout(function () {
        var ok = ta.value ? store.set("code:" + id, ta.value) : (store.del("code:" + id), true);
        saved.textContent = ok ? "guardado às " + hhmm() : "não foi possível guardar neste navegador";
        if (ta.value && !prog()[id]) setStatus(id, "doing");
      }, 400);
    });
    var clear = $("[data-clear]", art), armed = null;
    clear.addEventListener("click", function () {
      if (!armed) {
        clear.textContent = "confirmar limpeza";
        armed = window.setTimeout(function () { clear.textContent = "limpar"; armed = null; }, 3000);
        return;
      }
      window.clearTimeout(armed); armed = null;
      clear.textContent = "limpar";
      ta.value = ""; store.del("code:" + id); lines(); outEl.innerHTML = ""; saved.textContent = "apagado";
    });
    var check = $("[data-check]", art);
    if (check) check.addEventListener("click", function () {
      if (!ta.value.trim()) { outEl.innerHTML = '<ul><li class="wa">Ainda não há código para verificar.</li></ul>'; return; }
      var res = normCheck(ta.value);
      var errs = res.filter(function (r) { return r.kind === "er"; }).length;
      var html = res.map(function (r) { return '<li class="' + r.kind + '">linha ' + r.n + ": " + esc(r.msg) + "</li>"; }).join("");
      if (!errs) html = '<li class="ok">Nenhum erro encontrado pelas regras básicas.</li>' + html;
      html += '<li class="mute">Esta verificação só apanha os erros mais comuns. A referência é a norminette.</li>';
      outEl.innerHTML = "<ul>" + html + "</ul>";
    });
  });

  /* ------------------------------------------------------------ exercício atual (j/k) */
  var exs = $$("[data-ex]");
  var current = -1;
  function nearestEx() {
    var best = 0, bestD = Infinity, top = 90;
    exs.forEach(function (el, i) {
      var r = el.getBoundingClientRect();
      var d = Math.abs(r.top - top);
      if (r.top <= top + 40 && r.bottom > top) d = 0;
      if (d < bestD) { bestD = d; best = i; }
    });
    return best;
  }
  function goEx(i) {
    if (!exs.length) return;
    i = Math.max(0, Math.min(exs.length - 1, i));
    exs.forEach(function (el) { el.classList.remove("is-focus"); });
    var el = exs[i];
    el.classList.add("is-focus");
    el.scrollIntoView({ behavior: REDUCE ? "auto" : "smooth", block: "start" });
    current = i;
    if (history.replaceState) history.replaceState(null, "", "#" + el.id);
    $$(".idx a").forEach(function (a) { a.classList.toggle("is-here", a.getAttribute("data-idx") === el.id); });
  }
  /* nas filas de etiquetas que deslizam (telemóvel), mantém a etiqueta atual à vista */
  function centerChip(a, smooth) {
    var ol = a && a.closest("ol");
    if (!ol || ol.scrollWidth <= ol.clientWidth + 1) return;
    var d = a.getBoundingClientRect().left - ol.getBoundingClientRect().left - (ol.clientWidth - a.offsetWidth) / 2;
    if (ol.scrollBy) ol.scrollBy({ left: d, behavior: smooth && !REDUCE ? "smooth" : "auto" });
    else ol.scrollLeft += d;
  }
  if (exs.length && "IntersectionObserver" in window) {
    var idxObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        $$(".idx a").forEach(function (a) {
          var on = a.getAttribute("data-idx") === e.target.id;
          if (on && !a.classList.contains("is-here")) centerChip(a, true);
          a.classList.toggle("is-here", on);
        });
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    exs.forEach(function (el) { idxObs.observe(el); });
    var dl = $("#entrega");
    if (dl) idxObs.observe(dl);
  }
  centerChip($(".ansnav a[aria-current]"), false);

  /* telemóvel: a barra de baixo esconde-se ao descer e volta ao subir ou no fim da página */
  var mqNav = window.matchMedia && window.matchMedia("(max-width: 899px)"), lastY = window.pageYOffset || 0;
  window.addEventListener("scroll", function () {
    if (!mqNav || !mqNav.matches) return;
    var y = window.pageYOffset || 0, dy = y - lastY;
    var end = window.innerHeight + y >= document.documentElement.scrollHeight - 48;
    /* saltos grandes (ligações #, j/k) não são o utilizador a deslizar: a barra fica como está */
    if (end || y < 120) document.body.classList.remove("nav-off");
    else if (Math.abs(dy) > 10 && Math.abs(dy) < window.innerHeight * .8) document.body.classList.toggle("nav-off", dy > 0);
    if (Math.abs(dy) > 10 || end) lastY = y;
  }, { passive: true });

  /* ------------------------------------------------------------ início: retomar */
  var start = $("[data-start]");
  if (start) {
    var p0 = prog(), last = store.get("last", null), target = null;
    (DATA.mods || []).some(function (m) {
      return m.exs.some(function (id) { if (p0[id] !== "done") { target = { m: m, id: id }; return true; } return false; });
    });
    var any = Object.keys(p0).length > 0;
    if (target && any) {
      start.setAttribute("href", target.m.href + "#" + target.id);
      start.innerHTML = '<span class="br">[</span> Continuar <span class="br">]</span>';
      var res = $("[data-resume]");
      if (res) {
        res.hidden = false;
        res.innerHTML = "Próximo exercício por fazer: <b>" + esc(target.m.nome) + " · " + esc(target.id.split("-")[1]) + "</b>" +
          (last ? ' · último que mexeste: <a href="' + esc((modById(last.split("-")[0]) || {}).href || "#") + "#" + esc(last) + '">' + esc(last.replace("-", " · ")) + "</a>" : "");
      }
    }
  }

  /* ------------------------------------------------------------ linha de comandos */
  var cmd = $("[data-cmd]"), cmdIn = $("[data-cmd-in]"), cmdOut = $("[data-cmd-out]"), cmdForm = $("[data-cmd-form]");
  var help = $("[data-help]");
  var PAGES = DATA.pages || {};
  var MODIDS = (DATA.mods || []).map(function (m) { return m.id; });
  var COMMANDS = ["help", "ls", "cd", "open", "pwd", "whoami", "progresso", "norminette", "examshell", "clear", "exit", "date", "reset-progresso"];
  var pending = null;
  var hist = store.get("hist", []) || [], hpos = -1;
  var path = ($(".pr-p") || {}).textContent || "~";
  var cmdPath = $("[data-cmd-path]");
  if (cmdPath) cmdPath.textContent = path;
  var lastFocus = null;

  function print(html, cls) {
    var div = document.createElement("div");
    if (cls) div.className = cls;
    div.innerHTML = html;
    cmdOut.appendChild(div);
    cmdOut.scrollTop = cmdOut.scrollHeight;
  }
  function openCmd(prefill) {
    if (!cmd) return;
    lastFocus = document.activeElement;
    closeHelp();
    cmd.hidden = false;
    cmdIn.value = prefill || "";
    window.setTimeout(function () { cmdIn.focus(); }, 0);
  }
  function closeCmd() {
    if (!cmd || cmd.hidden) return;
    cmd.hidden = true; pending = null;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  function openHelp() { if (help) { lastFocus = document.activeElement; help.hidden = false; var b = $("[data-help-close]"); if (b) b.focus(); } }
  function closeHelp() { if (help && !help.hidden) { help.hidden = true; if (lastFocus && lastFocus.focus) lastFocus.focus(); } }
  function go(url) { window.location.href = url; }

  var DESTS = { "inicio": PAGES.inicio, "início": PAGES.inicio, "~": PAGES.inicio, "home": PAGES.inicio,
    "tutorial": PAGES.tutorial, "ajuda-site": PAGES.tutorial,
    "modulos": PAGES.modulos, "módulos": PAGES.modulos, "exames": PAGES.exames, "exame": PAGES.exames, "examshell": PAGES.exames,
    "norminette": PAGES.norminette, "norma": PAGES.norminette };

  function resolve(arg) {
    arg = (arg || "").toLowerCase().replace(/\/+$/, "").replace(/^~\//, "");
    if (!arg || arg === "~") return PAGES.inicio;
    if (arg === "..") return document.body.getAttribute("data-kind") === "modulo" ? PAGES.modulos : PAGES.inicio;
    if (DESTS[arg]) return DESTS[arg];
    var parts = arg.replace(/^modulos\//, "").split(/[\/ ]/);
    var m = modById(parts[0]);
    if (m) {
      if (parts[1]) {
        var exid = m.id + "-" + parts[1].replace(/^ex?(\d)$/, "ex0$1").replace(/^(\d\d)$/, "ex$1");
        if (m.exs.indexOf(exid) >= 0) return m.href + "#" + exid;
      }
      return m.href;
    }
    var mod = document.body.getAttribute("data-mod");
    if (mod && /^ex?\d+$/.test(arg)) {
      var n = arg.replace(/^ex?/, "");
      var id2 = mod + "-ex" + (n.length === 1 ? "0" + n : n);
      if (document.getElementById(id2)) return "#" + id2;
    }
    return null;
  }

  function run(line) {
    line = line.trim();
    print('<span class="o-cmd"><b>$</b> ' + esc(line) + "</span>");
    if (pending) { var f = pending; pending = null; f(line); return; }
    if (!line) return;
    hist.unshift(line); hist = hist.slice(0, 40); store.set("hist", hist); hpos = -1;
    var parts = line.split(/\s+/), c = parts[0].toLowerCase(), arg = parts.slice(1).join(" ");
    if (c === "help" || c === "ajuda" || c === "man") {
      print("comandos:\n" +
        "  ls                   o que existe\n" +
        "  cd &lt;destino&gt;          ir para: inicio, modulos, exames, norminette, c00 … bsq\n" +
        "  open &lt;mod/ex&gt;         abrir um exercício: open c03/ex02 (ou ex02 dentro de um módulo)\n" +
        "  progresso            o teu progresso por módulo\n" +
        "  examshell            simulador de exames\n" +
        "  norminette           regras da Norma\n" +
        "  pwd, whoami, date    o costume\n" +
        "  reset-progresso      apagar o progresso guardado neste navegador\n" +
        "  clear, exit          limpar, fechar (ou Esc)\n" +
        "  cd respostas         soluções (pede confirmação)");
    } else if (c === "ls" || c === "ll" || c === "dir") {
      var kind = document.body.getAttribute("data-kind");
      if (kind === "modulo") {
        print($$("[data-ex]").map(function (a) { return a.id.split("-")[1] + "/  " + esc($(".ex__h", a).textContent.replace(/^ex\d+\s*/, "")); }).join("\n"));
      } else {
        print("inicio/  modulos/  exames/  norminette/\n" + MODIDS.join("/  ") + "/");
      }
    } else if (c === "cd" || c === "open" || c === "vim" || c === "cat") {
      if ((arg || "").toLowerCase().replace(/\/$/, "") === "respostas") {
        print('<span class="o-er">Tenta primeiro sozinho.</span> Abrir as respostas mesmo assim? [s/N]');
        pending = function (ans) { if (/^s(im)?$/i.test(ans)) go(PAGES.respostas); else print("ficas por aqui. boa."); };
        return;
      }
      var url = resolve(arg);
      if (url === null) { print('<span class="o-er">cd: ' + esc(arg) + ": não existe.</span> Escreve ls."); return; }
      if (url.charAt(0) === "#") { closeCmd(); var idx = exs.map(function (e) { return "#" + e.id; }).indexOf(url); goEx(idx); return; }
      go(url);
    } else if (c === "pwd") {
      print(esc(path.replace("~", "/home/" + (DATA.prompt || "piscine").split("@")[0])));
    } else if (c === "whoami") {
      print("piscine: candidato à 42 Lisboa (" + allIds().filter(function (i) { return prog()[i] === "done"; }).length + " exercícios feitos)");
    } else if (c === "date") {
      print(esc(new Date().toLocaleString("pt-PT")));
    } else if (c === "progresso" || c === "status") {
      var p = prog();
      print((DATA.mods || []).map(function (m) {
        var d = m.exs.filter(function (i) { return p[i] === "done"; }).length;
        var w = 20, f = Math.round(d / m.exs.length * w);
        return (m.nome + "        ").slice(0, 8) + " [" + new Array(f + 1).join("#") + new Array(w - f + 1).join(".") + "] " + d + "/" + m.exs.length;
      }).join("\n"));
    } else if (c === "norminette" || c === "norma") {
      go(PAGES.norminette);
    } else if (c === "examshell" || c === "exam" || c === "exame") {
      go(PAGES.exames);
    } else if (c === "clear") {
      cmdOut.innerHTML = "";
    } else if (c === "exit" || c === "q" || c === ":q") {
      closeCmd();
    } else if (c === "reset-progresso") {
      print('<span class="o-er">Isto apaga o progresso e o código guardados neste navegador.</span> Escreve <b>sim</b> para confirmar.');
      pending = function (ans) {
        if (ans === "sim") { store.keys().forEach(function (k) { try { window.localStorage.removeItem(k); } catch (e) { /* nada */ } }); renderProgress(); print('<span class="o-ok">progresso apagado.</span>'); }
        else print("cancelado.");
      };
    } else if (c === "sudo") {
      print("piscine não está no ficheiro sudoers. Este incidente será reportado.");
    } else {
      print('<span class="o-er">' + esc(c) + ": comando não encontrado.</span> Escreve help.");
    }
  }

  function complete() {
    var v = cmdIn.value, parts = v.split(/\s+/);
    var pool = parts.length <= 1 ? COMMANDS : ["inicio", "tutorial", "modulos", "exames", "norminette"].concat(MODIDS);
    var last = parts[parts.length - 1].toLowerCase();
    var hits = pool.filter(function (x) { return x.indexOf(last) === 0; });
    if (hits.length === 1) { parts[parts.length - 1] = hits[0]; cmdIn.value = parts.join(" ") + (parts.length <= 1 ? " " : ""); }
    else if (hits.length > 1) print(hits.join("  "));
  }

  if (cmd) {
    cmdForm.addEventListener("submit", function (ev) { ev.preventDefault(); var v = cmdIn.value; cmdIn.value = ""; run(v); });
    cmdIn.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") { ev.preventDefault(); closeCmd(); }
      else if (ev.key === "Tab") { ev.preventDefault(); complete(); }
      else if (ev.key === "ArrowUp") { if (hist.length) { ev.preventDefault(); hpos = Math.min(hist.length - 1, hpos + 1); cmdIn.value = hist[hpos]; } }
      else if (ev.key === "ArrowDown") { ev.preventDefault(); hpos = Math.max(-1, hpos - 1); cmdIn.value = hpos >= 0 ? hist[hpos] : ""; }
      else if (ev.key === "l" && ev.ctrlKey) { ev.preventDefault(); cmdOut.innerHTML = ""; }
    });
    cmd.addEventListener("click", function (ev) { if (ev.target === cmd) closeCmd(); });
  }
  $$("[data-cmd-open]").forEach(function (b) { b.addEventListener("click", function () { openCmd(); }); });
  if (help) {
    help.addEventListener("click", function (ev) { if (ev.target === help) closeHelp(); });
    var hc = $("[data-help-close]");
    if (hc) hc.addEventListener("click", closeHelp);
  }

  /* ------------------------------------------------------------ atalhos */
  document.addEventListener("keydown", function (ev) {
    if (ev.defaultPrevented || ev.ctrlKey || ev.metaKey || ev.altKey) return;
    var t = ev.target, tag = t && t.tagName;
    var typing = tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || (t && t.isContentEditable);
    if (ev.key === "Escape") { closeCmd(); closeHelp(); return; }
    if (typing) return;
    if (cmd && !cmd.hidden) return;
    if (document.body.classList.contains("in-exam")) return;
    var k = ev.key;
    if (k === "/" || k === ":") { ev.preventDefault(); openCmd(); return; }
    if (k === "?") { ev.preventDefault(); if (help.hidden) openHelp(); else closeHelp(); return; }
    var nav = $('.nav a[data-key="' + k + '"]');
    if (nav) { ev.preventDefault(); go(nav.getAttribute("href")); return; }
    if (k === "j" || k === "k") {
      if (!exs.length) return;
      ev.preventDefault();
      var base = current >= 0 ? current : nearestEx();
      if (current < 0 && k === "j" && exs[base].getBoundingClientRect().top > 100) goEx(base);
      else goEx(base + (k === "j" ? 1 : -1));
      return;
    }
    if (k === "n" || k === "p") {
      var a = $(k === "n" ? "[data-next]" : "[data-prev]");
      if (a) { ev.preventDefault(); go(a.getAttribute("href")); }
      return;
    }
    if (k === "e" && exs.length) {
      var ta = $("[data-code]", exs[current >= 0 ? current : nearestEx()]);
      if (ta) { ev.preventDefault(); ta.focus(); }
      return;
    }
    if (k === "f" && exs.length) {
      ev.preventDefault();
      var el = exs[current >= 0 ? current : nearestEx()];
      setStatus(el.getAttribute("data-ex"), "done");
      return;
    }
    if (k === "g") { ev.preventDefault(); window.scrollTo({ top: 0, behavior: REDUCE ? "auto" : "smooth" }); exs.forEach(function (el) { el.classList.remove("is-focus"); }); current = -1; }
  });

  /* entrada direta num exercício (#c03-ex02): destaca-o */
  if (window.location.hash && exs.length) {
    var hit = exs.map(function (e) { return "#" + e.id; }).indexOf(window.location.hash);
    if (hit >= 0) { current = hit; exs[hit].classList.add("is-focus"); }
  }

  renderProgress();
  window.P42.renderProgress = renderProgress;
  window.P42.normCheck = normCheck;
})();
