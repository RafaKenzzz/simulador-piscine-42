#include <unistd.h>

/*
** De '9' a '0' e uma quebra de linha.
*/
int	main(void)
{
	char	c;

	c = '9';
	while (c >= '0')
	{
		write(1, &c, 1);
		c--;
	}
	write(1, "\n", 1);
	return (0);
}
