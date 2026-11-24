/*
** 1 se a string só tiver letras maiúsculas (ou estiver vazia).
*/
int	ft_str_is_uppercase(char *str)
{
	while (*str)
	{
		if (*str < 'A' || *str > 'Z')
			return (0);
		str++;
	}
	return (1);
}
