#include <unistd.h>

/*
** Escreve n em hexadecimal com exatamente width algarismos (zeros à
** esquerda), por recursão: primeiro os algarismos da esquerda.
*/
static void	ft_put_hex(unsigned long n, int width)
{
	char	*hex;

	hex = "0123456789abcdef";
	if (width > 1)
		ft_put_hex(n / 16, width - 1);
	write(1, &hex[n % 16], 1);
}

/*
** Coluna do meio: 16 posições, 2 algarismos por byte e um espaço a cada
** 2 bytes. Na última linha, as posições sem byte levam espaços, para a
** coluna dos caracteres ficar alinhada.
*/
static void	ft_put_bytes(unsigned char *p, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < 16)
	{
		if (i < n)
			ft_put_hex(p[i], 2);
		else
			write(1, "  ", 2);
		if (i % 2 == 1)
			write(1, " ", 1);
		i++;
	}
}

/*
** Coluna da direita: o carácter, se for imprimível, ou um ponto.
*/
static void	ft_put_chars(unsigned char *p, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < n)
	{
		if (p[i] >= 32 && p[i] <= 126)
			write(1, &p[i], 1);
		else
			write(1, ".", 1);
		i++;
	}
}

/*
** Uma linha por cada bloco de 16 bytes: endereço com 16 algarismos, ": ",
** bytes em hexadecimal, caracteres e quebra de linha.
*/
void	*ft_print_memory(void *addr, unsigned int size)
{
	unsigned char	*p;
	unsigned int	off;
	unsigned int	n;

	p = (unsigned char *)addr;
	off = 0;
	while (off < size)
	{
		n = 16;
		if (size - off < 16)
			n = size - off;
		ft_put_hex((unsigned long)(p + off), 16);
		write(1, ": ", 2);
		ft_put_bytes(p + off, n);
		ft_put_chars(p + off, n);
		write(1, "\n", 1);
		off += 16;
	}
	return (addr);
}
