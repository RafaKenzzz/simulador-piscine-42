#include "ft_list.h"

/*
** Segue os next até NULL, contando os elementos.
*/
int	ft_list_size(t_list *begin_list)
{
	int	size;

	size = 0;
	while (begin_list)
	{
		size++;
		begin_list = begin_list->next;
	}
	return (size);
}
