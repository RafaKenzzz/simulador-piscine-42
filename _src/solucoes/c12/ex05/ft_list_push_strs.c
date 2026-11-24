#include <stddef.h>
#include "ft_list.h"

/*
** Cada string é posta à frente da lista: a primeira (strs[0]) acaba no
** fim e a última no início, como pede o enunciado.
*/
t_list	*ft_list_push_strs(int size, char **strs)
{
	t_list	*begin;
	t_list	*elem;
	int		i;

	begin = NULL;
	i = 0;
	while (i < size)
	{
		elem = ft_create_elem(strs[i]);
		if (!elem)
			return (begin);
		elem->next = begin;
		begin = elem;
		i++;
	}
	return (begin);
}
