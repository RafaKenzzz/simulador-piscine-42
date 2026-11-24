#include "rush02.h"

/*
** Procura a chave no dicionário (sem zeros à esquerda). No modo de
** verificação (print == 0) só regista se falta alguma; no modo de
** escrita mostra o valor com um espaço antes, exceto no primeiro.
*/
static void	ft_word(t_dict *d, char *key)
{
	int	i;

	i = 0;
	while (i < d->size && ft_strcmp(d->entries[i].key, key) != 0)
		i++;
	if (i == d->size)
	{
		d->ok = 0;
		return ;
	}
	if (!d->print)
		return ;
	if (!d->first)
		ft_putstr(" ");
	ft_putstr(d->entries[i].value);
	d->first = 0;
}

/*
** Um grupo de três algarismos (h, t, u): "três cem vinte um" vira
** "three hundred twenty one". De 1 a 20, e nas dezenas certas, a
** palavra existe inteira no dicionário.
*/
static void	ft_group(t_dict *d, int h, int t, int u)
{
	char	key[3];

	key[1] = '\0';
	key[2] = '\0';
	if (h > 0)
	{
		key[0] = '0' + h;
		ft_word(d, key);
		ft_word(d, "100");
	}
	key[0] = '0' + t;
	key[1] = '0' + u;
	if (t == 0 && u > 0)
		ft_word(d, key + 1);
	else if (t == 1 || (t > 1 && u == 0))
		ft_word(d, key);
	else if (t > 1)
	{
		key[1] = '0';
		ft_word(d, key);
		key[0] = '0' + u;
		key[1] = '\0';
		ft_word(d, key);
	}
}

/*
** Nome da ordem de grandeza: "1" seguido de 3 * k zeros (1000, 1000000…).
*/
static void	ft_scale(t_dict *d, int k)
{
	char	*key;
	int		i;

	key = (char *)malloc(3 * k + 2);
	if (!key)
	{
		d->ok = 0;
		return ;
	}
	key[0] = '1';
	i = 1;
	while (i <= 3 * k)
		key[i++] = '0';
	key[i] = '\0';
	ft_word(d, key);
	free(key);
}

/*
** Algarismo na posição i de nbr, ou 0 se i for negativo (para completar
** o primeiro grupo à esquerda).
*/
static int	ft_digit(char *nbr, int i)
{
	if (i < 0)
		return (0);
	return (nbr[i] - '0');
}

/*
** nbr só tem algarismos, sem zeros à esquerda. Divide-se em grupos de
** três a partir da direita; cada grupo diferente de zero é escrito com
** o nome da sua ordem de grandeza (thousand, million, ...).
*/
void	ft_convert(char *nbr, t_dict *d)
{
	int	len;
	int	g;
	int	start;

	d->first = 1;
	if (nbr[0] == '0')
	{
		ft_word(d, "0");
		return ;
	}
	len = ft_strlen(nbr);
	g = (len - 1) / 3;
	while (g >= 0)
	{
		start = len - 3 * g - 3;
		if (ft_digit(nbr, start) || ft_digit(nbr, start + 1)
			|| ft_digit(nbr, start + 2))
		{
			ft_group(d, ft_digit(nbr, start), ft_digit(nbr, start + 1),
				ft_digit(nbr, start + 2));
			if (g > 0)
				ft_scale(d, g);
		}
		g--;
	}
}
