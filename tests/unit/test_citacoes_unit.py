from servico_citacoes.app import Citacao

def test_citacao_to_dict():
    """
    Testa se a classe Citacao converte seus dados
    corretamente para um dicionário.
    """
    # ARRANGE (Organizar)
    citacao = Citacao(
        id=1, 
        texto="A imaginação é mais importante que o conhecimento.", 
        autor="Albert Einstein", 
        area="Ciência"
    )
    
    # ACT (Agir)
    resultado_dict = citacao.to_dict()
    
    # ASSERT (Verificar)
    esperado = {
        "id": 1,
        "texto": "A imaginação é mais importante que o conhecimento.",
        "autor": "Albert Einstein",
        "area": "Ciência"
    }
    
    assert resultado_dict == esperado
    assert resultado_dict["autor"] == "Albert Einstein"