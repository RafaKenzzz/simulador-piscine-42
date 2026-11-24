/*
** Uma potência de 2 tem um só bit a 1. n - 1 troca esse bit por 0 e
** todos os de baixo por 1, por isso n & (n - 1) dá 0. O 0 não é potência.
*/
int	is_power_of_2(unsigned int n)
{
	return (n != 0 && (n & (n - 1)) == 0);
}
