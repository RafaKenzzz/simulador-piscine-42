#include <stddef.h>
#include "ft_btree.h"

/*
** Percurso infixo: procura primeiro à esquerda, depois no nó, depois à
** direita. Devolve o primeiro item igual a data_ref, ou NULL.
*/
void	*btree_search_item(t_btree *root, void *data_ref,
		int (*cmpf)(void *, void *))
{
	void	*found;

	if (!root)
		return (NULL);
	found = btree_search_item(root->left, data_ref, cmpf);
	if (found)
		return (found);
	if (cmpf(root->item, data_ref) == 0)
		return (root->item);
	return (btree_search_item(root->right, data_ref, cmpf));
}
