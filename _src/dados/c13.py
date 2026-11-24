# -*- coding: utf-8 -*-
from dados import ex

ID = "c13"
NOME = "C13"
TIPO = "C"
DIAS = "quarta semana"
RESUMO = "Árvores binárias: criar nós, os três percursos, inserir, procurar, medir e percorrer por níveis."
INTRO = [
    "Todos os exercícios usam esta estrutura, num ficheiro `ft_btree.h` entregue com cada exercício:",
    "`typedef struct s_btree { struct s_btree *left; struct s_btree *right; void *item; } t_btree;`",
    "Quase tudo se resolve com recursão: tratar o nó e chamar a mesma função para a esquerda e para a direita. Uma árvore vazia (`NULL`) é sempre o caso de paragem.",
]

N = "Nenhuma"


def bt(num, nome, funcoes, texto, proto, passos, erros, limites):
    sol = [f"c13/{num}/{nome}.c"] + (["c13/ex00/ft_btree.h"] if num == "ex00" else [])
    return ex(num, nome, f"{nome}.c, ft_btree.h", funcoes, texto, proto=proto, sol=sol,
              passos=passos, erros=erros, limites=limites)


EXS = [
    bt("ex00", "btree_create_node", "malloc",
       ["Cria a função `btree_create_node`, que reserva um nó novo. O `item` fica com o valor do argumento e todos os outros campos a 0.",
        "Devolve o endereço do nó criado."],
       "t_btree\t*btree_create_node(void *item);",
       ["Reserva-se `sizeof(t_btree)`, guarda-se o `item` e põem-se os dois filhos a `NULL`."],
       ["Esquecer de pôr os filhos a `NULL`: o `malloc` não limpa a memória."],
       ["O `ft_btree.h` tem a estrutura e o protótipo desta função, que os exercícios seguintes usam."]),

    bt("ex01", "btree_apply_prefix", N,
       ["Cria uma função `btree_apply_prefix` que aplica a função recebida ao `item` de cada nó, percorrendo a árvore em prefixo."],
       "void\tbtree_apply_prefix(t_btree *root, void (*applyf)(void *));",
       ["Prefixo: primeiro o nó, depois toda a subárvore esquerda, depois toda a direita.",
        "Na árvore `d(b(a, c), f(e, g))` dá `d b a c f e g`."],
       ["Esquecer o caso `root == NULL`."],
       ["Árvore vazia não chama `applyf`."]),

    bt("ex02", "btree_apply_infix", N,
       ["Cria uma função `btree_apply_infix` que aplica a função recebida ao `item` de cada nó, percorrendo a árvore em infixo."],
       "void\tbtree_apply_infix(t_btree *root, void (*applyf)(void *));",
       ["Infixo: esquerda, nó, direita.",
        "Numa árvore de pesquisa (menores à esquerda), dá os itens por ordem crescente: `a b c d e f g`."],
       ["Trocar a ordem das chamadas."],
       ["Árvore só com filhos à esquerda ou só à direita."]),

    bt("ex03", "btree_apply_suffix", N,
       ["Cria uma função `btree_apply_suffix` que aplica a função recebida ao `item` de cada nó, percorrendo a árvore em sufixo."],
       "void\tbtree_apply_suffix(t_btree *root, void (*applyf)(void *));",
       ["Sufixo: esquerda, direita e só no fim o nó. A raiz é a última: `a c b e g f d`."],
       ["Confundir sufixo com infixo invertido."],
       ["Árvore com um só nó."]),

    bt("ex04", "btree_insert_data", "btree_create_node",
       ["Cria uma função `btree_insert_data` que insere o elemento `item` numa árvore.",
        "A árvore está ordenada: em cada nó, os elementos menores ficam à esquerda e os maiores ou iguais à direita. Recebe também uma função de comparação parecida com o `strcmp`.",
        "`root` aponta para o nó raiz. Na primeira chamada, aponta para `NULL`."],
       "void\tbtree_insert_data(t_btree **root, void *item,\n\t\tint (*cmpf)(void *, void *));",
       ["Se `*root` for `NULL`, é ali que o nó novo fica: `*root = btree_create_node(item)`.",
        "Senão, compara-se `item` com o do nó: menor vai para a esquerda, maior ou igual vai para a direita.",
        "A recursão recebe `&(*root)->left`: o endereço do ponteiro do filho, para o poder alterar."],
       ["Pôr os iguais à esquerda: o enunciado diz que vão para a direita.",
        "Passar `(*root)->left` em vez do endereço: a árvore nunca muda."],
       ["Primeira inserção numa árvore vazia; valores repetidos."]),

    bt("ex05", "btree_search_item", N,
       ["Cria uma função `btree_search_item` que devolve o primeiro elemento igual à referência recebida.",
        "A árvore é percorrida em infixo. Se o elemento não existir, devolve `NULL`."],
       "void\t*btree_search_item(t_btree *root, void *data_ref,\n\t\tint (*cmpf)(void *, void *));",
       ["Infixo: procura-se primeiro na esquerda; se encontrar, devolve-se logo.",
        "Depois testa-se o próprio nó e, por fim, a direita.",
        "Assim, com repetidos, devolve-se o primeiro na ordem infixa."],
       ["Procurar só num lado, como numa árvore de pesquisa: o enunciado pede o percurso infixo completo.",
        "Devolver o nó em vez do item."],
       ["Elemento inexistente e árvore vazia dão `NULL`."]),

    bt("ex06", "btree_level_count", N,
       ["Cria uma função `btree_level_count` que devolve o tamanho do maior ramo da árvore recebida."],
       "int\tbtree_level_count(t_btree *root);",
       ["Uma árvore vazia tem 0 níveis.",
        "Senão, tem 1 (o próprio nó) mais o maior dos dois lados."],
       ["Contar as ligações em vez dos nós (dá menos 1)."],
       ["Árvore com um nó dá 1; árvore em linha (todos à direita) dá o número de nós."]),

    bt("ex07", "btree_apply_by_level", "malloc, free",
       ["Cria uma função `btree_apply_by_level` que aplica a função recebida a cada nó da árvore, percorrendo-a nível a nível.",
        "A função chamada recebe três argumentos:",
        "- o `item` do nó (`void *`);",
        "- o nível em que o nó está: 0 para a raiz, 1 para os filhos, 2 para os netos, e assim por diante (`int`);",
        "- 1 se for o primeiro nó do nível, 0 nos outros casos (`int`)."],
       "void\tbtree_apply_by_level(t_btree *root, void (*applyf)(void *item,\n\t\tint current_level, int is_first_elem));",
       ["É um percurso em largura, com uma fila: um array com espaço para todos os nós da árvore (contados com `ft_size`).",
        "A raiz entra na fila. Em cada volta trata-se um nível inteiro: os nós que estão na fila nesse momento.",
        "Cada nó tratado é passado a `applyf` e os filhos entram no fim da fila. São o nível seguinte.",
        "O primeiro nó de cada nível leva `is_first_elem = 1`.",
        "Para não passar das 4 variáveis por parâmetro e das 5 por função, a cabeça e o fim da fila ficam num array `ht[2]`."],
       ["Usar recursão em profundidade: a ordem sai errada.",
        "Marcar como primeiro só o da raiz."],
       ["Árvore vazia não chama nada; árvore em linha tem um nó por nível, todos primeiros."]),
]
