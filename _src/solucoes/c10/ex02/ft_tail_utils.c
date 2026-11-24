#include "ft_tail.h"

void	ft_putstr_fd(char *s, int fd)
{
	int	len;

	len = 0;
	while (s[len])
		len++;
	write(fd, s, len);
}

void	ft_error(char *prog, char *file)
{
	ft_putstr_fd(basename(prog), 2);
	ft_putstr_fd(": ", 2);
	ft_putstr_fd(file, 2);
	ft_putstr_fd(": ", 2);
	ft_putstr_fd(strerror(errno), 2);
	ft_putstr_fd("\n", 2);
}

/*
** Número de bytes do -c. Só algarismos: qualquer outro carácter (ou
** nenhum algarismo) devolve -1, que o main trata como erro.
*/
long	ft_atol(char *s)
{
	long	n;

	if (!*s)
		return (-1);
	n = 0;
	while (*s >= '0' && *s <= '9')
	{
		n = n * 10 + (*s - '0');
		s++;
	}
	if (*s)
		return (-1);
	return (n);
}

/*
** Novo buffer com o dobro do tamanho, com o conteúdo do antigo.
*/
static char	*ft_grow(char *old, long used, long *cap)
{
	char	*new;
	long	i;

	*cap *= 2;
	new = (char *)malloc(*cap);
	if (new)
	{
		i = -1;
		while (++i < used)
			new[i] = old[i];
	}
	free(old);
	return (new);
}

/*
** Lê o ficheiro inteiro para memória (o tamanho não se sabe à partida,
** por isso o buffer cresce sempre que enche). Devolve NULL se falhar.
*/
char	*ft_read_all(int fd, long *size)
{
	char	*buf;
	long	cap;
	int		n;

	cap = BUF_SIZE;
	*size = 0;
	buf = (char *)malloc(cap);
	n = 1;
	while (buf && n > 0)
	{
		if (*size == cap)
			buf = ft_grow(buf, *size, &cap);
		if (buf)
			n = read(fd, buf + *size, cap - *size);
		if (buf && n > 0)
			*size += n;
	}
	if (buf && n < 0)
	{
		free(buf);
		buf = NULL;
	}
	return (buf);
}
