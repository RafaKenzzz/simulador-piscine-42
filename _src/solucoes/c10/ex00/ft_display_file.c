#include <fcntl.h>
#include <unistd.h>

#define BUF_SIZE 4096

static void	ft_puterr(char *s)
{
	int	len;

	len = 0;
	while (s[len])
		len++;
	write(2, s, len);
}

/*
** Lê o ficheiro aos bocados para um array de tamanho fixo (o malloc é
** proibido) e escreve cada bocado na saída. read devolve o número de
** bytes lidos, 0 no fim do ficheiro e -1 em caso de erro.
** As mensagens de erro vão para a saída de erro (descritor 2).
*/
int	main(int argc, char **argv)
{
	char	buf[BUF_SIZE];
	int		fd;
	int		n;

	if (argc < 2)
		ft_puterr("File name missing.\n");
	if (argc > 2)
		ft_puterr("Too many arguments.\n");
	if (argc != 2)
		return (1);
	fd = open(argv[1], O_RDONLY);
	n = -1;
	if (fd >= 0)
		n = read(fd, buf, BUF_SIZE);
	while (n > 0)
	{
		write(1, buf, n);
		n = read(fd, buf, BUF_SIZE);
	}
	if (fd >= 0)
		close(fd);
	if (n < 0)
		ft_puterr("Cannot read file.\n");
	return (n < 0);
}
