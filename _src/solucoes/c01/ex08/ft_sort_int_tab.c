/*
** Ordenação por bolha: percorre o array e troca cada par fora de ordem.
** Sempre que há uma troca, recomeça do início. Quando chega ao fim sem
** trocar nada, o array está ordenado.
*/
void	ft_sort_int_tab(int *tab, int size)
{
	int	i;
	int	tmp;

	i = 0;
	while (i < size - 1)
	{
		if (tab[i] > tab[i + 1])
		{
			tmp = tab[i];
			tab[i] = tab[i + 1];
			tab[i + 1] = tmp;
			i = 0;
		}
		else
			i++;
	}
}
