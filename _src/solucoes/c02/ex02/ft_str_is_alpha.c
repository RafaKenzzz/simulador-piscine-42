/*
** Devolve 0 ao primeiro carácter que não seja letra. Se chegar ao fim
** (ou a string estiver vazia), devolve 1.
*/
int	ft_str_is_alpha(char *str)
{
	while (*str)
	{
		if (!((*str >= 'a' && *str <= 'z') || (*str >= 'A' && *str <= 'Z')))
			return (0);
		str++;
	}
	return (1);
}
