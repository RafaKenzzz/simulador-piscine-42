#include <stdlib.h>
#include "ft_list.h"

/*
** prev é o último elemento que fica. Quando se apaga um elemento, o
** anterior (ou o início da lista, se for o primeiro) passa a apontar
** para o seguinte. O next é guardado antes do free.
*/
void	ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)(),
		void (*free_fct)(void *))
{
	t_list	*cur;
	t_list	*prev;
	t_list	*next;

	prev = NULL;
	cur = *begin_list;
	while (cur)
	{
		next = cur->next;
		if ((*cmp)(cur->data, data_ref) == 0)
		{
			if (prev)
				prev->next = next;
			else
				*begin_list = next;
			(*free_fct)(cur->data);
			free(cur);
		}
		else
			prev = cur;
		cur = next;
	}
}
