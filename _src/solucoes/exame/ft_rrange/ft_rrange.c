#include <stdlib.h>

/*
** Como o ft_range, mas de end até start.
*/
int	*ft_rrange(int start, int end)
{
	int		*tab;
	long	size;
	long	i;
	int		step;

	size = (long)start - end;
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
		tab[i] = end + i * step;
		i++;
	}
	return (tab);
}
