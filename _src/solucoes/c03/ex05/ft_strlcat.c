/*
** size é o tamanho TOTAL do buffer dest. Copia-se src para o fim de dest
** até ocupar size - 1 caracteres e termina-se com '\0'.
** Devolve o tamanho da string que se tentou criar: dlen + slen. Se size
** for menor ou igual ao tamanho de dest, não se copia nada e devolve-se
** size + slen.
*/
unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int	dlen;
	unsigned int	slen;
	unsigned int	i;

	dlen = 0;
	while (dlen < size && dest[dlen])
		dlen++;
	slen = 0;
	while (src[slen])
		slen++;
	if (dlen == size)
		return (size + slen);
	i = 0;
	while (src[i] && dlen + i < size - 1)
	{
		dest[dlen + i] = src[i];
		i++;
	}
	dest[dlen + i] = '\0';
	return (dlen + slen);
}
