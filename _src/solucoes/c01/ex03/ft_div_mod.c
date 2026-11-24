/*
** O resultado da divisão inteira vai para *div e o resto para *mod.
*/
void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}
