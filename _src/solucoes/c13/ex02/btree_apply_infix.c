#include "ft_btree.h"

/*
** Infixo: esquerda, nó, direita. Numa árvore de pesquisa, dá os itens
** por ordem crescente.
*/
void	btree_apply_infix(t_btree *root, void (*applyf)(void *))
{
	if (!root)
		return ;
	btree_apply_infix(root->left, applyf);
	applyf(root->item);
	btree_apply_infix(root->right, applyf);
}
