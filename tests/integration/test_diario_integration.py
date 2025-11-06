import requests.exceptions

def test_get_citacao_do_dia_sucesso(diario_client, mocker):
    """
    Testa se o servico_diario lida corretamente com uma
    resposta 200 OK do servico_citacoes.
    """
    # 1. ARRANGE (Mock)
    # Criamos uma resposta simulada
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 99, "texto": "Texto Simulado", "autor": "Autor Simulado", "area": "Area Simulada"
    }
    # Configuramos o 'raise_for_status' para não fazer nada
    mock_response.raise_for_status.return_value = None
    
    # "Patcheamos" o requests.get DENTRO do app do servico_diario
    mocker.patch('servico_diario.app.requests.get', return_value=mock_response)
    
    # 2. ACT
    response = diario_client.get('/citacao-do-dia?autor=Autor Simulado')
    
    # 3. ASSERT
    assert response.status_code == 200
    data = response.json
    assert data['texto'] == "Texto Simulado"
    assert data['autor'] == "Autor Simulado"

def test_get_citacao_do_dia_falha_conexao(diario_client, mocker):
    """
    Testa se o servico_diario retorna 503 se o servico_citacoes
    estiver indisponível (ConnectionError).
    """
    # 1. ARRANGE (Mock)
    # Simulamos a exceção de Conexão
    mocker.patch(
        'servico_diario.app.requests.get', 
        side_effect=requests.exceptions.ConnectionError
    )
    
    # 2. ACT
    response = diario_client.get('/citacao-do-dia')
    
    # 3. ASSERT
    assert response.status_code == 503
    data = response.json
    assert "indisponível" in data['erro']

def test_get_citacao_do_dia_falha_404(diario_client, mocker):
    """
    Testa se o servico_diario repassa o 404 se o 
    servico_citacoes retornar 404 (nenhuma citação encontrada).
    """
    # 1. ARRANGE (Mock)
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    # Simulamos o 'raise_for_status' lançando um HTTPError
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        response=mock_response
    )
    mocker.patch('servico_diario.app.requests.get', return_value=mock_response)
    
    # 2. ACT
    response = diario_client.get('/citacao-do-dia?autor=Inexistente')
    
    # 3. ASSERT
    assert response.status_code == 404
    data = response.json
    assert "Nenhuma citação encontrada" in data['erro']