#include <stdlib.h>
#include "ft_list.h"

/*
** Percorre a lista através do endereço do ponteiro que aponta para o
** elemento atual (*cur): no início é begin_list, depois o next do
** anterior. Para apagar, esse ponteiro passa a apontar para o seguinte;
** assim o primeiro elemento não precisa de um caso à parte.
*/
void	ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)())
{
	t_list	**cur;
	t_list	*del;

	cur = begin_list;
	while (*cur)
	{
		if ((*cmp)((*cur)->data, data_ref) == 0)
		{
			del = *cur;
			*cur = del->next;
			free(del);
		}
		else
			cur = &(*cur)->next;
	}
}
