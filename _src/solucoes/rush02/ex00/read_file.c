#include "rush02.h"

/*
** Novo buffer com o dobro do tamanho, com o conteúdo do antigo.
*/
static char	*ft_grow(char *old, long used, long *cap)
{
	char	*new;
	long	i;

	*cap *= 2;
	new = (char *)malloc(*cap + 1);
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
** Lê tudo o que há em fd para uma string terminada em '\0'.
** O buffer duplica sempre que enche. Devolve NULL se a leitura falhar.
*/
static char	*ft_read_fd(int fd)
{
	char	*buf;
	long	cap;
	long	used;
	long	n;

	cap = BUF_SIZE;
	used = 0;
	buf = (char *)malloc(cap + 1);
	n = 1;
	while (buf && n > 0)
	{
		if (used == cap)
			buf = ft_grow(buf, used, &cap);
		if (buf)
			n = read(fd, buf + used, cap - used);
		if (buf && n > 0)
			used += n;
	}
	if (buf && n < 0)
		free(buf);
	if (!buf || n < 0)
		return (NULL);
	buf[used] = '\0';
	return (buf);
}

/*
** Abre o dicionário, lê-o e fecha-o. NULL se não conseguir.
*/
char	*ft_read_file(char *path)
{
	char	*content;
	int		fd;

	fd = open(path, O_RDONLY);
	if (fd < 0)
		return (NULL);
	content = ft_read_fd(fd);
	close(fd);
	return (content);
}
