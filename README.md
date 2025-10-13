Este projeto contém um teste automatizado usando **Playwright com Python**, que realiza as seguintes ações no site da Amazon Brasil:

1. Acessa a página inicial da [Amazon.com.br](https://www.amazon.com.br/).
2. Busca o livro **"AI Engineering: Building Applications with Foundation Models"**.
3. Garante que:
   - A edição seja em **Inglês**.
   - O autor seja **Chip Huyen**.
   - Você está comprando o livro físico.
   - Que o livro é físico, possuindo uma capa comum.
4. Adiciona o livro ao carrinho.
5. Valida a mensagem exibida: **“Adicionado ao carrinho”**.

## Pré-requisitos

Antes de rodar o teste, verifique se possui:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- Navegadores suportados pelo Playwright

## Instalação

- Para rodar os testes, é necessário clonar o repositório: [https://github.com/GildoFreitas/DotTesteTecnico.git](https://github.com/GildoFreitas/TesteAutomatizadoPython.git)
- Instalar as dependências, via linha de comando pode utilizar: pip install pytest playwright
- Baixar os navegadores utilizados pelo Playwright, via linha de comando pode utilizar: playwright install

## Executando o Teste

Via terminal, acesse o pasta "Questão 01" e execute:
- pytest test_amazon.py

Por padrão, está com o headless setado como False para acompanhar a execução do teste.

