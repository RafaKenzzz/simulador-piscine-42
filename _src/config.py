# -*- coding: utf-8 -*-
"""Definições do site. As cores são copiadas para o :root do CSS pelo build.py."""

# ---------------------------------------------------------------- identidade
NAME = "Simulador da Piscine"
SHORT = "piscine.sim"
PROMPT_USER = "piscine"
PROMPT_HOST = "42lisboa"
LANG = "pt-PT"
OG_LOCALE = "pt_PT"
TAGLINE = "Treina a Piscine da 42 Lisboa antes de te candidatares."
DESCRIPTION = ("Simulador de treino da Piscine C da 42 Lisboa: módulos Shell00–01, C00–C13, Rush00–02 e BSQ "
               "com enunciados em português, progresso guardado no navegador, simulador de exames por níveis "
               "e resumo da Norminette.")

# Endereço público, com / no fim. Vazio = site local (sem sitemap nem endereços absolutos).
SITE = "https://rafakenzzz.github.io/simulador-piscine-42/"

# ---------------------------------------------------------------- aspeto
FONT_MONO = '"JetBrains Mono"'
COLORS = {
    "bg": "#07090b",
    "bg-2": "#0c1013",
    "bg-3": "#121a1e",
    "line": "#1d272c",
    "line-2": "#2b3940",
    "fg": "#d5e2db",
    "fg-2": "#a3b5ac",
    "mute": "#73867d",
    "green": "#4dff9a",
    "green-2": "#2bd97a",
    "green-dim": "#0f3323",
    "cyan": "#5ce1ff",
    "cyan-dim": "#0c2e38",
    "amber": "#ffcc66",
    "red": "#ff7070",
    "violet": "#c4a7ff",
    "orange": "#ffa066",
}
THEME_COLOR = "#07090b"

# ---------------------------------------------------------------- navegação
# (ficheiro, rótulo, tecla). A página de respostas fica de fora de propósito:
# não há ligações para ela nas páginas de exercícios.
NAV = [("index.html", "início", "1"), ("tutorial.html", "tutorial", "2"), ("modulos.html", "módulos", "3"),
       ("exames.html", "exames", "4"), ("norminette.html", "norminette", "5")]

# Chave usada no localStorage (progresso, código, exames)
STORE = "p42"
