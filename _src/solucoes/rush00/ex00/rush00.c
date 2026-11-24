void	ft_putchar(char c);

/*
** Uma linha com x caracteres: left na primeira coluna, right na última
** e mid no meio. Com x == 1 só há a primeira coluna.
*/
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
** Primeira linha, linhas do meio e última linha. Com y == 1 só há a
** primeira. Valores menores do que 1 não desenham nada.
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
			ft_line(x, 'o', '-', 'o');
		else if (j == y)
			ft_line(x, 'o', '-', 'o');
		else
			ft_line(x, '|', ' ', '|');
		j++;
	}
}
