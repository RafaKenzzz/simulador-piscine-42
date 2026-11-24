/*
** Array vazio devolve 0. Senão, começa no primeiro e guarda o maior.
*/
int	max(int *tab, unsigned int len)
{
	unsigned int	i;
	int				result;

	if (len == 0)
		return (0);
	result = tab[0];
	i = 1;
	while (i < len)
	{
		if (tab[i] > result)
			result = tab[i];
		i++;
	}
	return (result);
}
