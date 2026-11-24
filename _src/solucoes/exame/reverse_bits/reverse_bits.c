/*
** Tira o bit 0 de octet e põe-no em res, que vai andando para a esquerda.
** Ao fim de 8 voltas, o bit 0 está no 7, o 1 no 6, e assim por diante.
*/
unsigned char	reverse_bits(unsigned char octet)
{
	unsigned char	res;
	int				i;

	res = 0;
	i = 0;
	while (i < 8)
	{
		res = (res << 1) | (octet & 1);
		octet >>= 1;
		i++;
	}
	return (res);
}
