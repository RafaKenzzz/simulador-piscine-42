#include <unistd.h>

/*
** Escreve uma barra invertida seguida dos dois algarismos hexadecimais
** (em minúsculas) de c.
*/
static void	ft_put_hex(unsigned char c)
{
	char	*hex;

	hex = "0123456789abcdef";
	write(1, "\\", 1);
	write(1, &hex[c / 16], 1);
	write(1, &hex[c % 16], 1);
}

/*
** Cada carácter é lido como unsigned char: assim os bytes acima de 127
** (letras com acento em UTF-8, por exemplo) dão 128 a 255 e não negativos.
*/
void	ft_putstr_non_printable(char *str)
{
	unsigned char	c;

	while (*str)
	{
		c = (unsigned char)*str;
		if (c < 32 || c > 126)
			ft_put_hex(c);
		else
			write(1, str, 1);
		str++;
	}
}
