#include <unistd.h>

/*
** seen marca os caracteres já escritos. Percorre-se a 1.ª string e
** depois a 2.ª; cada carácter sai na primeira vez que aparece.
*/
static void	ft_put_new(char *s, int *seen)
{
	while (*s)
	{
		if (!seen[(unsigned char)*s])
		{
			seen[(unsigned char)*s] = 1;
			write(1, s, 1);
		}
		s++;
	}
}

int	main(int argc, char **argv)
{
	int	seen[256];
	int	i;

	if (argc == 3)
	{
		i = 0;
		while (i < 256)
			seen[i++] = 0;
		ft_put_new(argv[1], seen);
		ft_put_new(argv[2], seen);
	}
	write(1, "\n", 1);
	return (0);
}
