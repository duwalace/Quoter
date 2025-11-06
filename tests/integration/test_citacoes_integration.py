def test_get_filtros_endpoint(citacoes_client):
    """ Testa se a rota /filtros retorna os dados do citacoes.json. """
    response = citacoes_client.get('/citacoes/filtros')
    
    assert response.status_code == 200
    data = response.json
    assert "autores" in data
    assert "areas" in data
    # Verifica alguns dados que sabemos que existem no citacoes.json
    assert "Albert Einstein" in data["autores"]
    assert "Ciência" in data["areas"]

def test_get_citacao_filtrada_sucesso(citacoes_client):
    """ Testa se a rota /filtrada retorna uma citação correta. """
    params = {'autor': 'Albert Einstein', 'area': 'Ciência'}
    response = citacoes_client.get('/citacoes/filtrada', query_string=params)
    
    assert response.status_code == 200
    data = response.json
    assert data['autor'] == 'Albert Einstein'
    assert data['area'] == 'Ciência'

def test_get_citacao_filtrada_nao_encontrado(citacoes_client):
    """ Testa se a rota /filtrada retorna 404 para um filtro impossível. """
    params = {'autor': 'Autor Inexistente', 'area': 'Area Falsa'}
    response = citacoes_client.get('/citacoes/filtrada', query_string=params)
    
    assert response.status_code == 404
    data = response.json
    assert "erro" in data
    assert "Nenhuma citação encontrada" in data["erro"]