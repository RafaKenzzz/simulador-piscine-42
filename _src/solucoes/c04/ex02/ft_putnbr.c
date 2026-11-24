#include <unistd.h>

/*
** O valor passa para um long, onde -2147483648 tem simétrico.
** A recursão escreve primeiro os algarismos da esquerda.
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
