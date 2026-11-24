#include <stdlib.h>

int		ft_base_len(char *base);
int		ft_index(char c, char *base);
char	*ft_itoa_base(long n, char *base, int len);

/*
** Salta os espaços e lê os sinais, como o ft_atoi. Devolve o sinal e
** deixa *s a apontar para o primeiro algarismo.
*/
static int	ft_skip(char **s)
{
	int	sign;

	while (**s == ' ' || (**s >= 9 && **s <= 13))
		(*s)++;
	sign = 1;
	while (**s == '+' || **s == '-')
	{
		if (**s == '-')
			sign = -sign;
		(*s)++;
	}
	return (sign);
}

/*
** Lê nbr na base de origem (como o ft_atoi_base) para um long e
** escreve o resultado na base de destino.
** Se alguma das bases for inválida, devolve NULL.
*/
char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	int		len_from;
	int		len_to;
	int		sign;
	long	n;

	len_from = ft_base_len(base_from);
	len_to = ft_base_len(base_to);
	if (len_from == 0 || len_to == 0)
		return (NULL);
	sign = ft_skip(&nbr);
	n = 0;
	while (ft_index(*nbr, base_from) >= 0)
	{
		n = n * len_from + ft_index(*nbr, base_from);
		nbr++;
	}
	return (ft_itoa_base(n * sign, base_to, len_to));
}
