/*
** Algoritmo de Euclides para o máximo divisor comum (HCF): troca (a, b)
** por (b, a % b) até b ser 0. O mínimo múltiplo comum é a / mdc * b
** (dividir primeiro evita transbordar). Se algum for 0, o resultado é 0.
*/
unsigned int	lcm(unsigned int a, unsigned int b)
{
	unsigned int	x;
	unsigned int	y;
	unsigned int	tmp;

	if (a == 0 || b == 0)
		return (0);
	x = a;
	y = b;
	while (y != 0)
	{
		tmp = x % y;
		x = y;
		y = tmp;
	}
	return (a / x * b);
}
