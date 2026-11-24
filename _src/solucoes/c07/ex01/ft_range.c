#include <stdlib.h>

/*
** Array com min, min + 1, ..., max - 1. O tamanho é max - min, calculado
** em long: com min = -2147483648 e max = 2147483647 não cabe num int.
*/
int	*ft_range(int min, int max)
{
	int		*range;
	long	size;
	long	i;

	if (min >= max)
		return (NULL);
	size = (long)max - min;
	range = (int *)malloc(sizeof(int) * size);
	if (!range)
		return (NULL);
	i = 0;
	while (i < size)
	{
		range[i] = min + i;
		i++;
	}
	return (range);
}
