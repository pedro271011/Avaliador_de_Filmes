Este programa é uma aplicação simples feita em Python usando a biblioteca Tkinter, que permite o cadastro de usuários e filmes, além da possibilidade de avaliar filmes com notas de 1 a 5.
Este programa foi criado com o objetivo de estudar conceitos da programação orientadas a objetos.
Este repositórios possui "dois contribuidores" mas as duas contas pertencem a mim. Acabaram ficando duas contas devido a minha falta de familiaridade com o github.

Bibliotecas Requeridas:

tkinter para a interface gráfica.
json para a manipulação de dados.
requests para buscar pôsteres de filmes na API do The Movie Database (TMDb).
PIL (Python Imaging Library) para manipulação e exibição de imagens (posters de filmes).

Essas bibliotecas precisam ser instaladas para que o programa funcione.


Instruções de Uso:

Execução Inicial:
O programa deve ser executado a partir do termial com o comando python3 main.py
Ao rodar o programa, será aberta uma janela de login.
Se você já possui um usuário, insira o nome na caixa de texto e clique em "Entrar"(Os usuarios Fulano e Ciclano ja estão cadastrados). Caso contrário, clique em "Criar nova conta" para se registrar.

Pesquisando Filmes:
Digite o nome do filme na caixa de pesquisa e pressione Enter. Se o filme não for encontrado, você será informado de que o filme não existe e será dado a opção de cadastrá-lo.
Se o filme for encontrado, a janela do filme sera aberta.

Avaliação de Filmes:
Para avaliar um filme, clique no botão "Avaliar" após buscar o filme na lista. Será possível atribuir uma nota de 1 a 5.
A média de notas será recalculada automaticamente e quando a janela do filem for aberta novamente a nota ja estara atualizada.

Cadastro de Filmes:
Após o login, será aberta uma nova janela com uma caixa de pesquisa.
Caso você queira cadastrar um filme, basta clicar em "Cadastrar", onde será solicitada a entrada de informações do filme (nome, ano e nota).

Sair do Programa:
Para sair do sistema, basta digitar "sair" na barra de pesquisa e o programa será encerrado.


Comentario:

Eu pretendia adicionar mais funcionalidades ao programa, como:
- Um sistema de login mais completo, com senha e foto de usuários;
- Uma lista de filmes assistidos para cada usuário;
- E, principalmente, uma área de debate para cada filme.

Entretanto, subestimei a complexidade que seria implementar essas coisas e não consegui adicionar essas funcionalidades a tempo. 
Digo isso porque, no código, podem ser encontradas algumas partes que parecem ser inúteis, mas que na verdade são o embrião dessas funcionalidades.
