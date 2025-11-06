from locust import HttpUser, task, between
import random

class UserDoQuoter(HttpUser):
    # Simula um usuário que espera entre 1 e 3 segundos
    wait_time = between(1, 3)
    
    autores_list = []
    areas_list = []

    def on_start(self):
        """ Chamado quando um usuário simulado 'nasce'. """
        self.carregar_filtros()
        
    def carregar_filtros(self):
        """ Pega a lista de filtros para usar nos outros testes. """
        try:
            with self.client.get("/filtros", catch_response=True) as response:
                if response.ok:
                    data = response.json()
                    self.autores_list = ["todos"] + data.get("autores", [])
                    self.areas_list = ["todos"] + data.get("areas", [])
                else:
                    response.failure("Falha ao carregar /filtros")
        except Exception:
            pass 

    @task(10) # Tarefa 10x mais comum
    def buscar_citacao_filtrada(self):
        """ 
        Simula busca com filtros aleatórios.
        AGORA CORRIGIDO para aceitar 404 (Não Encontrado) como SUCESSO.
        """
        if not self.autores_list or not self.areas_list:
            return

        autor = random.choice(self.autores_list)
        area = random.choice(self.areas_list)
        
        # --- INÍCIO DA CORREÇÃO ---
        
        with self.client.get(
            f"/citacao-do-dia?autor={autor}&area={area}", 
            name="/citacao-do-dia?filtro=true",
            catch_response=True  # <-- 1. Diz ao Locust para não falhar sozinho
        ) as response:
            
            # 2. Verificamos a resposta
            if response.status_code == 404:
                # 3. Se for 404 (Não encontrado), marcamos como SUCESSO!
                response.success()
            
            elif not response.ok:
                # 4. Se for qualquer OUTRO erro (ex: 500), aí sim marcamos como falha.
                response.failure(f"Status code foi {response.status_code}, não 200 ou 404")
        
        # --- FIM DA CORREÇÃO ---

    @task(5) # Tarefa 5x mais comum
    def buscar_citacao_geral(self):
        """ Simula busca sem filtros. """
        self.client.get("/citacao-do-dia", name="/citacao-do-dia?filtro=false")

    @task(1) # Tarefa menos comum
    def carregar_pagina_inicial(self):
        """ Simula usuário carregando o HTML. """
        self.client.get("/")