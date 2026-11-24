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
	return (n);
}

/*
** Como o ft_putnbr, mas em base 16 com os símbolos "0123456789abcdef".
*/
static void	ft_put_hex(unsigned int n)
{
	if (n >= 16)
		ft_put_hex(n / 16);
	write(1, &"0123456789abcdef"[n % 16], 1);
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		ft_put_hex(ft_atoi(argv[1]));
	write(1, "\n", 1);
	return (0);
}
