#ifndef RUSH02_H
# define RUSH02_H

# include <fcntl.h>
# include <stdlib.h>
# include <unistd.h>

# define BUF_SIZE 4096

typedef struct s_entry
{
	char	*key;
	char	*value;
}	t_entry;

typedef struct s_dict
{
	t_entry	*entries;
	int		size;
	int		print;
	int		first;
	int		ok;
}	t_dict;

char	*ft_read_file(char *path);
int		ft_parse_dict(char *content, t_dict *dict);
void	ft_free_dict(t_dict *dict);
void	ft_convert(char *nbr, t_dict *dict);
int		ft_strlen(char *s);
int		ft_strcmp(char *s1, char *s2);
char	*ft_strndup(char *s, int n);
void	ft_putstr(char *s);

#endif
