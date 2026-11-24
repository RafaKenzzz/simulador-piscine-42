# -*- coding: utf-8 -*-
from dados import ex

ID = "c12"
NOME = "C12"
TIPO = "C"
DIAS = "quarta semana"
RESUMO = "Listas ligadas: criar, percorrer, inverter, ordenar e juntar listas de `t_list`."
INTRO = [
    "Todos os exercícios usam esta estrutura, num ficheiro `ft_list.h` que entregas com cada exercício (exceto no ex08, onde a moulinette usa o dela):",
    "`typedef struct s_list { struct s_list *next; void *data; } t_list;`",
    "A partir do ex01, a moulinette usa o `ft_create_elem` dela: põe o protótipo no `ft_list.h`. Quando uma função usa `NULL` sem incluir `<stdlib.h>`, inclui `<stddef.h>`, para não depender do header de quem compila.",
    "Vários protótipos usam `int (*cmp)()`. Em C anterior a C23 (o da moulinette), `()` quer dizer «argumentos não especificados». Num `gcc` 15 ou mais recente, compila com `-std=gnu17` para testar.",
]

N = "Nenhuma"
L = "ft_list.h"


def lst(num, nome, funcoes, texto, proto, passos, erros, limites, header=True, ficheiro=None):
    f = ficheiro or f"{nome}.c"
    sol = [f"c12/{num}/{f}"] + ([f"c12/{num}/ft_list.h"] if num == "ex00" else [])
    return ex(num, nome, f"{f}, {L}" if header else f, funcoes, texto, proto=proto, sol=sol,
              passos=passos, erros=erros, limites=limites)


