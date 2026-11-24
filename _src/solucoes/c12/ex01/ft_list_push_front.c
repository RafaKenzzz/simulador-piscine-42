#include "ft_list.h"

/*
** O elemento novo passa a apontar para o antigo primeiro e torna-se o
** novo início. begin_list é o endereço do ponteiro de início, por isso
** a mudança fica visível fora da função.
*/
void	ft_list_push_front(t_list **begin_list, void *data)
{
	t_list	*elem;

	elem = ft_create_elem(data);
	if (!elem)
		return ;
	elem->next = *begin_list;
	*begin_list = elem;
}
