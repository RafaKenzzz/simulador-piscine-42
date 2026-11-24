#include <unistd.h>

static void	ft_putnbr(int n)
{
	char	c;

	if (n >= 10)
		ft_putnbr(n / 10);
	c = '0' + n % 10;
	write(1, &c, 1);
}

/*
** O número de argumentos é argc - 1 (argv[0] é o programa).
*/
int	main(int argc, char **argv)
{
	(void)argv;
	ft_putnbr(argc - 1);
	write(1, "\n", 1);
	return (0);
}
