#include <unistd.h>

/*
** Escreve a combinação guardada em tab. A última combinação é a única
** que começa pelo algarismo 10 - n (por exemplo "89" para n = 2).
*/
static void	ft_put_comb(char *tab, int n)
{
	write(1, tab, n);
	if (tab[0] != '0' + 10 - n)
		write(1, ", ", 2);
}

/*
** Preenche a posição pos com cada algarismo possível e chama-se a si
** própria para a posição seguinte. Cada algarismo tem de ser maior do que
** o anterior e deixar espaço para os que faltam (no máximo '9' - restantes).
*/
static void	ft_fill(char *tab, int pos, int n)
{
	char	d;

	if (pos == n)
	{
		ft_put_comb(tab, n);
		return ;
	}
	d = '0';
	if (pos > 0)
		d = tab[pos - 1] + 1;
	while (d <= '9' - (n - 1 - pos))
	{
		tab[pos] = d;
		ft_fill(tab, pos + 1, n);
		d++;
	}
}

void	ft_print_combn(int n)
{
	char	tab[10];

	if (n <= 0 || n >= 10)
		return ;
	ft_fill(tab, 0, n);
}
