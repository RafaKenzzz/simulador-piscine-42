#include <unistd.h>

/*
** As letras são números na tabela ASCII ('a' = 97 … 'z' = 122),
** por isso basta somar 1 a 'a' até passar de 'z'.
*/
void	ft_print_alphabet(void)
{
	char	c;

	c = 'a';
	while (c <= 'z')
	{
		write(1, &c, 1);
		c++;
	}
}
