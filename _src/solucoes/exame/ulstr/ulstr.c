#include <unistd.h>

/*
** Troca maiúsculas por minúsculas e vice-versa (diferença de 32 na
** tabela ASCII). O resto fica igual.
*/
int	main(int argc, char **argv)
{
	char	c;
	int		i;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i])
		{
			c = argv[1][i];
			if (c >= 'a' && c <= 'z')
				c -= 32;
			else if (c >= 'A' && c <= 'Z')
				c += 32;
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
