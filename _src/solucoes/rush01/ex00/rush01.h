#ifndef RUSH01_H
# define RUSH01_H

# include <unistd.h>

int		ft_parse(char *str, int *views);
int		ft_solve(int grid[4][4], int *views, int pos);
void	ft_print_grid(int grid[4][4]);

#endif
