/*
** nb! = 1 * 2 * ... * nb. O factorial de um negativo não existe (0) e
** 0! vale 1, que é o valor inicial do resultado.
*/
int	ft_iterative_factorial(int nb)
{
	int	result;

	if (nb < 0)
		return (0);
	result = 1;
	while (nb > 1)
	{
		result *= nb;
		nb--;
	}
	return (result);
}
