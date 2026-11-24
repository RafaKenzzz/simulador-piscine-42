/*
** Multiplica nb por si próprio power vezes. Potência negativa dá 0.
** Com power == 0 o ciclo não corre e devolve 1 (incluindo 0 ^ 0).
*/
int	ft_iterative_power(int nb, int power)
{
	int	result;

	if (power < 0)
		return (0);
	result = 1;
	while (power > 0)
	{
		result *= nb;
		power--;
	}
	return (result);
}
