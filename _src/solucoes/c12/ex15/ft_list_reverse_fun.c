#include "ft_list.h"

static t_list	*ft_at(t_list *list, int n)
{
	while (n > 0)
	{
		list = list->next;
		n--;
	}
	return (list);
}

/*
** Aqui só se recebe o primeiro elemento (não o endereço do ponteiro de
** início), por isso o início não pode mudar. Em vez de mexer nas
** ligações, trocam-se os dados: o primeiro com o último, o segundo com o
** penúltimo, até ao meio.
*/
void	ft_list_reverse_fun(t_list *begin_list)
{
	t_list	*a;
	t_list	*b;
	void	*tmp;
	int		size;
	int		i;

	size = 0;
	a = begin_list;
	while (a)
	{
		size++;
		a = a->next;
	}
	i = 0;
	while (i < size / 2)
	{
		a = ft_at(begin_list, i);
		b = ft_at(begin_list, size - 1 - i);
		tmp = a->data;
		a->data = b->data;
		b->data = tmp;
		i++;
	}
}
