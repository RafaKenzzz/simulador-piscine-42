# -*- coding: utf-8 -*-
from dados import ex

ID = "c03"
NOME = "C03"
TIPO = "C"
DIAS = "primeira semana"
RESUMO = "Comparar, juntar e procurar strings: `strcmp`, `strcat`, `strstr` e o traiçoeiro `strlcat`."
INTRO = [
    "Todos os exercícios reproduzem funções da biblioteca padrão. A moulinette chama a tua função e a original com os mesmos argumentos e compara o resultado.",
]

N = "Nenhuma"
EXS = [
    ex("ex00", "ft_strcmp", "ft_strcmp.c", N,
       ["Reproduz o comportamento da função `strcmp` (`man strcmp`)."],
       proto="int\tft_strcmp(char *s1, char *s2);",
       sol=["c03/ex00/ft_strcmp.c"],
       passos=["Avança-se enquanto os caracteres são iguais e `s1` não acabou.",
               "Devolve-se a diferença entre os primeiros caracteres diferentes: negativo se `s1` vem antes, positivo se vem depois, 0 se são iguais.",
               "Os caracteres são convertidos para `unsigned char` antes da subtração, como no `strcmp`."],
       erros=["Devolver só 1, 0 e -1: a moulinette pode comparar o valor exato com o do `strcmp`.",
              "Parar quando `s2` acaba mas `s1` não: `\"ab\"` contra `\"abc\"` tem de dar negativo."],
       limites=["Strings vazias, uma prefixo da outra, caracteres acima de 127."]),

    ex("ex01", "ft_strncmp", "ft_strncmp.c", N,
       ["Reproduz o comportamento da função `strncmp` (`man strncmp`)."],
       proto="int\tft_strncmp(char *s1, char *s2, unsigned int n);",
       sol=["c03/ex01/ft_strncmp.c"],
       passos=["Igual ao `ft_strcmp`, mas compara no máximo `n` caracteres.",
               "Com `n == 0` devolve-se logo 0.",
               "O ciclo pára em `n - 1` para a comparação final ser feita no carácter `n - 1`, no máximo."],
       erros=["Não tratar `n == 0`: `n - 1` com `unsigned int` dá um número enorme.",
              "Comparar um carácter a mais do que `n`."],
       limites=["`n` maior do que as duas strings; `n` a meio da primeira diferença."]),

    ex("ex02", "ft_strcat", "ft_strcat.c", N,
       ["Reproduz o comportamento da função `strcat` (`man strcat`)."],
       proto="char\t*ft_strcat(char *dest, char *src);",
       sol=["c03/ex02/ft_strcat.c"],
       passos=["Procura-se o `'\\0'` de `dest`: é aí que `src` começa a ser copiada.",
               "Copia-se `src` e termina-se com `'\\0'`. Devolve-se `dest`."],
       erros=["Copiar por cima do início de `dest`.",
              "Esquecer o `'\\0'` final."],
       limites=["`src` vazia não muda `dest`."]),

    ex("ex03", "ft_strncat", "ft_strncat.c", N,
       ["Reproduz o comportamento da função `strncat` (`man strncat`)."],
       proto="char\t*ft_strncat(char *dest, char *src, unsigned int nb);",
       sol=["c03/ex03/ft_strncat.c"],
       passos=["Como o `ft_strcat`, mas copia no máximo `nb` caracteres de `src`.",
               "Ao contrário do `strncpy`, o `strncat` termina **sempre** com `'\\0'`."],
       erros=["Não terminar com `'\\0'` quando se copiam exatamente `nb` caracteres."],
       limites=["`nb` 0, menor, igual e maior do que o tamanho de `src`."]),

    ex("ex04", "ft_strstr", "ft_strstr.c", N,
       ["Reproduz o comportamento da função `strstr` (`man strstr`)."],
       proto="char\t*ft_strstr(char *str, char *to_find);",
       sol=["c03/ex04/ft_strstr.c"],
       passos=["Para cada posição `i` de `str`, compara-se `to_find` a partir dali.",
               "Se a comparação chegar ao fim de `to_find`, encontrou-se: devolve-se `str + i`.",
               "Se `to_find` for vazia, devolve-se `str` (está no `man`). Se não encontrar, devolve-se `NULL` (0)."],
       erros=["Não voltar atrás depois de uma correspondência parcial: em `\"aaab\"`, `\"aab\"` começa na posição 1.",
              "Devolver `NULL` quando `to_find` é vazia."],
       limites=["`to_find` maior do que `str`; `str` vazia; correspondência no fim."]),

    ex("ex05", "ft_strlcat", "ft_strlcat.c", N,
       ["Reproduz o comportamento da função `strlcat` (`man strlcat`)."],
       proto="unsigned int\tft_strlcat(char *dest, char *src, unsigned int size);",
       sol=["c03/ex05/ft_strlcat.c"],
       passos=["`size` é o tamanho total do buffer `dest`, não o número de caracteres a juntar.",
               "Mede-se `dest`, mas sem passar de `size`, e mede-se `src`.",
               "Se `dest` já ocupa `size` ou mais, não se copia nada e devolve-se `size + strlen(src)`.",
               "Senão, copia-se `src` até o total chegar a `size - 1` caracteres, termina-se com `'\\0'` e devolve-se `strlen(dest) + strlen(src)` (com o tamanho inicial de `dest`)."],
       erros=["Tratar `size` como o número de caracteres a acrescentar, como no `strncat`.",
              "Devolver o tamanho final em vez do tamanho que se tentou criar.",
              "Ler `dest` para lá de `size` quando não tem `'\\0'` dentro desse tamanho."],
       limites=["É o exercício do C03 que mais chumba. Testam `size` 0, menor do que `dest`, igual e maior do que o total.",
                "O valor devolvido é comparado com o do `strlcat` original em todos os casos."]),
]
