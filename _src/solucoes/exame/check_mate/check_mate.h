#ifndef CHECK_MATE_H
# define CHECK_MATE_H

# include <unistd.h>

typedef struct s_board
{
	char	**rows;
	int		size;
}	t_board;

int	ft_attacked(t_board *b, int kr, int kc);

#endif
