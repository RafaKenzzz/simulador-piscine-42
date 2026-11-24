#include <stdlib.h>

/*
** Número de caracteres: os algarismos e, se for negativo, o '-'.
** O 0 tem 1 algarismo (por isso len começa em 1 para n <= 0).
*/
static int	ft_len(long n)
{
	int	len;

	len = (n <= 0);
	while (n != 0)
	{
		n /= 10;
		len++;
	}
	return (len);
}

/*
** Reserva a string com o tamanho exato e preenche-a do fim para o
** início. O long evita o problema do INT_MIN. Se for negativo, a
** posição 0 recebe o '-' no fim.
*/
char	*ft_itoa(int nbr)
{
	char	*s;
	long	n;
	int		len;

	n = nbr;
	len = ft_len(n);
	s = (char *)malloc(len + 1);
	if (!s)
		return (NULL);
	s[len] = '\0';
	if (n < 0)
		n = -n;
	while (len-- > 0)
	{
		s[len] = '0' + n % 10;
		n /= 10;
	}
	if (nbr < 0)
		s[0] = '-';
	return (s);
}
