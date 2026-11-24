/*
** Entre maiúsculas e minúsculas a diferença na tabela ASCII é sempre 32
** ('a' = 97, 'A' = 65). Só se mexe nas letras minúsculas.
*/
char	*ft_strupcase(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] >= 'a' && str[i] <= 'z')
			str[i] -= 32;
		i++;
	}
	return (str);
}
