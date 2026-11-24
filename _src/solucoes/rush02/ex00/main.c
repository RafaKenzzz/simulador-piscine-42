#include "rush02.h"

/*
** Só algarismos, pelo menos um. Devolve o número sem zeros à esquerda
** (mas "0" fica "0"), ou NULL se não for um inteiro positivo válido.
*/
static char	*ft_check_number(char *s)
{
	int	i;

	i = 0;
	while (s[i] >= '0' && s[i] <= '9')
		i++;
	if (i == 0 || s[i] != '\0')
		return (NULL);
	while (s[0] == '0' && s[1] != '\0')
		s++;
	return (s);
}

/*
** Dois passos: primeiro verifica se o dicionário tem todas as palavras
** necessárias (sem escrever nada); só depois escreve. Assim um "Dict
** Error" nunca aparece a meio de uma frase.
*/
static int	ft_run(char *path, char *nbr)
{
	t_dict	dict;
	char	*content;
	int		ok;

	content = ft_read_file(path);
	if (!content)
		return (0);
	ok = ft_parse_dict(content, &dict);
	free(content);
	dict.ok = 1;
	dict.print = 0;
	if (ok)
		ft_convert(nbr, &dict);
	if (ok && dict.ok)
	{
		dict.print = 1;
		ft_convert(nbr, &dict);
		ft_putstr("\n");
	}
	ft_free_dict(&dict);
	return (ok && dict.ok);
}

int	main(int argc, char **argv)
{
	char	*nbr;
	char	*path;

	if (argc != 2 && argc != 3)
	{
		ft_putstr("Error\n");
		return (1);
	}
	path = "numbers.dict";
	if (argc == 3)
		path = argv[1];
	nbr = ft_check_number(argv[argc - 1]);
	if (!nbr)
	{
		ft_putstr("Error\n");
		return (1);
	}
	if (!ft_run(path, nbr))
	{
		ft_putstr("Dict Error\n");
		return (1);
	}
	return (0);
}
