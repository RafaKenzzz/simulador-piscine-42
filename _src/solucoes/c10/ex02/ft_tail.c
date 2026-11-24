#include "ft_tail.h"

/*
** Escreve os últimos n bytes do que se leu de fd (todos, se o ficheiro
** for mais pequeno). Devolve 1 em caso de erro de leitura.
*/
static int	ft_tail_fd(int fd, long n)
{
	char	*data;
	long	size;
	long	start;

	data = ft_read_all(fd, &size);
	if (!data)
		return (1);
	start = 0;
	if (size > n)
		start = size - n;
	write(1, data + start, size - start);
	free(data);
	return (0);
}

/*
** Com mais de um ficheiro, cada um leva o cabeçalho "==> nome <==", com
** uma linha vazia antes a partir do segundo (como o tail).
*/
static int	ft_tail_file(char **argv, char *file, long n, int *shown)
{
	int	fd;
	int	err;

	fd = open(file, O_RDONLY);
	if (fd < 0)
	{
		ft_error(argv[0], file);
		return (1);
	}
	if (shown[1] > 1)
	{
		if (shown[0])
			ft_putstr_fd("\n", 1);
		ft_putstr_fd("==> ", 1);
		ft_putstr_fd(file, 1);
		ft_putstr_fd(" <==\n", 1);
	}
	shown[0] = 1;
	err = ft_tail_fd(fd, n);
	if (err)
		ft_error(argv[0], file);
	close(fd);
	return (err);
}

/*
** Aceita "-c N" e "-cN". Devolve o índice do primeiro ficheiro, ou 0 se
** a opção estiver mal escrita.
*/
static int	ft_parse(int argc, char **argv, long *n)
{
	if (argc < 2 || argv[1][0] != '-' || argv[1][1] != 'c')
		return (0);
	if (argv[1][2])
	{
		*n = ft_atol(argv[1] + 2);
		return (2 * (*n >= 0));
	}
	if (argc < 3)
		return (0);
	*n = ft_atol(argv[2]);
	return (3 * (*n >= 0));
}

int	main(int argc, char **argv)
{
	long	n;
	int		first;
	int		shown[2];
	int		ret;

	first = ft_parse(argc, argv, &n);
	if (first == 0)
	{
		ft_putstr_fd("usage: ft_tail -c number [file ...]\n", 2);
		return (1);
	}
	if (first == argc)
		return (ft_tail_fd(0, n));
	shown[0] = 0;
	shown[1] = argc - first;
	ret = 0;
	while (first < argc)
	{
		if (ft_tail_file(argv, argv[first], n, shown))
			ret = 1;
		first++;
	}
	return (ret);
}
