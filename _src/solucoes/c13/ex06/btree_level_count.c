#include "ft_btree.h"

/*
** Número de níveis do ramo mais comprido: 1 (o nó) mais o maior dos
** dois lados. Árvore vazia tem 0 níveis.
*/
int	btree_level_count(t_btree *root)
{
	int	left;
	int	right;

	if (!root)
		return (0);
	left = btree_level_count(root->left);
	right = btree_level_count(root->right);
	if (left > right)
		return (left + 1);
	return (right + 1);
}
