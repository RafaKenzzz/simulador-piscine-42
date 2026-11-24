#ifndef FT_TAIL_H
# define FT_TAIL_H

# include <errno.h>
# include <fcntl.h>
# include <libgen.h>
# include <stdlib.h>
# include <string.h>
# include <unistd.h>

# define BUF_SIZE 4096

char	*ft_read_all(int fd, long *size);
void	ft_putstr_fd(char *s, int fd);
void	ft_error(char *prog, char *file);
long	ft_atol(char *s);

#endif
