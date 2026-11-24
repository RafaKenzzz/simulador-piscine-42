#include "ft_list.h"

/*
** Ordenação por bolha que troca os dados de elementos vizinhos (as
** ligações ficam iguais). Depois de cada troca recomeça do início.
*/
void	ft_list_sort(t_list **begin_list, int (*cmp)())
{
	t_list	*cur;
	void	*tmp;

	cur = *begin_list;
	while (cur && cur->next)
	{
		if ((*cmp)(cur->data, cur->next->data) > 0)
		{
			tmp = cur->data;
			cur->data = cur->next->data;
			cur->next->data = tmp;
			cur = *begin_list;
		}
		else
			cur = cur->next;
	}
}
