# -*- coding: utf-8 -*-
from dados import ex

ID = "c01"
NOME = "C01"
TIPO = "C"
DIAS = "primeira semana"
RESUMO = "Ponteiros: ler e escrever através de um endereço, trocar valores, percorrer arrays e strings."
INTRO = [
    "Este módulo é todo sobre ponteiros. Se `*` e `&` ainda te confundem: `&x` é o endereço de `x`; `*p` é o valor que está no endereço `p`.",
]

N = "Nenhuma"
EXS = [
    ex("ex00", "ft_ft", "ft_ft.c", N,
       ["Cria uma função que recebe um ponteiro para `int` e põe o valor `42` nesse `int`."],
       proto="void\tft_ft(int *nbr);",
       sol=["c01/ex00/ft_ft.c"],
       passos=["`nbr` é um endereço. `*nbr` é o `int` que está nesse endereço.",
               "Escrever em `*nbr` muda a variável de quem chamou a função, por exemplo `ft_ft(&n)` muda `n`."],
       erros=["Escrever `nbr = 42`: muda o ponteiro local e o compilador recusa (atribuir um int a um ponteiro)."],
       limites=["O teste faz `int n = 0; ft_ft(&n);` e verifica que `n == 42`."]),

    ex("ex01", "ft_ultimate_ft", "ft_ultimate_ft.c", N,
       ["Cria uma função que recebe um ponteiro para ponteiro para ponteiro… (nove vezes) para `int` e põe o valor `42` nesse `int`."],
       proto="void\tft_ultimate_ft(int *********nbr);",
       sol=["c01/ex01/ft_ultimate_ft.c"],
       passos=["Cada `*` desfaz um nível de endereço. Com nove `*` na declaração, são precisos nove `*` para chegar ao `int`.",
               "`*********nbr = 42;` resolve o exercício numa linha."],
       erros=["Contar mal os asteriscos: com oito, escreves num ponteiro e o compilador recusa."],
       limites=["O teste cria a cadeia de 9 ponteiros e confirma o valor no `int` do fundo."]),

    ex("ex02", "ft_swap", "ft_swap.c", N,
       ["Cria uma função que troca os valores de dois inteiros cujos endereços são passados como parâmetros."],
       proto="void\tft_swap(int *a, int *b);",
       sol=["c01/ex02/ft_swap.c"],
       passos=["Guarda-se `*a` numa variável temporária, copia-se `*b` para `*a` e o valor guardado para `*b`.",
               "Sem a variável temporária, o valor de `*a` perdia-se quando era escrito por cima."],
       erros=["Trocar os ponteiros locais (`tmp = a; a = b; b = tmp;`): não muda nada fora da função.",
              "Fazer `*a = *b; *b = *a;`: os dois ficam com o valor de `*b`."],
       limites=["Testam valores negativos e iguais."]),

    ex("ex03", "ft_div_mod", "ft_div_mod.c", N,
       ["Cria uma função que divide `a` por `b`, guarda o resultado no `int` apontado por `div` e o resto da divisão no `int` apontado por `mod`."],
       proto="void\tft_div_mod(int a, int b, int *div, int *mod);",
       sol=["c01/ex03/ft_div_mod.c"],
       passos=["`/` entre inteiros dá a divisão inteira (sem casas decimais) e `%` dá o resto.",
               "Os resultados são escritos nos endereços recebidos: `*div` e `*mod`."],
       erros=["Atribuir a `div` e `mod` em vez de `*div` e `*mod`."],
       limites=["Com negativos, C arredonda para zero: `-7 / 2` dá `-3` e `-7 % 2` dá `-1`.",
                "A divisão por zero não é testada (o resultado é indefinido)."]),

    ex("ex04", "ft_ultimate_div_mod", "ft_ultimate_div_mod.c", N,
       ["Cria uma função que divide `a` por `b`. O resultado fica no `int` apontado por `a` e o resto no `int` apontado por `b`."],
       proto="void\tft_ultimate_div_mod(int *a, int *b);",
       sol=["c01/ex04/ft_ultimate_div_mod.c"],
       passos=["O problema é a ordem: depois de escrever o resultado em `*a`, o valor original de `*a` desaparece, mas ainda é preciso para o resto.",
               "Por isso guarda-se primeiro o valor original numa variável e calcula-se tudo a partir dela."],
       erros=["Escrever `*a = *a / *b; *b = *a % *b;`: o resto é calculado com o resultado da divisão, não com o valor original."],
       limites=["`42` e `10` têm de dar `4` e `2`."]),

    ex("ex05", "ft_putstr", "ft_putstr.c", "write",
       ["Cria uma função que mostra uma string de caracteres na saída padrão."],
       proto="void\tft_putstr(char *str);",
       sol=["c01/ex05/ft_putstr.c"],
       passos=["Uma string em C é uma sequência de caracteres terminada por `'\\0'`.",
               "Escreve-se um carácter de cada vez e avança-se o ponteiro até ao `'\\0'`."],
       erros=["Escrever também o `'\\0'`.",
              "Acrescentar uma quebra de linha."],
       limites=["Uma string vazia não mostra nada."]),

    ex("ex06", "ft_strlen", "ft_strlen.c", N,
       ["Cria uma função que conta e devolve o número de caracteres de uma string."],
       proto="int\tft_strlen(char *str);",
       sol=["c01/ex06/ft_strlen.c"],
       passos=["Conta-se até encontrar o `'\\0'`, que não entra na conta."],
       erros=["Começar a contar em 1.",
              "Contar o `'\\0'`."],
       limites=["`\"\"` devolve 0."]),

    ex("ex07", "ft_rev_int_tab", "ft_rev_int_tab.c", N,
       ["Cria uma função que inverte um array de inteiros: o primeiro passa a último, e assim por diante.",
        "Os parâmetros são um ponteiro para `int` e o número de elementos do array."],
       proto="void\tft_rev_int_tab(int *tab, int size);",
       sol=["c01/ex07/ft_rev_int_tab.c"],
       passos=["Troca-se o elemento `i` com o `size - 1 - i`.",
               "Pára-se a meio (`i < size / 2`): se o ciclo fosse até ao fim, cada par seria trocado duas vezes e o array voltava ao início."],
       erros=["Ir até `size`: o array fica igual ao original.",
              "Errar o índice do fim (`size - i` em vez de `size - 1 - i`) e ler fora do array."],
       limites=["Arrays com tamanho par e ímpar; com 1 elemento ou 0, nada muda."]),

    ex("ex08", "ft_sort_int_tab", "ft_sort_int_tab.c", N,
       ["Cria uma função que ordena um array de inteiros por ordem crescente.",
        "Os parâmetros são um ponteiro para `int` e o número de elementos do array."],
       proto="void\tft_sort_int_tab(int *tab, int size);",
       sol=["c01/ex08/ft_sort_int_tab.c"],
       passos=["Ordenação por bolha: compara-se cada elemento com o seguinte e trocam-se se estiverem fora de ordem.",
               "Depois de uma troca, recomeça-se do início (`i = 0`). Quando se chega ao fim sem trocas, está ordenado.",
               "É lento para arrays grandes, mas curto, fácil de acertar e cabe nas 25 linhas."],
       erros=["Ir até `i < size` e comparar `tab[i]` com `tab[size]`, fora do array.",
              "Esquecer os valores repetidos: têm de ficar todos."],
       limites=["Negativos, repetidos, `INT_MIN` e `INT_MAX`, array já ordenado e array com 0 ou 1 elementos."]),
]
