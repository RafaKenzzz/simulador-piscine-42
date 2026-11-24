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
** Uma palavra começa onde há um carácter que não é separador e o
** anterior é separador (ou é o início da string).
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

/*
** Copia a palavra que começa em str (até ao próximo separador ou ao
** fim) para uma string nova.
*/
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
** Reserva o array com espaço para todas as palavras e para o 0 final;
** depois salta separadores, copia uma palavra, salta-a, e repete.
** Os separadores seguidos nunca geram strings vazias.
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
