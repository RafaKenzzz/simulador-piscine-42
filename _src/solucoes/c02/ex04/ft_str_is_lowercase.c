/*
** 1 se a string só tiver letras minúsculas (ou estiver vazia).
*/
int	ft_str_is_lowercase(char *str)
{
	while (*str)
	{
		if (*str < 'a' || *str > 'z')
			return (0);
		str++;
	}
	return (1);
}
