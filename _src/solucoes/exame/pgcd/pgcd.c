#include <stdio.h>
#include <stdlib.h>

/*
** Máximo divisor comum pelo algoritmo de Euclides.
*/
int	main(int argc, char **argv)
{
	int	a;
	int	b;
	int	tmp;

	if (argc == 3)
	{
		a = atoi(argv[1]);
		b = atoi(argv[2]);
		while (b != 0)
		{
			tmp = a % b;
			a = b;
			b = tmp;
		}
		printf("%d", a);
	}
	printf("\n");
	return (0);
}
