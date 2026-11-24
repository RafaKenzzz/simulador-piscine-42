/*
** Troca os valores apontados por a e b. Sem a variável temporária,
** o primeiro valor perdia-se ao ser escrito por cima.
*/
void	ft_swap(int *a, int *b)
{
	int	tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}
