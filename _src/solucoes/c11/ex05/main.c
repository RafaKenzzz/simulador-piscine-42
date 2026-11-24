#include "do_op.h"

/*
** Array de ponteiros para funções, pela mesma ordem dos símbolos da
** string symbols: o operador na posição i é calculado por ops[i].
*/
static void	ft_init(t_op *ops)
{
	ops[0] = &ft_add;
	ops[1] = &ft_sub;
	ops[2] = &ft_div;
	ops[3] = &ft_mul;
	ops[4] = &ft_mod;
}

/*
** O operador tem de ser exatamente um destes cinco caracteres. Se não
** for, mostra 0. A divisão e o resto por zero têm mensagens próprias.
*/
int	main(int argc, char **argv)
{
	t_op	ops[5];
	char	*symbols;
	int		i;
	int		b;

	if (argc != 4)
		return (0);
	ft_init(ops);
	symbols = "+-/*%";
	i = 0;
	while (symbols[i] && !(argv[2][0] == symbols[i] && argv[2][1] == '\0'))
		i++;
	b = ft_atoi(argv[3]);
	if (!symbols[i])
		ft_putstr("0");
	else if (b == 0 && symbols[i] == '/')
		ft_putstr("Stop : division by zero");
	else if (b == 0 && symbols[i] == '%')
		ft_putstr("Stop : modulo by zero");
	else
		ft_putnbr(ops[i](ft_atoi(argv[1]), b));
	ft_putstr("\n");
	return (0);
}
