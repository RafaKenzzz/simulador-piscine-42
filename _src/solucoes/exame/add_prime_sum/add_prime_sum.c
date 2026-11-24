#include <unistd.h>

static int	ft_atoi(char *s)
{
	int	n;

	n = 0;
	while (*s >= '0' && *s <= '9')
	{
		n = n * 10 + (*s - '0');
		s++;
	}
	if (*s)
		return (0);
	return (n);
}

static void	ft_putnbr(int n)
{
	char	c;

	if (n >= 10)
		ft_putnbr(n / 10);
	c = '0' + n % 10;
	write(1, &c, 1);
}

static int	ft_is_prime(int n)
{
	int	i;

	if (n < 2)
		return (0);
	i = 2;
	while (i <= n / i)
	{
		if (n % i == 0)
			return (0);
		i++;
	}
	return (1);
}

/*
** Só aceita algarismos (um número positivo); tudo o resto dá 0.
** Soma todos os primos de 2 até n.
*/
int	main(int argc, char **argv)
{
	int	n;
	int	sum;

	sum = 0;
	if (argc == 2)
	{
		n = ft_atoi(argv[1]);
		while (n > 1)
		{
			if (ft_is_prime(n))
				sum += n;
			n--;
		}
	}
	ft_putnbr(sum);
	write(1, "\n", 1);
	return (0);
}
