#provedor
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Dados fictícios de livros e preferências dos usuários
livros = {
    1: {'titulo': 'Livro A', 'genero': 'Ficção', 'autor': 'Autor A'},
    2: {'titulo': 'Livro B', 'genero': 'Fantasia', 'autor': 'Autor B'},
    3: {'titulo': 'Livro C', 'genero': 'Ficção', 'autor': 'Autor C'},
    4: {'titulo': 'Livro D', 'genero': 'Fantasia', 'autor': 'Autor D'},
    # Adicione mais livros conforme necessário
}

def recomendar_livros(usuario_id, preferencias):
    genero_preferido = preferencias.get('genero')
    autor_preferido = preferencias.get('autor')

    # Filtrar livros com base nas preferências do usuário
    livros_filtrados = [livro for livro in livros.values() if
                        (not genero_preferido or livro['genero'] == genero_preferido) and
                        (not autor_preferido or livro['autor'] == autor_preferido)]

    # Embaralhar e retornar alguns livros aleatórios (limitado a 3 neste exemplo)
    livros_recomendados = random.sample(livros_filtrados, min(3, len(livros_filtrados)))

    return livros_recomendados

@app.route('/recomendacao', methods=['POST'])
def obter_recomendacao():
    dados_requisicao = request.json

    # Verificação de dados de entrada
    if 'usuario_id' not in dados_requisicao or 'preferencias' not in dados_requisicao:
        return jsonify({'erro': 'Dados de entrada incompletos'}), 400

    usuario_id = dados_requisicao['usuario_id']
    preferencias = dados_requisicao['preferencias']

    livros_recomendados = recomendar_livros(usuario_id, preferencias)

    if not livros_recomendados:
        return jsonify({'mensagem': 'Não há recomendações de livros disponíveis com as preferências fornecidas.'}), 200

    return jsonify({'livros_recomendados': livros_recomendados})

if __name__ == '__main__':
    app.run(port=5002)
