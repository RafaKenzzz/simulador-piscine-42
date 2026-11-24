#include "do_op.h"

/*
** O mesmo ft_atoi do C04: espaços, vários sinais, algarismos.
** "42amis" dá 42 e "--+-20toto12" dá -20.
*/
int	ft_atoi(char *str)
{
	int	sign;
	int	result;

	while (*str == ' ' || (*str >= 9 && *str <= 13))
		str++;
	sign = 1;
	while (*str == '+' || *str == '-')
	{
		if (*str == '-')
			sign = -sign;
		str++;
	}
	result = 0;
	while (*str >= '0' && *str <= '9')
	{
		result = result * 10 + (*str - '0');
		str++;
	}
	return (result * sign);
}

void	ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}

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
