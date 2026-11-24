#include <unistd.h>

/*
** A rainha da coluna col pode ficar na linha row se nenhuma rainha das
** colunas anteriores estiver na mesma linha ou na mesma diagonal
** (mesma distância em linhas e em colunas).
*/
static int	ft_safe(int *rows, int col, int row)
{
	int	c;
	int	d;

	c = 0;
	while (c < col)
	{
		d = rows[c] - row;
		if (d < 0)
			d = -d;
		if (rows[c] == row || d == col - c)
			return (0);
		c++;
	}
	return (1);
}

static void	ft_print(int *rows)
{
	char	c;
	int		i;

	i = 0;
	while (i < 10)
	{
		c = '0' + rows[i];
		write(1, &c, 1);
		i++;
	}
	write(1, "\n", 1);
}

/*
** Backtracking: tenta cada linha na coluna col; se for segura, avança
** para a coluna seguinte. Na coluna 10 há uma solução completa.
** Devolve quantas soluções encontrou a partir daqui.
*/
static int	ft_solve(int *rows, int col)
{
	int	row;
	int	count;

	if (col == 10)
	{
		ft_print(rows);
		return (1);
	}
	count = 0;
	row = 0;
	while (row < 10)
	{
		if (ft_safe(rows, col, row))
		{
			rows[col] = row;
			count += ft_solve(rows, col + 1);
		}
		row++;
	}
	return (count);
}

int	ft_ten_queens_puzzle(void)
{
	int	rows[10];

	return (ft_solve(rows, 0));
}
