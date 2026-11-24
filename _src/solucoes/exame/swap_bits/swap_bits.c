/*
** As 4 metades: a de cima desce 4 posições e a de baixo sobe 4.
*/
unsigned char	swap_bits(unsigned char octet)
{
	return ((octet >> 4) | (octet << 4));
}
