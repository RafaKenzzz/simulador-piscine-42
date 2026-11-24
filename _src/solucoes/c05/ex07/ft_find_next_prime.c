/*
** Mesmo teste do ft_is_prime (só pode haver 5 funções por ficheiro, mas
** cada exercício tem de funcionar sozinho, por isso repete-se aqui).
*/
static int	ft_is_prime(int nb)
{
	int	i;

	if (nb < 2)
		return (0);
	i = 2;
	while (i <= nb / i)
	{
		if (nb % i == 0)
			return (0);
		i++;
	}
	return (1);
}

/*
** O primeiro primo maior ou igual a nb. Abaixo de 2 a resposta é 2.
*/
int	ft_find_next_prime(int nb)
{
	if (nb <= 2)
		return (2);
	while (!ft_is_prime(nb))
		nb++;
	return (nb);
}
