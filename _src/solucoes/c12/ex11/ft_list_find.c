#include <stddef.h>
#include "ft_list.h"

/*
** Devolve o primeiro elemento em que cmp(dados, data_ref) dá 0, ou NULL.
*/
t_list	*ft_list_find(t_list *begin_list, void *data_ref, int (*cmp)())
{
	while (begin_list)
	{
		if ((*cmp)(begin_list->data, data_ref) == 0)
			return (begin_list);
		begin_list = begin_list->next;
	}
	return (NULL);
}
