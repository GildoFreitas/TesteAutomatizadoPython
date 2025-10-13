import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="session")
def browser_context():
    """
    Abre o navegador apenas uma vez por sessão de teste.
    Usa o Playwright em modo síncrono para simplificar a execução.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(locale="pt-BR")
        yield context
        context.close()
        browser.close()


@pytest.fixture
def page(browser_context):
    """
    Cria uma nova aba limpa antes de cada teste.
    Fecha a aba ao final.
    """
    page = browser_context.new_page()
    yield page
    page.close()

#Teste para adicionar livro ao carrinho
def test_amazon(page):
    """
    Caso de Teste: adicionar o livro 'AI Engineering: Building Applications with Foundation Models'
    ao carrinho da Amazon Brasil e validar mensagem de sucesso.
    """

    #Acessando a página inicial da Amazon
    page.goto("https://www.amazon.com.br/")

    #Clicando no campo de pesquisa, colocando o nome "AI Engineering: Building Applications with Foundation Models" e clicando para pesquisar
    search_box = page.get_by_role("searchbox", name="Pesquisar Amazon.com.br")
    search_box.click()
    search_box.fill("AI Engineering: Building Applications with Foundation Models")
    page.get_by_role("button", name="Ir", exact=True).click()

    #Clicando no link do livro
    page.get_by_role("link", name="AI Engineering: Building Applications with Foundation Models").click()

    #Conferindo o autor e o idioma
    edition_info = page.get_by_text("Edição Inglês por Chip Huyen", exact=False)

    #Conferindo se é livro físico
    expect(page.get_by_role("button", name="Outros Novo a partir de R$")).to_be_visible()

    #Conferindo se é novo
    expect(page.get_by_role("button", name="Outros Novo a partir de R$")).to_be_visible()

    #Clicando no botão de adicionar ao carrinho e conferindo a mensagem
    page.get_by_role("button", name="Adicionar ao carrinho", exact=True).click()
    expect(page.get_by_role("heading", name="Adicionado ao carrinho")).to_be_visible()



