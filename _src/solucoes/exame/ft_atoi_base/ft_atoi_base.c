/*
** Valor do algarismo c (0-9, a-f, A-F), ou -1 se não for algarismo.
*/
static int	ft_value(char c)
{
	if (c >= '0' && c <= '9')
		return (c - '0');
	if (c >= 'a' && c <= 'f')
		return (c - 'a' + 10);
	if (c >= 'A' && c <= 'F')
		return (c - 'A' + 10);
	return (-1);
}

/*
** O '-' só conta se for o primeiro carácter. Cada algarismo tem de ser
** menor do que a base; o primeiro que não for termina a leitura.
*/
int	ft_atoi_base(const char *str, int str_base)
{
	int	sign;
	int	result;
	int	v;

	if (str_base < 2 || str_base > 16)
		return (0);
	sign = 1;
	if (*str == '-')
	{
		sign = -1;
		str++;
	}
	result = 0;
	v = ft_value(*str);
	while (v >= 0 && v < str_base)
	{
		result = result * str_base + v;
		str++;
		v = ft_value(*str);
	}
	return (result * sign);
}
