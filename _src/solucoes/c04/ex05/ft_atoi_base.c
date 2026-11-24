/*
** Base inválida (devolve 0): menos de 2 símbolos, símbolos repetidos,
** '+', '-' ou espaços em branco. Senão devolve o tamanho da base.
*/
static int	ft_base_len(char *base)
{
	int	i;
	int	j;

	i = 0;
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-' || base[i] == ' '
			|| (base[i] >= 9 && base[i] <= 13))
			return (0);
		j = i + 1;
		while (base[j])
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		i++;
	}
	if (i < 2)
		return (0);
	return (i);
}

/*
** Posição de c na base, ou -1 se c não for um símbolo da base.
*/
static int	ft_index(char c, char *base)
{
	int	i;

	i = 0;
	while (base[i])
	{
		if (base[i] == c)
			return (i);
		i++;
	}
	return (-1);
}

/*
** As mesmas regras do ft_atoi; só muda o que conta como algarismo e o
** valor de cada um (a posição na base).
*/
int	ft_atoi_base(char *str, char *base)
{
	int	len;
	int	sign;
	int	result;

	len = ft_base_len(base);
	if (len == 0)
		return (0);
	while (*str == ' ' || (*str >= 9 && *str <= 13))
		str++;
	sign = 1;
	while (*str == '+' || *str == '-')
	{
		if (*str == '-')
			sign = -sign;
		str++;
	}
	result = 0;
	while (ft_index(*str, base) >= 0)
	{
		result = result * len + ft_index(*str, base);
		str++;
	}
	return (result * sign);
}
