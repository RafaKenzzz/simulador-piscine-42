/*
** Espaços em branco segundo o isspace(3): espaço, \t, \n, \v, \f e \r
** (códigos 9 a 13 e 32).
*/
static int	ft_is_space(char c)
{
	return (c == ' ' || (c >= 9 && c <= 13));
}

/*
** 1) salta os espaços; 2) lê todos os '+' e '-', trocando o sinal a cada
** '-'; 3) acumula os algarismos até aparecer outro carácter.
*/
int	ft_atoi(char *str)
{
	int	i;
	int	sign;
	int	result;

	i = 0;
	while (ft_is_space(str[i]))
		i++;
	sign = 1;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			sign = -sign;
		i++;
	}
	result = 0;
	while (str[i] >= '0' && str[i] <= '9')
	{
		result = result * 10 + (str[i] - '0');
		i++;
	}
	return (result * sign);
}
