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
** 'A' em cima à esquerda e em baixo à direita; 'C' nos outros dois
** cantos; bordas com 'B'.
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
			ft_line(x, 'A', 'B', 'C');
		else if (j == y)
			ft_line(x, 'C', 'B', 'A');
		else
			ft_line(x, 'B', ' ', 'B');
		j++;
	}
}
