#include <stdio.h>
#include <stdlib.h>

/*
** Os números vêm sempre bem formados e o resultado cabe num int, por
** isso basta o atoi. O operador é o primeiro carácter do 2.º argumento.
*/
int	main(int argc, char **argv)
{
	int	a;
	int	b;

	if (argc == 4)
	{
		a = atoi(argv[1]);
		b = atoi(argv[3]);
		if (argv[2][0] == '+')
			printf("%d", a + b);
		else if (argv[2][0] == '-')
			printf("%d", a - b);
		else if (argv[2][0] == '*')
			printf("%d", a * b);
		else if (argv[2][0] == '/')
			printf("%d", a / b);
		else if (argv[2][0] == '%')
			printf("%d", a % b);
	}
	printf("\n");
	return (0);
}
