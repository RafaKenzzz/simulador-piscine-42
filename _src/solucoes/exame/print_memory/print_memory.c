#include <unistd.h>

static void	ft_hex(unsigned char c)
{
	write(1, &"0123456789abcdef"[c / 16], 1);
	write(1, &"0123456789abcdef"[c % 16], 1);
}

/*
** Uma linha: 16 posições em hexadecimal (2 algarismos por byte, um
** espaço a cada 2 bytes, espaços onde já não há bytes) e os caracteres,
** com '.' para os não imprimíveis.
*/
static void	ft_line(const unsigned char *p, size_t n)
{
	size_t	i;

	i = 0;
	while (i < 16)
	{
		if (i < n)
			ft_hex(p[i]);
		else
			write(1, "  ", 2);
		if (i % 2 == 1)
			write(1, " ", 1);
		i++;
	}
	i = 0;
	while (i < n)
	{
		if (p[i] >= 32 && p[i] <= 126)
			write(1, &p[i], 1);
		else
			write(1, ".", 1);
		i++;
	}
	write(1, "\n", 1);
}

void	print_memory(const void *addr, size_t size)
{
	const unsigned char	*p;
	size_t				off;

	p = (const unsigned char *)addr;
	off = 0;
	while (off < size)
	{
		if (size - off >= 16)
			ft_line(p + off, 16);
		else
			ft_line(p + off, size - off);
		off += 16;
	}
}
