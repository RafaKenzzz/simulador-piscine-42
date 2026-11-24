#include <unistd.h>

/*
** O mesmo que ft_print_alphabet, a descer de 'z' até 'a'.
*/
void	ft_print_reverse_alphabet(void)
{
	char	c;

	c = 'z';
	while (c >= 'a')
	{
		write(1, &c, 1);
		c--;
	}
}
