#ifndef BSQ_H
# define BSQ_H

# include <fcntl.h>
# include <stdlib.h>
# include <unistd.h>

# define BUF_SIZE 65536

typedef struct s_map
{
	char	**rows;
	int		height;
	int		width;
	char	empty;
	char	obstacle;
	char	full;
	int		best;
	int		bi;
	int		bj;
}	t_map;

char	*ft_read_fd(int fd);
int		ft_parse(char *content, t_map *map);
int		ft_solve(t_map *map);
void	ft_print(t_map *map);

#endif
