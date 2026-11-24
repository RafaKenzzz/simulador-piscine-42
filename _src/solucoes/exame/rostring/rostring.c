#include <unistd.h>

static int	ft_sp(char c)
{
	return (c == ' ' || c == '\t');
}

/*
** Escreve as palavras a partir de s, separadas por um espaço. Devolve 1
** se escreveu alguma (para saber se é preciso um espaço antes da
** primeira palavra, que vai para o fim).
*/
static int	ft_put_words(char *s)
{
	int	any;

	any = 0;
	while (*s)
	{
		while (ft_sp(*s))
			s++;
		if (*s && any)
			write(1, " ", 1);
		while (*s && !ft_sp(*s))
		{
			write(1, s++, 1);
			any = 1;
		}
	}
	return (any);
}

/*
** Encontra a primeira palavra, escreve as restantes e só depois ela.
*/
int	main(int argc, char **argv)
{
	char	*s;
	char	*first;
	int		len;

	if (argc > 1)
	{
		s = argv[1];
		while (ft_sp(*s))
			s++;
		first = s;
		len = 0;
		while (first[len] && !ft_sp(first[len]))
			len++;
		if (ft_put_words(first + len) && len > 0)
			write(1, " ", 1);
		write(1, first, len);
	}
	write(1, "\n", 1);
	return (0);
}
