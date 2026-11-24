#include "list.h"

/*
** cmp(a, b) diz se a e b estão pela ordem certa (diferente de 0) ou não
** (0). Ordenação por bolha que troca os dados de vizinhos fora de ordem
** e recomeça do início. Devolve o início da lista (que não muda).
*/
t_list	*sort_list(t_list *lst, int (*cmp)(int, int))
{
	t_list	*cur;
	int		tmp;

	cur = lst;
	while (cur && cur->next)
	{
		if ((*cmp)(cur->data, cur->next->data) == 0)
		{
			tmp = cur->data;
			cur->data = cur->next->data;
			cur->next->data = tmp;
			cur = lst;
		}
		else
			cur = cur->next;
	}
	return (lst);
}
