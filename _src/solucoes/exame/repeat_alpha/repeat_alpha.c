#include <unistd.h>

/*
** Quantas vezes se repete: a posição da letra no alfabeto (a = 1,
** z = 26), em minúscula ou maiúscula. Os outros caracteres saem uma vez.
*/
static int	ft_times(char c)
{
	if (c >= 'a' && c <= 'z')
		return (c - 'a' + 1);
	if (c >= 'A' && c <= 'Z')
		return (c - 'A' + 1);
	return (1);
}

int	main(int argc, char **argv)
{
	char	*s;
	int		n;

	if (argc == 2)
	{
		s = argv[1];
		while (*s)
		{
			n = ft_times(*s);
			while (n-- > 0)
				write(1, s, 1);
			s++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
