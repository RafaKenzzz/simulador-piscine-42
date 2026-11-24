/*
** Copia no máximo size - 1 caracteres e termina sempre com '\0'
** (se size > 0). Devolve o tamanho de src, para quem chama perceber se
** a cópia ficou cortada (retorno >= size).
*/
unsigned int	ft_strlcpy(char *dest, char *src, unsigned int size)
{
	unsigned int	len;
	unsigned int	i;

	len = 0;
	while (src[len])
		len++;
	if (size == 0)
		return (len);
	i = 0;
	while (src[i] && i < size - 1)
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (len);
}
