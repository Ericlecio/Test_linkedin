from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://br.linkedin.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_conectar_usuario_linkedin(driver):
    wait = WebDriverWait(driver, 25)

    # Botão "Entrar"
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav__button-secondary"))).click()

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("loracslv356@gmail.com")
    driver.find_element(By.ID, "password").send_keys("My_Test!")
    driver.find_element(By.CLASS_NAME, "btn__primary--large").click()

    # Barra de pesquisa
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Pesquisar')]"))).send_keys("Manuela Lopes" + Keys.RETURN)

    # Clicar no perfil
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Manuela Lopes')]"))).click()

    # Botão "Conectar"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".CPfmsPVoIJFtAWVqgTbYUlTBwhnbTSFiOY button"))).click()

    # Botão "Enviar agora"
    botoes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".artdeco-modal__actionbar button")))
    botoes[1].click()

    # Espera o modal desaparecer como confirmação
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".artdeco-modal__actionbar button")))

    # Confirma que o teste finalizou sem exceção
    assert True

def test_pesquisar_usuario_linkedin(driver):
    driver = driver
    wait = WebDriverWait(driver, 20)

    # Botão "Entrar"
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav__button-secondary"))).click()

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("loracslv356@gmail.com")
    driver.find_element(By.ID, "password").send_keys("My_Test!")
    driver.find_element(By.CLASS_NAME, "btn__primary--large").click()

    # Barra de pesquisa
    barra_pesquisa = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Pesquisar')]")))
    barra_pesquisa.send_keys("Kauã Gabriel" + Keys.RETURN)

    time.sleep(3)


