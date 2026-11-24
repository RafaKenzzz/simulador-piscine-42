# -*- coding: utf-8 -*-
"""Gera o site a partir de config.py (aspeto) e dados/ (conteúdo).

Uso:  python _src/build.py
Escreve os .html na raiz do projeto (index, modulos, exames, norminette), em modulos/ e em
respostas/, mais robots.txt, llms.txt, site.webmanifest e, se config.SITE estiver preenchido,
sitemap.xml. As ligações são relativas e terminam em .html, para o site abrir com duplo clique
(file://) e também num servidor.
"""
import sys as _sys
try:
    _sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import hashlib
import json
import os
import re
from html import escape

_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config as C
import dados
import realce
import seo
from dados import exames as EX
from dados import inicio as INI
from dados import norma as NORMA
from dados import tutorial as TUT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src")
SOL = os.path.join(SRC, "solucoes")
MODS = dados.modulos()
_HASH = {}
BUILT = []


# ---------------------------------------------------------------- utilitários

def ver(rel):
    if rel not in _HASH:
        try:
            with open(os.path.join(ROOT, rel), "rb") as f:
                _HASH[rel] = hashlib.md5(f.read()).hexdigest()[:8]
        except FileNotFoundError:
            _HASH[rel] = "0"
    return f"{rel}?v={_HASH[rel]}"


