API de Livros
Essa é uma API desenvolvida em Flask para cadastrar, buscar e deletar livros em um banco de dados SQLite.

Endpoints
A API conta com os seguintes endpoints:

Swagger
bash
Copy code
GET /swagger
Esse endpoint retorna a documentação da API no formato Swagger.

Cadastrar Livro
bash
Copy code
POST /v1/cadastrar_livro
Esse endpoint cadastra um novo livro no banco de dados.

Parâmetros
Nome	Tipo	Descrição	Obrigatório
titulo	string	Título do livro	sim
autor	string	Autor do livro	sim
ano	int	Ano de publicação do livro	sim
Respostas
Código	Descrição
200	Livro cadastrado com sucesso.
Buscar Livro
bash
Copy code
GET /v1/buscar_livro?id=<id>
Esse endpoint busca um livro pelo ID.

Parâmetros
Nome	Tipo	Descrição	Obrigatório
id	int	ID do livro a buscar	sim
Respostas
Código	Descrição
200	Livro encontrado.
404	Livro não encontrado.
Deletar Livro
bash
Copy code
POST /v1/deletar_livro
Esse endpoint deleta um livro pelo ID.

Parâmetros
Nome	Tipo	Descrição	Obrigatório
id	int	ID do livro a deletar	sim
Respostas
Código	Descrição
200	Livro deletado com sucesso.
404	Livro não encontrado.
Banco de dados
A API utiliza um banco de dados SQLite para armazenar os livros cadastrados. O banco é criado automaticamente caso não exista, com uma tabela chamada livros_registrados. A tabela conta com as seguintes colunas:

Coluna	Tipo	Descrição
id	int	ID do livro
titulo	string	Título do livro
autor	string	Autor do livro
ano	int	Ano de publicação do livro
Executando a API
Para executar a API, siga os seguintes passos:

Clone o repositório e acesse a pasta do projeto.

Instale as dependências com o comando pip install -r requirements.txt.

Execute o arquivo app.py com o comando python app.py.

A API estará disponível em http://localhost:5000/.
