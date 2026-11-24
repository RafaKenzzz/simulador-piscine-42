#include <unistd.h>

/*
** Uma letra fica maiúscula se for a primeira da palavra (no início ou
** depois de um espaço ou tab); todas as outras ficam minúsculas.
*/
static void	ft_cap(char *s)
{
	char	c;
	int		i;

	i = 0;
	while (s[i])
	{
		c = s[i];
		if (c >= 'A' && c <= 'Z')
			c += 32;
		if (c >= 'a' && c <= 'z'
			&& (i == 0 || s[i - 1] == ' ' || s[i - 1] == '\t'))
			c -= 32;
		write(1, &c, 1);
		i++;
	}
	write(1, "\n", 1);
}

int	main(int argc, char **argv)
{
	int	i;

	if (argc == 1)
		write(1, "\n", 1);
	i = 1;
	while (i < argc)
	{
		ft_cap(argv[i]);
		i++;
	}
	return (0);
}
