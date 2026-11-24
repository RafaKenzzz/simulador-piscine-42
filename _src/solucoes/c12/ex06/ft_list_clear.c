#include <stdlib.h>
#include "ft_list.h"

/*
** Guarda o next antes de libertar o elemento: depois do free já não se
** pode ler. O free_fct liberta os dados; o free liberta o elemento.
*/
void	ft_list_clear(t_list *begin_list, void (*free_fct)(void *))
{
	t_list	*next;

	while (begin_list)
	{
		next = begin_list->next;
		free_fct(begin_list->data);
		free(begin_list);
		begin_list = next;
	}
}
