#include <stdlib.h>

static int	ft_len(unsigned int n, int base)
{
	int	len;

	len = 1;
	while (n >= (unsigned int)base)
	{
		n /= base;
		len++;
	}
	return (len);
}

/*
** Em base 10 os negativos levam '-'. Nas outras bases, o valor é lido
** como unsigned (um -1 em base 16 dá FFFFFFFF). Conta os algarismos,
** reserva o tamanho exato e preenche do fim para o início.
*/
char	*ft_itoa_base(int value, int base)
{
	char			*s;
	unsigned int	n;
	int				len;

	if (base < 2 || base > 16)
		return (NULL);
	n = (unsigned int)value;
	if (base == 10 && value < 0)
		n = -(unsigned int)value;
	len = ft_len(n, base) + (base == 10 && value < 0);
	s = (char *)malloc(len + 1);
	if (!s)
		return (NULL);
	s[len] = '\0';
	s[0] = '-';
	while (len > 0 && !(len == 1 && base == 10 && value < 0))
	{
		s[--len] = "0123456789ABCDEF"[n % base];
		n /= base;
	}
	return (s);
}
