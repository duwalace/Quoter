# <<< MUDANÇA 1: Importar 'render_template'
from flask import Flask, jsonify, request, render_template
import requests 
# 'os' e 'send_from_directory' não são mais necessários para esta rota

app = Flask(__name__)
# O Flask automaticamente encontra a pasta 'templates'

# URL do outro serviço (o "banco de dados")
URL_BASE_CITATCOES = "http://127.0.0.1:5001/citacoes"

# --- Rota 1: Servir o Frontend (o site bonito) ---
@app.route('/') 
def index():
    """ 
    Serve a página principal 'index.html' a partir da pasta 'templates'.
    """
    # <<< MUDANÇA 2: Usar 'render_template'
    # Isso processa o HTML e resolve o 'url_for'
    return render_template('index.html')

# --- Rota 2: A API que o site bonito chama ---
@app.route('/citacao-do-dia', methods=['GET'])
def get_citacao_do_dia():
    """ 
    Consome o serviço de citações e repassa o JSON.
    (Esta função não muda)
    """
    
    autor = request.args.get('autor', 'todos')
    area = request.args.get('area', 'todos')
    params = {'autor': autor, 'area': area}
    
    try:
        response = requests.get(f"{URL_BASE_CITATCOES}/filtrada", params=params)
        response.raise_for_status() 
        citacao_escolhida = response.json()
        return jsonify(citacao_escolhida)
    
    except requests.exceptions.ConnectionError:
        return jsonify({"erro": "O serviço de citações está indisponível"}), 503 
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return jsonify({"erro": "Nenhuma citação encontrada com esses filtros."}), 404
        return jsonify({"erro": f"Serviço de citações retornou erro: {e.response.status_code}"}), 500
    except Exception as e:
        return jsonify({"erro": f"Um erro interno ocorreu: {str(e)}"}), 500

# --- Rota 3: API para buscar os filtros ---
@app.route('/filtros', methods=['GET'])
def get_filtros_disponiveis():
    """ 
    Busca os autores e áreas do serviço de citações.
    (Esta função não muda)
    """
    try:
        response = requests.get(f"{URL_BASE_CITATCOES}/filtros")
        response.raise_for_status()
        return jsonify(response.json())
    except Exception:
        return jsonify({"autores": [], "areas": []}), 500

# --- Roda o servidor ---
if __name__ == '__main__':
    app.run(port=5000, debug=True)