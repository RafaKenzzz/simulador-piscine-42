# -*- coding: utf-8 -*-
"""Simulador de exames. Os exercícios estão em exame0.py … exame5.py (um ficheiro por nível).

Fontes: joaquim-oliveira-neto/42-Piscine-C-Exam (levels 0 a 5) e nigal.freeshell.org/42/exam-review.php.
Duração: 4 h por exame semanal e 8 h no exame final (jotavare/42-piscine).
"""
import importlib

LEAD = ("Como o examshell da 42, mas sem relógio: entras com o teu login, recebes um exercício sorteado do level 0, "
        "escreves o ficheiro, entregas com git add, git commit e git push, e pedes a correção com grademe. "
        "Se passar, sobes de level; se falhar, recebes outro exercício do mesmo level. Não há dicas nem ligações para as respostas.")

REGRAS = [
    "**Entrega como no dia:** o examshell só corrige o que está no repositório. Escreve o código, faz `git add .`, `git commit -m \"…\"` e `git push`, e só depois `grademe`.",
    "**grademe:** primeiro, verificações automáticas: o ficheiro existe, há `main` só quando é um programa, a função tem o nome do enunciado e não há funções proibidas. Depois, os testes que o examshell faria: corre-os no teu terminal e diz se passam.",
    "**Se falhar:** recebes outro exercício do mesmo level, como na 42. O histórico de tentativas fica guardado.",
    "**Sem tempo limite:** o relógio só conta o tempo que levas. Na Piscine, os exames de sexta têm 4 horas e o final 8 horas; aqui treinas sem pressa. O exame fica guardado neste navegador e retoma onde estava.",
]

EXAMES = [
    {"id": "exam00", "nome": "Exam00", "duracao": 240, "max_nivel": 5,
     "desc": "Primeira sexta-feira. Para muitos candidatos, o primeiro contacto com o examshell."},
    {"id": "exam01", "nome": "Exam01", "duracao": 240, "max_nivel": 5,
     "desc": "Segunda sexta-feira. Mesmo formato, mesmos levels: o objetivo é ir mais longe."},
    {"id": "exam02", "nome": "Exam02", "duracao": 240, "max_nivel": 5,
     "desc": "Terceira sexta-feira. Boa altura para chegar às listas e ao level 4."},
    {"id": "final", "nome": "Exame final", "duracao": 480, "max_nivel": 5,
     "desc": "O último exame da Piscine. Na 42 tem o dobro do tempo dos semanais."},
]



def x(nivel, nome, tipo, funcoes, texto, proto=None, exemplo=None, ficheiros=None, sol=None,
      passos=(), erros=(), limites=(), lang="c"):
    return {"nivel": nivel, "nome": nome, "tipo": tipo, "funcoes": funcoes, "texto": list(texto), "proto": proto,
            "exemplo": exemplo, "ficheiros": ficheiros or f"{nome}.c",
            "sol": list(sol) if sol else [f"exame/{nome}/{nome}.c"],
            "passos": list(passos), "erros": list(erros), "limites": list(limites), "lang": lang}


NIVEIS = {}
for _n in range(6):
    try:
        _m = importlib.import_module(f"dados.exame{_n}")
    except ModuleNotFoundError:
        continue
    NIVEIS[_n] = _m.EXS


def total():
    return sum(len(v) for v in NIVEIS.values())
