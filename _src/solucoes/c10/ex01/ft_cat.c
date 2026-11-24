#include <errno.h>
#include <fcntl.h>
#include <libgen.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 29696

static void	ft_putstr_fd(char *s, int fd)
{
	int	len;

	len = 0;
	while (s[len])
		len++;
	write(fd, s, len);
}

/*
** Mensagem igual à do cat: "ft_cat: ficheiro: motivo". O motivo vem do
** errno, traduzido para texto pelo strerror.
*/
static void	ft_error(char *prog, char *file)
{
	ft_putstr_fd(basename(prog), 2);
	ft_putstr_fd(": ", 2);
	ft_putstr_fd(file, 2);
	ft_putstr_fd(": ", 2);
	ft_putstr_fd(strerror(errno), 2);
	ft_putstr_fd("\n", 2);
}

/*
** Copia tudo o que há em fd para a saída. Devolve -1 se o read falhar
** (por exemplo, numa pasta) e 0 quando chega ao fim.
*/
static int	ft_copy(int fd)
{
	char	buf[BUF_SIZE];
	int		n;

	n = read(fd, buf, BUF_SIZE);
	while (n > 0)
	{
		write(1, buf, n);
		n = read(fd, buf, BUF_SIZE);
	}
	return (n);
}

/*
** "-" quer dizer entrada padrão, como no cat. Um ficheiro com erro não
** pára o programa: mostra a mensagem e passa ao seguinte.
*/
static int	ft_cat_file(char *prog, char *file)
{
	int	fd;
	int	ret;

	fd = 0;
	if (!(file[0] == '-' && file[1] == '\0'))
		fd = open(file, O_RDONLY);
	ret = 0;
	if (fd < 0 || ft_copy(fd) < 0)
	{
		ft_error(prog, file);
		ret = 1;
	}
	if (fd > 0)
		close(fd);
	return (ret);
}

int	main(int argc, char **argv)
{
	int	i;
	int	ret;

	if (argc < 2)
		return (ft_copy(0) < 0);
	ret = 0;
	i = 1;
	while (i < argc)
	{
		if (ft_cat_file(argv[0], argv[i]))
			ret = 1;
		i++;
	}
	return (ret);
}
