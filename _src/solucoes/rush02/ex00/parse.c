#include "rush02.h"

/*
** Uma linha válida: algarismos, espaços, ':', espaços e um valor só com
** caracteres imprimíveis. Os espaços antes e depois do valor são
** cortados. Devolve o tamanho da linha (sem o '\n') ou -1 se for
** inválida. As linhas vazias dão 0 e não criam entradas.
*/
static int	ft_skip_spaces(char *s, int i)
{
	while (s[i] == ' ')
		i++;
	return (i);
}

static int	ft_parse_line(char *s, t_entry *e)
{
	int	i;
	int	k;
	int	v;
	int	end;

	k = 0;
	while (s[k] >= '0' && s[k] <= '9')
		k++;
	i = ft_skip_spaces(s, k);
	if (k == 0 || s[i] != ':')
		return (-1);
	i = ft_skip_spaces(s, i + 1);
	v = i;
	while (s[i] >= 32 && s[i] <= 126)
		i++;
	if (s[i] != '\n' && s[i] != '\0')
		return (-1);
	end = i;
	while (end > v && s[end - 1] == ' ')
		end--;
	e->key = ft_strndup(s, k);
	e->value = ft_strndup(s + v, end - v);
	if (end == v || !e->key || !e->value)
		return (-1);
	return (i);
}

static int	ft_count_lines(char *s)
{
	int	count;

	count = 1;
	while (*s)
	{
		if (*s == '\n')
			count++;
		s++;
	}
	return (count);
}

void	ft_free_dict(t_dict *dict)
{
	int	i;

	i = 0;
	while (i < dict->size)
	{
		free(dict->entries[i].key);
		free(dict->entries[i].value);
		i++;
	}
	free(dict->entries);
}

/*
** Uma entrada por linha não vazia. Devolve 0 ao primeiro erro (a
** entrada incompleta também é contada, para ser libertada).
*/
int	ft_parse_dict(char *s, t_dict *dict)
{
	int	len;

	dict->size = 0;
	dict->entries = (t_entry *)malloc(sizeof(t_entry) * ft_count_lines(s));
	if (!dict->entries)
		return (0);
	while (*s)
	{
		if (*s == '\n')
		{
			s++;
			continue ;
		}
		dict->entries[dict->size].key = NULL;
		dict->entries[dict->size].value = NULL;
		len = ft_parse_line(s, &dict->entries[dict->size]);
		dict->size++;
		if (len < 0)
			return (0);
		s += len;
	}
	return (1);
}
