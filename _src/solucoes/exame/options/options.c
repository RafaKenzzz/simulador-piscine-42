#include <unistd.h>

static void	ft_usage(void)
{
	write(1, "options: abcdefghijklmnopqrstuvwxyz\n", 36);
}

/*
** 32 bits do mais significativo para o menos, em 4 grupos de 8.
*/
static void	ft_print(unsigned int opts)
{
	int		i;
	char	c;

	i = 31;
	while (i >= 0)
	{
		c = '0' + ((opts >> i) & 1);
		write(1, &c, 1);
		if (i % 8 == 0)
			write(1, &" \n"[i == 0], 1);
		i--;
	}
}

/*
** Cada letra a-z de uma opção (argumento começado por '-') acende o bit
** da sua posição. Devolve 1 ao encontrar um 'h' (ajuda) e 2 ao encontrar
** um carácter fora de a-z; os argumentos sem '-' são ignorados.
*/
static int	ft_parse(int argc, char **argv, unsigned int *opts)
{
	int		i;
	char	*s;

	i = 0;
	while (++i < argc)
	{
		s = argv[i] + 1;
		while (argv[i][0] == '-' && *s)
		{
			if (*s == 'h')
				return (1);
			if (*s < 'a' || *s > 'z')
				return (2);
			*opts |= 1u << (*s - 'a');
			s++;
		}
	}
	return (0);
}

/*
** Sem argumentos, ou com -h, mostra a ajuda.
*/
int	main(int argc, char **argv)
{
	unsigned int	opts;
	int				r;

	opts = 0;
	r = ft_parse(argc, argv, &opts);
	if (argc == 1 || r == 1)
		ft_usage();
	else if (r == 2)
		write(1, "Invalid Option\n", 15);
	else
		ft_print(opts);
	return (0);
}
