#consumidor
import requests

class Livro:
    def __init__(self, titulo, genero, autor):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor

# Dados fictícios do usuário e suas preferências
usuario_id = 123
preferencias = {'genero': 'Ficção', 'autor': 'Autor C'}

# URL do Webservice de Recomendação
url_recomendacao = 'http://localhost:5002/recomendacao'

# Requisição POST para obter recomendações
dados_requisicao = {'usuario_id': usuario_id, 'preferencias': preferencias}
try:
    resposta = requests.post(url_recomendacao, json=dados_requisicao)
    resposta.raise_for_status()  # Gera uma exceção para códigos de status HTTP diferentes de 2xx

    # Verifica se a chave 'livros_recomendados' está presente na resposta
    if 'livros_recomendados' in resposta.json():
        print('Não há recomendações de livros disponíveis com as preferências fornecidas.')

except requests.exceptions.RequestException as e:
    print(f'Erro na requisição: {str(e)}')
