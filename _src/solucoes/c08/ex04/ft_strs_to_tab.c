#include <stdlib.h>
#include "ft_stock_str.h"

static int	ft_strlen(char *s)
{
	int	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

static char	*ft_strdup(char *src)
{
	char	*dup;
	int		i;

	dup = (char *)malloc(sizeof(char) * (ft_strlen(src) + 1));
	if (!dup)
		return (NULL);
	i = 0;
	while (src[i])
	{
		dup[i] = src[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}

/*
** Liberta as cópias já feitas e o array, quando um malloc falha a meio.
*/
static struct s_stock_str	*ft_free_tab(struct s_stock_str *tab, int n)
{
	while (n > 0)
	{
		n--;
		free(tab[n].copy);
	}
	free(tab);
	return (NULL);
}

/*
** Um elemento por argumento, mais um último com str = 0 para marcar o
** fim. size é o tamanho, str aponta para o original e copy para uma
** cópia nova.
*/
struct s_stock_str	*ft_strs_to_tab(int ac, char **av)
{
	struct s_stock_str	*tab;
	int					i;

	tab = (struct s_stock_str *)malloc(sizeof(struct s_stock_str) * (ac + 1));
	if (!tab)
		return (NULL);
	i = 0;
	while (i < ac)
	{
		tab[i].size = ft_strlen(av[i]);
		tab[i].str = av[i];
		tab[i].copy = ft_strdup(av[i]);
		if (!tab[i].copy)
			return (ft_free_tab(tab, i));
		i++;
	}
	tab[i].size = 0;
	tab[i].str = 0;
	tab[i].copy = 0;
	return (tab);
}
