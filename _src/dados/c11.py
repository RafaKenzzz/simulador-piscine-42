# -*- coding: utf-8 -*-
from dados import ex

ID = "c11"
NOME = "C11"
TIPO = "C"
DIAS = "terceira semana"
RESUMO = "Ponteiros para funções: aplicar, filtrar, ordenar e o programa `do-op`."
INTRO = [
    "Um ponteiro para função guarda o endereço de uma função. `int (*f)(int)` é «um ponteiro `f` para uma função que recebe um `int` e devolve um `int`». Chama-se como uma função normal: `f(42)`.",
]

N = "Nenhuma"
EXS = [
    ex("ex00", "ft_foreach", "ft_foreach.c", N,
       ["Cria a função `ft_foreach`, que aplica uma função a todos os elementos de um array de inteiros, pela ordem do array.",
        "Por exemplo, pode ser chamada assim para mostrar todos os inteiros do array: `ft_foreach(tab, 1337, &ft_putnbr);`"],
       proto="void\tft_foreach(int *tab, int length, void (*f)(int));",
       sol=["c11/ex00/ft_foreach.c"],
       passos=["Percorre-se o array de 0 a `length - 1` e chama-se `f(tab[i])` para cada elemento."],
       erros=["Aplicar fora de ordem ou ir até `length` (inclusive)."],
       limites=["`length` 0 não chama a função."]),

    ex("ex01", "ft_map", "ft_map.c", "malloc",
       ["Cria a função `ft_map`, que aplica uma função a todos os elementos de um array de inteiros (por ordem) e devolve um array novo com os resultados."],
       proto="int\t*ft_map(int *tab, int length, int (*f)(int));",
       sol=["c11/ex01/ft_map.c"],
       passos=["Reserva-se um array novo com `length` inteiros.",
               "Cada posição `i` recebe `f(tab[i])`. O array original não muda."],
       erros=["Escrever os resultados no array original.",
              "Esquecer o `sizeof(int)` no `malloc`."],
       limites=["O array original tem de ficar igual."]),

    ex("ex02", "ft_any", "ft_any.c", N,
       ["Cria uma função `ft_any` que devolve 1 se, passado à função `f`, pelo menos um elemento do array der algo diferente de 0. Caso contrário, devolve 0.",
        "A função é aplicada pela ordem do array. O array acaba num ponteiro nulo."],
       proto="int\tft_any(char **tab, int (*f)(char *));",
       sol=["c11/ex02/ft_any.c"],
       passos=["Percorre-se o array até ao ponteiro nulo.",
               "Logo que `f` devolva algo diferente de 0, devolve-se 1 sem testar os restantes."],
       erros=["Comparar com 1 em vez de 0: `f` pode devolver qualquer valor diferente de 0."],
       limites=["Array vazio (só o ponteiro nulo) devolve 0."]),

    ex("ex03", "ft_count_if", "ft_count_if.c", N,
       ["Cria uma função `ft_count_if` que devolve quantos elementos do array dão algo diferente de 0 quando passados à função `f`.",
        "A função é aplicada pela ordem do array."],
       proto="int\tft_count_if(char **tab, int length, int (*f)(char *));",
       sol=["c11/ex03/ft_count_if.c"],
       passos=["Aqui o tamanho vem em `length` (não há ponteiro nulo no fim). Conta-se cada elemento para o qual `f` não devolve 0."],
       erros=["Somar o valor devolvido por `f` em vez de contar 1."],
       limites=["`f` pode devolver valores diferentes de 1."]),

    ex("ex04", "ft_is_sort", "ft_is_sort.c", N,
       ["Cria uma função `ft_is_sort` que devolve 1 se o array estiver ordenado e 0 se não estiver.",
        "A função passada como argumento devolve um número negativo se o primeiro argumento for menor do que o segundo, 0 se forem iguais e um número positivo nos outros casos."],
       proto="int\tft_is_sort(int *tab, int length, int (*f)(int, int));",
       sol=["c11/ex04/ft_is_sort.c"],
       passos=["«Ordenado» vale para as duas ordens: crescente e decrescente.",
               "Verificam-se as duas ao mesmo tempo. Um par com `f > 0` estraga a crescente; um par com `f < 0` estraga a decrescente.",
               "Se alguma das duas sobreviver, está ordenado."],
       erros=["Só testar a ordem crescente: `9 4 4 -1` tem de dar 1."],
       limites=["Arrays com todos os valores iguais, com 0 ou 1 elemento: estão ordenados."]),

    ex("ex05", "do-op", "Makefile, do_op.h, main.c, ft_ops.c, ft_utils.c", "write",
       ["Cria um programa chamado `do-op`, que é executado com três argumentos: `do-op valor1 operador valor2`.",
        "Usa um array de ponteiros para funções para tratar do operador.",
        "Aceita os operadores `+`, `-`, `/`, `*` e `%`. Com um operador inválido, mostra `0`.",
        "Se o número de argumentos estiver errado, não mostra nada.",
        "Numa divisão por zero mostra `Stop : division by zero` e num resto por zero mostra `Stop : modulo by zero`."],
       exemplo="$> make clean\n$> make\n$> ./do-op\n$> ./do-op 1 + 1\n2\n$> ./do-op 42amis - --+-20toto12\n62\n$> ./do-op 1 p 1\n0\n$> ./do-op 1 + toto3\n1\n$> ./do-op toto3 + 4\n4\n$> ./do-op foo plus bar\n0\n$> ./do-op 25 / 0\nStop : division by zero\n$> ./do-op 25 % 0\nStop : modulo by zero",
       sol=["c11/ex05/Makefile", "c11/ex05/do_op.h", "c11/ex05/main.c", "c11/ex05/ft_ops.c", "c11/ex05/ft_utils.c"],
       passos=["Os números são lidos com o `ft_atoi` do C04 (espaços, vários sinais, algarismos). Por isso `42amis` dá 42, `--+-20toto12` dá -20 e `toto3` dá 0.",
               "Há uma função por operação e um array `ops` com as cinco, pela mesma ordem da string `\"+-/*%\"`. Encontrado o símbolo na posição `i`, o resultado é `ops[i](a, b)`.",
               "O `typedef int (*t_op)(int, int);` dá um nome ao tipo «ponteiro para função», o que torna a declaração do array legível.",
               "O operador tem de ser exatamente um carácter: `plus` ou `++` são inválidos e mostram 0.",
               "A divisão e o resto por zero são verificados antes de calcular. Todas as saídas terminam com quebra de linha."],
       erros=["Usar uma cadeia de `if` em vez do array de ponteiros para funções: o enunciado pede o array.",
              "Aceitar só o primeiro carácter do operador (`p` de `plus`).",
              "Mostrar alguma coisa com o número errado de argumentos.",
              "Esquecer o Makefile: a moulinette corre `make`."],
       limites=["Todos os testes do exemplo, com a quebra de linha final.",
                "`./do-op 1 + 2 3` (4 argumentos) não mostra nada."],
       lang="c"),

    ex("ex06", "ft_sort_string_tab", "ft_sort_string_tab.c", N,
       ["Cria a função `ft_sort_string_tab`, que ordena as strings de `tab` pela ordem ASCII.",
        "`tab` acaba num ponteiro nulo. A ordenação é feita trocando os ponteiros do array."],
       proto="void\tft_sort_string_tab(char **tab);",
       sol=["c11/ex06/ft_sort_string_tab.c"],
       passos=["Ordenação por bolha com `ft_strcmp`, até ao ponteiro nulo.",
               "Trocam-se os ponteiros; o conteúdo das strings não muda."],
       erros=["Copiar o conteúdo das strings em vez de trocar os ponteiros.",
              "Ler `tab[i + 1]` depois do ponteiro nulo."],
       limites=["Array vazio ou com um só elemento; strings repetidas ou vazias."]),

    ex("ex07", "ft_advanced_sort_string_tab", "ft_advanced_sort_string_tab.c", N,
       ["Cria a função `ft_advanced_sort_string_tab`, que ordena as strings de `tab` conforme o resultado da função passada como argumento.",
        "A ordenação é feita trocando os ponteiros. `tab` acaba num ponteiro nulo.",
        "Chamá-la com `ft_strcmp` como segundo argumento dá o mesmo resultado que `ft_sort_string_tab`."],
       proto="void\tft_advanced_sort_string_tab(char **tab, int (*cmp)(char *, char *));",
       sol=["c11/ex07/ft_advanced_sort_string_tab.c"],
       passos=["É o exercício anterior com `cmp` no lugar de `ft_strcmp`: se `cmp(a, b) > 0`, `a` deve ficar depois de `b`."],
       erros=["Interpretar o sinal de `cmp` ao contrário."],
       limites=["Testam com comparações diferentes: por tamanho, por ordem inversa."]),
]
