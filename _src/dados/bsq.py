# -*- coding: utf-8 -*-
from dados import ex

ID = "bsq"
NOME = "BSQ"
TIPO = "Projeto"
DIAS = "fim da Piscine"
RESUMO = "O projeto final: encontrar e desenhar o maior quadrado possível num mapa com obstáculos."
INTRO = [
    "O BSQ (Biggest SQuare) fecha a Piscine. Junta tudo: leitura de ficheiros e da entrada padrão, validação rigorosa, memória dinâmica, um algoritmo eficiente e um Makefile que não volta a compilar o que não mudou.",
    "Os mapas de avaliação podem ser enormes: uma solução que testa todos os quadrados possíveis em cada casa é demasiado lenta. Gera mapas grandes com o script em Perl do enunciado.",
]

EXS = [
    ex("ex00", "bsq", "Makefile e todos os ficheiros necessários", "open, close, read, write, malloc, free, exit",
       ["Escreve um programa `bsq` que encontra e desenha o maior quadrado possível num mapa, evitando os obstáculos.",
        "O mapa vem num ficheiro passado como argumento. A primeira linha diz como ler o mapa: o número de linhas, o carácter «vazio», o carácter «obstáculo» e o carácter «cheio».",
        "O mapa é feito de caracteres «vazio», «obstáculo» e quebras de linha. O objetivo é trocar os «vazio» pelos «cheio» de forma a desenhar o maior quadrado possível.",
        "Se houver mais do que uma solução, escolhe-se o quadrado mais acima e, depois, o mais à esquerda.",
        "O programa trata de 1 a n ficheiros. Com mais de um mapa, cada solução ou erro é seguido de uma quebra de linha. Sem argumentos, lê da entrada padrão.",
        "Mapa válido: todas as linhas com o mesmo tamanho; pelo menos uma linha com pelo menos uma casa; cada linha termina numa quebra de linha; só aparecem os caracteres da primeira linha; os três caracteres são diferentes e imprimíveis (até algarismos).",
        "Num mapa inválido, mostra `map error` na saída de erro, seguido de uma quebra de linha, e passa ao mapa seguinte.",
        "O Makefile não pode voltar a compilar (relink) sem necessidade."],
       exemplo="%>cat example_file\n9.ox\n...........................\n....o......................\n............o..............\n...........................\n....o......................\n...............o...........\n...........................\n......o..............o.....\n..o.......o................\n%>./bsq example_file\n.....xxxxxxx...............\n....oxxxxxxx...............\n.....xxxxxxxo..............\n.....xxxxxxx...............\n....oxxxxxxx...............\n.....xxxxxxx...o...........\n.....xxxxxxx...............\n......o..............o.....\n..o.......o................",
       sol=["bsq/ex00/Makefile", "bsq/ex00/bsq.h", "bsq/ex00/main.c", "bsq/ex00/read.c", "bsq/ex00/parse.c", "bsq/ex00/solve.c"],
       passos=["**Ler**: o ficheiro (ou a entrada padrão) é lido inteiro para memória com um buffer que duplica de tamanho. Não se sabe o tamanho antes de ler, e a entrada padrão não se pode reler.",
               "**Validar o cabeçalho**: a primeira linha tem pelo menos 4 caracteres. Os três últimos são vazio, obstáculo e cheio; o resto é o número de linhas (só algarismos, maior do que 0). Os três caracteres têm de ser imprimíveis e diferentes.",
               "**Validar o mapa**: exatamente esse número de linhas, todas com a mesma largura (pelo menos 1), cada uma terminada em `\\n` e só com vazio e obstáculos. Nada depois da última linha. Cada `\\n` passa a `\\0` e o início de cada linha fica guardado, para escrever o mapa linha a linha no fim.",
               "**Encontrar o quadrado (programação dinâmica)**: para cada casa calcula-se o lado do maior quadrado cujo canto inferior direito é essa casa. É 0 num obstáculo e, numa casa vazia, 1 mais o menor dos três vizinhos (cima, esquerda e diagonal). Cada casa custa um passo, por isso um mapa de 2000×2000 resolve-se num instante.",
               "Só são precisas duas linhas de valores (a de cima e a atual), que trocam de papel no fim de cada linha.",
               "**Desempate**: percorre-se o mapa de cima para baixo e da esquerda para a direita, e só um quadrado **estritamente** maior substitui o melhor. Assim fica o primeiro encontrado, que é o mais acima e, depois, o mais à esquerda.",
               "**Escrever**: pinta-se o quadrado com o carácter «cheio» e escreve-se cada linha seguida de `\\n`. Com vários mapas, depois de cada um vem uma quebra de linha extra."],
       erros=["Testar todos os quadrados em todas as casas: demasiado lento nos mapas grandes da avaliação.",
              "Usar `>=` em vez de `>` na comparação: fica o último quadrado em vez do primeiro.",
              "Aceitar mapas sem `\\n` na última linha, com linhas vazias ou com mais linhas do que o cabeçalho diz.",
              "Esquecer a entrada padrão quando não há argumentos.",
              "Escrever `map error` na saída normal.",
              "Um Makefile que volta a criar o executável a cada `make` (relink)."],
       limites=["O exemplo do enunciado, com o ficheiro e pela entrada padrão.",
                "Mapas só com obstáculos (quadrado de tamanho 0: o mapa sai igual), só vazios, de uma linha, de uma coluna.",
                "Caracteres invulgares no cabeçalho, como espaços e algarismos (`5 #@`, `3012`).",
                "Vários ficheiros com um mapa inválido no meio.",
                "Mapas grandes (milhares de linhas e colunas) dentro do tempo limite."]),
]
