from flask import Flask, jsonify

# --- Requisito 2: Programação Orientada a Objetos ---
# Modelando o conceito central como uma Classe
class Citacao:
    def __init__(self, id, texto, autor):
        self.id = id
        self.texto = texto
        self.autor = autor

    # Método para facilitar a conversão para JSON
    def to_dict(self):
        return {
            "id": self.id,
            "texto": self.texto,
            "autor": self.autor
        }

# --- Requisito 1: Linguagem Python ---
app = Flask(__name__)

# Banco de dados em memória (substitua por um banco real se necessário)
citacoes_db = [
    Citacao(1, "A persistência é o caminho do êxito.", "Charles Chaplin"),
    Citacao(2, "A imaginação é mais importante que o conhecimento.", "Albert Einstein"),
    Citacao(3, "O único lugar onde o sucesso vem antes do trabalho é no dicionário.", "Vidal Sassoon"),
    Citacao(4, "Tente ser um arco-íris na nuvem de alguém.", "Maya Angelou")
]

# --- Requisito 3: Arquitetura de Microsserviços ---
# Endpoint privado para o servico_diario consumir
@app.route('/citacoes', methods=['GET'])
def get_citacoes():
    """
    Retorna a lista completa de todas as citações.
    """
    # Usando o método to_dict() da nossa classe
    lista_de_citacoes_dict = [c.to_dict() for c in citacoes_db]
    return jsonify(lista_de_citacoes_dict)

# Futuramente, Davi pode adicionar os outros endpoints de CRUD aqui
# @app.route('/citacoes', methods=['POST'])
# def create_citacao():
#     ...

# @app.route('/citacoes/<int:id>', methods=['PUT'])
# def update_citacao(id):
#     ...

if __name__ == '__main__':
    # Rodando em uma porta diferente (ex: 5001) para não conflitar
    # com o serviço diário.
    app.run(port=5001, debug=True)