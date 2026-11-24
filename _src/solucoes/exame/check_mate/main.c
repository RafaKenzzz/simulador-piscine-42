#include "check_mate.h"

/*
** Procura o rei (há sempre um só) e diz se está atacado.
*/
static int	ft_find_king(t_board *b)
{
	int	r;
	int	c;

	r = -1;
	while (++r < b->size)
	{
		c = -1;
		while (++c < b->size)
			if (b->rows[r][c] == 'K')
				return (ft_attacked(b, r, c));
	}
	return (0);
}

/*
** Cada argumento é uma linha do tabuleiro, que é sempre quadrado.
*/
int	main(int argc, char **argv)
{
	t_board	b;

	if (argc < 2)
	{
		write(1, "\n", 1);
		return (0);
	}
	b.rows = argv + 1;
	b.size = argc - 1;
	if (ft_find_king(&b))
		write(1, "Success\n", 8);
	else
		write(1, "Fail\n", 5);
	return (0);
}
