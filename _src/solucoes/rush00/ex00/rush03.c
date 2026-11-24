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
** Cantos da esquerda com 'A', cantos da direita com 'C', bordas com 'B'.
*/
void	rush(int x, int y)
{
	int	j;

	if (x <= 0 || y <= 0)
		return ;
	j = 1;
	while (j <= y)
	{
		if (j == 1 || j == y)
			ft_line(x, 'A', 'B', 'C');
		else
			ft_line(x, 'B', ' ', 'B');
		j++;
	}
}
