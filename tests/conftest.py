import pytest
import sys
import os

# Adiciona o diretório raiz (QUOTER) ao path do Python
# Isso permite que os testes encontrem 'servico_citacoes' e 'servico_diario'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa os apps DEPOIS de ajustar o path
from servico_citacoes.app import app as citacoes_app
from servico_diario.app import app as diario_app

@pytest.fixture(scope='module')
def citacoes_client():
    """ Cria um cliente de teste para o servico_citacoes. """
    citacoes_app.config['TESTING'] = True
    with citacoes_app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def diario_client():
    """ Cria um cliente de teste para o servico_diario. """
    diario_app.config['TESTING'] = True
    with diario_app.test_client() as client:
        yield client