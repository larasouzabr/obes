# :checkered_flag: OBES - Sebo Online

Para pessoas que buscam adquirir livros por preços mais acessíveis e contribuir para a preservação do meio ambiente, que encontram dificuldades em ter acesso a livros novos devido aos preços elevados.
O OBES é uma plataforma online de vendas e doação de livros usados que oferece preços mais acessíveis e uma grande variedade de títulos em comparação às lojas físicas tradicionais.
Nosso produto contribui para a formação de uma sociedade mais instruída e crítica, além de colaborar para a preservação do meio ambiente por meio da reutilização de recursos.

## :technologist: Membros da equipe

508159 – Lara Gabrielly Souza Batista Lima - Engenharia de Software
508653 – Victor Anthony Pereira Alves - Engenharia de Software
509278 – Vinícius Lemos Araújo - Engenharia de Software
516098 – Antonio Herik Cosmo Martins - Engenharia de Software

## :people_holding_hands: Papéis ou tipos de usuário da aplicação

### Resumo dos Envolvidos

| Nome                                       |                                                            Descrição                                                            |                                                                                            Responsabilidades                                                                                            |
| ------------------------------------------ | :-----------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| E01- Leitores                              |       Leitores ávidos procuram comprar livros usados ou raros, além de doar livros que não são mais utilizados por eles.        |                                                    - Assegurar que o sistema tem utilidade e poderá ser mantido;- Utilizar o sistema com frequência.                                                    |
| E02- Estudantes                            |                          Estudantes que buscam encontrar livros didáticos usados a preços acessíveis.                           |                                                              Garantir que a proposta do sistema esteja sendo cumprida a fins educacionais;                                                              |
| E03- Instituições de ensino                | Instituições de ensino que buscam popular suas devidas bibliotecas e fornecer uma acessibilidade cultural para seus estudantes. | - Assegurar que o sistema tem utilidade e poderá ser mantido;- Utilizar o sistema quando necessário. - Garantir que o sistema tem caráter de extensão. - Aprova financeiramente (instituições privadas) |
| E04- Bibliotecas                           |                              Bibliotecas que procuram novos livros para popular suas prateleiras.                               |                          -Assegurar que o sistema tem utilidade e poderá ser mantido;- Utilizar o sistema quando necessário. - Garantir que o sistema tem caráter de extensão,                          |
| E05- Grupos de estudos e clubes de leitura |       Determinados grupos procuram acessar livros por um valor abaixo da média e encontrar estoques de livros para doar.        |                       - Utilizar o sistema como um promotor da acessibilidade cultural; - Promover uma cultura de democratização da leitura utilizando o sistema como meio/modo.                        |
| E06- ONG’s                                 |                 Organizações sem fins lucrativos que buscam arrecadar fundos através da venda de livros usados.                 |                        -Utilizar o sistema como um promotor da acessibilidade cultural; -Promover uma cultura de democratização da leitura utilizando o sistema como meio/modo.                         |

### Resumo dos Usuários

| Nome                       | Descrição                                                                                                                                                                                                                                         | Responsabilidades                                                                                               | Envolvido     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------- |
| UC - Usuário Comum         | Leitores ávidos que procurem comprar livros usados ou raros, além de doar livros que não são mais utilizados por eles. Pessoas que desejam doar livros usados para que outros possam desfrutar deles.                                             | - Vender livros usados.- Doar livros usados.- Comprar livros usados por preços acessíveis.- Avaliar vendedores. | E01, E02      |
| UI - Usuário Institucional | Instituições de ensino que buscam popular suas devidas bibliotecas e seus acervos para fornecer uma acessibilidade cultural para seus estudantes. Organizações sem fins lucrativos que buscam arrecadar fundos através da venda de livros usados. | - Utilizar o sistema para encontrar livros para doação.- Filtrar livros e vendedores.- Avaliar vendedores.      | E03, E04, E06 |

## :spiral_calendar: Entidades ou tabelas do sistema

1. **Livros**: representa os livros disponíveis para venda/doação no sebo online. Os atributos podem incluir título, autor, editora, ano de publicação, condição (novo, usado), preço, descrição e imagem do livro.
2. **Usuários**: a entidade que representa os usuários do sistema, incluindo usuário comum e usuário institucional. Os atributos podem incluir nome, endereço, telefone, e-mail e senha.
3. **Doação/venda**: a entidade que representa as doações/vendas feitas pelos usuários. Os atributos podem incluir informações do cliente e informações do livro.
4. **Avaliações**: a entidade que representa as avaliações feitas pelos clientes sobre os livros e usuários. Os atributos podem incluir número da avaliação, data, informações do cliente, nome do livro ou usuário avaliado, nota (em uma escala de 1 a 5) e comentário.

## :triangular_flag_on_post: Principais funcionalidades da aplicação

- **Receber livros disponíveis para doação**: assim como todos os sistemas e-commerce, será implementada no Obes uma plataforma de envios para que os usuários registrados acompanhem os pedidos.
- **Colocar livros usados à venda**: os usuários registrados a qualquer momento poderão cadastrar livros usados por meio da página de cadastro que ficará disponível no menu.
- **Cadastrar livro para doação**: os usuários registrados a qualquer momento poderão cadastrar livros usados por meio da página de cadastro que ficará disponível no menu.
- **Visualizar livros usados que estão sendo vendidos e doados**: o sistema será dividido em duas categorias, a primeira é o Sebo no qual constará os livros à venda, essa página ficará disponível tanto para o UC (Usuário Comum) quanto para o UI (Usuário Institucional). Já a categoria de doação estará visível apenas para o UI, o UC não poderá receber livros doados e a página de doação para ele constará apenas aqueles materiais que ele cadastrou para doação.

## :desktop_computer: Tecnologias e frameworks utilizados

**Frontend:**

VUE,vue-router, vue-star-rating, vue3-carousel, axios, jwt-decode

**Backend:**

Lista as tecnologias, frameworks e bibliotecas utilizados.

## :shipit: Operações implementadas para cada entidade da aplicação

| Entidade     | Criação | Leitura | Atualização | Remoção |
| ------------ | ------- | ------- | ----------- | ------- |
| Livros       | X       | X       | X           | X       |
| Usuários     | X       | X       | X           |         |
| Doação/venda | X       | X       | X           | X       |
| Avaliações   |         |         |             |         |

## :neckbeard: Rotas da API REST utilizadas

| Método HTTP | URL                           |
| ----------- | ----------------------------- |
| POST        | /api/login                    |
| GET         | /api/addresses                |
| PUT         | /api/address/{adressID}       |
| DELETE      | /api/address/{adressID}       |
| GET         | /api/books                    |
| POST        | /api/books                    |
| GET         | /api/{userId}/books           |
| GET         | /api/books/{bookID}           |
| PUT         | /api/books/{bookID}           |
| DELETE      | /api/books/{bookID}           |
| GET         | /api/categories               |
| GET         | /api/categories/{bookId}      |
| GET         | /api/user                     |
| POST        | /api/user                     |
| PUT         | /api/user                     |
| DELETE      | /api/user                     |
| GET         | /api/user/{userId}            |
| GET         | /api/donation-orders          |
| GET         | /api/donation-orders/{bookId} |
