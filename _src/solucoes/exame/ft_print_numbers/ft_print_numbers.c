#include <unistd.h>

/*
** É uma função (sem main) e não leva quebra de linha.
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
