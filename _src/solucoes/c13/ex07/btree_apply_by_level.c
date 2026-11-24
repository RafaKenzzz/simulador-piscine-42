#include <stdlib.h>
#include "ft_btree.h"

static int	ft_size(t_btree *root)
{
	if (!root)
		return (0);
	return (1 + ft_size(root->left) + ft_size(root->right));
}

/*
** Trata um nível inteiro: os nós que estão na fila entre ht[0] e o fim
** atual. Cada um é passado a applyf e os filhos entram no fim da fila,
** formando o nível seguinte. O primeiro de cada nível leva is_first = 1.
*/
static void	ft_level(t_btree **queue, int *ht, int level,
		void (*applyf)(void *, int, int))
{
	t_btree	*node;
	int		end;
	int		first;

	end = ht[1];
	first = 1;
	while (ht[0] < end)
	{
		node = queue[ht[0]];
		ht[0]++;
		applyf(node->item, level, first);
		first = 0;
		if (node->left)
			queue[ht[1]++] = node->left;
		if (node->right)
			queue[ht[1]++] = node->right;
	}
}

/*
** Percurso em largura com uma fila (um array com espaço para todos os
** nós). ht[0] é a cabeça da fila e ht[1] o fim.
*/
void	btree_apply_by_level(t_btree *root, void (*applyf)(void *item,
		int current_level, int is_first_elem))
{
	t_btree	**queue;
	int		ht[2];
	int		level;

	if (!root)
		return ;
	queue = (t_btree **)malloc(sizeof(t_btree *) * ft_size(root));
	if (!queue)
		return ;
	queue[0] = root;
	ht[0] = 0;
	ht[1] = 1;
	level = 0;
	while (ht[0] < ht[1])
	{
		ft_level(queue, ht, level, applyf);
		level++;
	}
	free(queue);
}
