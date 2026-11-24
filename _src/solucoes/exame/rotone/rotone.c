#include <unistd.h>

/*
** Letra seguinte, com 'z' a voltar a 'a' e 'Z' a 'A'.
*/
static char	ft_rotone(char c)
{
	if (c >= 'a' && c <= 'z')
		return ('a' + (c - 'a' + 1) % 26);
	if (c >= 'A' && c <= 'Z')
		return ('A' + (c - 'A' + 1) % 26);
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
			c = ft_rotone(argv[1][i]);
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
