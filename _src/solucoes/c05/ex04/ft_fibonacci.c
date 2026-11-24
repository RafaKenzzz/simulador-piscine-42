/*
** F(0) = 0, F(1) = 1 e F(n) = F(n - 1) + F(n - 2).
** Índice negativo devolve -1.
*/
int	ft_fibonacci(int index)
{
	if (index < 0)
		return (-1);
	if (index < 2)
		return (index);
	return (ft_fibonacci(index - 1) + ft_fibonacci(index - 2));
}
