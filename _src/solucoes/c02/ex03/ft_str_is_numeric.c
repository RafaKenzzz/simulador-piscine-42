/*
** 1 se a string só tiver algarismos (ou estiver vazia), 0 caso contrário.
*/
int	ft_str_is_numeric(char *str)
{
	while (*str)
	{
		if (*str < '0' || *str > '9')
			return (0);
		str++;
	}
	return (1);
}
