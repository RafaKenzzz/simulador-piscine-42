#include "rush01.h"

/*
** Quatro linhas de quatro algarismos separados por espaços.
*/
void	ft_print_grid(int grid[4][4])
{
	int		r;
	int		c;
	char	ch;

	r = 0;
	while (r < 4)
	{
		c = 0;
		while (c < 4)
		{
			ch = '0' + grid[r][c];
			write(1, &ch, 1);
			if (c < 3)
				write(1, " ", 1);
			c++;
		}
		write(1, "\n", 1);
		r++;
	}
}
