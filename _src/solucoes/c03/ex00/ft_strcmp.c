/*
** Avança enquanto os caracteres são iguais e a primeira string não acabou.
** Devolve a diferença entre os primeiros caracteres diferentes, lidos como
** unsigned char, tal como o strcmp: negativo, zero ou positivo.
*/
int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] && s1[i] == s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}
