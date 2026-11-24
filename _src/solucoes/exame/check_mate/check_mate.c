#include "check_mate.h"

/*
** Peça na casa (r, c), ou '.' se estiver fora do tabuleiro. Tudo o que
** não for P, B, R, Q ou K conta como casa vazia.
*/
static char	ft_at(t_board *b, int r, int c)
{
	char	p;

	if (r < 0 || c < 0 || r >= b->size || c >= b->size)
		return ('.');
	p = b->rows[r][c];
	if (p == 'P' || p == 'B' || p == 'R' || p == 'Q' || p == 'K')
		return (p);
	return ('.');
}

/*
** A partir do rei, anda na direção (dr, dc) até encontrar a primeira
** peça: só essa pode atacar (as outras estão tapadas). Ataca se for uma
** das duas peças que se movem nessa direção (a ou q).
*/
static int	ft_ray(t_board *b, int *k, int *d, char a)
{
	int		r;
	int		c;
	char	p;

	r = k[0] + d[0];
	c = k[1] + d[1];
	while (r >= 0 && c >= 0 && r < b->size && c < b->size)
	{
		p = ft_at(b, r, c);
		if (p != '.')
			return (p == a || p == 'Q');
		r += d[0];
		c += d[1];
	}
	return (0);
}

/*
** Torre e dama nas 4 direções retas, bispo e dama nas 4 diagonais, e
** os peões que estão na linha de baixo, nas diagonais (os peões atacam
** para cima, na diagonal).
*/
int	ft_attacked(t_board *b, int kr, int kc)
{
	int	k[2];
	int	d[2];
	int	i;

	k[0] = kr;
	k[1] = kc;
	if (ft_at(b, kr + 1, kc - 1) == 'P' || ft_at(b, kr + 1, kc + 1) == 'P')
		return (1);
	i = 0;
	while (i < 9)
	{
		d[0] = i / 3 - 1;
		d[1] = i % 3 - 1;
		if (i != 4 && ft_ray(b, k, d, "BRB"[(d[0] == 0 || d[1] == 0)]))
			return (1);
		i++;
	}
	return (0);
}
