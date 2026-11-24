#include <unistd.h>

/*
** 1 se o carácter c aparece nos primeiros n caracteres de s
** (n = -1 quer dizer «na string toda»).
*/
static int	ft_in(char *s, char c, int n)
{
	int	i;

	i = 0;
	while (s[i] && (n < 0 || i < n))
	{
		if (s[i] == c)
			return (1);
		i++;
	}
	return (0);
}

/*
** Cada carácter da 1.ª string sai se ainda não tiver saído (não aparece
** antes na 1.ª) e se existir na 2.ª.
*/
int	main(int argc, char **argv)
{
	int	i;

	if (argc == 3)
	{
		i = 0;
		while (argv[1][i])
		{
			if (!ft_in(argv[1], argv[1][i], i)
				&& ft_in(argv[2], argv[1][i], -1))
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
