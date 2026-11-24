#include <unistd.h>

/*
** Do bit 7 (o mais significativo) ao bit 0: (octet >> i) & 1 isola o
** bit i. Sem quebra de linha no fim.
*/
void	print_bits(unsigned char octet)
{
	int		i;
	char	c;

	i = 7;
	while (i >= 0)
	{
		c = '0' + ((octet >> i) & 1);
		write(1, &c, 1);
		i--;
	}
}
