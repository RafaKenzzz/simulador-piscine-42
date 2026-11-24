#include <unistd.h>

/*
** Escreve um carácter de cada vez até ao '\0'.
*/
void	ft_putstr(char *str)
{
	while (*str)
	{
		write(1, str, 1);
		str++;
	}
}
