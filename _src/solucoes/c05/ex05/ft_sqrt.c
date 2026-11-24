/*
** Procura i tal que i * i == nb. A condição i <= nb / i é o mesmo que
** i * i <= nb, mas sem transbordar perto de 2147483647.
** Se nenhum i servir, a raiz não é inteira e devolve 0.
*/
int	ft_sqrt(int nb)
{
	int	i;

	if (nb <= 0)
		return (0);
	i = 1;
	while (i <= nb / i)
	{
		if (i * i == nb)
			return (i);
		i++;
	}
	return (0);
}
