#include "rush02.h"

int	ft_strlen(char *s)
{
	int	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

int	ft_strcmp(char *s1, char *s2)
{
	while (*s1 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

/*
** Cópia nova dos primeiros n caracteres de s.
*/
char	*ft_strndup(char *s, int n)
{
	char	*dup;
	int		i;

	dup = (char *)malloc(n + 1);
	if (!dup)
		return (NULL);
	i = 0;
	while (i < n)
	{
		dup[i] = s[i];
		i++;
	}
	dup[n] = '\0';
	return (dup);
}

void	ft_putstr(char *s)
{
	write(1, s, ft_strlen(s));
}
