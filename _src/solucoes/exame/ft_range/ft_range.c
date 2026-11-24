#include <stdlib.h>

/*
** De start até end, os dois incluídos, a subir ou a descer: o tamanho é
** a distância entre eles mais 1 e o passo é +1 ou -1.
*/
int	*ft_range(int start, int end)
{
	int		*tab;
	long	size;
	long	i;
	int		step;

	size = (long)end - start;
	step = 1;
	if (size < 0)
	{
		size = -size;
		step = -1;
	}
	tab = (int *)malloc(sizeof(int) * (size + 1));
	if (!tab)
		return (NULL);
	i = 0;
	while (i <= size)
	{
		tab[i] = start + i * step;
		i++;
	}
	return (tab);
}
