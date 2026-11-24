# -*- coding: utf-8 -*-
"""Destaque de sintaxe feito no build (sem bibliotecas no navegador).

highlight(codigo, lingua) devolve HTML já escapado, com <span class="t-…">.
Línguas: c, sh, make, txt (sem destaque).
"""
import re
from html import escape

C_KEYWORDS = {"if", "else", "while", "return", "break", "continue", "sizeof", "typedef", "struct",
              "static", "const", "extern", "union", "enum", "volatile", "register", "inline"}
C_TYPES = {"int", "char", "void", "long", "short", "unsigned", "signed", "float", "double",
           "size_t", "ssize_t", "t_bool", "t_point", "t_list", "t_btree", "t_stock_str", "bool"}
C_CONST = {"NULL", "TRUE", "FALSE", "SUCCESS", "EVEN_MSG", "ODD_MSG", "BUF_SIZE", "errno"}

C_RE = re.compile(r"""
 (?P<com>/\*[\s\S]*?\*/|//[^\n]*)
|(?P<pre>^[ \t]*\#[ \t]*(?:include|define|ifndef|ifdef|endif|if|else|elif|undef|pragma)\b)
|(?P<inc><[\w./]+\.h>)
|(?P<str>"(?:\\.|[^"\\\n])*")
|(?P<chr>'(?:\\.|[^'\\\n])+')
|(?P<num>\b(?:0[xX][0-9a-fA-F]+|\d+)[uUlL]*\b)
|(?P<id>[A-Za-z_]\w*)(?P<call>(?=[ \t]*\())?
""", re.X | re.M)

SH_KEYWORDS = {"if", "then", "else", "elif", "fi", "for", "in", "do", "done", "while", "case", "esac", "function"}
SH_RE = re.compile(r"""
 (?P<com>(?:(?<=\s)|^)\#[^\n]*)
|(?P<str>'[^']*'|"(?:\\.|[^"\\])*")
|(?P<var>\$\{?[A-Za-z_][\w]*\}?|\$[0-9@#?*])
|(?P<opt>(?<=[\s])--?[A-Za-z][\w-]*)
|(?P<num>\b\d+\b)
|(?P<cmd>(?:(?<=^)|(?<=\|)|(?<=\|\s)|(?<=;\s)|(?<=&&\s)|(?<=\$\()|(?<=xargs\s))[A-Za-z_./][\w./-]*)
|(?P<id>[A-Za-z_][\w-]*)
""", re.X | re.M)

MK_RE = re.compile(r"""
 (?P<com>\#[^\n]*)
|(?P<var>\$\([A-Za-z_]+\)|\$[@<^*?])
|(?P<tgt>^[A-Za-z0-9_.%/$()-]+(?=\s*:(?!=)))
|(?P<asg>^[A-Z_]+(?=\s*[:+?]?=))
|(?P<kw>\.PHONY|\.SUFFIXES)
""", re.X | re.M)


def _wrap(cls, text):
    return f'<span class="t-{cls}">{escape(text, quote=False)}</span>'


def _c(code):
    out, pos = [], 0
    for m in C_RE.finditer(code):
        out.append(escape(code[pos:m.start()], quote=False))
        kind = m.lastgroup if m.lastgroup != "call" else "id"
        text = m.group(0)
        if m.group("com"):
            out.append(_wrap("com", text))
        elif m.group("pre"):
            out.append(_wrap("pre", text))
        elif m.group("inc"):
            out.append(_wrap("str", text))
        elif m.group("str"):
            out.append(_wrap("str", text))
        elif m.group("chr"):
            out.append(_wrap("chr", text))
        elif m.group("num"):
            out.append(_wrap("num", text))
        else:
            word = m.group("id")
            if word in C_KEYWORDS:
                out.append(_wrap("kw", word))
            elif word in C_TYPES or re.fullmatch(r"t_\w+", word):
                out.append(_wrap("ty", word))
            elif word in C_CONST or re.fullmatch(r"[A-Z][A-Z0-9_]{2,}", word):
                out.append(_wrap("con", word))
            elif m.group("call") is not None:
                out.append(_wrap("fn", word))
            else:
                out.append(escape(word, quote=False))
        pos = m.end()
    out.append(escape(code[pos:], quote=False))
    return "".join(out)


def _sh(code):
    out, pos = [], 0
    for m in SH_RE.finditer(code):
        out.append(escape(code[pos:m.start()], quote=False))
        g, text = m.lastgroup, m.group(0)
        if g == "id":
            out.append(_wrap("kw", text) if text in SH_KEYWORDS else escape(text, quote=False))
        else:
            out.append(_wrap({"com": "com", "str": "str", "var": "var", "opt": "opt", "num": "num", "cmd": "fn"}[g], text))
        pos = m.end()
    out.append(escape(code[pos:], quote=False))
    return "".join(out)


def _make(code):
    out, pos = [], 0
    for m in MK_RE.finditer(code):
        out.append(escape(code[pos:m.start()], quote=False))
        g, text = m.lastgroup, m.group(0)
        out.append(_wrap({"com": "com", "var": "var", "tgt": "fn", "asg": "ty", "kw": "kw"}[g], text))
        pos = m.end()
    out.append(escape(code[pos:], quote=False))
    return "".join(out)


def highlight(code, lang):
    """Os tabs ficam no HTML (o CSS usa tab-size: 4), para o botão copiar manter a indentação da Norma."""
    if lang == "c":
        return _c(code)
    if lang == "sh":
        return _sh(code)
    if lang == "make":
        return _make(code)
    return escape(code, quote=False)


def lang_of(filename):
    f = filename.lower()
    if f.endswith((".c", ".h")):
        return "c"
    if f.endswith(".sh") or f in ("clean", "midls", "z.sh"):
        return "sh"
    if f == "makefile":
        return "make"
    return "txt"
