# -*- coding: utf-8 -*-
from dados import ex

ID = "c06"
NOME = "C06"
TIPO = "C"
DIAS = "segunda semana"
RESUMO = "Os primeiros programas: `main(argc, argv)` e os argumentos da linha de comandos."
INTRO = [
    "Pela primeira vez entregas uma `main`. `argc` é o número de argumentos (incluindo o nome do programa) e `argv` é o array com eles: `argv[0]` é o nome, `argv[1]` o primeiro argumento, e assim por diante.",
]

W = "write"
EXS = [
    ex("ex00", "ft_print_program_name", "ft_print_program_name.c", W,
       ["É um programa, por isso o ficheiro tem de ter uma função `main`.",
        "Cria um programa que mostra o seu próprio nome."],
       exemplo="$>./a.out\n./a.out\n$>",
       sol=["c06/ex00/ft_print_program_name.c"],
       passos=["O nome com que o programa foi chamado está em `argv[0]`.",
               "Mede-se a string e escreve-se de uma vez, seguida de `\\n`.",
               "`(void)argc;` diz ao compilador que `argc` não é usado de propósito. Sem isso, o `-Wextra` avisa e o `-Werror` transforma o aviso em erro."],
       erros=["Esquecer o `(void)argc`: não compila com as flags da moulinette.",
              "Escrever um nome fixo como `a.out`: o nome muda conforme a forma como o programa é chamado."],
       limites=["Testam com caminhos diferentes, como `./a.out` e `../ex00/a.out`."]),

    ex("ex01", "ft_print_params", "ft_print_params.c", W,
       ["É um programa, por isso o ficheiro tem de ter uma função `main`.",
        "Cria um programa que mostra os argumentos recebidos, um por linha, pela mesma ordem da linha de comandos.",
        "Mostra todos os argumentos exceto `argv[0]`."],
       exemplo="$>./a.out test1 test2 test3\ntest1\ntest2\ntest3\n$>",
       sol=["c06/ex01/ft_print_params.c"],
       passos=["Percorre-se `argv` de 1 até `argc - 1` e escreve-se cada argumento seguido de `\\n`."],
       erros=["Começar em 0 e mostrar o nome do programa."],
       limites=["Sem argumentos, não mostra nada.",
                "Argumentos com espaços (entre aspas) aparecem numa só linha."]),

    ex("ex02", "ft_rev_params", "ft_rev_params.c", W,
       ["É um programa, por isso o ficheiro tem de ter uma função `main`.",
        "Cria um programa que mostra os argumentos recebidos, um por linha, pela ordem inversa da linha de comandos.",
        "Mostra todos os argumentos exceto `argv[0]`."],
       sol=["c06/ex02/ft_rev_params.c"],
       passos=["O mesmo ciclo do exercício anterior, de `argc - 1` a descer até 1."],
       erros=["Parar em 0 e mostrar o nome do programa no fim."],
       limites=["Sem argumentos, não mostra nada."]),

    ex("ex03", "ft_sort_params", "ft_sort_params.c", W,
       ["É um programa, por isso o ficheiro tem de ter uma função `main`.",
        "Cria um programa que mostra os argumentos recebidos ordenados pela ordem ASCII, um por linha.",
        "Mostra todos os argumentos exceto `argv[0]`."],
       sol=["c06/ex03/ft_sort_params.c"],
       passos=["Ordena-se o array `argv + 1` (que tem `argc - 1` elementos) com uma ordenação por bolha.",
               "A comparação é um `ft_strcmp`: a ordem ASCII põe maiúsculas antes de minúsculas e algarismos antes de letras.",
               "Trocam-se só os ponteiros: as strings ficam onde estão.",
               "Cada função auxiliar é `static`, e o ficheiro tem 4 funções (o máximo da Norma é 5)."],
       erros=["Ordenar só pelo primeiro carácter.",
              "Não tratar argumentos iguais ou vazios."],
       limites=["`Zebra` vem antes de `apple`; `\"\"` (argumento vazio) vem primeiro e aparece como linha vazia.",
                "Argumentos repetidos aparecem todos."]),
]
