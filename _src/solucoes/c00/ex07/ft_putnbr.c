#include <unistd.h>

/*
** Copiamos nb para um long: -2147483648 não tem simétrico em int,
** mas em long tem. A recursão escreve primeiro os algarismos da esquerda
** (n / 10) e depois o último (n % 10).
*/
void	ft_putnbr(int nb)
{
	long	n;
	char	c;

	n = nb;
	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	if (n >= 10)
		ft_putnbr(n / 10);
	c = '0' + n % 10;
	write(1, &c, 1);
}
