#include "rush01.h"

/*
** Quantas caixas se veem numa linha de quatro, a olhar a partir de a:
** uma caixa vê-se se for mais alta do que todas as que estão à frente.
*/
static int	ft_visible(int a, int b, int c, int d)
{
	int	count;
	int	max;

	count = 1;
	max = a;
	if (b > max)
	{
		count++;
		max = b;
	}
	if (c > max)
	{
		count++;
		max = c;
	}
	if (d > max)
		count++;
	return (count);
}

/*
** Linha r completa: confirma as vistas da esquerda e da direita.
*/
static int	ft_row_ok(int g[4][4], int *v, int r)
{
	return (ft_visible(g[r][0], g[r][1], g[r][2], g[r][3]) == v[8 + r]
		&& ft_visible(g[r][3], g[r][2], g[r][1], g[r][0]) == v[12 + r]);
}

/*
** Coluna c completa: confirma as vistas de cima e de baixo.
*/
static int	ft_col_ok(int g[4][4], int *v, int c)
{
	return (ft_visible(g[0][c], g[1][c], g[2][c], g[3][c]) == v[c]
		&& ft_visible(g[3][c], g[2][c], g[1][c], g[0][c]) == v[4 + c]);
}

/*
** Uma altura h pode ir para (r, c) se ainda não estiver na linha r nem
** na coluna c (só se olha para as casas já preenchidas).
*/
static int	ft_free(int g[4][4], int r, int c, int h)
{
	int	i;

	i = 0;
	while (i < c)
		if (g[r][i++] == h)
			return (0);
	i = 0;
	while (i < r)
		if (g[i++][c] == h)
			return (0);
	return (1);
}

/*
** Backtracking casa a casa (pos de 0 a 15, linha a linha). Quando uma
** linha ou coluna fica completa, confirma-se logo as vistas; se falhar,
** tenta-se a altura seguinte. Devolve 1 na primeira solução encontrada.
*/
int	ft_solve(int grid[4][4], int *views, int pos)
{
	int	r;
	int	c;
	int	h;

	if (pos == 16)
		return (1);
	r = pos / 4;
	c = pos % 4;
	h = 1;
	while (h <= 4)
	{
		if (ft_free(grid, r, c, h))
		{
			grid[r][c] = h;
			if ((c < 3 || ft_row_ok(grid, views, r))
				&& (r < 3 || ft_col_ok(grid, views, c))
				&& ft_solve(grid, views, pos + 1))
				return (1);
		}
		h++;
	}
	return (0);
}
