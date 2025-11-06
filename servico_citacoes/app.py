from flask import Flask, jsonify, request # <<< request foi importado
import random 
import json
import os

# --- Classe Citacao (Atualizada com 'area') ---
class Citacao:
    def __init__(self, id, texto, autor, area): # <<< 'area' adicionada
        self.id = id
        self.texto = texto
        self.autor = autor
        self.area = area # <<< 'area' adicionada

    def to_dict(self):
        return {
            "id": self.id,
            "texto": self.texto,
            "autor": self.autor,
            "area": self.area # <<< 'area' adicionada
        }

app = Flask(__name__)

# --- Função de Carga (Atualizada para ler 'area') ---
def carregar_citacoes_do_json():
    print("Iniciando carga de citações do arquivo 'citacoes.json'...")
    db = []
    
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    JSON_PATH = os.path.join(APP_ROOT, 'citacoes.json')

    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            dados_json = json.load(f)
            
            for i, item in enumerate(dados_json):
                db.append(
                    Citacao(
                        id=i+1, 
                        texto=item['texto'], 
                        autor=item['autor'], 
                        area=item['area'] # <<< 'area' adicionada
                    )
                )
            
            print(f"Carga finalizada. Total de {len(db)} citações no banco.")
            
    except FileNotFoundError:
        print("ERRO CRÍTICO: Arquivo 'citacoes.json' não encontrado!")
        db.append(Citacao(1, "Arquivo 'citacoes.json' não encontrado.", "Sistema", "Erro"))
    except Exception as e:
        print(f"ERRO CRÍTICO ao ler o JSON: {e}")
        db.append(Citacao(1, "Erro ao ler o arquivo de citações.", "Sistema", "Erro"))
        
    return db

# --- Banco de dados em memória ---
citacoes_db = carregar_citacoes_do_json()

# --- Endpoints da API ---

@app.route('/citacoes', methods=['GET'])
def get_citacoes():
    lista_de_citacoes_dict = [c.to_dict() for c in citacoes_db]
    return jsonify(lista_de_citacoes_dict)

@app.route('/citacoes/aleatoria', methods=['GET'])
def get_citacao_aleatoria():
    """ Endpoint antigo, mantido por compatibilidade. """
    if not citacoes_db:
        return jsonify({"erro": "Nenhuma citação disponível"}), 404
    citacao_escolhida = random.choice(citacoes_db)
    return jsonify(citacao_escolhida.to_dict())

# --- NOVO ENDPOINT DE FILTRO ---
@app.route('/citacoes/filtrada', methods=['GET'])
def get_citacao_filtrada():
    """
    Retorna uma citação aleatória com base nos filtros
    de 'autor' e/ou 'area' passados na URL.
    Ex: /citacoes/filtrada?autor=Albert Einstein&area=Ciência
    """
    
    # 1. Pega os filtros da URL
    autor_filtro = request.args.get('autor')
    area_filtro = request.args.get('area')
    
    # Começa com a lista completa
    lista_filtrada = citacoes_db
    
    # 2. Aplica os filtros se eles existirem
    if autor_filtro and autor_filtro != 'todos':
        lista_filtrada = [c for c in lista_filtrada if c.autor == autor_filtro]
        
    if area_filtro and area_filtro != 'todos':
        lista_filtrada = [c for c in lista_filtrada if c.area == area_filtro]

    # 3. Verifica se sobrou alguma citação
    if not lista_filtrada:
        return jsonify({"erro": "Nenhuma citação encontrada com esses filtros."}), 404
        
    # 4. Sorteia uma da lista filtrada
    citacao_escolhida = random.choice(lista_filtrada)
    return jsonify(citacao_escolhida.to_dict())

# --- NOVO ENDPOINT PARA POPULAR OS FILTROS ---
@app.route('/citacoes/filtros', methods=['GET'])
def get_filtros():
    """
    Retorna uma lista única de todos os autores e áreas
    para o frontend usar nos menus <select>.
    """
    autores = sorted(list(set([c.autor for c in citacoes_db])))
    areas = sorted(list(set([c.area for c in citacoes_db])))
    
    return jsonify({
        "autores": autores,
        "areas": areas
    })

# --- Roda o servidor ---
if __name__ == '__main__':
    app.run(port=5001, debug=True)