def fmt(text):
    """Texto simples → HTML: `código`, **negrito**, ligações [texto](url)."""
    s = escape(text, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    return s


def paras(items, cls="txt"):
    """Lista de strings → parágrafos; as que começam por '- ' viram lista."""
    out, ul = [], []
    for t in items:
        if t.startswith("- "):
            ul.append(f"<li>{fmt(t[2:])}</li>")
            continue
        if ul:
            out.append("<ul>" + "".join(ul) + "</ul>")
            ul = []
        out.append(f"<p>{fmt(t)}</p>")
    if ul:
        out.append("<ul>" + "".join(ul) + "</ul>")
    return f'<div class="{cls}">' + "".join(out) + "</div>"


def read_sol(rel):
    with open(os.path.join(SOL, rel), encoding="utf-8") as f:
        return f.read().rstrip("\n") + "\n"


def code_block(code, lang, label, copy=True):
    btn = '<button class="copy" type="button" data-copy aria-label="Copiar código">copiar</button>' if copy else ""
    return (f'<figure class="code" data-lang="{lang}"><figcaption><span class="code__name">{escape(label)}</span>'
            f'<span class="code__lang">{lang}</span>{btn}</figcaption>'
            f'<pre tabindex="0"><code>{realce.highlight(code, lang)}</code></pre></figure>')


def term_block(text, label="exemplo"):
    lines = []
    for ln in text.rstrip("\n").split("\n"):
        e = escape(ln, quote=False)
        m = re.match(r"^(\$&gt;|%&gt;|\?&gt;|&gt;|[\w.-]+@[\w.-]+:[^$\s]*\$)(.*)$", e)
        if m:
            e = f'<span class="t-prompt">{m.group(1)}</span><span class="t-cmd">{m.group(2)}</span>'
        lines.append(e)
    return (f'<figure class="term"><figcaption><span>{escape(label)}</span></figcaption>'
            f'<pre tabindex="0">{chr(10).join(lines)}</pre></figure>')


def ex_id(mod, e):
    return f"{mod.ID}-{e['num']}"


def ex_lang(e):
    if e.get("lang"):
        return e["lang"]
    first = e["ficheiros"].split(",")[0].strip()
    return realce.lang_of(first)


# ---------------------------------------------------------------- moldura

def tokens_style():
    v = [f"--{k}:{c}" for k, c in C.COLORS.items()]
    v.append(f"--f-mono:{C.FONT_MONO},ui-monospace,'Cascadia Mono','Segoe UI Mono',Menlo,Consolas,monospace")
    return f"<style>:root{{{';'.join(v)}}}</style>"


def site_data(p):
    mods = [{"id": m.ID, "nome": m.NOME, "href": f"{p}modulos/{m.ID}.html",
             "exs": [ex_id(m, e) for e in m.EXS]} for m in MODS]
    pages = {"inicio": f"{p}index.html", "tutorial": f"{p}tutorial.html", "modulos": f"{p}modulos.html", "exames": f"{p}exames.html",
             "norminette": f"{p}norminette.html", "respostas": f"{p}respostas/index.html"}
    data = {"store": C.STORE, "mods": mods, "pages": pages, "prompt": f"{C.PROMPT_USER}@{C.PROMPT_HOST}"}
    return '<script id="site-data" type="application/json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def header(p, active, path_label):
    links = "".join(
        f'<a href="{p}{h}" data-key="{k}"{" aria-current=page" if active == h else ""}><span class="k">[{k}]</span>{t}</a>'
        for h, t, k in C.NAV)
    return f'''<a class="skip" href="#conteudo">Saltar para o conteúdo</a>
<header class="top" data-top>
  <div class="w top__in">
    <a class="brand" href="{p}index.html" aria-label="{C.NAME}: página inicial"><span class="pr-u">{C.PROMPT_USER}@{C.PROMPT_HOST}</span><span class="pr-s">:</span><span class="pr-p">{escape(path_label)}</span><span class="pr-s">$</span></a>
    <nav class="nav" aria-label="Principal">{links}</nav>
    <button class="cmd-btn" type="button" data-cmd-open aria-label="Abrir a linha de comandos (tecla /)"><span aria-hidden="true">&gt;_</span><span class="cmd-btn__t">comando</span><kbd>/</kbd></button>
  </div>
</header>'''


def footer(p):
    return f'''<footer class="foot">
  <div class="w foot__in">
    <p class="foot__brand"><span class="t-prompt">$</span> {C.SHORT} <span class="mute">· treino para a Piscine C</span></p>
    <p class="foot__note">Projeto de treino pessoal, sem ligação à 42 Lisboa nem à rede 42. Os enunciados são resumos em português dos originais públicos; confirma sempre o enunciado oficial no dia.</p>
    <p class="foot__keys"><kbd>/</kbd> comando · <kbd>?</kbd> atalhos · <kbd>1</kbd>–<kbd>5</kbd> páginas</p>
  </div>
</footer>
<div class="cmd" data-cmd hidden>
  <div class="cmd__box" role="dialog" aria-modal="true" aria-label="Linha de comandos">
    <div class="cmd__out" data-cmd-out aria-live="polite"></div>
    <form class="cmd__form" data-cmd-form autocomplete="off">
      <label class="cmd__pr" for="cmd-in">{C.PROMPT_USER}@{C.PROMPT_HOST}:<span data-cmd-path>~</span>$</label>
      <input id="cmd-in" class="cmd__in" data-cmd-in type="text" spellcheck="false" autocapitalize="off" enterkeyhint="go" aria-describedby="cmd-hint">
    </form>
    <p class="cmd__hint" id="cmd-hint">escreve <b>help</b> · <kbd>Tab</kbd> completa · <kbd>↑</kbd> histórico · <kbd>Esc</kbd> fecha</p>
  </div>
</div>
<div class="help" data-help hidden>
  <div class="help__box" role="dialog" aria-modal="true" aria-labelledby="help-t">
    <h2 id="help-t">Atalhos de teclado</h2>
    <dl>
      <div><dt><kbd>/</kbd> ou <kbd>:</kbd></dt><dd>abrir a linha de comandos</dd></div>
      <div><dt><kbd>1</kbd> … <kbd>5</kbd></dt><dd>início, tutorial, módulos, exames, norminette</dd></div>
      <div><dt><kbd>j</kbd> / <kbd>k</kbd></dt><dd>exercício seguinte / anterior</dd></div>
      <div><dt><kbd>n</kbd> / <kbd>p</kbd></dt><dd>módulo seguinte / anterior</dd></div>
      <div><dt><kbd>e</kbd></dt><dd>escrever no exercício atual</dd></div>
      <div><dt><kbd>f</kbd></dt><dd>marcar o exercício atual como feito</dd></div>
      <div><dt><kbd>g</kbd></dt><dd>voltar ao topo</dd></div>
      <div><dt><kbd>?</kbd></dt><dd>mostrar ou esconder esta ajuda</dd></div>
      <div><dt><kbd>Esc</kbd></dt><dd>fechar / sair do campo de código</dd></div>
    </dl>
    <button class="btn btn--ghost" type="button" data-help-close>fechar</button>
  </div>
</div>'''


def page(path, title, desc, body, active=None, path_label="~", kind="page", extra_head="", scripts=(),
         robots="index, follow", crumbs=None, ld_extra=None, body_attrs=""):
    depth = path.count("/")
    p = "../" * depth
    full_title = title if C.NAME in title else f"{title} · {C.NAME}"
    canon = seo.url(path)
    canon_tag = f'\n  <link rel="canonical" href="{canon}">\n  <meta property="og:url" content="{canon}">' if canon else ""
    ld = seo.graph(path, full_title, desc, crumbs, ld_extra or [])
    js = "".join(f'\n<script src="{p}{ver(s)}" defer></script>' for s in ("assets/js/site.js",) + tuple(scripts))
    html = f'''<!DOCTYPE html>
<html lang="{C.LANG}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{escape(full_title)}</title>
  <meta name="description" content="{escape(desc)}">
  <meta name="robots" content="{robots}">{canon_tag}
  <meta name="theme-color" content="{C.THEME_COLOR}">
  <meta name="color-scheme" content="dark">
  <meta name="format-detection" content="telephone=no">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{C.NAME}">
  <meta property="og:title" content="{escape(full_title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta property="og:locale" content="{C.OG_LOCALE}">
  <meta name="twitter:card" content="summary">
  <link rel="icon" type="image/svg+xml" href="{p}assets/favicon.svg">
  <link rel="manifest" href="{p}site.webmanifest">
  <link rel="preload" href="{p}assets/fonts/jetbrains-mono-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{p}{ver('assets/css/site.css')}">
  {tokens_style()}
  <script type="application/ld+json">{ld}</script>{extra_head}
</head>
<body data-kind="{kind}" data-root="{p}"{body_attrs}>
{header(p, active, path_label)}
<main id="conteudo" tabindex="-1">
{body}
</main>
{footer(p)}
{site_data(p)}{js}
</body>
</html>
'''
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    BUILT.append(path)
    return path


# ---------------------------------------------------------------- peças comuns

def typed_h1(text, cls=""):
    return f'<h1 class="h1 {cls}" data-type>{escape(text)}</h1>'


def progress_bar(key, label=True):
    lab = f'<p class="bar__t" data-bar-text="{key}">0 feitos</p>' if label else ""
    return f'<div class="bar" data-bar="{key}" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" aria-label="Progresso"><span></span></div>{lab}'


def btn(href, text, cls="btn"):
    return f'<a class="{cls}" href="{href}"><span class="br">[</span> {text} <span class="br">]</span></a>'


# ---------------------------------------------------------------- páginas

def build_index():
    total = sum(len(m.EXS) for m in MODS)
    boot = "".join(f'<li data-boot><span class="ok">[ ok ]</span> {fmt(t)}</li>' for t in INI.BOOT(len(MODS), total, EX.total()))
    facts = "".join(f'<li><span class="fact__k">{escape(k)}</span><span class="fact__v">{fmt(v)}</span></li>' for k, v in INI.FACTS)
    about = paras(INI.ABOUT)
    how = "".join(
        f'<a class="card" href="{h}" data-rv><span class="card__k">{escape(k)}</span><h3>{escape(t)}</h3><p>{fmt(d)}</p></a>'
        for k, t, d, h in INI.HOW)
    mods = "".join(
        f'<li><a href="modulos/{m.ID}.html"><span class="pm__n">{m.NOME}</span>{progress_bar(m.ID, label=False)}<span class="pm__c" data-bar-text="{m.ID}" data-short>0/{len(m.EXS)}</span></a></li>'
        for m in MODS)
    keys = "".join(f"<li><kbd>{k}</kbd><span>{fmt(v)}</span></li>" for k, v in INI.KEYS)
    rules = "".join(f'<li data-rv><span class="rule__n">{i + 1:02d}</span><div><h3>{escape(t)}</h3><p>{fmt(d)}</p></div></li>' for i, (t, d) in enumerate(INI.RULES))
    body = f'''<section class="hero w">
  <ul class="boot" aria-label="Arranque">{boot}</ul>
  {typed_h1(INI.H1, "hero__t")}
  <p class="lead">{fmt(INI.LEAD)}</p>
  <div class="hero__cta">
    <a class="btn btn--go" href="tutorial.html" data-start><span class="br">[</span> Começar <span class="br">]</span></a>
    <a class="link" href="tutorial.html">como funciona <span aria-hidden="true">→</span></a><a class="link" href="exames.html">simular um exame <span aria-hidden="true">→</span></a>
  </div>
  <p class="hero__resume" data-resume hidden></p>
</section>

<section class="sec w" aria-labelledby="t-piscine">
  <p class="eyebrow"># o que é a piscine</p>
  <h2 id="t-piscine" class="h2">{escape(INI.ABOUT_H2)}</h2>
  <div class="split">
    {about}
    <ul class="facts" aria-label="A Piscine em números">{facts}</ul>
  </div>
</section>

<section class="sec w" aria-labelledby="t-regras">
  <p class="eyebrow"># as regras que pesam na nota</p>
  <h2 id="t-regras" class="h2">{escape(INI.RULES_H2)}</h2>
  <ol class="rules">{rules}</ol>
</section>

<section class="sec w" aria-labelledby="t-como">
  <p class="eyebrow"># como funciona este simulador</p>
  <h2 id="t-como" class="h2">{escape(INI.HOW_H2)}</h2>
  <div class="cards">{how}</div>
</section>

<section class="sec w" aria-labelledby="t-prog">
  <p class="eyebrow"># progresso (guardado neste navegador)</p>
  <h2 id="t-prog" class="h2">O teu caminho até ao BSQ</h2>
  <div class="prog-total">{progress_bar("all")}</div>
  <ul class="pm">{mods}</ul>
</section>

<section class="sec w sec--split" aria-labelledby="t-keys">
  <div>
    <p class="eyebrow"># atalhos</p>
    <h2 id="t-keys" class="h2">Navega como num terminal</h2>
    <p class="muted">{fmt(INI.KEYS_LEAD)}</p>
  </div>
  <ul class="keys">{keys}</ul>
</section>

<section class="sec w" aria-labelledby="t-resp">
  <div class="answers-cta">
    <p class="eyebrow"># respostas</p>
    <h2 id="t-resp" class="h2">{escape(INI.ANS_H2)}</h2>
    <p>{fmt(INI.ANS_P)}</p>
    {btn("respostas/index.html", "abrir as respostas", "btn btn--ghost")}
  </div>
</section>'''
    ld = [seo.website()]
    return page("index.html", f"{C.NAME}: treino para a Piscine da 42 Lisboa", C.DESCRIPTION, body,
                active="index.html", path_label="~", kind="home", ld_extra=ld)


def build_modulos():
    groups = {}
    for m in MODS:
        groups.setdefault(m.TIPO, []).append(m)
    order = [("Shell", "Shell: o terminal antes do C"), ("C", "C: dos ponteiros às árvores binárias"),
             ("Rush", "Rushes: projetos de grupo ao fim de semana"), ("Projeto", "Projeto final")]
    blocks = ""
    for key, title in order:
        if key not in groups:
            continue
        cards = "".join(
            f'''<a class="mcard" href="modulos/{m.ID}.html" data-rv>
  <span class="mcard__top"><span class="mcard__id">{m.NOME}</span><span class="mcard__n">{len(m.EXS)} ex.</span></span>
  <span class="mcard__d">{fmt(m.RESUMO)}</span>
  {progress_bar(m.ID, label=False)}
  <span class="mcard__p" data-bar-text="{m.ID}" data-short>0/{len(m.EXS)}</span>
</a>''' for m in groups[key])
        blocks += f'<section class="sec w" aria-label="{escape(title)}"><h2 class="h2 h2--sm"><span class="t-prompt">#</span> {escape(title)}</h2><div class="mgrid">{cards}</div></section>'
    total = sum(len(m.EXS) for m in MODS)
    body = f'''<section class="phero w">
  <p class="crumbs">~/<b>modulos</b></p>
  {typed_h1("Módulos")}
  <p class="lead">Os {len(MODS)} módulos da Piscine C da 42 Lisboa, pela ordem em que aparecem: {total} exercícios. Cada um tem enunciado, ficheiros a entregar, funções permitidas e um campo para colares o teu código. O progresso fica guardado neste navegador.</p>
  <div class="prog-total">{progress_bar("all")}</div>
</section>
{blocks}'''
    return page("modulos.html", "Módulos da Piscine", f"Os {len(MODS)} módulos da Piscine C da 42 Lisboa com {total} exercícios: Shell00–01, C00–C13, Rush00–02 e BSQ.",
                body, active="modulos.html", path_label="~/modulos", kind="modulos",
                crumbs=[("Início", "index.html"), ("Módulos", "modulos.html")])


def proto_label(proto):
    if "main(" in proto:
        return "main dado no enunciado"
    if "typedef" in proto:
        return "protótipo e estrutura"
    return "protótipo"


def exercise_html(mod, e):
    eid = ex_id(mod, e)
    files = ", ".join(f"<code>{escape(f.strip())}</code>" for f in e["ficheiros"].split(","))
    funcs = e["funcoes"]
    funcs_html = "Nenhuma" if funcs in ("", None, "Nenhuma") else ", ".join(f"<code>{escape(x.strip())}</code>" for x in funcs.split(","))
    proto = code_block(e["proto"], "c", proto_label(e["proto"])) if e.get("proto") else ""
    exemplo = term_block(e["exemplo"]) if e.get("exemplo") else ""
    nota = f'<p class="note"><span class="note__k">nota</span> {fmt(e["nota"])}</p>' if e.get("nota") else ""
    win_title = f'{e["pasta"]}{e["ficheiros"].split(",")[0].strip()}' if e["pasta"] else e["ficheiros"].split(",")[0].strip()
    lang = ex_lang(e)
    if e.get("sem_codigo"):
        mine = ""
    else:
        mine = f'''<div class="mine">
      <div class="mine__head"><label for="code-{eid}">O teu código</label><span class="mine__saved" data-saved aria-live="polite"></span></div>
      <textarea id="code-{eid}" class="mine__ta" data-code data-lang="{lang}" spellcheck="false" autocapitalize="off" autocomplete="off" rows="9" placeholder="Cola ou escreve aqui o teu código. Fica guardado neste navegador."></textarea>
      <div class="mine__bar">
        {'<button type="button" class="btn btn--sm" data-check>verificar norma (básico)</button>' if lang == "c" else ""}
        <button type="button" class="btn btn--sm btn--ghost" data-clear>limpar</button>
        <span class="mine__count" data-count>0 linhas</span>
      </div>
      <div class="mine__out" data-check-out aria-live="polite"></div>
    </div>'''
    return f'''<article class="ex" id="{eid}" data-ex="{eid}" data-rv>
  <header class="win"><span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="win__t">{escape(win_title)}</span><span class="pill" data-pill>por fazer</span></header>
  <div class="ex__body">
    <h2 class="ex__h"><span class="ex__num">{e["num"]}</span> {escape(e["nome"])}</h2>
    <dl class="spec">
      <div><dt>Pasta de entrega</dt><dd><code>{escape(e["pasta"] or "—")}</code></dd></div>
      <div><dt>Ficheiros a entregar</dt><dd>{files}</dd></div>
      <div><dt>Funções permitidas</dt><dd>{funcs_html}</dd></div>
    </dl>
    {paras(e["texto"])}
    {proto}{exemplo}{nota}
    {mine}
    <fieldset class="status">
      <legend>Estado</legend>
      <label><input type="radio" name="st-{eid}" value="todo" data-st checked> por fazer</label>
      <label><input type="radio" name="st-{eid}" value="doing" data-st> em curso</label>
      <label><input type="radio" name="st-{eid}" value="done" data-st> feito</label>
    </fieldset>
  </div>
</article>'''


def names_from_proto(proto):
    """Funções que o enunciado pede: as declaradas no protótipo (linhas que acabam em ';' ou ',').
    Definições de exemplo (como o 'ascending' do sort_list) e o main dado ficam de fora."""
    if not proto or "main(" in proto:
        return []
    out = []
    for line in proto.split("\n"):
        if not line.rstrip().endswith((";", ",")):
            continue
        m = re.match(r"^[\w \t\*]*?\b(\w+)\s*\(", line)
        if m and m.group(1) not in out and m.group(1) not in ("return", "if", "while", "sizeof"):
            out.append(m.group(1))
    return out


def funcs_list(funcoes):
    if funcoes in ("", None, "Nenhuma"):
        return []
    return [f.strip() for f in funcoes.split(",") if f.strip()]


def ex_spec(e, kind=None):
    """O que a moulinette do simulador verifica: tipo de entrega, ficheiros, funções permitidas e nomes."""
    files = [f.strip() for f in e["ficheiros"].split(",")]
    if kind is None:
        lang = ex_lang(e)
        sols = [read_sol(r) for r in e["sol"] if r.endswith((".c", ".h"))]
        if e.get("sem_codigo"):
            kind = "none"
        elif lang != "c":
            kind = "script"
        elif any(re.search(r"\bint\s+main\s*\(", t) for t in sols):
            kind = "programa"
        elif sols and all(r.endswith(".h") for r in e["sol"] if r.endswith((".c", ".h"))):
            kind = "header"
        else:
            kind = "funcao"
    return {"kind": kind, "files": files, "funcs": funcs_list(e["funcoes"]), "names": names_from_proto(e.get("proto"))}


def eval_tests(e):
    tests = []
    if e.get("exemplo"):
        tests.append("O exemplo do enunciado dá exatamente a mesma saída (compara com <code>cat -e</code>).")
    tests += [fmt(t) for t in e["limites"]]
    tests.append("Compila sem avisos com <code>gcc -Wall -Wextra -Werror</code> e passa na <code>norminette</code>." if ex_lang(e) == "c"
                 else "Funciona quando o corretor o executa no terminal dele.")
    return tests


def deliver_html(mod):
    data = {"mod": mod.ID, "nome": mod.NOME,
            "exs": [{"id": ex_id(mod, e), "num": e["num"], "nome": e["nome"], "spec": ex_spec(e), "tests": eval_tests(e)}
                    for e in mod.EXS]}
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    btns = "".join(f'<button type="button" class="btn btn--sm{" btn--ghost" if i > 0 else ""}" data-sh="{c}">{escape(t)}</button>'
                   for i, (c, t) in enumerate([("inscrever", "inscrever-me"), ("git clone", "git clone"), ("git status", "git status"),
                                               ("git add .", "git add ."), (f'git commit -m "{mod.ID}"', "git commit"),
                                               ("git push", "git push"), ("moulinette", "moulinette"), ("avaliacao", "avaliação")]))
    return f'''<section class="w deliver" id="entrega" data-deliver aria-labelledby="t-entrega">
  <p class="eyebrow"># entrega, como na 42 (sem prazo)</p>
  <h2 id="t-entrega" class="h2">Entregar o {mod.NOME}</h2>
  <p class="muted deliver__lead">O teu código vai para o repositório com <code>git push</code>, a moulinette corrige-o por ordem (o primeiro exercício errado faz com que os seguintes não contem) e depois há a avaliação, como entre colegas. Podes entregar quantas vezes quiseres.</p>
  <ol class="flow" aria-label="Passos da entrega">
    <li data-step="inscricao"><span>01</span>inscrição</li>
    <li data-step="push"><span>02</span>git push</li>
    <li data-step="moulinette"><span>03</span>moulinette</li>
    <li data-step="avaliacao"><span>04</span>avaliação</li>
  </ol>
  <p class="deliver__sum" data-deliver-sum aria-live="polite"></p>
  <div class="shell">
    <div class="shell__out" data-shell-out aria-live="polite"></div>
    <form class="shell__form" data-shell-form autocomplete="off">
      <label class="shell__pr" for="sh-{mod.ID}">piscine@42lisboa:~/{mod.ID}$</label>
      <input id="sh-{mod.ID}" class="shell__in" data-shell-in type="text" spellcheck="false" autocapitalize="off" enterkeyhint="go" placeholder="help">
    </form>
  </div>
  <div class="shell__btns">{btns}</div>
  <div class="eval" data-eval hidden></div>
</section>
<script id="deliver-data" type="application/json">{js}</script>'''


def build_modulo(i, mod):
    prev = MODS[i - 1] if i > 0 else None
    nxt = MODS[i + 1] if i + 1 < len(MODS) else None
    index = "".join(
        f'<li><a href="#{ex_id(mod, e)}" data-idx="{ex_id(mod, e)}"><i class="dot" aria-hidden="true"></i><span class="idx__n">{e["num"]}</span><span class="idx__t">{escape(e["nome"])}</span></a></li>'
        for e in mod.EXS)
    exs = "\n".join(exercise_html(mod, e) for e in mod.EXS)
    intro = paras(mod.INTRO, "txt intro") if mod.INTRO else ""
    pn = ""
    if prev:
        pn += f'<a class="mnav__a" href="{prev.ID}.html" data-prev rel="prev"><span class="mute">← anterior</span><b>{prev.NOME}</b></a>'
    else:
        pn += '<span></span>'
    if nxt:
        pn += f'<a class="mnav__a mnav__a--r" href="{nxt.ID}.html" data-next rel="next"><span class="mute">seguinte →</span><b>{nxt.NOME}</b></a>'
    deliver = deliver_html(mod)
    body = f'''<section class="phero w">
  <p class="crumbs"><a href="../modulos.html">~/modulos</a>/<b>{mod.ID}</b></p>
  {typed_h1(mod.NOME)}
  <p class="lead">{fmt(mod.RESUMO)}</p>
  <p class="meta"><span>[ {len(mod.EXS)} exercícios ]</span><span>[ {escape(mod.DIAS)} ]</span><a class="link" href="#entrega">ir para a entrega ↓</a></p>
  <div class="prog-total">{progress_bar(mod.ID)}</div>
  {intro}
</section>
<div class="w mod">
  <aside class="idx" aria-label="Exercícios de {mod.NOME}">
    <p class="idx__h">exercícios</p>
    <ol>{index}<li><a href="#entrega" class="idx__deliver" data-idx="entrega"><i class="dot" aria-hidden="true"></i><span class="idx__n">git push</span><span class="idx__t">entrega</span></a></li></ol>
    <p class="idx__keys"><kbd>j</kbd> <kbd>k</kbd> para saltar</p>
  </aside>
  <div class="exs">
{exs}
  </div>
</div>
{deliver}
<nav class="w mnav" aria-label="Outros módulos">{pn}</nav>'''
    desc = f"{mod.NOME} da Piscine C da 42 Lisboa: {len(mod.EXS)} exercícios com enunciado em português, ficheiros, funções permitidas e campo para treinar."
    ld = [seo.learning(mod, f"modulos/{mod.ID}.html")]
    return page(f"modulos/{mod.ID}.html", f"{mod.NOME}: exercícios", desc, body, active="modulos.html",
                path_label=f"~/modulos/{mod.ID}", kind="modulo", body_attrs=f' data-mod="{mod.ID}"',
                crumbs=[("Início", "index.html"), ("Módulos", "modulos.html"), (mod.NOME, f"modulos/{mod.ID}.html")],
                ld_extra=ld, scripts=("assets/js/entrega.js",))


def build_exames():
    pool = {}
    for n in sorted(EX.NIVEIS):
        items = []
        for e in EX.NIVEIS[n]:
            kind = "programa" if e["tipo"] == "programa" else "funcao"
            items.append({"nome": e["nome"], "tipo": e["tipo"], "ficheiros": e["ficheiros"], "funcoes": e["funcoes"],
                          "texto": paras(e["texto"], "x"),
                          "proto": code_block(e["proto"], "c", proto_label(e["proto"])) if e.get("proto") else "",
                          "exemplo": term_block(e["exemplo"]) if e.get("exemplo") else "",
                          "spec": {"kind": kind, "files": [f.strip() for f in e["ficheiros"].split(",")],
                                   "funcs": funcs_list(e["funcoes"]), "names": names_from_proto(e.get("proto"))},
                          "tests": (["O exemplo do enunciado dá exatamente a mesma saída (compara com <code>cat -e</code>)."] if e.get("exemplo") else [])
                          + [fmt(t) for t in e["limites"]]
                          + ["Compila sem avisos com <code>gcc -Wall -Wextra -Werror</code>."]})
        pool[str(n)] = items
    data = json.dumps({"exams": EX.EXAMES, "levels": pool}, ensure_ascii=False).replace("</", "<\\/")
    cards = "".join(
        f'''<li class="xcard" data-rv>
  <label><input type="radio" name="exam" value="{x["id"]}"{" checked" if j == 0 else ""}>
    <span class="xcard__n">{escape(x["nome"])}</span>
    <span class="xcard__d">{fmt(x["desc"])}</span>
    <span class="xcard__t">na Piscine: {x["duracao"] // 60} h · aqui: sem limite · level 0 a {x["max_nivel"]}</span>
  </label>
</li>''' for j, x in enumerate(EX.EXAMES))
    levels = "".join(f"<li><b>level {n}</b> <span>{len(EX.NIVEIS[n])} exercícios</span></li>" for n in sorted(EX.NIVEIS))
    sh_btns = "".join(f'<button type="button" class="btn btn--sm{" btn--ghost" if c not in ("git push", "grademe") else ""}" data-xs="{c}">{t}</button>'
                      for c, t in [("status", "status"), ("git status", "git status"), ("git add .", "git add ."),
                                   ("git commit -m \"rendu\"", "git commit"), ("git push", "git push"), ("grademe", "grademe")])
    body = f'''<section class="phero w">
  <p class="crumbs">~/<b>exames</b></p>
  {typed_h1("examshell")}
  <p class="lead">{fmt(EX.LEAD)}</p>
</section>
<div class="w exam" data-exam-app>
  <section class="exam__setup" data-setup aria-labelledby="t-setup">
    <h2 id="t-setup" class="h2 h2--sm"><span class="t-prompt">$</span> escolhe o exame</h2>
    <ul class="xcards">{cards}</ul>
    <div class="exam__opts">
      <label for="x-login">login</label>
      <input id="x-login" class="field" data-login type="text" spellcheck="false" autocapitalize="off" maxlength="12" placeholder="o teu login" value="piscine">
    </div>
    <div class="txt exam__rules">{"".join(f"<p>{fmt(t)}</p>" for t in EX.REGRAS)}</div>
    <ul class="levels" aria-label="Exercícios por nível">{levels}</ul>
    <button class="btn btn--go" type="button" data-begin><span class="br">[</span> entrar no examshell <span class="br">]</span></button>
  </section>

  <section class="exam__run" data-xrun hidden aria-labelledby="t-run">
    <div class="xbar" data-xbar>
      <div><span class="mute">exame</span> <b data-x-name></b></div>
      <div><span class="mute">level</span> <b data-x-level>0</b></div>
      <div class="xbar__time" role="timer" aria-live="off"><span class="mute">tempo<span class="xbar__x"> (sem limite)</span></span> <b data-x-time>00:00:00</b></div>
      <div><span class="mute"><span class="xbar__x">níveis </span>feitos</span> <b data-x-done>0</b></div>
    </div>
    <article class="ex ex--exam">
      <header class="win"><span class="win__dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="win__t" data-x-subject>subjects/</span><span class="pill" data-x-try>tentativa 1</span></header>
      <div class="ex__body">
        <h2 id="t-run" class="ex__h"><span class="ex__num" data-x-lvtag>level 0</span> <span data-x-title></span></h2>
        <dl class="spec">
          <div><dt>Ficheiros a entregar</dt><dd data-x-files></dd></div>
          <div><dt>Funções permitidas</dt><dd data-x-funcs></dd></div>
          <div><dt>Tipo</dt><dd data-x-type></dd></div>
        </dl>
        <div class="txt" data-x-text></div>
        <div data-x-proto></div>
        <div data-x-example></div>
        <div class="mine">
          <div class="mine__head"><label for="x-code" data-x-file>rendu/</label><span class="mine__saved" data-x-saved aria-live="polite"></span></div>
          <textarea id="x-code" class="mine__ta" data-x-code spellcheck="false" autocapitalize="off" autocomplete="off" rows="14" placeholder="Escreve aqui o ficheiro. Testa-o no teu terminal e depois entrega: git add, git commit e git push. A seguir, grademe."></textarea>
        </div>
      </div>
    </article>
    <div class="shell shell--exam">
      <div class="shell__out" data-shell-out aria-live="polite"></div>
      <form class="shell__form" data-shell-form autocomplete="off">
        <label class="shell__pr" for="x-sh" data-x-prompt>examshell&gt;</label>
        <input id="x-sh" class="shell__in" data-shell-in type="text" spellcheck="false" autocapitalize="off" enterkeyhint="go" placeholder="help">
      </form>
    </div>
    <div class="shell__btns">{sh_btns}<button type="button" class="btn btn--sm btn--ghost btn--danger" data-x-stop>terminar exame</button></div>
    <section class="grade" data-x-grade hidden aria-labelledby="t-grade">
      <h3 id="t-grade" class="h3">grademe: verificação final</h3>
      <p class="muted">A entrega passou nas verificações automáticas. Como o simulador não executa C, falta o que o examshell testa a correr o teu programa: corre estes testes no teu terminal e diz se passam todos.</p>
      <ul class="bul" data-x-tests></ul>
      <div class="exam__act">
        <button class="btn btn--go" type="button" data-x-pass><span class="br">[</span> passa em todos <span class="br">]</span></button>
        <button class="btn btn--ghost" type="button" data-x-fail>falha algum</button>
      </div>
    </section>
  </section>

  <section class="exam__end" data-end hidden aria-labelledby="t-end">
    <h2 id="t-end" class="h2" data-end-title>Exame terminado</h2>
    <div class="txt" data-end-text></div>
    <ol class="trail" data-end-list></ol>
    <button class="btn btn--go" type="button" data-again><span class="br">[</span> novo exame <span class="br">]</span></button>
  </section>

  <section class="exam__hist" aria-labelledby="t-hist">
    <h2 id="t-hist" class="h2 h2--sm"><span class="t-prompt">$</span> histórico</h2>
    <ol class="hist" data-hist><li class="mute">Ainda não fizeste nenhum exame neste navegador.</li></ol>
  </section>
</div>
<script id="exam-data" type="application/json">{data}</script>'''
    return page("exames.html", "Simulador de exames (examshell)",
                "Simulador do examshell da Piscine C: exercícios sorteados por níveis (level 0 a 5), entrega com git push e grademe, sem dicas e sem limite de tempo.",
                body, active="exames.html", path_label="~/exames", kind="exames", scripts=("assets/js/entrega.js", "assets/js/exame.js"),
                crumbs=[("Início", "index.html"), ("Exames", "exames.html")])


def build_tutorial():
    toc = "".join(f'<li><a href="#{i}">{escape(t)}</a></li>' for i, t, _, _ in TUT.SECOES)
    secs = ""
    for i, t, ps, term in TUT.SECOES:
        tb = term_block(term, "terminal") if term else ""
        secs += f'''<section class="rule tut" id="{i}" data-rv>
  <h2 class="h2 h2--sm"><span class="t-prompt">#</span> {escape(t)}</h2>
  {paras(ps)}
  {tb}
</section>'''
    body = f'''<section class="phero w">
  <p class="crumbs">~/<b>tutorial</b></p>
  {typed_h1(TUT.H1)}
  <p class="lead">{fmt(TUT.LEAD)}</p>
  <div class="hero__cta">{btn("modulos/shell00.html", "começar pelo Shell00", "btn btn--go")}<a class="link" href="exames.html">ou entrar no examshell <span aria-hidden="true">→</span></a><a class="link" href="respostas/index.html">respostas (tenta primeiro sozinho) <span aria-hidden="true">→</span></a></div>
</section>
<div class="w norm">
  <nav class="norm__toc" aria-label="Secções"><p class="idx__h">tutorial</p><ol>{toc}</ol></nav>
  <div class="norm__body">{secs}</div>
</div>'''
    return page("tutorial.html", "Introdução e tutorial",
                "Como usar o simulador da Piscine: exercícios, entrega com git push, moulinette, avaliação, examshell sem tempo limite, atalhos e progresso.",
                body, active="tutorial.html", path_label="~/tutorial", kind="tutorial",
                crumbs=[("Início", "index.html"), ("Tutorial", "tutorial.html")])


def build_norminette():
    toc = "".join(f'<li><a href="#{r["id"]}">{escape(r["titulo"])}</a></li>' for r in NORMA.REGRAS)
    secs = ""
    for r in NORMA.REGRAS:
        ex_html = ""
        if r.get("mal"):
            ex_html += f'<div class="cmp__i cmp__i--bad"><p class="cmp__k">✗ errado</p>{code_block(r["mal"], "c", r.get("ficheiro_mal", "errado.c"))}</div>'
        if r.get("bem"):
            ex_html += f'<div class="cmp__i cmp__i--ok"><p class="cmp__k">✓ certo</p>{code_block(r["bem"], "c", r.get("ficheiro_bem", "certo.c"))}</div>'
        cmp = f'<div class="cmp">{ex_html}</div>' if ex_html else ""
        secs += f'''<section class="rule" id="{r["id"]}" data-rv>
  <h2 class="h2 h2--sm"><span class="t-prompt">#</span> {escape(r["titulo"])}</h2>
  {paras(r["texto"])}
  {cmp}
</section>'''
    body = f'''<section class="phero w">
  <p class="crumbs">~/<b>norminette</b></p>
  {typed_h1("norminette")}
  <p class="lead">{fmt(NORMA.LEAD)}</p>
  {term_block(NORMA.TERM, "terminal")}
</section>
<div class="w norm">
  <nav class="norm__toc" aria-label="Regras"><p class="idx__h">regras</p><ol>{toc}</ol></nav>
  <div class="norm__body">{secs}</div>
</div>'''
    return page("norminette.html", "Norminette: as regras da Norma em resumo",
                "Resumo das regras principais da Norma da 42 que a norminette verifica, com exemplos de código certo e errado.",
                body, active="norminette.html", path_label="~/norminette", kind="norma",
                crumbs=[("Início", "index.html"), ("Norminette", "norminette.html")])


# ---------------------------------------------------------------- respostas

WARN = '''<div class="warn" role="note">
  <p class="warn__t">Tenta primeiro sozinho.</p>
  <p>Ler a solução antes de tentar tira-te o treino de que vais precisar no exame, onde não há respostas. Usa esta página só depois de teres o teu código a funcionar, ou depois de estares mesmo bloqueado. Cada solução está fechada: só abre quando carregares em «mostrar solução».</p>
</div>'''


def answer_html(prefix, e, mod_label):
    aid = f"r-{prefix}-{e['num'] if 'num' in e else e['nome']}"
    files = ""
    for rel in e["sol"]:
        name = os.path.basename(rel)
        lang = e.get("lang") if (e.get("lang") and len(e["sol"]) == 1) else realce.lang_of(name)
        files += code_block(read_sol(rel), lang, rel.split("/", 1)[1] if "/" in rel else name)
    if not files:
        files = '<p class="muted">Este exercício não tem código para entregar.</p>'
    steps = "".join(f"<li>{fmt(s)}</li>" for s in e["passos"])
    errs = "".join(f"<li>{fmt(s)}</li>" for s in e["erros"])
    lims = "".join(f"<li>{fmt(s)}</li>" for s in e["limites"])
    head = f'<span class="ex__num">{e.get("num") or "level " + str(e.get("nivel"))}</span> {escape(e["nome"])}'
    resumo = fmt(e["texto"][0]) if e["texto"] else ""
    return f'''<article class="ans" id="{aid}">
  <h2 class="ex__h">{head}</h2>
  <p class="ans__q">{resumo}</p>
  <details class="reveal">
    <summary><span class="reveal__s">mostrar solução</span><span class="reveal__h">esconder solução</span></summary>
    <div class="reveal__in">
      {files}
      <h3 class="h3">Passo a passo</h3><ol class="steps">{steps}</ol>
      <div class="ans__cols">
        <div><h3 class="h3">Erros comuns</h3><ul class="bul bul--bad">{errs}</ul></div>
        <div><h3 class="h3">Casos limite que a moulinette testa</h3><ul class="bul">{lims}</ul></div>
      </div>
    </div>
  </details>
</article>'''


def ans_nav(active):
    items = "".join(
        f'<li><a href="{m.ID}.html"{" aria-current=page" if active == m.ID else ""}>{m.NOME}</a></li>' for m in MODS)
    items += "".join(
        f'<li><a href="exame-nivel-{n}.html"{" aria-current=page" if active == f"n{n}" else ""}>exame · level {n}</a></li>'
        for n in sorted(EX.NIVEIS))
    return f'<nav class="ansnav" aria-label="Respostas por módulo"><ol>{items}</ol></nav>'


def build_respostas():
    rows = "".join(
        f'<li><a href="respostas/{m.ID}.html"><b>{m.NOME}</b><span>{len(m.EXS)} soluções</span></a></li>' for m in MODS)
    rows_x = "".join(
        f'<li><a href="respostas/exame-nivel-{n}.html"><b>level {n}</b><span>{len(EX.NIVEIS[n])} soluções</span></a></li>'
        for n in sorted(EX.NIVEIS))
    body = f'''<section class="phero w">
  <p class="crumbs">~/<b>respostas</b></p>
  {typed_h1("respostas")}
  {WARN}
  <p class="lead">Soluções comentadas de todos os exercícios e de todos os exercícios de exame, com explicação passo a passo, erros comuns e casos limite. O código segue a Norma (sem comentários dentro das funções, por isso a explicação está fora do código) e foi compilado com <code>gcc -Wall -Wextra -Werror</code> e testado.</p>
</section>
<section class="sec w" aria-labelledby="t-rm"><h2 id="t-rm" class="h2 h2--sm"><span class="t-prompt">#</span> módulos</h2><ul class="alist">{rows}</ul></section>
<section class="sec w" aria-labelledby="t-rx"><h2 id="t-rx" class="h2 h2--sm"><span class="t-prompt">#</span> exames</h2><ul class="alist">{rows_x}</ul></section>'''
    page("respostas/index.html", "Respostas", "Soluções comentadas da Piscine C e dos exames, numa área separada dos exercícios.",
         body.replace('href="respostas/', 'href="'), path_label="~/respostas", kind="respostas", robots="noindex, follow")
    for m in MODS:
        arts = "\n".join(answer_html(m.ID, e, m.NOME) for e in m.EXS)
        body = f'''<section class="phero w">
  <p class="crumbs"><a href="index.html">~/respostas</a>/<b>{m.ID}</b></p>
  {typed_h1(f"{m.NOME}: respostas")}
  {WARN}
</section>
<div class="w ans-wrap">{ans_nav(m.ID)}<div class="ans-list">{arts}</div></div>'''
        page(f"respostas/{m.ID}.html", f"{m.NOME}: respostas", f"Soluções comentadas de {m.NOME}, com passo a passo, erros comuns e casos limite.",
             body, path_label=f"~/respostas/{m.ID}", kind="respostas", robots="noindex, follow")
    for n in sorted(EX.NIVEIS):
        arts = "\n".join(answer_html(f"x{n}", e, f"level {n}") for e in EX.NIVEIS[n])
        body = f'''<section class="phero w">
  <p class="crumbs"><a href="index.html">~/respostas</a>/<b>exame-level-{n}</b></p>
  {typed_h1(f"exame: level {n}")}
  {WARN}
</section>
<div class="w ans-wrap">{ans_nav(f"n{n}")}<div class="ans-list">{arts}</div></div>'''
        page(f"respostas/exame-nivel-{n}.html", f"Exame, level {n}: respostas", f"Soluções comentadas dos exercícios de exame do level {n}.",
             body, path_label=f"~/respostas/level-{n}", kind="respostas", robots="noindex, follow")


def build_404():
    body = f'''<section class="phero w">
  <p class="crumbs">~/<b>404</b></p>
  {typed_h1("bash: página não encontrada")}
  <p class="lead">Este caminho não existe. Escreve <code>/</code> e depois <code>ls</code> para veres para onde podes ir.</p>
  {btn("index.html", "voltar ao início", "btn btn--go")}
</section>'''
    return page("404.html", "Página não encontrada", "Esta página não existe.", body, path_label="~/404", robots="noindex, follow")


def write_static():
    fav = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#07090b"/><path d="M14 20l12 12-12 12" fill="none" stroke="#4dff9a" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><rect x="32" y="40" width="18" height="6" rx="2" fill="#4dff9a"/></svg>'''
    with open(os.path.join(ROOT, "assets", "favicon.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(fav)
    m = {"name": C.NAME, "short_name": C.SHORT, "lang": C.LANG, "start_url": "index.html", "display": "browser",
         "background_color": C.COLORS["bg"], "theme_color": C.THEME_COLOR,
         "icons": [{"src": "assets/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}
    with open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)


def main():
    write_static()
    build_index()
    build_tutorial()
    build_modulos()
    for i, m in enumerate(MODS):
        build_modulo(i, m)
    build_exames()
    build_norminette()
    build_respostas()
    build_404()
    seo.robots(ROOT)
    seo.llms(ROOT, MODS, EX)
    seo.sitemap(ROOT, [b for b in BUILT if not b.startswith("respostas") and b != "404.html"])
    print(f"{len(BUILT)} páginas · {sum(len(m.EXS) for m in MODS)} exercícios · {EX.total()} de exame")


if __name__ == "__main__":
    main()
