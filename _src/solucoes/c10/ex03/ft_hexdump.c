#include "ft_hexdump.h"

static void	ft_init(t_hex *h, int argc, char **argv)
{
	h->blen = 0;
	h->bpos = 0;
	h->fd = -1;
	h->next = 1;
	h->argc = argc;
	h->argv = argv;
	h->err = 0;
	h->has_prev = 0;
	h->star = 0;
	h->off = 0;
}

static int	ft_usage(void)
{
	ft_putstr_fd("usage: ft_hexdump -C [file ...]\n", 2);
	return (1);
}

/*
** O primeiro argumento tem de ser -C (a única opção pedida).
** Lê 16 bytes de cada vez, escreve a linha e avança o deslocamento.
** No fim escreve o deslocamento total, se tiver havido algum byte.
*/
int	main(int argc, char **argv)
{
	t_hex			h;
	unsigned char	c;

	if (argc < 2 || argv[1][0] != '-' || argv[1][1] != 'C' || argv[1][2])
		return (ft_usage());
	ft_init(&h, argc - 1, argv + 1);
	h.argv[0] = argv[0];
	h.len = 16;
	while (h.len == 16)
	{
		h.len = 0;
		while (h.len < 16 && ft_next_byte(&h, &c))
			h.line[h.len++] = c;
		if (h.len > 0)
			ft_put_line(&h);
		h.off += h.len;
	}
	if (h.off > 0)
	{
		ft_put_hex(h.off, 8);
		write(1, "\n", 1);
	}
	return (h.err);
}
