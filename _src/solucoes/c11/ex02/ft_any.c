/*
** O array acaba num ponteiro nulo. Devolve 1 logo que f dê algo
** diferente de 0; se nenhum der, devolve 0.
*/
int	ft_any(char **tab, int (*f)(char *))
{
	int	i;

	i = 0;
	while (tab[i])
	{
		if (f(tab[i]) != 0)
			return (1);
		i++;
	}
	return (0);
}
