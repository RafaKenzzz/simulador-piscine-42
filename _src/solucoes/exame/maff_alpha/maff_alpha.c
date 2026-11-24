#include <unistd.h>

/*
** A letra na posição i (a = 0) sai em maiúscula quando i é ímpar:
** a B c D ... (a "par" do enunciado é a 2.ª, 4.ª, ... letra).
*/
int	main(void)
{
	char	c;
	int		i;

	i = 0;
	while (i < 26)
	{
		c = 'a' + i;
		if (i % 2 == 1)
			c = 'A' + i;
		write(1, &c, 1);
		i++;
	}
	write(1, "\n", 1);
	return (0);
}
