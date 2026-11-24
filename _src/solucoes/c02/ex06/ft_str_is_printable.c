/*
** Imprimíveis são os caracteres ASCII de 32 (espaço) a 126 ('~').
*/
int	ft_str_is_printable(char *str)
{
	while (*str)
	{
		if (*str < 32 || *str > 126)
			return (0);
		str++;
	}
	return (1);
}
