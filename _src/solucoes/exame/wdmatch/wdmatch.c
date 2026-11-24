#include <unistd.h>

/*
** Percorre a 2.ª string; cada vez que encontra o próximo carácter da 1.ª,
** avança na 1.ª. Se chegar ao fim da 1.ª, deu para a escrever.
*/
int	main(int argc, char **argv)
{
	int	i;
	int	j;

	if (argc == 3)
	{
		i = 0;
		j = 0;
		while (argv[1][i] && argv[2][j])
		{
			if (argv[1][i] == argv[2][j])
				i++;
			j++;
		}
		if (argv[1][i] == '\0')
			write(1, argv[1], i);
	}
	write(1, "\n", 1);
	return (0);
}
