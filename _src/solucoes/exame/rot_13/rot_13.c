#include <unistd.h>

/*
** Avança 13 letras dentro do alfabeto: (posição + 13) % 26 faz o 'n'
** voltar ao 'a'. Maiúsculas e minúsculas mantêm-se.
*/
static char	ft_rot13(char c)
{
	if (c >= 'a' && c <= 'z')
		return ('a' + (c - 'a' + 13) % 26);
	if (c >= 'A' && c <= 'Z')
		return ('A' + (c - 'A' + 13) % 26);
	return (c);
}

int	main(int argc, char **argv)
{
	char	c;
	int		i;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i])
		{
			c = ft_rot13(argv[1][i]);
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
