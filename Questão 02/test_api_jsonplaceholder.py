import requests        # Para realizar requisições HTTP (GET/POST)
import random
import string
import pytest

# URL da que será testada
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def gerar_dados_test_post():
    """
    Gera massa de dados aleatória para o teste do método POST.
    """
    return {
        "title": "Título " + "".join(random.choices(string.ascii_letters, k=8)), #GEra um título aleatório
        "body": "Corpo de teste automatizado",
        "userId": random.randint(1, 5) #Gera um número aleatório entre 1 e 5
    }


def validar_campos_post(post):
    """
    Valida se o dicionário retornado contém os campos esperados e verifica que o tipo de dado seja um dicionário JSON válido.
    """
    campos_esperados = {"userId", "id", "title", "body"}

    #Garante que o retorno seja um dicionário
    assert isinstance(post, dict), "O post não é um dicionário JSON válido."

    #Verifica se todos os campos esperados estão presentes no dicionário retornado
    assert campos_esperados.issubset(post.keys()), (
        f"Campos ausentes no post: {set(campos_esperados) - set(post.keys())}"
    )

#TESTE GET /posts
def test_get_posts():
    """
    Testa o endpoint GET /posts
    -Verifica se o retorno é bem-sucedido (status 200)
    -Valida formato e conteúdo da resposta
    -Confirma que o JSON contém os campos esperados
    """

    #Envolve a chamada da API em try/except para capturar erros de rede
    try:
        response = requests.get(BASE_URL, timeout=10)
    except requests.exceptions.RequestException as e:
        #Falha o teste com uma mensagem descritiva, caso não entre no try
        pytest.fail(f"Erro de conexão com a API: {e}")

    #Valida que o código de status é 200 de requisição bem sucedida
    assert response.status_code == 200, f"Status inesperado: {response.status_code}"

    #Converte a resposta JSON para lista de posts
    data = response.json()

    #Verifica se o retorno é uma lista não vazia
    assert isinstance(data, list), "A resposta não é uma lista."
    assert len(data) > 0, "Lista de posts retornou vazia."

    #Valida os campos do primeiro post da lista
    validar_campos_post(data[0])

#TESTE POST /posts
def test_post_novo_post():
    """
    Testa o endpoint POST /posts
    -Envia dados aleatórios gerados por 'gerar_dados_test_post()'
    -Valida o status, o corpo da resposta e o ID retornado
    """

    #Gera a massa de dados
    payload = gerar_dados_test_post()

    #Tenta enviar o POST e trata possíveis erros de rede
    try:
        response = requests.post(BASE_URL, json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Erro ao enviar requisição POST: {e}")

    #Valida o status HTTP de criação (201)
    assert response.status_code == 201, f"Esperado 201, recebido {response.status_code}"

    #Converte a resposta para JSON
    data = response.json()

    #Verifica que o JSON retornado tem a estrutura esperada
    validar_campos_post(data)

    #Garante que os campos enviados estão refletidos no retorno
    for campo in ["title", "body", "userId"]:
        assert data[campo] == payload[campo], f"Dado divergente no campo {campo}"

    #Valida que a API retornou um ID gerado
    assert "id" in data and isinstance(data["id"], int), "Campo 'id' ausente ou inválido"
    assert data["id"] > 0, f"ID inválido retornado: {data['id']}"
