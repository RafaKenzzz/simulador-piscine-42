#include <unistd.h>

/*
** Escreve cada palavra; antes de cada uma, exceto a primeira, um espaço.
** Os espaços e tabs entre palavras (e nas pontas) nunca são escritos.
*/
int	main(int argc, char **argv)
{
	char	*s;
	int		first;

	if (argc == 2)
	{
		s = argv[1];
		first = 1;
		while (*s)
		{
			while (*s == ' ' || *s == '\t')
				s++;
			if (*s && !first)
				write(1, " ", 1);
			while (*s && *s != ' ' && *s != '\t')
			{
				write(1, s, 1);
				first = 0;
				s++;
			}
		}
	}
	write(1, "\n", 1);
	return (0);
}
