import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import os

@pytest.fixture(scope="module")
def servers():
    """ Fixture para iniciar e parar os servidores reais. """
    print("\nIniciando servidores via start.bat...")
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    start_script = os.path.join(base_dir, 'start.bat')
    
    # Inicia os servidores em segundo plano
    pro = subprocess.Popen(['cmd', '/c', start_script], cwd=base_dir)
    
    # Dá um tempo para os servidores subirem
    time.sleep(5) 
    
    yield
    
    # TEARDOWN: Mata os servidores
    print("\nParando servidores...")
    # Este comando é específico do Windows e fecha as janelas 'cmd'
    # e os processos 'python' associados.
    subprocess.Popen("taskkill /F /IM cmd.exe /T", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen("taskkill /F /IM python.exe /T", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

@pytest.fixture(scope="module")
def driver():
    """ Fixture para iniciar e fechar o navegador. """
    # Assumindo chromedriver.exe no PATH ou na pasta
    driver = webdriver.Chrome() 
    driver.implicitly_wait(10) # Espera implícita
    yield driver
    driver.quit()

def test_fluxo_completo_com_filtro(servers, driver):
    # 1. Acessa a página home
    driver.get("http://127.0.0.1:5000/")
    
    # 2. Navega para a página de citações
    # Espera o botão CTA aparecer e clica nele
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cta-button"))
    )
    cta_button = driver.find_element(By.CLASS_NAME, "cta-button")
    cta_button.click()
    
    # 3. Espera os filtros carregarem na página de citações
    # Espera a opção "Ciência" aparecer no select (timeout de 20s)
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "filtro-area"), "Ciência")
    )
    
    # 3. Interage com os filtros
    select_area = Select(driver.find_element(By.ID, "filtro-area"))
    select_area.select_by_visible_text("Ciência")
    
    select_autor = Select(driver.find_element(By.ID, "filtro-autor"))
    select_autor.select_by_visible_text("Albert Einstein")
    
    # 4. Clica no botão
    btn = driver.find_element(By.ID, "btn-buscar")
    btn.click()
    
    # 5. Verifica o resultado
    # Espera o texto da citação ser atualizado (não ser o inicial)
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "quote-autor"), "Albert Einstein")
    )
    
    autor_texto = driver.find_element(By.ID, "quote-autor").text
    area_texto = driver.find_element(By.ID, "quote-area").text
    
    assert autor_texto == "— Albert Einstein"
    assert area_texto == "CIÊNCIA"