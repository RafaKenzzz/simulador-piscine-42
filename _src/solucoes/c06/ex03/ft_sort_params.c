#include <unistd.h>

static int	ft_strcmp(char *s1, char *s2)
{
	while (*s1 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

static void	ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}

/*
** Ordena argv[1..argc-1] trocando ponteiros (ordenação por bolha com
** ft_strcmp): as strings não se mexem, só a ordem dos ponteiros.
*/
static void	ft_sort(char **tab, int size)
{
	int		i;
	char	*tmp;

	i = 0;
	while (i < size - 1)
	{
		if (ft_strcmp(tab[i], tab[i + 1]) > 0)
		{
			tmp = tab[i];
			tab[i] = tab[i + 1];
			tab[i + 1] = tmp;
			i = 0;
		}
		else
			i++;
	}
}

int	main(int argc, char **argv)
{
	int	i;

	ft_sort(argv + 1, argc - 1);
	i = 1;
	while (i < argc)
	{
		ft_putstr(argv[i]);
		write(1, "\n", 1);
		i++;
	}
	return (0);
}
