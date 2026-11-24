#include <unistd.h>

/*
** argv[1] é o primeiro argumento. Sem argumentos, só a quebra de linha.
*/
int	main(int argc, char **argv)
{
	int	i;

	if (argc > 1)
	{
		i = 0;
		while (argv[1][i])
			i++;
		write(1, argv[1], i);
	}
	write(1, "\n", 1);
	return (0);
}
