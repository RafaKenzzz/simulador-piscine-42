#include <unistd.h>

/*
** Devolve o tamanho da base, ou 0 se for inválida: menos de 2 símbolos,
** um símbolo repetido, ou um '+' ou '-'.
*/
static int	ft_base_len(char *base)
{
	int	i;
	int	j;

	i = 0;
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-')
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

/*
** Igual ao ft_putnbr, mas em vez de 10 usa o tamanho da base e em vez de
** '0' + algarismo escreve o símbolo base[algarismo].
*/
static void	ft_put_base(long n, char *base, int len)
{
	if (n >= len)
		ft_put_base(n / len, base, len);
	write(1, &base[n % len], 1);
}

void	ft_putnbr_base(int nbr, char *base)
{
	int		len;
	long	n;

	len = ft_base_len(base);
	if (len == 0)
		return ;
	n = nbr;
	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	ft_put_base(n, base, len);
}
