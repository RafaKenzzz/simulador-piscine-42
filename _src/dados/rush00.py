# -*- coding: utf-8 -*-
from dados import ex

ID = "rush00"
NOME = "Rush00"
TIPO = "Rush"
DIAS = "primeiro fim de semana"
RESUMO = "Desenhar um retângulo com `ft_putchar`. Primeiro projeto de grupo, com cinco variantes."
INTRO = [
    "Os rushes são projetos de grupo ao fim de semana, defendidos numa avaliação de cerca de 30 minutos. Cada grupo recebe uma das variantes (rush00 a rush04): todas pedem o mesmo retângulo com caracteres diferentes.",
    "Na defesa, o `main` é alterado para testar outros tamanhos, por exemplo `rush(123, 42)`. Todos os elementos do grupo têm de saber explicar o código.",
]

EXS = [
    ex("ex00", "Rush0X", "main.c, ft_putchar.c, rush0X.c", "write",
       ["Entrega `main.c`, `ft_putchar.c` e o teu `rush0X.c`, em que `0X` é o número do teu rush (por exemplo `rush00.c`).",
        "Cria a função `rush`, que recebe dois `int`, `x` e `y`, e desenha no ecrã um retângulo com `x` caracteres de largura e `y` de altura.",
        "O `main` vai ser alterado na avaliação para testar tudo o que deves tratar.",
        "Os caracteres de cada variante:",
        "- rush00: cantos `o`, bordas de cima e de baixo `-`, bordas laterais `|`;",
        "- rush01: `/` nos cantos de cima à esquerda e de baixo à direita, `\\` nos outros dois, bordas `*`;",
        "- rush02: cantos de cima `A`, cantos de baixo `C`, bordas `B`;",
        "- rush03: cantos da esquerda `A`, cantos da direita `C`, bordas `B`;",
        "- rush04: `A` em cima à esquerda e em baixo à direita, `C` nos outros dois cantos, bordas `B`.",
        "O interior é sempre feito de espaços."],
       proto="void\trush(int x, int y);\n\nint\tmain(void)\n{\n\trush(5, 5);\n\treturn (0);\n}",
       exemplo="rush00, rush(5, 3):\n$>./a.out\no---o\n|   |\no---o\n$>\n\nrush01, rush(5, 3):\n$>./a.out\n/***\\\n*   *\n\\***/\n$>\n\nrush02, rush(1, 5):\n$>./a.out\nA\nB\nB\nB\nC\n$>\n\nrush04, rush(4, 4):\n$>./a.out\nABBC\nB  B\nB  B\nCBBA\n$>",
       sol=["rush00/ex00/main.c", "rush00/ex00/ft_putchar.c", "rush00/ex00/rush00.c", "rush00/ex00/rush01.c",
            "rush00/ex00/rush02.c", "rush00/ex00/rush03.c", "rush00/ex00/rush04.c"],
       passos=["Cada linha tem três partes: o primeiro carácter, o do meio (repetido) e o último. A função `ft_line` recebe esses três e a largura.",
               "O retângulo tem três tipos de linha: a primeira, as do meio e a última. Em cada variante só mudam os caracteres passados a `ft_line`.",
               "Com `x == 1`, cada linha tem só o primeiro carácter; com `y == 1`, só há a primeira linha. É por isso que `rush(1, 5)` do rush02 dá `A B B B C` em coluna.",
               "Valores menores do que 1 não desenham nada (não está no enunciado, mas a avaliação costuma testar).",
               "As cinco variantes têm o mesmo código e só mudam os caracteres: é a melhor forma de explicar o projeto na defesa."],
       erros=["Escrever o último carácter também quando `x == 1` (dá `oo` em vez de `o`).",
              "Trocar largura e altura: `x` é o número de colunas.",
              "Não tratar `x` ou `y` a 0 ou negativos (o programa entra em ciclo ou desenha lixo).",
              "Entregar um `main.c` com outro nome de função ou sem `return (0);`."],
       limites=["Os exemplos do enunciado: `(5, 3)`, `(5, 1)`, `(1, 1)`, `(1, 5)` e `(4, 4)`.",
                "Tamanhos grandes como `(123, 42)` e valores 0 ou negativos."]),
]
