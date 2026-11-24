#include <unistd.h>

static void	ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}

/*
** Os argumentos estão em argv[1] até argv[argc - 1]. Um por linha.
*/
int	main(int argc, char **argv)
{
	int	i;

	i = 1;
	while (i < argc)
	{
		ft_putstr(argv[i]);
		write(1, "\n", 1);
		i++;
	}
	return (0);
}
