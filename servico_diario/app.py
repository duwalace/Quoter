from flask import Flask, jsonify
import requests
import random
from flask_cors import CORS  # <--- 1. IMPORTE A BIBLIOTECA

app = Flask(__name__)
CORS(app)  # <--- 2. HABILITE O CORS PARA TODO O APP

URL_SERVICO_CITACOES = "http://127.0.0.1:5001/citacoes"

@app.route('/citacao-do-dia', methods=['GET'])
def get_citacao_do_dia():
    try:
        response = requests.get(URL_SERVICO_CITACOES)
        response.raise_for_status() 
        lista_de_citacoes = response.json()

        if not lista_de_citacoes:
            return jsonify({"erro": "Nenhuma citação encontrada"}), 404

        citacao_escolhida = random.choice(lista_de_citacoes)
        return jsonify(citacao_escolhida)

    except requests.exceptions.ConnectionError:
        return jsonify({"erro": "O serviço de citações está indisponível"}), 503

    except Exception as e:
        return jsonify({"erro": f"Um erro interno ocorreu: {str(e)}"}), 500

if __name__ == '__main__':
    # 3. NÃO PRECISA MUDAR NADA AQUI
    app.run(port=5000, debug=True)