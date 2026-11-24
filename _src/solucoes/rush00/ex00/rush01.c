void	ft_putchar(char c);

static void	ft_line(int x, char left, char mid, char right)
{
	int	i;

	i = 1;
	while (i <= x)
	{
		if (i == 1)
			ft_putchar(left);
		else if (i == x)
			ft_putchar(right);
		else
			ft_putchar(mid);
		i++;
	}
	ft_putchar('\n');
}

/*
** Cantos: '/' em cima à esquerda e em baixo à direita; '\' nos outros
** dois. Bordas com '*'.
*/
void	rush(int x, int y)
{
	int	j;

	if (x <= 0 || y <= 0)
		return ;
	j = 1;
	while (j <= y)
	{
		if (j == 1)
			ft_line(x, '/', '*', '\\');
		else if (j == y)
			ft_line(x, '\\', '*', '/');
		else
			ft_line(x, '*', ' ', '*');
		j++;
	}
}
