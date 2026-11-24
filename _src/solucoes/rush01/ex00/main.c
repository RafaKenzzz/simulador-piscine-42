#include "rush01.h"

/*
** O argumento tem de ser exatamente 16 algarismos de 1 a 4 separados por
** um espaço: 31 caracteres, algarismos nas posições pares e espaços nas
** ímpares. views fica com: colunas de cima (0-3), colunas de baixo (4-7),
** linhas da esquerda (8-11) e linhas da direita (12-15).
*/
int	ft_parse(char *str, int *views)
{
	int	i;

	i = 0;
	while (str[i] && i < 31)
	{
		if (i % 2 == 0 && (str[i] < '1' || str[i] > '4'))
			return (0);
		if (i % 2 == 1 && str[i] != ' ')
			return (0);
		if (i % 2 == 0)
			views[i / 2] = str[i] - '0';
		i++;
	}
	return (i == 31 && str[i] == '\0');
}

int	main(int argc, char **argv)
{
	int	views[16];
	int	grid[4][4];

	if (argc != 2 || !ft_parse(argv[1], views) || !ft_solve(grid, views, 0))
	{
		write(1, "Error\n", 6);
		return (1);
	}
	ft_print_grid(grid);
	return (0);
}
