/*
** Copia no máximo n caracteres. Se src acabar antes, o resto de dest
** (até n) é preenchido com '\0'. Se src tiver n ou mais caracteres,
** dest NÃO fica terminado em '\0': é assim que o strncpy funciona.
*/
char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < n && src[i])
	{
		dest[i] = src[i];
		i++;
	}
	while (i < n)
	{
		dest[i] = '\0';
		i++;
	}
	return (dest);
}
