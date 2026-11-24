#include <stdio.h>
#include <stdlib.h>

/*
** Divide n pelo menor divisor possível enquanto der; esse divisor é
** sempre primo. Quando i * i passa de n, o que sobra (se for > 1) é o
** último fator primo. Os fatores saem separados por '*'. 1 dá "1".
*/
int	main(int argc, char **argv)
{
	int	n;
	int	i;

	if (argc == 2)
	{
		n = atoi(argv[1]);
		if (n == 1)
			printf("1");
		i = 2;
		while (i <= n / i)
		{
			if (n % i == 0)
			{
				printf("%d*", i);
				n /= i;
			}
			else
				i++;
		}
		if (n > 1)
			printf("%d", n);
	}
	printf("\n");
	return (0);
}
