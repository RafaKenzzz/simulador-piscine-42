#include "ft_hexdump.h"

void	ft_putstr_fd(char *s, int fd)
{
	int	len;

	len = 0;
	while (s[len])
		len++;
	write(fd, s, len);
}

static void	ft_error(t_hex *h, char *file)
{
	ft_putstr_fd(basename(h->argv[0]), 2);
	ft_putstr_fd(": ", 2);
	ft_putstr_fd(file, 2);
	ft_putstr_fd(": ", 2);
	ft_putstr_fd(strerror(errno), 2);
	ft_putstr_fd("\n", 2);
	h->err = 1;
}

/*
** Abre a próxima entrada: a entrada padrão se não houver ficheiros, ou o
** próximo ficheiro que se consiga abrir. Devolve 0 quando já não há mais.
*/
static int	ft_open_next(t_hex *h)
{
	if (h->argc == 1)
	{
		if (h->next > 1)
			return (0);
		h->next = 2;
		h->fd = 0;
		return (1);
	}
	while (h->next < h->argc)
	{
		h->fd = open(h->argv[h->next], O_RDONLY);
		h->next++;
		if (h->fd >= 0)
			return (1);
		ft_error(h, h->argv[h->next - 1]);
	}
	return (0);
}

/*
** Dá o byte seguinte da entrada, passando de um ficheiro para o outro
** sem interrupção (o hexdump trata todos os ficheiros como um só).
** Devolve 0 quando acabaram todas as entradas.
*/
int	ft_next_byte(t_hex *h, unsigned char *c)
{
	while (h->bpos >= h->blen)
	{
		if (h->fd < 0 && !ft_open_next(h))
			return (0);
		h->blen = read(h->fd, h->buf, BUF_SIZE);
		h->bpos = 0;
		if (h->blen <= 0)
		{
			if (h->blen < 0 && h->argc > 1)
				ft_error(h, h->argv[h->next - 1]);
			if (h->fd > 0)
				close(h->fd);
			h->fd = -1;
			h->blen = 0;
		}
	}
	*c = h->buf[h->bpos];
	h->bpos++;
	return (1);
}
