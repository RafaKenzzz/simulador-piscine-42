#include <unistd.h>

/*
** Escreve um carácter de cada vez até encontrar o '\0' que fecha a string.
*/
void	ft_putstr(char *str)
{
	while (*str)
	{
		write(1, str, 1);
		str++;
	}
}
