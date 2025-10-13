Este projeto contém testes automatizados para a API pública JSONPlaceholder, utilizando Python, Requests e Pytest. Foram implementados dois testes principais:

- Testa o endpoint GET /posts, verificando se o retorno é bem-sucedido (status 200), validando também o formato e conteúdo da resposta e confirmando se o JSON contém os campos esperados.

- Testa o endpoint POST /posts, em que envia dados aleatórios gerados e valida o status, o corpo da resposta e o ID retornado.


## Pré-requisitos

Antes de rodar o teste, verifique se possui:

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)

## Instalação

- Para rodar os testes, é necessário clonar o repositório: [https://github.com/GildoFreitas/DotTesteTecnico.git](https://github.com/GildoFreitas/TesteAutomatizadoPython.git)
- Acessar a pasta principal do teste, pode usar via linha de comando: "cd '.\Questão 02\'"
- Instalar as dependências, via linha de comando pode utilizar: "pip install -r requirements.txt"

## Executando o Teste

Via terminal dentro da pasta "Questão 02" e execute:
- pytest test_api_jsonplaceholder.py