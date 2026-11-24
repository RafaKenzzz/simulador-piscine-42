#include <unistd.h>

/*
** Escreve um número de 0 a 99 sempre com dois algarismos (7 -> "07").
*/
static void	ft_put_two(int n)
{
	char	digits[2];

	digits[0] = '0' + n / 10;
	digits[1] = '0' + n % 10;
	write(1, digits, 2);
}

/*
** Pares (a, b) com a < b, de "00 01" até "98 99".
** Só a última combinação não leva ", " a seguir.
*/
void	ft_print_comb2(void)
{
	int	a;
	int	b;

	a = 0;
	while (a <= 98)
	{
		b = a + 1;
		while (b <= 99)
		{
			ft_put_two(a);
			write(1, " ", 1);
			ft_put_two(b);
			if (a != 98)
				write(1, ", ", 2);
			b++;
		}
		a++;
	}
}
