#include "ft_btree.h"

/*
** Sufixo: esquerda, direita e só no fim o nó.
*/
void	btree_apply_suffix(t_btree *root, void (*applyf)(void *))
{
	if (!root)
		return ;
	btree_apply_suffix(root->left, applyf);
	btree_apply_suffix(root->right, applyf);
	applyf(root->item);
}
