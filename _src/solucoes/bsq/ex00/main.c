#include "bsq.h"

/*
** Lê, valida, resolve e escreve um mapa. Em caso de erro escreve
** "map error" na saída de erro.
*/
static void	ft_bsq(int fd)
{
	t_map	map;
	char	*content;

	content = ft_read_fd(fd);
	if (content && ft_parse(content, &map) && ft_solve(&map))
		ft_print(&map);
	else
		write(2, "map error\n", 10);
	if (content)
		free(map.rows);
	free(content);
}

/*
** Sem argumentos, lê da entrada padrão. Com vários mapas, cada resultado
** (ou erro) é seguido de uma quebra de linha.
*/
int	main(int argc, char **argv)
{
	int	i;
	int	fd;

	if (argc == 1)
		ft_bsq(0);
	i = 1;
	while (i < argc)
	{
		fd = open(argv[i], O_RDONLY);
		if (fd < 0)
			write(2, "map error\n", 10);
		else
		{
			ft_bsq(fd);
			close(fd);
		}
		if (argc > 2)
			write(1, "\n", 1);
		i++;
	}
	return (0);
}
