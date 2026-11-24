# -*- coding: utf-8 -*-
from dados import ex

ID = "rush01"
NOME = "Rush01"
TIPO = "Rush"
DIAS = "segundo fim de semana"
RESUMO = "Skyscraper 4×4: preencher uma grelha de prédios com as vistas dadas. Backtracking em grupo."
INTRO = [
    "O primeiro rush com um algoritmo a sério. Antes de escrever código, resolvam um tabuleiro à mão em papel: percebe-se logo como funciona a contagem de prédios visíveis.",
]

EXS = [
    ex("ex00", "rush-01", "Todos os ficheiros necessários", "write, malloc, free",
       ["O código é compilado assim: `gcc -Wall -Wextra -Werror -o rush-01 *.c`. A pasta de entrega tem de ter todos os ficheiros necessários.",
        "Cria um programa que resolve este problema: num mapa de 4×4, coloca em cada casa uma caixa de altura 1 a 4, de forma a que cada linha e cada coluna veja o número certo de caixas a partir de cada ponto de vista (esquerda e direita nas linhas, cima e baixo nas colunas).",
        "Por exemplo, uma caixa de altura 3 esconde uma de altura 1 vista da esquerda; e quem olha da direita só vê uma caixa se a de altura 4 estiver encostada a esse lado.",
        "Cada linha e cada coluna só tem uma caixa de cada altura. O programa mostra a primeira solução que encontrar.",
        "O programa é lançado assim: `./rush-01 \"col1up col2up col3up col4up col1down col2down col3down col4down row1left row2left row3left row4left row1right row2right row3right row4right\"`. Cada valor é um carácter de `1` a `4`. Esta é a ÚNICA entrada aceitável; qualquer outra é um erro.",
        "Em caso de erro, ou se não houver solução, mostra `Error` seguido de uma quebra de linha."],
       exemplo="$> ./rush-01 \"4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2\" | cat -e\n1 2 3 4$\n2 3 4 1$\n3 4 1 2$\n4 1 2 3$",
       sol=["rush01/ex00/rush01.h", "rush01/ex00/main.c", "rush01/ex00/solve.c", "rush01/ex00/print.c"],
       passos=["**Validar a entrada**: 16 algarismos de `1` a `4` separados por um só espaço dão exatamente 31 caracteres, com algarismos nas posições pares e espaços nas ímpares. Qualquer outra coisa é `Error`.",
               "As vistas ficam num array de 16: colunas de cima (0–3), colunas de baixo (4–7), linhas da esquerda (8–11) e linhas da direita (12–15).",
               "**Contar o que se vê**: numa linha de quatro alturas, a primeira vê-se sempre; cada uma das seguintes vê-se se for mais alta do que todas as anteriores. `ft_visible(a, b, c, d)` faz essa contagem.",
               "**Backtracking**: preenche-se a grelha casa a casa (16 posições). Em cada casa tenta-se a altura 1, 2, 3 e 4, saltando as que já estão na mesma linha ou coluna.",
               "Quando uma linha fica completa, confirmam-se as vistas da esquerda e da direita; quando uma coluna fica completa, as de cima e de baixo. Se falhar, desfaz-se a escolha e tenta-se a altura seguinte.",
               "Se a casa 16 for alcançada, todas as restrições estão cumpridas: escreve-se a grelha. Se todas as tentativas falharem, `Error`.",
               "Num 4×4 há só 576 grelhas válidas, por isso esta procura é instantânea."],
       erros=["Aceitar espaços a mais, números de dois algarismos ou mais de 16 valores.",
              "Escrever `Error` na saída de erro: o enunciado não o pede, e o exemplo usa a saída normal.",
              "Confirmar as vistas só no fim: funciona, mas é muito mais lento.",
              "Pôr um espaço no fim de cada linha da solução."],
       limites=["Entradas inválidas: argumento vazio, sem argumento, 2 argumentos, 15 ou 17 valores, valor 0 ou 5, separadores errados.",
                "Vistas impossíveis (como todas a 1) dão `Error`.",
                "Todas as vistas que vêm de uma grelha válida têm de ter solução (testado com as 576)."]),
]
