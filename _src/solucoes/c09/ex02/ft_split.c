#include <stdlib.h>

static int	ft_is_sep(char c, char *charset)
{
	while (*charset)
	{
		if (c == *charset)
			return (1);
		charset++;
	}
	return (0);
}

/*
** Uma palavra começa num carácter que não é separador e cujo anterior é
** separador (ou que está no início da string).
*/
static int	ft_count_words(char *str, char *charset)
{
	int	count;
	int	i;

	count = 0;
	i = 0;
	while (str[i])
	{
		if (!ft_is_sep(str[i], charset)
			&& (i == 0 || ft_is_sep(str[i - 1], charset)))
			count++;
		i++;
	}
	return (count);
}

static char	*ft_word_dup(char *str, char *charset)
{
	char	*word;
	int		len;
	int		i;

	len = 0;
	while (str[len] && !ft_is_sep(str[len], charset))
		len++;
	word = (char *)malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	i = -1;
	while (++i < len)
		word[i] = str[i];
	word[len] = '\0';
	return (word);
}

/*
** Salta separadores, copia uma palavra, salta-a, e repete até ao fim.
** O array tem uma posição a mais para o 0 final.
*/
char	**ft_split(char *str, char *charset)
{
	char	**tab;
	int		w;

	tab = (char **)malloc(sizeof(char *) * (ft_count_words(str, charset) + 1));
	if (!tab)
		return (NULL);
	w = 0;
	while (*str)
	{
		while (*str && ft_is_sep(*str, charset))
			str++;
		if (*str)
		{
			tab[w] = ft_word_dup(str, charset);
			w++;
		}
		while (*str && !ft_is_sep(*str, charset))
			str++;
	}
	tab[w] = 0;
	return (tab);
}
