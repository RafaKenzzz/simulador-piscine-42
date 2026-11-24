#include <stdlib.h>

/*
** Igual ao ft_range, mas o array é devolvido através de *range e a
** função devolve o tamanho: 0 se min >= max (com *range = NULL) e -1 se
** o malloc falhar.
*/
int	ft_ultimate_range(int **range, int min, int max)
{
	long	size;
	long	i;

	if (min >= max)
	{
		*range = NULL;
		return (0);
	}
	size = (long)max - min;
	*range = (int *)malloc(sizeof(int) * size);
	if (!*range)
		return (-1);
	i = 0;
	while (i < size)
	{
		(*range)[i] = min + i;
		i++;
	}
	return (size);
}
