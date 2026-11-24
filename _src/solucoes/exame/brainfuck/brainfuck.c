#include <stdlib.h>
#include <unistd.h>

/*
** Salta do '[' para o ']' correspondente (dir = 1) ou do ']' para o '['
** (dir = -1), contando os parênteses encaixados pelo caminho.
*/
static char	*ft_jump(char *c, int dir)
{
	int	depth;

	depth = 1;
	while (depth > 0)
	{
		c += dir;
		if (*c == '[')
			depth += dir;
		else if (*c == ']')
			depth -= dir;
	}
	return (c);
}

/*
** Executa o operador em c e devolve a posição do próximo. Os saltos
** levam ao parêntese correspondente; o + 1 passa para o carácter seguinte.
*/
static char	*ft_exec(char *c, unsigned char **p)
{
	if (*c == '>')
		(*p)++;
	else if (*c == '<')
		(*p)--;
	else if (*c == '+')
		(**p)++;
	else if (*c == '-')
		(**p)--;
	else if (*c == '.')
		write(1, *p, 1);
	else if (*c == '[' && **p == 0)
		c = ft_jump(c, 1);
	else if (*c == ']' && **p != 0)
		c = ft_jump(c, -1);
	return (c + 1);
}

/*
** Memória de 2048 bytes a zero e um ponteiro para o primeiro. Qualquer
** carácter que não seja um operador é comentário.
*/
int	main(int argc, char **argv)
{
	unsigned char	*mem;
	unsigned char	*p;
	char			*c;
	int				i;

	if (argc != 2)
	{
		write(1, "\n", 1);
		return (0);
	}
	mem = (unsigned char *)malloc(2048);
	if (!mem)
		return (1);
	i = 0;
	while (i < 2048)
		mem[i++] = 0;
	p = mem;
	c = argv[1];
	while (*c)
		c = ft_exec(c, &p);
	free(mem);
	return (0);
}
