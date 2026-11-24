#include <unistd.h>

/*
** Os algarismos '0' a '9' também são consecutivos na tabela ASCII.
*/
void	ft_print_numbers(void)
{
	char	c;

	c = '0';
	while (c <= '9')
	{
		write(1, &c, 1);
		c++;
	}
}
