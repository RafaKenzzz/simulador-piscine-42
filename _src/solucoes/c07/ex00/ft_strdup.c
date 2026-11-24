#include <stdlib.h>

/*
** Reserva len + 1 bytes (o + 1 é para o '\0'), copia e devolve a cópia.
** Se o malloc falhar, devolve NULL, como o strdup.
*/
char	*ft_strdup(char *src)
{
	char	*dup;
	int		len;
	int		i;

	len = 0;
	while (src[len])
		len++;
	dup = (char *)malloc(sizeof(char) * (len + 1));
	if (!dup)
		return (NULL);
	i = 0;
	while (i <= len)
	{
		dup[i] = src[i];
		i++;
	}
	return (dup);
}
