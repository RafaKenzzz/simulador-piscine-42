# -*- coding: utf-8 -*-
"""Dados estruturados (schema.org), robots.txt, llms.txt e sitemap.xml.

Com config.SITE vazio (site local), os endereços ficam relativos e o sitemap não é gerado,
porque o protocolo exige endereços absolutos.
"""
import datetime
import json
import os
import re

import config as C

TODAY = datetime.date.today().isoformat()
SITE = C.SITE


def url(path):
    if not SITE:
        return ""
    if path.endswith("index.html"):
        path = path[: -len("index.html")]
    return SITE + path


def strip(html):
    return re.sub(r"<[^>]+>|`", "", html)


def website():
    o = {"@type": "WebSite", "name": C.NAME, "inLanguage": C.LANG, "description": C.DESCRIPTION}
    if SITE:
        o.update({"@id": SITE + "#website", "url": SITE})
    return o


def learning(mod, path):
    o = {"@type": "LearningResource", "name": f"{mod.NOME}: exercícios da Piscine C", "inLanguage": C.LANG,
         "learningResourceType": "exercício", "educationalLevel": "iniciante",
         "teaches": strip(mod.RESUMO), "numberOfItems": len(mod.EXS)}
    if SITE:
        o["url"] = url(path)
    return o


def graph(path, name, desc, crumbs, extra):
    page = {"@type": "WebPage", "name": name, "description": desc, "inLanguage": C.LANG, "dateModified": TODAY}
    if SITE:
        page["url"] = url(path)
        page["isPartOf"] = {"@id": SITE + "#website"}
    if crumbs:
        items = []
        for i, (n, p) in enumerate(crumbs):
            it = {"@type": "ListItem", "position": i + 1, "name": n}
            if SITE:
                it["item"] = url(p)
            items.append(it)
        page["breadcrumb"] = {"@type": "BreadcrumbList", "itemListElement": items}
    nodes = [page] + list(extra)
    return json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False,
                      separators=(",", ":")).replace("</", "<\\/")


def write(root, name, text):
    with open(os.path.join(root, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def robots(root):
    sm = f"\nSitemap: {SITE}sitemap.xml\n" if SITE else ""
    write(root, "robots.txt", f"""# {C.NAME}: assistentes de IA e motores de pesquisa são bem-vindos.
# As respostas (respostas/) não são indexadas, para não aparecerem antes dos enunciados.

User-agent: *
Allow: /
Disallow: /_src/
Disallow: /respostas/
{sm}""")


def llms(root, mods, ex):
    lines = [f"# {C.NAME}", "", f"> {C.DESCRIPTION}", "",
             "Site estático de treino. Não é oficial nem tem ligação à 42 Lisboa.", "",
             "## Páginas", "",
             "- [Início](index.html): o que é a Piscine e como funciona este simulador",
             "- [Tutorial](tutorial.html): como usar o simulador, entregar e fazer o exame",
             "- [Módulos](modulos.html): todos os módulos e exercícios, com entrega e moulinette",
             "- [Exames](exames.html): simulador do examshell por níveis, sem tempo limite",
             "- [Norminette](norminette.html): resumo das regras da Norma", "",
             "## Módulos", ""]
    for m in mods:
        lines.append(f"- [{m.NOME}](modulos/{m.ID}.html): {strip(m.RESUMO)} ({len(m.EXS)} exercícios)")
    lines += ["", "## Exames", ""]
    for n in sorted(ex.NIVEIS):
        lines.append(f"- level {n}: " + ", ".join(e["nome"] for e in ex.NIVEIS[n]))
    write(root, "llms.txt", "\n".join(lines) + "\n")


def sitemap(root, pages):
    path = os.path.join(root, "sitemap.xml")
    if not SITE:
        if os.path.exists(path):
            os.remove(path)
        return
    rows = "\n".join(f"  <url><loc>{url(p)}</loc><lastmod>{TODAY}</lastmod></url>" for p in pages)
    write(root, "sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n')
