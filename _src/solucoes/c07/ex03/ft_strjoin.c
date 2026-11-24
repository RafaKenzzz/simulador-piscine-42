#include <stdlib.h>

static int	ft_strlen(char *s)
{
	int	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

/*
** Copia src para o fim de dest e devolve o novo fim de dest.
*/
static char	*ft_append(char *dest, char *src)
{
	while (*src)
		*dest++ = *src++;
	return (dest);
}

/*
** Primeiro calcula o tamanho total (todas as strings, size - 1
** separadores e o '\0'), reserva-o de uma vez e depois copia tudo.
** Com size 0 devolve uma string vazia que pode ser libertada com free.
*/
char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*res;
	char	*end;
	int		total;
	int		i;

	total = 1;
	i = -1;
	while (++i < size)
		total += ft_strlen(strs[i]);
	if (size > 0)
		total += ft_strlen(sep) * (size - 1);
	res = (char *)malloc(sizeof(char) * total);
	if (!res)
		return (NULL);
	end = res;
	i = -1;
	while (++i < size)
	{
		end = ft_append(end, strs[i]);
		if (i < size - 1)
			end = ft_append(end, sep);
	}
	*end = '\0';
	return (res);
}
