#include "ft_btree.h"

/*
** Desce pela árvore: para a esquerda se o item for menor do que o do
** nó, para a direita se for maior ou igual. No primeiro lugar vazio
** cria-se o nó. root é o endereço do ponteiro, para o poder mudar.
*/
void	btree_insert_data(t_btree **root, void *item,
		int (*cmpf)(void *, void *))
{
	if (!*root)
	{
		*root = btree_create_node(item);
		return ;
	}
	if (cmpf(item, (*root)->item) < 0)
		btree_insert_data(&(*root)->left, item, cmpf);
	else
		btree_insert_data(&(*root)->right, item, cmpf);
}
