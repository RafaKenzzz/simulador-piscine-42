/*
** Conta os caracteres antes do '\0' (o '\0' não conta).
*/
int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}
