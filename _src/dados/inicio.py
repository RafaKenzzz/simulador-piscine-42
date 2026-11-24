# -*- coding: utf-8 -*-
"""Texto da página inicial. Factos tirados dos enunciados (capítulo «Instructions») e do
repositório jotavare/42-piscine (avaliações e duração dos exames)."""


def BOOT(n_mods, n_ex, n_exam):
    return [
        f"módulos: Shell00–01, C00–C13, Rush00–02 e BSQ ({n_mods} módulos, {n_ex} exercícios)",
        f"examshell: {n_exam} exercícios de exame em 6 níveis (level 0 a 5)",
        "norminette: regras principais com exemplos certos e errados",
        "progresso: guardado neste navegador, sem conta nem servidor",
    ]


H1 = "Treina a Piscine antes de lá chegares."
LEAD = ("Os 20 módulos da Piscine C da 42 Lisboa, com enunciados em português, um simulador do examshell "
        "e as regras da Norminette. Escreves o código, marcas o que já fizeste e voltas quando quiseres.")

ABOUT_H2 = "26 dias, sem professores."
ABOUT = [
    "A Piscine é a seleção da 42: um mês intensivo, 26 dias, em que aprendes a programar em C com o método da escola. "
    "Não há aulas nem professores. Aprendes com os enunciados, com o `man`, com a internet e, sobretudo, com os outros "
    "candidatos. O próprio enunciado diz: se tiveres uma dúvida, pergunta ao colega da direita; se ele não souber, ao da esquerda.",
    "Cada módulo de Shell e de C é corrigido três vezes: por dois colegas, em avaliações de cerca de 15 minutos, "
    "e pela moulinette, um programa automático que compila e testa o teu código sem negociar. Os rushes são projetos "
    "de grupo, defendidos numa avaliação de 30 minutos.",
    "Às sextas-feiras há exame no examshell: 4 horas, sozinho, com exercícios que sobem de nível à medida que os acertas. "
    "Tens de te inscrever no evento e no projeto do exame durante a semana. A Piscine fecha com um exame final de 8 horas.",
]
FACTS = [
    ("26", "dias de Piscine"),
    ("20", "módulos: 2 de Shell, 14 de C, 3 rushes e o BSQ"),
    ("2 + 1", "correções por módulo: dois colegas e a moulinette"),
    ("4 h", "cada exame de sexta-feira"),
    ("8 h", "o exame final"),
    ("-42", "a nota de quem usa uma função proibida"),
]

RULES_H2 = "O que a moulinette não perdoa"
RULES = [
    ("Compila com flags", "A moulinette compila com `gcc -Wall -Wextra -Werror`. Um aviso passa a erro e, se não compilar, tens 0."),
    ("Norminette primeiro", "Antes de testar, a moulinette corre a norminette. Se o código não respeitar a Norma, o exercício falha, mesmo que funcione."),
    ("Por ordem de dificuldade", "Um exercício difícil certo não conta se um mais fácil antes dele estiver errado. Não saltes exercícios."),
    ("Funções proibidas valem -42", "Usar uma função que não está nas «funções permitidas» é batota. A nota é -42 e não se discute."),
    ("Só o que é pedido", "Nada de ficheiros a mais na pasta de entrega. Só entregas uma `main` quando o enunciado pede um programa."),
    ("Os exemplos contam", "Os exemplos mostram detalhes que o texto não diz: a quebra de linha final, os espaços, as vírgulas. Lê-os com atenção."),
]

HOW_H2 = "Quatro ferramentas, um objetivo"
HOW = [
    ("01 / módulos", "Exercícios e entrega", "Enunciado em português, ficheiros, funções permitidas e um campo para o código. No fim de cada módulo: git push, moulinette e avaliação, como na 42.", "modulos.html"),
    ("02 / exames", "Examshell", "Exercícios sorteados por level, entrega com git push e grademe, nenhuma dica e sem tempo limite. Se falhar, sai outro exercício do mesmo level.", "exames.html"),
    ("03 / norma", "Norminette", "As regras que a norminette verifica, cada uma com um exemplo errado e outro certo.", "norminette.html"),
    ("04 / código", "Verificação rápida", "Em cada exercício, um botão aponta os erros de Norma mais óbvios no teu código: linhas longas, `for`, funções com mais de 25 linhas. Não substitui a norminette.", "modulos/c00.html"),
]

KEYS_LEAD = "Tudo se faz pelo teclado. Carrega em `/` para abrir a linha de comandos e escreve `help`, ou carrega em `?` para veres os atalhos."
KEYS = [
    ("/", "abre a linha de comandos: `cd c03`, `open c03/ex02`, `progresso`, `ls`"),
    ("1–5", "início, tutorial, módulos, exames, norminette"),
    ("j  k", "exercício seguinte e anterior"),
    ("n  p", "módulo seguinte e anterior"),
    ("e", "escrever no exercício atual (Esc para sair)"),
    ("f", "marcar o exercício atual como feito"),
    ("?", "lista de atalhos"),
]

ANS_H2 = "Respostas, à parte."
ANS_P = ("As soluções comentadas estão numa área separada, sem ligações nas páginas de exercícios, para não espreitares "
         "sem querer. Cada solução vem fechada e traz o passo a passo, os erros comuns e os casos limite. Tenta primeiro sozinho.")
