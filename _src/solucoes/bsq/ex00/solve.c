#include "bsq.h"

static int	ft_min3(int a, int b, int c)
{
	if (b < a)
		a = b;
	if (c < a)
		a = c;
	return (a);
}

/*
** Programação dinâmica numa linha: cur[j + 1] é o lado do maior quadrado
** com o canto inferior direito em (i, j). É 0 num obstáculo; senão é 1
** mais o menor dos três vizinhos (cima, esquerda, diagonal).
** Só um quadrado ESTRITAMENTE maior substitui o melhor: assim fica o
** primeiro encontrado, que é o mais acima e, depois, o mais à esquerda.
*/
static void	ft_row(t_map *map, int i, int *prev, int *cur)
{
	int	j;

	cur[0] = 0;
	j = 0;
	while (j < map->width)
	{
		if (map->rows[i][j] == map->obstacle)
			cur[j + 1] = 0;
		else
			cur[j + 1] = 1 + ft_min3(prev[j + 1], cur[j], prev[j]);
		if (cur[j + 1] > map->best)
		{
			map->best = cur[j + 1];
			map->bi = i;
			map->bj = j;
		}
		j++;
	}
}

/*
** Só são precisas duas linhas de valores: a de cima e a atual. No fim
** de cada linha trocam de papel.
*/
int	ft_solve(t_map *map)
{
	int	*prev;
	int	*cur;
	int	*tmp;
	int	i;
	int	ok;

	prev = (int *)malloc(sizeof(int) * (map->width + 1));
	cur = (int *)malloc(sizeof(int) * (map->width + 1));
	ok = (prev != NULL && cur != NULL);
	i = -1;
	while (ok && ++i <= map->width)
		prev[i] = 0;
	map->best = 0;
	i = -1;
	while (ok && ++i < map->height)
	{
		ft_row(map, i, prev, cur);
		tmp = prev;
		prev = cur;
		cur = tmp;
	}
	free(prev);
	free(cur);
	return (ok);
}

/*
** Pinta o quadrado com o carácter "cheio" e escreve o mapa.
*/
void	ft_print(t_map *map)
{
	int	i;
	int	j;

	i = map->bi - map->best + 1;
	while (map->best > 0 && i <= map->bi)
	{
		j = map->bj - map->best + 1;
		while (j <= map->bj)
			map->rows[i][j++] = map->full;
		i++;
	}
	i = -1;
	while (++i < map->height)
	{
		write(1, map->rows[i], map->width);
		write(1, "\n", 1);
	}
}