EXS = [
    lst("ex00", "ft_create_elem", "malloc",
        ["Cria a função `ft_create_elem`, que cria um elemento novo do tipo `t_list`.",
         "`data` fica com o argumento recebido e `next` com `NULL`."],
        "t_list\t*ft_create_elem(void *data);",
        ["Reserva-se `sizeof(t_list)` com `malloc` e testa-se o resultado.",
         "`elem->data = data` e `elem->next = NULL`: um elemento sozinho é uma lista de um elemento.",
         "O `ft_list.h` tem a estrutura, a proteção contra inclusão dupla e o protótipo de `ft_create_elem`."],
        ["Reservar `sizeof(t_list *)` (o tamanho de um ponteiro) em vez de `sizeof(t_list)`.",
         "Copiar o conteúdo de `data` em vez de guardar o ponteiro."],
        ["`data` pode ser qualquer ponteiro, incluindo `NULL`."]),

    lst("ex01", "ft_list_push_front", "ft_create_elem",
        ["Cria a função `ft_list_push_front`, que acrescenta um elemento novo no início da lista, com `data` igual ao argumento.",
         "Se for preciso, atualiza o ponteiro para o início da lista."],
        "void\tft_list_push_front(t_list **begin_list, void *data);",
        ["`begin_list` é o endereço do ponteiro de início. Por isso a função consegue mudar o início da lista de quem a chama.",
         "O elemento novo aponta para o antigo primeiro (`elem->next = *begin_list`) e passa a ser o início (`*begin_list = elem`)."],
        ["Fazer `begin_list = &elem`: muda só a variável local."],
        ["Lista vazia: o elemento novo passa a ser o único."]),

    lst("ex02", "ft_list_size", N,
        ["Cria a função `ft_list_size`, que devolve o número de elementos da lista."],
        "int\tft_list_size(t_list *begin_list);",
        ["Segue-se `next` até chegar a `NULL`, contando os elementos."],
        ["Começar a contar em 1, o que dá 1 para a lista vazia."],
        ["Lista vazia (`NULL`) dá 0."]),

    lst("ex03", "ft_list_last", N,
        ["Cria a função `ft_list_last`, que devolve o último elemento da lista."],
        "t_list\t*ft_list_last(t_list *begin_list);",
        ["O último é o único com `next == NULL`.",
         "Uma lista vazia não tem último: devolve-se `NULL` antes de tentar ler `begin_list->next`."],
        ["Não testar a lista vazia: ler `NULL->next` rebenta o programa."],
        ["Lista com um elemento: devolve esse elemento."]),

    lst("ex04", "ft_list_push_back", "ft_create_elem",
        ["Cria a função `ft_list_push_back`, que acrescenta um elemento novo no fim da lista, com `data` igual ao argumento.",
         "Se for preciso, atualiza o ponteiro para o início da lista."],
        "void\tft_list_push_back(t_list **begin_list, void *data);",
        ["Se a lista estiver vazia, o elemento novo passa a ser o início.",
         "Senão, vai-se até ao último e liga-se o novo a seguir a ele."],
        ["Esquecer a lista vazia: é o caso em que «se for preciso, atualiza o início»."],
        ["Lista vazia e lista com vários elementos."]),

    lst("ex05", "ft_list_push_strs", "ft_create_elem",
        ["Cria a função `ft_list_push_strs`, que cria uma lista nova com todas as strings de `strs`.",
         "`size` é o tamanho de `strs`. O primeiro elemento de `strs` fica no **fim** da lista.",
         "Devolve o endereço do primeiro elemento da lista."],
        "t_list\t*ft_list_push_strs(int size, char **strs);",
        ["Se cada string for posta à frente da lista, pela ordem de `strs`, a primeira acaba no fim e a última no início, como pede o enunciado.",
         "O elemento guarda o ponteiro para a string, sem a copiar."],
        ["Pôr as strings pela ordem de `strs` (a primeira no início)."],
        ["`size` 0 devolve `NULL`."]),

    lst("ex06", "ft_list_clear", "free",
        ["Cria a função `ft_list_clear`, que retira e liberta todos os elementos da lista.",
         "`free_fct` é usada para libertar os dados de cada elemento."],
        "void\tft_list_clear(t_list *begin_list, void (*free_fct)(void *));",
        ["Para cada elemento: guarda-se o `next`, liberta-se o `data` com `free_fct`, liberta-se o elemento com `free` e passa-se ao `next` guardado.",
         "O `next` tem de ser guardado antes do `free`: depois, ler o elemento é usar memória já libertada."],
        ["Ler `begin_list->next` depois do `free(begin_list)`.",
         "Esquecer de chamar `free_fct` para os dados."],
        ["Lista vazia não faz nada."]),

    lst("ex07", "ft_list_at", N,
        ["Cria a função `ft_list_at`, que devolve o elemento na posição `nbr` (o primeiro é a posição 0).",
         "Em caso de erro, devolve um ponteiro nulo."],
        "t_list\t*ft_list_at(t_list *begin_list, unsigned int nbr);",
        ["Avança-se `nbr` vezes. Se a lista acabar antes, devolve-se `NULL`."],
        ["Avançar uma vez a mais (contar a partir de 1).",
         "Não parar quando a lista acaba."],
        ["`nbr` igual ou maior do que o tamanho dá `NULL`."]),

    lst("ex08", "ft_list_reverse", N,
        ["Cria a função `ft_list_reverse`, que inverte a ordem dos elementos de uma lista. Os dados de cada elemento ficam iguais.",
         "Atenção: aqui a moulinette usa o `ft_list.h` dela."],
        "void\tft_list_reverse(t_list **begin_list);",
        ["Percorre-se a lista com três ponteiros: o anterior, o atual e o seguinte.",
         "Em cada passo, o `next` do atual passa a apontar para o anterior.",
         "No fim, o anterior é o antigo último, que passa a ser o início."],
        ["Trocar os dados em vez das ligações: o enunciado diz que os dados de cada elemento ficam iguais.",
         "Perder o resto da lista por não guardar o `next` antes de o mudar."],
        ["Lista vazia, com um elemento e com vários."],
        header=False),

    lst("ex09", "ft_list_foreach", N,
        ["Cria a função `ft_list_foreach`, que aplica a função `f` a todos os elementos da lista, pela ordem da lista.",
         "A função é usada assim: `(*f)(list_ptr->data);`"],
        "void\tft_list_foreach(t_list *begin_list, void (*f)(void *));",
        ["Percorre-se a lista e chama-se `f` com o `data` de cada elemento."],
        ["Passar o elemento a `f` em vez do `data`."],
        ["Lista vazia não chama `f`."]),

    lst("ex10", "ft_list_foreach_if", N,
        ["Cria a função `ft_list_foreach_if`, que aplica a função `f` a alguns elementos da lista.",
         "Só é aplicada aos elementos em que `cmp`, comparando os dados com `data_ref`, devolve 0. É aplicada pela ordem da lista.",
         "As funções são usadas assim: `(*f)(list_ptr->data);` e `(*cmp)(list_ptr->data, data_ref);`"],
        "void\tft_list_foreach_if(t_list *begin_list, void (*f)(void *),\n\t\tvoid *data_ref, int (*cmp)());",
        ["Para cada elemento, chama-se `cmp(data, data_ref)`; se der 0, chama-se `f(data)`.",
         "A ordem dos argumentos de `cmp` é a do enunciado: primeiro os dados do elemento, depois a referência.",
         "O protótipo passa das 80 colunas, por isso parte-se a seguir a uma vírgula."],
        ["Trocar a ordem dos argumentos de `cmp`.",
         "Aplicar `f` quando `cmp` é diferente de 0."],
        ["Nenhum elemento igual: `f` nunca é chamada."]),

    lst("ex11", "ft_list_find", N,
        ["Cria a função `ft_list_find`, que devolve o endereço do primeiro elemento cujos dados, comparados com `data_ref` por `cmp`, fazem `cmp` devolver 0.",
         "A função é usada assim: `(*cmp)(list_ptr->data, data_ref);`"],
        "t_list\t*ft_list_find(t_list *begin_list, void *data_ref, int (*cmp)());",
        ["Percorre-se a lista e devolve-se o primeiro elemento em que `cmp` dá 0.",
         "Se nenhum der, devolve-se `NULL`."],
        ["Devolver os dados em vez do elemento: o protótipo devolve `t_list *`."],
        ["Vários elementos iguais: devolve o primeiro."]),

    lst("ex12", "ft_list_remove_if", "free",
        ["Cria a função `ft_list_remove_if`, que retira da lista todos os elementos cujos dados, comparados com `data_ref` por `cmp`, fazem `cmp` devolver 0.",
         "Os dados de um elemento retirado são libertados com `free_fct`.",
         "As funções são usadas assim: `(*cmp)(list_ptr->data, data_ref);` e `(*free_fct)(list_ptr->data);`"],
        "void\tft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)(),\n\t\tvoid (*free_fct)(void *));",
        ["`prev` guarda o último elemento que fica na lista.",
         "Quando um elemento sai, quem apontava para ele (o `prev`, ou o início da lista se for o primeiro) passa a apontar para o seguinte.",
         "Depois liberta-se os dados com `free_fct` e o elemento com `free`.",
         "O `next` é guardado antes, porque depois do `free` já não se pode ler."],
        ["Esquecer o caso em que o primeiro elemento (ou vários seguidos no início) sai.",
         "Avançar o `prev` para um elemento que acabou de ser apagado."],
        ["Todos os elementos iguais: a lista fica vazia (`*begin_list == NULL`).",
         "Elementos iguais seguidos."]),

    lst("ex13", "ft_list_merge", N,
        ["Cria a função `ft_list_merge`, que põe os elementos da lista `begin_list2` no fim da lista `begin_list1`.",
         "Não é permitido criar elementos."],
        "void\tft_list_merge(t_list **begin_list1, t_list *begin_list2);",
        ["Liga-se o último elemento da primeira lista ao início da segunda.",
         "Se a primeira estiver vazia, o início dela passa a ser a segunda."],
        ["Criar elementos novos (copiar a segunda lista)."],
        ["Primeira lista vazia; segunda lista vazia."]),

    lst("ex14", "ft_list_sort", N,
        ["Cria a função `ft_list_sort`, que ordena os elementos da lista por ordem crescente, comparando os dados com uma função.",
         "A função é usada assim: `(*cmp)(list_ptr->data, list_other_ptr->data);` (por exemplo, `cmp` pode ser o `ft_strcmp`)."],
        "void\tft_list_sort(t_list **begin_list, int (*cmp)());",
        ["Ordenação por bolha: se `cmp(atual, seguinte) > 0`, trocam-se os dados dos dois elementos e recomeça-se do início.",
         "Trocar os dados é mais simples do que mexer nas ligações e dá o mesmo resultado à vista de quem percorre a lista."],
        ["Comparar elementos não vizinhos e esquecer-se de recomeçar.",
         "Tratar a lista vazia sem cuidado (`cur->next` com `cur == NULL`)."],
        ["Lista vazia, com um elemento, com repetidos."]),

    lst("ex15", "ft_list_reverse_fun", N,
        ["Cria a função `ft_list_reverse_fun`, que inverte a ordem dos elementos da lista."],
        "void\tft_list_reverse_fun(t_list *begin_list);",
        ["Ao contrário do ex08, aqui só se recebe o primeiro elemento: o início da lista não pode mudar.",
         "Por isso trocam-se os dados: o primeiro com o último, o segundo com o penúltimo, e assim até ao meio.",
         "`ft_at` encontra o elemento numa posição, como o `ft_list_at`."],
        ["Inverter as ligações: o chamador continua a apontar para o antigo primeiro, que passa a ser o último."],
        ["Listas com número par e ímpar de elementos; lista vazia."]),

    lst("ex16", "ft_sorted_list_insert", "ft_create_elem",
        ["Cria a função `ft_sorted_list_insert`, que cria um elemento novo e o insere numa lista ordenada, de forma a que continue ordenada por ordem crescente.",
         "A função é usada assim: `(*cmp)(list_ptr->data, list_other_ptr->data);`"],
        "void\tft_sorted_list_insert(t_list **begin_list, void *data, int (*cmp)());",
        ["Se a lista estiver vazia ou o dado novo for menor do que o primeiro, o elemento novo passa a ser o início.",
         "Senão, avança-se enquanto o seguinte for menor ou igual ao dado novo, e insere-se a seguir."],
        ["Esquecer a inserção no início.",
         "Usar `ft_list_sort` depois de um `push_back`: funciona mas não é o que se pede."],
        ["Inserir no início, no meio, no fim e valores repetidos."]),

    lst("ex17", "ft_sorted_list_merge", N,
        ["Cria a função `ft_sorted_list_merge`, que integra os elementos da lista ordenada `begin_list2` na lista ordenada `begin_list1`, de forma a que `begin_list1` continue ordenada por ordem crescente.",
         "A função é usada assim: `(*cmp)(list_ptr->data, list_other_ptr->data);`"],
        "void\tft_sorted_list_merge(t_list **begin_list1, t_list *begin_list2,\n\t\tint (*cmp)());",
        ["Cada elemento da segunda lista é retirado (guardando o seguinte) e inserido no sítio certo da primeira, como no ex16, mas sem criar elementos: reutiliza-se o próprio elemento."],
        ["Criar elementos novos (não há `ft_create_elem` nas funções permitidas).",
         "Perder o resto da segunda lista ao mudar o `next` do elemento antes de guardar o seguinte."],
        ["Primeira lista vazia; elementos da segunda menores do que todos os da primeira."]),
]
