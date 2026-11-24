#include <unistd.h>

/*
** Escreve os três algarismos e, se não for a última combinação (789),
** a separação ", ". A última é a única que começa por '7'.
*/
static void	ft_put_comb(char a, char b, char c)
{
	write(1, &a, 1);
	write(1, &b, 1);
	write(1, &c, 1);
	if (a != '7')
		write(1, ", ", 2);
}

/*
** Três ciclos encaixados com a < b < c: cada combinação aparece uma vez
** e já por ordem crescente.
*/
void	ft_print_comb(void)
{
	char	a;
	char	b;
	char	c;

	a = '0';
	while (a <= '7')
	{
		b = a + 1;
		while (b <= '8')
		{
			c = b + 1;
			while (c <= '9')
			{
				ft_put_comb(a, b, c);
				c++;
			}
			b++;
		}
		a++;
	}
}
