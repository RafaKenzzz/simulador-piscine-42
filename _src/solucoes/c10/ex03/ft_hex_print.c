#include "ft_hexdump.h"

/*
** n em hexadecimal minúsculo, com width algarismos (zeros à esquerda).
*/
void	ft_put_hex(unsigned long n, int width)
{
	char	*hex;

	hex = "0123456789abcdef";
	if (width > 1)
		ft_put_hex(n / 16, width - 1);
	write(1, &hex[n % 16], 1);
}

static int	ft_same(unsigned char *a, unsigned char *b)
{
	int	i;

	i = 0;
	while (i < 16 && a[i] == b[i])
		i++;
	return (i == 16);
}

/*
** Bytes em hexadecimal: "xx " por byte, um espaço extra depois do 8.º,
** e três espaços por cada byte que falta na última linha.
*/
static void	ft_put_bytes(t_hex *h)
{
	int	i;

	i = 0;
	while (i < 16)
	{
		if (i < h->len)
		{
			ft_put_hex(h->line[i], 2);
			write(1, " ", 1);
		}
		else
			write(1, "   ", 3);
		if (i == 7)
			write(1, " ", 1);
		i++;
	}
}

static void	ft_put_chars(t_hex *h)
{
	int	i;

	write(1, " |", 2);
	i = 0;
	while (i < h->len)
	{
		if (h->line[i] >= 32 && h->line[i] <= 126)
			write(1, &h->line[i], 1);
		else
			write(1, ".", 1);
		i++;
	}
	write(1, "|\n", 2);
}

/*
** Linhas completas iguais à anterior não se repetem: aparece um "*" na
** primeira e as seguintes são omitidas, como no hexdump -C.
*/
void	ft_put_line(t_hex *h)
{
	int	i;

	if (h->len == 16 && h->has_prev && ft_same(h->line, h->prev))
	{
		if (!h->star)
			write(1, "*\n", 2);
		h->star = 1;
		return ;
	}
	h->star = 0;
	ft_put_hex(h->off, 8);
	write(1, "  ", 2);
	ft_put_bytes(h);
	ft_put_chars(h);
	i = -1;
	while (++i < 16)
		h->prev[i] = h->line[i];
	h->has_prev = (h->len == 16);
}
