# -*- coding: utf-8 -*-
from dados import ex

ID = "c09"
NOME = "C09"
TIPO = "C"
DIAS = "terceira semana"
RESUMO = "Bibliotecas estáticas (`ar`), o primeiro Makefile e o `ft_split` de novo."
INTRO = [
    "Uma biblioteca estática (`libft.a`) é um arquivo de ficheiros `.o`. Cria-se com `ar rc` e indexa-se com `ranlib`. Depois compila-se com `-L. -lft`.",
    "No Makefile, as linhas de comando começam por um **tab**, não por espaços. É o erro mais comum.",
]

EXS = [
    ex("ex00", "libft", "libft_creator.sh, ft_putchar.c, ft_swap.c, ft_putstr.c, ft_strlen.c, ft_strcmp.c", "write",
       ["Cria a tua biblioteca, chamada `libft.a`.",
        "Um script de shell `libft_creator.sh` compila os ficheiros e cria a biblioteca.",
        "A biblioteca tem estas funções: `ft_putchar`, `ft_swap`, `ft_putstr`, `ft_strlen` e `ft_strcmp`.",
        "A moulinette corre `sh libft_creator.sh`."],
       proto="void\tft_putchar(char c);\nvoid\tft_swap(int *a, int *b);\nvoid\tft_putstr(char *str);\nint\t\tft_strlen(char *str);\nint\t\tft_strcmp(char *s1, char *s2);",
       sol=["c09/ex00/libft_creator.sh", "c09/ex00/ft_putchar.c", "c09/ex00/ft_swap.c", "c09/ex00/ft_putstr.c",
            "c09/ex00/ft_strlen.c", "c09/ex00/ft_strcmp.c"],
       passos=["`gcc -c` compila cada `.c` para um `.o`, sem criar um executável (não há `main`).",
               "`ar rc libft.a` junta os `.o` numa biblioteca: `r` acrescenta ou substitui, `c` cria o arquivo se não existir.",
               "`ranlib` cria o índice da biblioteca, que permite ao compilador encontrar as funções.",
               "Os ficheiros são escritos pelo nome, sem `*.c`: assim nada que esteja a mais na pasta entra na biblioteca."],
       erros=["Compilar sem `-c`: o `gcc` tenta criar um programa e falha por não haver `main`.",
              "Esquecer o `ranlib` (em alguns sistemas a ligação falha sem índice).",
              "Esquecer as flags `-Wall -Wextra -Werror`."],
       limites=["A moulinette compila um `main` dela com `-L. -lft` e chama as cinco funções."],
       lang="sh"),

    ex("ex01", "Makefile", "Makefile", "Nenhuma",
       ["Cria o Makefile que compila a biblioteca `libft.a`:",
        "- mostra todos os comandos que corre e não corre comandos desnecessários;",
        "- vai buscar os `.c` à pasta `srcs` (`ft_putchar.c`, `ft_swap.c`, `ft_putstr.c`, `ft_strlen.c`, `ft_strcmp.c`) e os headers à pasta `includes` (`ft.h`);",
        "- compila com `gcc` e as flags `-Wall -Wextra -Werror`, por esta ordem;",
        "- a biblioteca fica na raiz do exercício e os `.o` ficam ao lado dos `.c`;",
        "- tem as regras `clean`, `fclean`, `re`, `all` e `libft.a`. `make` é o mesmo que `make all`, que é o mesmo que `make libft.a`;",
        "- `clean` apaga os ficheiros temporários; `fclean` faz `clean` e apaga o que o `all` criou; `re` faz `fclean` e depois `all`;",
        "- não compila nada sem necessidade. A moulinette só vai buscar o teu Makefile e testa-o com os ficheiros dela.",
        "Cuidado com os wildcards!"],
       sol=["c09/ex01/Makefile"],
       passos=["`OBJS = $(SRCS:.c=.o)` troca a extensão de cada fonte: os `.o` ficam na mesma pasta dos `.c`.",
               "A regra `$(NAME): $(OBJS)` só corre se algum `.o` for mais recente do que a biblioteca. Assim, um segundo `make` não faz nada.",
               "A regra `%.o: %.c` compila cada `.c` com `-I includes`, para encontrar o `ft.h`. Só recompila os `.c` que mudaram.",
               "`all` é a primeira regra, por isso é a que o `make` corre sem argumentos.",
               "`.PHONY` diz que `all`, `clean`, `fclean` e `re` não são ficheiros.",
               "As fontes estão escritas uma a uma: o enunciado avisa contra os wildcards (`*.c`)."],
       erros=["Usar espaços em vez de tabs antes dos comandos: `missing separator`.",
              "Usar `$(wildcard srcs/*.c)` ou `*.c`.",
              "Pôr `@` antes dos comandos: o enunciado pede que sejam mostrados.",
              "Um `re` que não volta a compilar tudo."],
       limites=["`make` duas vezes seguidas: a segunda não compila nada.",
                "Alterar um `.c` e correr `make`: só esse é recompilado."],
       pasta="ex01/", lang="make"),

    ex("ex02", "ft_split", "ft_split.c", "malloc",
       ["Cria uma função que divide uma string usando como separador cada carácter de `charset`.",
        "Devolve um array com o endereço de cada palavra entre separadores, terminado por 0. Não pode haver strings vazias. A string recebida não pode ser modificada."],
       proto="char\t**ft_split(char *str, char *charset);",
       sol=["c09/ex02/ft_split.c"],
       passos=["É o mesmo exercício do C07. Conta-se o número de palavras, reserva-se o array (+1 para o 0) e copia-se cada palavra.",
               "Uma palavra começa num carácter que não é separador e que vem depois de um separador ou no início."],
       erros=["Strings vazias entre separadores seguidos.",
              "Esquecer o 0 no fim."],
       limites=["String vazia, só separadores, `charset` vazio."]),
]
