#include <unistd.h>

/*
** A letra espelhada: a <-> z, b <-> y, ... Em posição: 25 - posição.
** 'a' + ('z' - c) faz isso sem calcular a posição.
*/
static char	ft_mirror(char c)
{
	if (c >= 'a' && c <= 'z')
		return ('a' + ('z' - c));
	if (c >= 'A' && c <= 'Z')
		return ('A' + ('Z' - c));
	return (c);
}

int	main(int argc, char **argv)
{
	char	c;
	int		i;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i])
		{
			c = ft_mirror(argv[1][i]);
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
