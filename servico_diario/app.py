from flask import Flask, jsonify
# --- Requisito 4: Bibliotecas Python ---
import requests  # Para comunicação entre serviços
import random    # Para seleção da citação

# --- Requisito 1: Linguagem Python ---
app = Flask(__name__)

# URL do microsserviço que armazena os dados
URL_SERVICO_CITACOES = "http://127.0.0.1:5001/citacoes"

# --- Requisito 3: Arquitetura de Microsserviços ---
# Endpoint público para o Projeto Integrador
@app.route('/citacao-do-dia', methods=['GET'])
def get_citacao_do_dia():
    """
    Consome o serviço de citações, escolhe uma aleatoriamente
    e a retorna para o cliente.
    """
    try:
        # 1. Comunicação HTTP entre serviços
        # O servico_diario atua como cliente do servico_citacoes
        response = requests.get(URL_SERVICO_CITACOES)
        
        # Lança um erro caso o servico_citacoes esteja fora ou dê erro
        response.raise_for_status() 
        
        lista_de_citacoes = response.json()
        
        if not lista_de_citacoes:
            return jsonify({"erro": "Nenhuma citação encontrada no serviço de dados"}), 404
            
        # 2. Uso da biblioteca 'random' (Requisito 4)
        citacao_escolhida = random.choice(lista_de_citacoes)
        
        # 3. Retorna a resposta final ao cliente
        return jsonify(citacao_escolhida)
    
    except requests.exceptions.ConnectionError:
        # Erro comum em microsserviços: um serviço está fora
        return jsonify({"erro": "O serviço de citações está indisponível"}), 503 # Service Unavailable
    
    except Exception as e:
        # Captura outros erros (ex: JSON inválido, etc.)
        return jsonify({"erro": f"Um erro interno ocorreu: {str(e)}"}), 500

if __name__ == '__main__':
    # Rodando na porta padrão (5000)
    app.run(port=5000, debug=True)