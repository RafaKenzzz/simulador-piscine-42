#include <stdlib.h>

static int	ft_sep(char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

static int	ft_count(char *s)
{
	int	count;

	count = 0;
	while (*s)
	{
		while (*s && ft_sep(*s))
			s++;
		if (*s)
			count++;
		while (*s && !ft_sep(*s))
			s++;
	}
	return (count);
}

static char	*ft_word(char *s)
{
	char	*w;
	int		len;
	int		i;

	len = 0;
	while (s[len] && !ft_sep(s[len]))
		len++;
	w = (char *)malloc(len + 1);
	if (!w)
		return (NULL);
	i = -1;
	while (++i < len)
		w[i] = s[i];
	w[len] = '\0';
	return (w);
}

/*
** Separadores: espaço, tab e quebra de linha. Conta as palavras,
** reserva o array (+1 para o NULL) e copia uma palavra de cada vez.
*/
char	**ft_split(char *str)
{
	char	**tab;
	int		w;

	tab = (char **)malloc(sizeof(char *) * (ft_count(str) + 1));
	if (!tab)
		return (NULL);
	w = 0;
	while (*str)
	{
		while (*str && ft_sep(*str))
			str++;
		if (*str)
			tab[w++] = ft_word(str);
		while (*str && !ft_sep(*str))
			str++;
	}
	tab[w] = NULL;
	return (tab);
}
