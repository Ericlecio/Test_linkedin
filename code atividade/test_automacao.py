from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.webdriver.support.ui import Select


@pytest.fixture
def setup_teardown():
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://br.linkedin.com/")
    # Teardown
    yield driver
    driver.quit()


def test_preencher_inputs_invalidos(setup_teardown):
    driver = setup_teardown
    # Botão page inicial
    btn_entrar = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    btn_entrar.click()
    time.sleep(2)

    # Page de login
    input_username = driver.find_element(By.ID, "username")
    input_username.send_keys("gabrielnbhd")
    time.sleep(1)
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("Teste")

    # Clicar no botão de login
    btn_login = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    btn_login.click()
    time.sleep(1)

    # Verificar se a mensagem de erro está presente
    erro_elementos = driver.find_elements(By.ID, "error-for-password")
    assert len(erro_elementos) > 0, "Erro esperado não foi exibido ao inserir dados inválidos."



def test_fazer_login_sucesso(setup_teardown):
    driver = setup_teardown
    # Botão page inicial
    btn_entrar = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    btn_entrar.click()
    time.sleep(2)

    # Page de login
    # Os inputs
    input_username = driver.find_element(By.ID, "username")
    input_username.send_keys("gabrielnbhd32475@gmail.com")
    time.sleep(1)
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("Teste@2025")

    # clicar no botão de entrar da page login
    btn_login = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    btn_login.click()
    time.sleep(1)
    
    assert "feed" in driver.current_url, "Login falhou: não redirecionado para a página principal."
    
