/*
** Uma palavra é uma sequência de letras e algarismos.
*/
static int	ft_is_alnum(char c)
{
	return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')
		|| (c >= '0' && c <= '9'));
}

/*
** Passa tudo a minúsculas e depois põe em maiúscula cada letra que esteja
** no início de uma palavra: na posição 0 ou depois de um carácter que não
** seja letra nem algarismo. "42mots" fica igual: começa por um algarismo.
*/
char	*ft_strcapitalize(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			str[i] += 32;
		i++;
	}
	i = 0;
	while (str[i])
	{
		if (str[i] >= 'a' && str[i] <= 'z'
			&& (i == 0 || !ft_is_alnum(str[i - 1])))
			str[i] -= 32;
		i++;
	}
	return (str);
}
