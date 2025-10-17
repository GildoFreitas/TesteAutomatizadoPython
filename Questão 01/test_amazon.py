import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="session")
def browser_context():
    """
    Abre o navegador apenas uma vez por sessão de teste e usa o Playwright em modo para simplificar a execução.
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
    Cria uma nova aba e fecha a aba ao final.
    """
    page = browser_context.new_page()
    yield page
    page.close()

#Teste para adicionar livro ao carrinho
def test_amazon(page):
    """
    Caso de Teste: adicionar o livro 'AI Engineering: Building Applications with Foundation Models' ao carrinho da Amazon Brasil e validar mensagem de sucesso.
    """
    #Acessando a página inicial da Amazon
    page.goto("https://www.amazon.com.br/")
    titulo = page.title()
    assert "Amazon.com.br" in titulo, f"Título inesperado: {titulo}"

    #Clicando no campo de pesquisa, colocando o nome "AI Engineering: Building Applications with Foundation Models" e clicando para pesquisar
    search_box = page.get_by_role("searchbox", name="Pesquisar Amazon.com.br")
    search_box.click()
    search_box.fill("AI Engineering: Building Applications with Foundation Models")
    page.get_by_role("button", name="Ir", exact=True).click()

    #Clicando no link do livro
    page.get_by_role("link", name="AI Engineering: Building Applications with Foundation Models").click()

    #Conferindo o autor
    autor_livro = page.get_by_text("Edição Inglês por Chip Huyen", exact=False)
    expect(autor_livro).to_be_visible()
    assert "Chip Huyen" in autor_livro.inner_text(), "O autor não é Chip Huyen!"

    #Conferindo o idioma
    idioma_livro = page.get_by_text("Edição Inglês por Chip Huyen", exact=False)
    expect(idioma_livro).to_be_visible()
    assert "Inglês" in autor_livro.inner_text(), "O idioma não é inglês!"

    #Conferindo se é livro físico
    livro_fisico = page.get_by_role("radio", name="Capa Comum Formato: R$")
    expect(livro_fisico).to_be_visible()
    assert "Capa Comum" in livro_fisico.inner_text(), "O livro não é físico"

    #Conferindo se é novo
    livro_novo = page.get_by_role("button", name="Outros Novo a partir de R$")
    expect(livro_novo).to_be_visible()
    assert "Novo" in livro_novo.inner_text(), "O livro não é novo"

    #Clicando no botão de adicionar ao carrinho e conferindo a mensagem
    page.get_by_role("button", name="Adicionar ao carrinho", exact=True).click()
    adicionado_carrinho = page.get_by_role("heading", name="Adicionado ao carrinho")
    expect(adicionado_carrinho).to_be_visible()
    assert "Adicionado ao carrinho" in adicionado_carrinho.inner_text(), "O livro não foi adicionado no carrinho"



