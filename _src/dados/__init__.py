# -*- coding: utf-8 -*-
"""Conteúdo do site. Cada módulo tem o seu ficheiro (shell00.py, c00.py, …) com:

ID, NOME, TIPO, DIAS (texto curto), RESUMO, INTRO (parágrafos), EXS (lista de ex(...)).

As soluções ficam em _src/solucoes/<modulo>/<exercicio>/<ficheiro> e são lidas pelo build,
para poderem ser compiladas, testadas e passadas na norminette tal como estão.
"""
import importlib

ORDEM = ["shell00", "shell01", "c00", "c01", "c02", "c03", "c04", "c05", "c06", "c07",
         "c08", "c09", "c10", "c11", "c12", "c13", "rush00", "rush01", "rush02", "bsq"]


def ex(num, nome, ficheiros, funcoes, texto, proto=None, exemplo=None, sol=(), passos=(), erros=(),
       limites=(), pasta=None, nota=None, lang=None, sem_codigo=False):
    """Um exercício. `sol` é uma lista de caminhos relativos a _src/solucoes/."""
    return {"num": num, "nome": nome, "ficheiros": ficheiros, "funcoes": funcoes, "texto": list(texto),
            "proto": proto, "exemplo": exemplo, "sol": list(sol), "passos": list(passos), "erros": list(erros),
            "limites": list(limites), "pasta": pasta if pasta is not None else f"{num}/", "nota": nota,
            "lang": lang, "sem_codigo": sem_codigo}


def modulos():
    out = []
    for nome in ORDEM:
        try:
            m = importlib.import_module(f"dados.{nome}")
        except ModuleNotFoundError:
            continue
        out.append(m)
    return out
