#include <unistd.h>

/*
** Pilha com os parênteses abertos. Cada fecho tem de corresponder ao
** último aberto; no fim, a pilha tem de estar vazia. Os outros
** caracteres são ignorados.
*/
static int	ft_check(char *s)
{
	char	stack[131072];
	int		top;

	top = 0;
	while (*s)
	{
		if (*s == '(' || *s == '[' || *s == '{')
		{
			if (top == 131072)
				return (0);
			stack[top++] = *s;
		}
		else if (*s == ')' || *s == ']' || *s == '}')
		{
			if (top == 0 || stack[top - 1] != "([{"[(*s != ')') + (*s == '}')])
				return (0);
			top--;
		}
		s++;
	}
	return (top == 0);
}

int	main(int argc, char **argv)
{
	int	i;

	if (argc == 1)
		write(1, "\n", 1);
	i = 1;
	while (i < argc)
	{
		if (ft_check(argv[i]))
			write(1, "OK\n", 3);
		else
			write(1, "Error\n", 6);
		i++;
	}
	return (0);
}
