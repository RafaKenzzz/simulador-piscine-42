# -*- coding: utf-8 -*-
"""Página «Introdução e tutorial»."""

H1 = "Como usar o simulador"
LEAD = ("Este simulador reproduz o que vais fazer na Piscine: ler o enunciado, escrever o código no teu computador, "
        "testá-lo, entregá-lo com git e ser corrigido pela moulinette e por um colega. Em dez minutos ficas a saber "
        "como tudo funciona.")

# (id, título, parágrafos, bloco de terminal opcional)
SECOES = [
    ("precisas", "O que precisas", [
        "- Um computador com terminal: macOS, Linux, ou Windows com WSL (o Linux dentro do Windows).",
        "- O compilador `gcc` (no macOS vem com as Xcode Command Line Tools; no Ubuntu, `sudo apt install gcc make`).",
        "- A `norminette`, a mesma da 42: `python3 -m pip install norminette`.",
        "- Um editor. Na 42 vais usar o `vim`; aproveita para o treinar desde já.",
        "O simulador funciona sem internet e não tem conta: abres o `index.html` e começas. O progresso fica guardado neste navegador.",
    ], None),
    ("percurso", "O percurso", [
        "Os módulos estão pela ordem da Piscine: Shell00 e Shell01, depois C00 a C13, os três rushes e, no fim, o BSQ. "
        "Na 42 os exercícios são corrigidos por ordem e um exercício difícil não conta se um mais fácil antes dele estiver errado: segue a mesma ordem aqui.",
        "Na Piscine há exame todas as sextas-feiras. Faz um exame no simulador ao fim de cada semana de módulos, mesmo que ainda não tenhas chegado aos últimos levels.",
    ], None),
    ("exercicio", "Um exercício, do início ao fim", [
        "1. **Lê o enunciado.** Em cada exercício vês a pasta de entrega, os ficheiros a entregar e as funções permitidas. Usar uma função que não está na lista vale -42 na 42.",
        "2. **Escreve o código no teu computador**, na pasta certa, com o nome certo.",
        "3. **Testa com um `main` teu**, que não entregas. Compila sempre com as flags da moulinette e usa `cat -e` para ver as quebras de linha.",
        "4. **Passa a norminette.** Se falhar, a moulinette chumba o exercício, mesmo que funcione.",
        "5. **Cola o código no campo «O teu código»** do exercício. Fica guardado e o exercício passa a «em curso». O botão «verificar norma (básico)» aponta os erros de Norma mais comuns.",
        "6. **Marca «feito»** quando estiver pronto. A barra de progresso do módulo e da página inicial atualiza.",
    ], "$> mkdir -p ~/piscine/c00/ex00 && cd ~/piscine/c00/ex00\n$> vim ft_putchar.c\n$> vim main.c\n$> gcc -Wall -Wextra -Werror main.c ft_putchar.c\n$> ./a.out | cat -e\na$\n$> norminette ft_putchar.c\nft_putchar.c: OK!"),
    ("entrega", "Entregar um módulo", [
        "No fim de cada página de módulo há a **entrega**, com um terminal. É o processo da 42, sem prazo:",
        "1. `inscrever`: inscreves-te no projeto e é criado o teu repositório.",
        "2. `git clone`, `git add .`, `git commit -m \"…\"` e `git push`: o código que colaste em cada exercício vai para o repositório. Só o que tiver push é corrigido.",
        "3. `moulinette`: corrige o último push, exercício a exercício e por ordem. Verifica se entregaste, a Norma, se há `main` só quando é pedida, os nomes das funções e as funções proibidas. Ao primeiro KO, os seguintes deixam de contar.",
        "4. `avaliacao`: abre a folha de avaliação, como numa correção entre colegas. Corre cada teste no teu terminal e marca os que passam. Ao fechar, tens a nota da avaliação.",
        "Podes corrigir e voltar a entregar quantas vezes quiseres. Os botões por baixo do terminal fazem o mesmo que os comandos.",
    ], "piscine@42lisboa:~/c00$ inscrever\nInscrito em C00. Repositório criado.\npiscine@42lisboa:~/c00$ git add .\npiscine@42lisboa:~/c00$ git commit -m \"c00\"\n[master 3f2a9c1] c00\npiscine@42lisboa:~/c00$ git push\npiscine@42lisboa:~/c00$ moulinette\nOK  ex00  ft_putchar\nKO  ex01  ft_print_alphabet\n      funções que não estão nas permitidas: printf\nnota da moulinette: 11/100"),
    ("exame", "Fazer um exame", [
        "Na página **exames** escolhes o exame e o teu login e entras no examshell. Não há tempo limite: o relógio só mostra quanto tempo levas.",
        "1. Recebes um exercício sorteado do level 0. O enunciado aparece por cima e o ficheiro a entregar é `~/rendu/<exercício>/<ficheiro>`.",
        "2. Escreve e testa o código no teu terminal; depois cola-o no campo do simulador.",
        "3. Entrega com `git add .`, `git commit -m \"…\"` e `git push`.",
        "4. `grademe`: primeiro as verificações automáticas; depois aparecem os testes que o examshell faria. Corre-os e diz se passam.",
        "5. **SUCCESS** sobe de level; **FAILURE** dá outro exercício do mesmo level, como na 42.",
        "Durante o exame não há dicas, atalhos nem ligações para as respostas. Escreve `finish` (ou carrega em «terminar exame») para acabar.",
    ], "piscine@examshell:~/rendu$ git add .\npiscine@examshell:~/rendu$ git commit -m \"aff_a\"\npiscine@examshell:~/rendu$ git push\npiscine@examshell:~/rendu$ grademe\n=> a corrigir aff_a…\n   verificações automáticas: OK\n>>>>>>>>>> SUCCESS <<<<<<<<<<"),
    ("norma-respostas", "Norminette e respostas", [
        "A página **norminette** resume as regras da Norma que mais apanham candidatos, cada uma com um exemplo errado e outro certo.",
        "As **respostas** estão numa área à parte, sem ligações a partir dos exercícios. Cada solução está fechada até carregares em «mostrar solução» e traz o passo a passo, os erros comuns e os casos limite. "
        "Só lá chegas pela página inicial, por este tutorial ou escrevendo `cd respostas` na linha de comandos, que te pede confirmação. Tenta primeiro sozinho.",
    ], None),
    ("teclado", "Teclado e linha de comandos", [
        "Carrega em `/` em qualquer página para abrir a linha de comandos: `cd c03`, `open c03/ex02`, `progresso`, `ls`, `help`.",
        "- `1` a `5`: início, tutorial, módulos, exames e norminette.",
        "- `j` e `k`: exercício seguinte e anterior; `n` e `p`: módulo seguinte e anterior.",
        "- `e`: escrever no exercício atual (`Esc` para sair); `f`: marcar como feito.",
        "- `?`: lista de atalhos.",
    ], None),
    ("progresso", "Onde fica o teu progresso", [
        "Tudo (o estado dos exercícios, o código, as entregas e os exames) fica guardado no armazenamento local **deste navegador**. Não vai para nenhum servidor.",
        "Se abrires o simulador noutro navegador, ou numa janela privada, começas do zero. Para apagar tudo, escreve `reset-progresso` na linha de comandos.",
    ], None),
    ("limites", "O que o simulador não faz", [
        "O simulador não compila nem executa C dentro do navegador. A moulinette daqui verifica a entrega, a Norma (as regras principais), os nomes das funções e as funções proibidas. "
        "O comportamento do código confirmas tu, a correr os testes da folha de avaliação no teu terminal, como faz um colega na 42.",
        "Os enunciados são resumos em português dos originais públicos. Na Piscine, a referência é sempre o enunciado oficial do dia.",
    ], None),
]
