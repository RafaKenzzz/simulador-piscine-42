#include <stdio.h>
#include <stdlib.h>

/*
** Um operando: sinal opcional seguido de algarismos, até ao espaço.
*/
static int	ft_is_num(char *s)
{
	if (*s == '-' || *s == '+')
		s++;
	if (*s < '0' || *s > '9')
		return (0);
	while (*s >= '0' && *s <= '9')
		s++;
	return (*s == ' ' || *s == '\0');
}

/*
** Aplica o operador aos dois últimos valores da pilha. Devolve 0 se não
** houver dois valores ou se for uma divisão ou resto por zero.
*/
static int	ft_apply(int *st, int *top, char op)
{
	int	a;
	int	b;

	if (*top < 2)
		return (0);
	b = st[--(*top)];
	a = st[*top - 1];
	if ((op == '/' || op == '%') && b == 0)
		return (0);
	if (op == '+')
		st[*top - 1] = a + b;
	else if (op == '-')
		st[*top - 1] = a - b;
	else if (op == '*')
		st[*top - 1] = a * b;
	else if (op == '/')
		st[*top - 1] = a / b;
	else
		st[*top - 1] = a % b;
	return (1);
}

static int	ft_is_op(char *s)
{
	return ((*s == '+' || *s == '-' || *s == '*' || *s == '/' || *s == '%')
		&& (s[1] == ' ' || s[1] == '\0'));
}

/*
** Lê os elementos separados por espaços: números vão para a pilha,
** operadores consomem os dois últimos. No fim tem de sobrar um só valor.
*/
static int	ft_rpn(char *s, int *st, int *top)
{
	while (*s)
	{
		while (*s == ' ')
			s++;
		if (!*s)
			break ;
		if (ft_is_num(s))
			st[(*top)++] = atoi(s);
		else if (!ft_is_op(s) || !ft_apply(st, top, *s))
			return (0);
		while (*s && *s != ' ')
			s++;
	}
	return (*top == 1);
}

/*
** A pilha nunca tem mais valores do que caracteres na expressão.
*/
int	main(int argc, char **argv)
{
	int	*st;
	int	top;
	int	len;

	if (argc != 2)
	{
		printf("Error\n");
		return (0);
	}
	len = 0;
	while (argv[1][len])
		len++;
	st = (int *)malloc(sizeof(int) * (len + 1));
	top = 0;
	if (st && ft_rpn(argv[1], st, &top))
		printf("%d\n", st[0]);
	else
		printf("Error\n");
	free(st);
	return (0);
}
