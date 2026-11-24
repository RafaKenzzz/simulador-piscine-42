#include <unistd.h>

/*
** Lê o enunciado com atenção: com 'z', sem 'z' ou com o número errado de
** argumentos, a saída é sempre "z\n".
*/
int	main(void)
{
	write(1, "z\n", 2);
	return (0);
}
