#include "ft_btree.h"

/*
** Prefixo: primeiro o nó, depois a subárvore esquerda, depois a direita.
*/
void	btree_apply_prefix(t_btree *root, void (*applyf)(void *))
{
	if (!root)
		return ;
	applyf(root->item);
	btree_apply_prefix(root->left, applyf);
	btree_apply_prefix(root->right, applyf);
}
