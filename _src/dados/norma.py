# -*- coding: utf-8 -*-
"""Página Norminette. Regras e mensagens confirmadas na norminette 3.3 (norm_error.py).
Os exemplos «certo» passam na norminette quando se junta o cabeçalho da 42; os «errado» falham."""

LEAD = ("A Norma é o estilo de código obrigatório da 42 e a norminette é o programa que a verifica. "
        "A moulinette corre-a antes de testar o teu código: se falhar, o exercício falha, mesmo que funcione. "
        "Isto é um resumo das regras que mais apanham candidatos. Entre parênteses está o código de erro que a norminette mostra.")

TERM = """$> norminette ft_putchar.c
ft_putchar.c: OK!
$> norminette teste.c
teste.c: Error!
Error: SPACE_REPLACE_TAB    (line:   3, col:   8):	Found space when expecting tab
Error: FORBIDDEN_CS         (line:   4, col:   5):	Forbidden control structure
Error: RETURN_PARENTHESIS   (line:   5, col:  16):	Return value must be in parenthesis"""

REGRAS = [
    {
        "id": "cabecalho", "titulo": "Cabeçalho da 42", "ficheiro_bem": "ft_putchar.c",
        "texto": [
            "Todos os ficheiros `.c` e `.h` começam com o cabeçalho da 42: 11 linhas de comentário com o nome do ficheiro, o teu login e as datas (`INVALID_HEADER`).",
            "No Vim das máquinas da 42 crias o cabeçalho com `:Stdheader` ou com a tecla F1. Não o escrevas à mão: um espaço a mais e a norminette recusa-o.",
            "Nas soluções deste site o cabeçalho foi tirado para poupar espaço. Põe-no sempre nos teus ficheiros.",
        ],
        "bem": """/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: piscine <piscine@student.42lisboa.com>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/11/23 10:00:00 by piscine           #+#    #+#             */
/*   Updated: 2026/11/23 10:00:00 by piscine          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}""",
    },
    {
        "id": "nomes", "titulo": "Nomes",
        "texto": [
            "Variáveis, funções, ficheiros e pastas só com minúsculas, algarismos e `_` (snake_case) (`FORBIDDEN_CHAR_NAME`).",
            "Prefixos obrigatórios: `s_` para struct, `t_` para typedef, `u_` para union, `e_` para enum e `g_` para variáveis globais.",
            "Macros (`#define`) em MAIÚSCULAS (`MACRO_NAME_CAPITAL`).",
        ],
        "mal": """int	getMax(int firstValue, int secondValue)
{
	if (firstValue > secondValue)
		return (firstValue);
	return (secondValue);
}""",
        "bem": """int	get_max(int first_value, int second_value)
{
	if (first_value > second_value)
		return (first_value);
	return (second_value);
}""",
    },
    {
        "id": "linhas", "titulo": "25 linhas por função",
        "texto": [
            "O corpo de uma função tem no máximo 25 linhas, sem contar as chavetas `{` e `}` (`TOO_MANY_LINES`).",
            "Quando passa, divide o trabalho em funções auxiliares. É a regra que mais vezes obriga a repensar o código.",
            "Um ficheiro tem no máximo 5 funções (`TOO_MANY_FUNCS`). As funções que só esse ficheiro usa devem ser `static`.",
        ],
        "mal": """void	ft_print_comb(void)
{
	char	a;
	char	b;
	char	c;

	a = '0';
	while (a <= '7')
	{
		b = a + 1;
		while (b <= '8')
		{
			c = b + 1;
			while (c <= '9')
			{
				write(1, &a, 1);
				write(1, &b, 1);
				write(1, &c, 1);
				if (a != '7')
				{
					write(1, ",", 1);
					write(1, " ", 1);
				}
				c++;
			}
			b++;
		}
		a++;
	}
}""",
        "bem": """static void	ft_put3(char a, char b, char c)
{
	write(1, &a, 1);
	write(1, &b, 1);
	write(1, &c, 1);
	if (a != '7')
		write(1, ", ", 2);
}

void	ft_print_comb(void)
{
	char	a;
	char	b;
	char	c;

	a = '0';
	while (a <= '7')
	{
		b = a + 1;
		while (b <= '8')
		{
			c = b + 1;
			while (c <= '9')
				ft_put3(a, b, c++);
			b++;
		}
		a++;
	}
}""",
    },
    {
        "id": "colunas", "titulo": "80 colunas",
        "texto": [
            "Nenhuma linha passa das 80 colunas, comentários incluídos (`LINE_TOO_LONG`). Um tab conta até à próxima coluna múltipla de 4.",
            "Para partir uma condição longa, o operador lógico vai para o início da linha seguinte, nunca para o fim da anterior (`EOL_OPERATOR`).",
        ],
        "mal": """int	ft_is_space(char c)
{
	return (c == ' ' || c == '\\t' || c == '\\n' || c == '\\v' || c == '\\f' || c == '\\r');
}""",
        "bem": """int	ft_is_space(char c)
{
	return (c == ' ' || c == '\\t' || c == '\\n'
		|| c == '\\v' || c == '\\f' || c == '\\r');
}""",
    },
    {
        "id": "parametros", "titulo": "Parâmetros",
        "texto": [
            "Uma função recebe no máximo 4 parâmetros (`TOO_MANY_ARGS`). Se precisares de mais, junta-os numa estrutura.",
            "Uma função sem parâmetros declara-se com `void` entre parênteses (`NO_ARGS_VOID`).",
        ],
        "mal": """void	ft_print_numbers()
{
	write(1, "0123456789", 10);
}""",
        "bem": """void	ft_print_numbers(void)
{
	write(1, "0123456789", 10);
}""",
    },
    {
        "id": "variaveis", "titulo": "Variáveis",
        "texto": [
            "No máximo 5 variáveis por função (`TOO_MANY_VARS_FUNC`), todas declaradas no início (`VAR_DECL_START_FUNC`).",
            "Uma declaração por linha (`MULT_DECL_LINE`) e sem atribuição na mesma linha (`DECL_ASSIGN_LINE`).",
            "Depois das declarações vem uma linha vazia (`NL_AFTER_VAR_DECL`). É a única linha vazia permitida dentro de uma função.",
            "O nome das variáveis fica alinhado com tabs na mesma coluna (`MISALIGNED_VAR_DECL`).",
        ],
        "mal": """int	ft_strlen(char *str)
{
	int i = 0;
	while (str[i])
		i++;
	return (i);
}""",
        "bem": """int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}""",
    },
    {
        "id": "proibido", "titulo": "Estruturas proibidas",
        "texto": [
            "Proibido: `for`, `do … while`, `switch`, `case`, `goto` (`FORBIDDEN_CS`, `GOTO_FBIDDEN`).",
            "Proibido: o operador ternário `? :` (`TERNARY_FBIDDEN`) e arrays de tamanho variável, como `int tab[n];` (`VLA_FORBIDDEN`).",
            "Tudo se faz com `while` e `if … else if … else`.",
        ],
        "mal": """int	ft_abs(int n)
{
	return (n < 0 ? -n : n);
}

void	ft_putnstr(char *s, int n)
{
	int	i;

	for (i = 0; i < n; i++)
		write(1, &s[i], 1);
}""",
        "bem": """int	ft_abs(int n)
{
	if (n < 0)
		return (-n);
	return (n);
}

void	ft_putnstr(char *s, int n)
{
	int	i;

	i = 0;
	while (i < n)
	{
		write(1, &s[i], 1);
		i++;
	}
}""",
    },
    {
        "id": "instrucoes", "titulo": "Uma instrução por linha",
        "texto": [
            "Uma instrução por linha (`TOO_MANY_INSTR`) e uma atribuição por linha (`MULT_ASSIGN_LINE`).",
            "Nada de atribuições dentro de condições, como `while ((c = s[i]))` (`ASSIGN_IN_CONTROL`).",
            "Um `if` ou `while` de uma só instrução pode dispensar chavetas, mas a instrução vai para a linha seguinte.",
        ],
        "mal": """void	ft_swap(int *a, int *b)
{
	int	tmp;

	tmp = *a; *a = *b; *b = tmp;
}""",
        "bem": """void	ft_swap(int *a, int *b)
{
	int	tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}""",
    },
    {
        "id": "espacos", "titulo": "Espaços e tabs",
        "texto": [
            "A indentação é feita com tabs, nunca com espaços (`SPC_INSTEAD_TAB`). Entre o tipo e o nome de uma função ou variável também vai um tab.",
            "Um espaço depois de cada vírgula e de cada palavra-chave (`if (`, `while (`, `return (`) (`SPACE_AFTER_KW`), e à volta dos operadores (`SPC_BFR_OPERATOR`).",
            "O valor de `return` vai entre parênteses (`RETURN_PARENTHESIS`). Num `void`, escreve só `return ;` ou nada.",
            "Nada de espaços no fim da linha (`SPC_BEFORE_NL`) nem dois espaços seguidos (`CONSECUTIVE_SPC`).",
            "As chavetas `{` e `}` ficam sozinhas na sua linha (`BRACE_NEWLINE`).",
        ],
        "mal": """int	ft_max(int a,int b){
	if(a>b)
		return a;
	return b;
}""",
        "bem": """int	ft_max(int a, int b)
{
	if (a > b)
		return (a);
	return (b);
}""",
    },
    {
        "id": "vazias", "titulo": "Linhas vazias",
        "texto": [
            "Sem linhas vazias dentro de uma função, exceto a que separa as declarações do resto (`EMPTY_LINE_FUNCTION`).",
            "Uma linha vazia entre funções (`NEWLINE_PRECEDES_FUNC`), nunca duas seguidas (`CONSECUTIVE_NEWLINES`), e nenhuma no fim do ficheiro (`EMPTY_LINE_EOF`).",
        ],
        "mal": """int	ft_is_negative(int n)
{

	if (n < 0)
		return (1);

	return (0);
}""",
        "bem": """int	ft_is_negative(int n)
{
	if (n < 0)
		return (1);
	return (0);
}""",
    },
    {
        "id": "comentarios", "titulo": "Comentários",
        "texto": [
            "Comentários dentro do corpo de uma função são proibidos (`WRONG_SCOPE_COMMENT`).",
            "Podes comentar fora das funções, por exemplo por cima de cada uma. É o que fazem as soluções deste site.",
        ],
        "mal": """int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	// conta até ao '\\0'
	while (str[i])
		i++;
	return (i);
}""",
        "bem": """/*
** Conta os caracteres até ao '\\0' (que não conta).
*/
int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}""",
    },
    {
        "id": "headers", "titulo": "Ficheiros .h e pré-processador", "ficheiro_mal": "ft_point.c", "ficheiro_bem": "ft_point.h",
        "texto": [
            "Um `.h` tem proteção contra inclusão dupla com o nome do ficheiro em maiúsculas: `#ifndef FT_H`, `#define FT_H` … `#endif` (`HEADER_PROT_NAME`).",
            "Estruturas, typedefs, unions e enums só podem ser declarados em `.h` (`FORBIDDEN_STRUCT`, `FORBIDDEN_TYPEDEF`).",
            "`#define` só para constantes (`PREPROC_CONSTANT`). Macros com parâmetros são proibidas (`MACRO_FUNC_FORBIDDEN`), exceto quando o enunciado as pede (C08 ex01 e ex02).",
            "Os `#include` vão no início do ficheiro (`INCLUDE_START_FILE`) e nunca incluem um `.c` (`INCLUDE_HEADER_ONLY`).",
        ],
        "mal": """#define MAX(a, b) (a > b)

typedef struct s_point
{
	int	x;
	int	y;
}	t_point;""",
        "bem": """#ifndef FT_POINT_H
# define FT_POINT_H

typedef struct s_point
{
	int	x;
	int	y;
}	t_point;

#endif""",
    },
    {
        "id": "globais", "titulo": "Variáveis globais",
        "texto": [
            "Variáveis globais começam por `g_` (`GLOBAL_VAR_NAMING`) e a norminette avisa sempre que encontra uma (`GLOBAL_VAR_DETECTED`).",
            "Na Piscine quase nunca são precisas. Passa os valores por parâmetro ou junta-os numa estrutura.",
        ],
    },
]
