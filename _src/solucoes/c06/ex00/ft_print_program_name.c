#include <unistd.h>

/*
** argv[0] é o nome com que o programa foi chamado (por exemplo ./a.out).
*/
int	main(int argc, char **argv)
{
	int	i;

	(void)argc;
	i = 0;
	while (argv[0][i])
		i++;
	write(1, argv[0], i);
	write(1, "\n", 1);
	return (0);
}
