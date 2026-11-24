#include <unistd.h>

/*
** O mesmo que o epur_str, com três espaços entre palavras.
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
				write(1, "   ", 3);
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
