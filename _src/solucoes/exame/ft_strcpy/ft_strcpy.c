/*
** Copia s2 para s1 (atenção à ordem dos parâmetros neste enunciado),
** com o '\0', e devolve s1.
*/
char	*ft_strcpy(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s2[i])
	{
		s1[i] = s2[i];
		i++;
	}
	s1[i] = '\0';
	return (s1);
}
