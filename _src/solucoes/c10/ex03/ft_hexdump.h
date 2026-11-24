#ifndef FT_HEXDUMP_H
# define FT_HEXDUMP_H

# include <errno.h>
# include <fcntl.h>
# include <libgen.h>
# include <string.h>
# include <unistd.h>

# define BUF_SIZE 4096

typedef struct s_hex
{
	unsigned char	buf[BUF_SIZE];
	int				blen;
	int				bpos;
	int				fd;
	int				next;
	int				argc;
	char			**argv;
	int				err;
	unsigned char	line[16];
	unsigned char	prev[16];
	int				len;
	int				has_prev;
	int				star;
	unsigned long	off;
}	t_hex;

int		ft_next_byte(t_hex *h, unsigned char *c);
void	ft_put_line(t_hex *h);
void	ft_put_hex(unsigned long n, int width);
void	ft_putstr_fd(char *s, int fd);

#endif
