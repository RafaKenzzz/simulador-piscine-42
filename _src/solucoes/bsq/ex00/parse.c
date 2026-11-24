#include "bsq.h"

/*
** Primeira linha: o número de linhas seguido dos três caracteres
** (vazio, obstáculo, cheio). Os três têm de ser imprimíveis e
** diferentes, e o número maior do que 0. Devolve o tamanho da linha.
*/
static int	ft_header(char *s, t_map *map)
{
	int	len;
	int	i;

	len = 0;
	while (s[len] && s[len] != '\n')
		len++;
	if (len < 4 || s[len] != '\n')
		return (-1);
	map->empty = s[len - 3];
	map->obstacle = s[len - 2];
	map->full = s[len - 1];
	map->height = 0;
	i = -1;
	while (++i < len - 3)
	{
		if (s[i] < '0' || s[i] > '9' || map->height > 100000000)
			return (-1);
		map->height = map->height * 10 + (s[i] - '0');
	}
	if (map->height <= 0 || map->empty == map->obstacle
		|| map->empty == map->full || map->obstacle == map->full
		|| map->empty < 32 || map->obstacle < 32 || map->full < 32)
		return (-1);
	return (len);
}

/*
** Uma linha do mapa: só vazio e obstáculos, com a mesma largura da
** primeira e terminada em '\n' (que passa a '\0' para a linha poder
** ser escrita sozinha). Devolve o tamanho, ou -1.
*/
static int	ft_line(char *s, t_map *map)
{
	int	i;

	i = 0;
	while (s[i] && s[i] != '\n')
	{
		if (s[i] != map->empty && s[i] != map->obstacle)
			return (-1);
		i++;
	}
	if (s[i] != '\n' || i == 0 || (map->width && i != map->width))
		return (-1);
	map->width = i;
	s[i] = '\0';
	return (i);
}

/*
** Valida o mapa inteiro e guarda o início de cada linha em map->rows.
** Tem de haver exatamente height linhas e nada depois delas.
*/
int	ft_parse(char *s, t_map *map)
{
	int	len;
	int	r;

	map->rows = NULL;
	len = ft_header(s, map);
	if (len < 0)
		return (0);
	s += len + 1;
	map->rows = (char **)malloc(sizeof(char *) * map->height);
	if (!map->rows)
		return (0);
	map->width = 0;
	r = 0;
	while (r < map->height)
	{
		map->rows[r] = s;
		len = ft_line(s, map);
		if (len < 0)
			return (0);
		s += len + 1;
		r++;
	}
	return (*s == '\0');
}
