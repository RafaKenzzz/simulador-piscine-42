#include <stddef.h>
#include "ft_list.h"

/*
** Percorre a lista e vira cada next para trás. prev é o elemento
** anterior (no fim, o novo início) e next guarda o seguinte antes de
** se perder a ligação.
*/
void	ft_list_reverse(t_list **begin_list)
{
	t_list	*prev;
	t_list	*cur;
	t_list	*next;

	prev = NULL;
	cur = *begin_list;
	while (cur)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*begin_list = prev;
}
