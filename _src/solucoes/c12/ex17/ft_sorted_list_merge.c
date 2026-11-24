#include "ft_list.h"

/*
** Insere o elemento node (já existente) no sítio certo da lista.
*/
static void	ft_insert(t_list **begin, t_list *node, int (*cmp)())
{
	t_list	*cur;

	if (!*begin || (*cmp)(node->data, (*begin)->data) < 0)
	{
		node->next = *begin;
		*begin = node;
		return ;
	}
	cur = *begin;
	while (cur->next && (*cmp)(cur->next->data, node->data) <= 0)
		cur = cur->next;
	node->next = cur->next;
	cur->next = node;
}

/*
** Cada elemento da segunda lista é retirado (guardando o seguinte) e
** inserido na primeira. Nenhum elemento é criado.
*/
void	ft_sorted_list_merge(t_list **begin_list1, t_list *begin_list2,
		int (*cmp)())
{
	t_list	*next;

	while (begin_list2)
	{
		next = begin_list2->next;
		ft_insert(begin_list1, begin_list2, cmp);
		begin_list2 = next;
	}
}
