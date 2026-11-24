#include <unistd.h>

static void	ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}

/*
** Do último argumento (argv[argc - 1]) até ao primeiro (argv[1]).
*/
int	main(int argc, char **argv)
{
	int	i;

	i = argc - 1;
	while (i > 0)
	{
		ft_putstr(argv[i]);
		write(1, "\n", 1);
		i--;
	}
	return (0);
}
