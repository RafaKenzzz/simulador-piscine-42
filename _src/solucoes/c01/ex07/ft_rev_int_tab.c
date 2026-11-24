/*
** Troca o primeiro com o último, o segundo com o penúltimo, e assim por
** diante. Pára a meio: se fosse até ao fim, voltava a trocar tudo.
*/
void	ft_rev_int_tab(int *tab, int size)
{
	int	i;
	int	tmp;

	i = 0;
	while (i < size / 2)
	{
		tmp = tab[i];
		tab[i] = tab[size - 1 - i];
		tab[size - 1 - i] = tmp;
		i++;
	}
}
