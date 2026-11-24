#include <unistd.h>

/*
** Mostra o carácter c na saída padrão (descritor 1).
** write recebe o endereço do que vai escrever, por isso passamos &c.
*/
void	ft_putchar(char c)
{
	write(1, &c, 1);
}
