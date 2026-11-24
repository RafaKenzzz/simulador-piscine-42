#include <unistd.h>

static int	ft_is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\0');
}

/*
** Uma letra fica maiúscula se for a última da palavra (o carácter a
** seguir é espaço, tab ou o fim); todas as outras ficam minúsculas.
*/
static void	ft_rcap(char *s)
{
	char	c;
	int		i;

	i = 0;
	while (s[i])
	{
		c = s[i];
		if (c >= 'A' && c <= 'Z')
			c += 32;
		if (c >= 'a' && c <= 'z' && ft_is_space(s[i + 1]))
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
		ft_rcap(argv[i]);
		i++;
	}
	return (0);
}
