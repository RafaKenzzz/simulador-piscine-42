#include <unistd.h>

/*
** De 'z' para 'a': a 1.ª (z) minúscula, a 2.ª (Y) maiúscula, e assim
** alternadamente.
*/
int	main(void)
{
	char	c;
	int		i;

	i = 0;
	while (i < 26)
	{
		c = 'z' - i;
		if (i % 2 == 1)
			c = 'Z' - i;
		write(1, &c, 1);
		i++;
	}
	write(1, "\n", 1);
	return (0);
}
