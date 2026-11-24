/*
** Um primo só é divisível por 1 e por si próprio. Basta testar divisores
** até à raiz quadrada (i <= nb / i): se nb = a * b, um deles é <= raiz.
*/
int	ft_is_prime(int nb)
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
