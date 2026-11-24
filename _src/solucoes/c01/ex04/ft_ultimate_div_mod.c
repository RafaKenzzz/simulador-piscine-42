/*
** *a recebe o resultado e *b o resto. Guarda-se o valor original de *a,
** porque ainda é preciso para o resto depois de *a ter mudado.
*/
void	ft_ultimate_div_mod(int *a, int *b)
{
	int	tmp;

	tmp = *a;
	*a = tmp / *b;
	*b = tmp % *b;
}
