#include <stdlib.h>

/*
** Tamanho da base, ou 0 se for inválida: menos de 2 símbolos, símbolos
** repetidos, '+', '-' ou espaços em branco.
*/
int	ft_base_len(char *base)
{
	int	i;
	int	j;

	i = 0;
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-' || base[i] == ' '
			|| (base[i] >= 9 && base[i] <= 13))
			return (0);
		j = i + 1;
		while (base[j])
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		i++;
	}
	if (i < 2)
		return (0);
	return (i);
}

int	ft_index(char c, char *base)
{
	int	i;

	i = 0;
	while (base[i])
	{
		if (base[i] == c)
			return (i);
		i++;
	}
	return (-1);
}

/*
** Quantos caracteres são precisos para escrever n na base: os
** algarismos e, se for negativo, o '-'.
*/
static int	ft_nb_len(long n, int len)
{
	int	size;

	size = 1;
	if (n < 0)
	{
		size++;
		n = -n;
	}
	while (n >= len)
	{
		n /= len;
		size++;
	}
	return (size);
}

/*
** Reserva a string com o tamanho exato e preenche-a do fim para o
** início, com o algarismo das unidades primeiro. Se houver sinal, a
** posição 0 fica com o '-' e o ciclo pára antes dela.
*/
char	*ft_itoa_base(long n, char *base, int len)
{
	char	*res;
	int		size;
	int		stop;

	size = ft_nb_len(n, len);
	res = (char *)malloc(sizeof(char) * (size + 1));
	if (!res)
		return (NULL);
	res[size] = '\0';
	stop = 0;
	if (n < 0)
	{
		res[0] = '-';
		n = -n;
		stop = 1;
	}
	while (size > stop)
	{
		res[size - 1] = base[n % len];
		n /= len;
		size--;
	}
	return (res);
}
