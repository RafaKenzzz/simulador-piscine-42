#include <unistd.h>

/*
** Começa no fim da string e anda para trás: cada vez que encontra o
** início de uma palavra, escreve-a. Entre palavras, um espaço.
*/
int	main(int argc, char **argv)
{
	char	*s;
	int		end;
	int		start;

	if (argc == 2)
	{
		s = argv[1];
		end = 0;
		while (s[end])
			end++;
		while (end > 0)
		{
			start = end;
			while (start > 0 && s[start - 1] != ' ' && s[start - 1] != '\t')
				start--;
			write(1, s + start, end - start);
			if (start > 0)
				write(1, " ", 1);
			end = start - 1;
		}
	}
	write(1, "\n", 1);
	return (0);
}
