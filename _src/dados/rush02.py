# -*- coding: utf-8 -*-
from dados import ex

ID = "rush02"
NOME = "Rush02"
TIPO = "Rush"
DIAS = "terceiro fim de semana"
RESUMO = "Converter números em palavras com um dicionário em ficheiro: leitura, parsing e memória dinâmica."
INTRO = [
    "Este rush junta tudo o que aprendeste até ao C10: `open`/`read`, `malloc`/`free`, strings e Makefile. Dividam o trabalho em três partes (ler o ficheiro, ler o dicionário, converter) e combinem as funções entre vocês.",
    "Todo o `malloc` tem de ser libertado: na avaliação verificam se há fugas de memória.",
]

EXS = [
    ex("ex00", "rush-02", "Makefile e todos os ficheiros necessários", "write, malloc, free, open, read, close",
       ["Cria um programa que recebe um número como argumento e o escreve por extenso.",
        "O executável chama-se `rush-02` e é compilado com `make fclean` e `make`.",
        "O programa aceita até 2 argumentos: com um, é o número a converter; com dois, o primeiro é um dicionário novo e o segundo é o número.",
        "Se o argumento não for um inteiro positivo válido, mostra `Error` seguido de uma quebra de linha.",
        "O programa lê o dicionário dado com o enunciado (`numbers.dict`) e usa os valores dele para escrever o resultado. Os valores podem ser alterados.",
        "Regras do dicionário: `[número][0 a n espaços]:[0 a n espaços][caracteres imprimíveis]\\n`.",
        "- os espaços antes e depois do valor são cortados;",
        "- o dicionário tem sempre pelo menos as chaves do original (os valores podem mudar e podem existir mais entradas);",
        "- só precisas das entradas originais: se alguém acrescentar `54: fifty-four`, usas na mesma `50: fifty` e `4: four`;",
        "- as entradas podem estar por qualquer ordem e pode haver linhas vazias;",
        "- se houver um erro a ler o dicionário, ou se ele não permitir escrever o número pedido, mostra `Dict Error\\n`."],
       exemplo="$> ./rush-02 42 | cat -e\nforty two$\n$> ./rush-02 0 | cat -e\nzero$\n$> ./rush-02 10.4 | cat -e\nError$\n$> ./rush-02 100000 | cat -e\none hundred thousand$\n$> grep \"20\" numbers.dict | cat -e\n20 : hey everybody !$\n$> ./rush-02 20 | cat -e\nhey everybody !$",
       sol=["rush02/ex00/Makefile", "rush02/ex00/rush02.h", "rush02/ex00/main.c", "rush02/ex00/read_file.c",
            "rush02/ex00/parse.c", "rush02/ex00/convert.c", "rush02/ex00/utils.c", "rush02/ex00/numbers.dict"],
       passos=["**Validar o número**: só algarismos, pelo menos um. Tiram-se os zeros à esquerda (`007` passa a `7`; `000` passa a `0`). O número fica como string, porque o dicionário vai até aos `undecillion` (10^36), muito para lá do `unsigned long`.",
               "**Ler o ficheiro**: lê-se tudo para memória com um buffer que duplica sempre que enche.",
               "**Ler o dicionário**: cada linha não vazia tem uma chave (algarismos), espaços, `:`, espaços e um valor imprimível. Cortam-se os espaços do fim do valor. Qualquer linha fora deste formato dá `Dict Error`.",
               "**Converter**: o número divide-se em grupos de três algarismos a partir da direita. Cada grupo de 1 a 999 escreve-se com as centenas (`three` + `hundred`), seguidas de 1–20 ou das dezenas certas diretamente, ou dezenas + unidades (`twenty` + `one`).",
               "Depois de cada grupo diferente de zero vem o nome da ordem de grandeza: `1000` (thousand), `1000000` (million), e assim por diante, construídos como `1` seguido de 3, 6, 9… zeros.",
               "**Duas passagens**: a primeira só verifica se o dicionário tem todas as palavras necessárias, sem escrever nada; a segunda escreve. Assim um `Dict Error` nunca aparece a meio de uma frase.",
               "No fim liberta-se o dicionário (cada chave, cada valor e o array)."],
       erros=["Converter o número para `int` ou `long`: falha com números grandes.",
              "Usar as entradas novas do dicionário (como `54: fifty-four`) em vez das originais.",
              "Não cortar os espaços à volta do valor: `20 : hey everybody !` tem de dar `hey everybody !`.",
              "Esquecer as linhas vazias do dicionário.",
              "Fugas de memória: libertar o dicionário também quando há erro."],
       limites=["`0`, `000`, `1`, `20`, `21`, `100`, `101`, `1001`, `999999`, `1000000002` e 10^36.",
                "Números maiores do que o dicionário permite dão `Dict Error`.",
                "Dicionário inexistente, linha sem `:`, valor vazio, chave com letras: `Dict Error`.",
                "Nota: o exemplo do enunciado mostra `error` em minúsculas para `10.4`, mas a regra diz `Error`. A solução segue a regra."]),
]
