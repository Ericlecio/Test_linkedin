from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


@pytest.fixture
def setup_teardown():
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.linkedin.com/login/pt")
    campo_nome = driver.find_element(By.ID, "username")
    campo_nome.send_keys("linkedinteste581@hotmail.com")
    campo_senha = driver.find_element(By.ID, "password")
    campo_senha.send_keys("linkedin123456@")
    btn_click_me = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating").click()    
    driver.implicitly_wait(10)
    time.sleep(2)
    # Teardown
    yield driver
    driver.quit()


def test_preencher_campo_texto(setup_teardown):
    driver = setup_teardown
    btn_acessar = driver.find_element(By.XPATH, '//strong[text()="Comece uma publicação"]/ancestor::button').click()
    time.sleep(5)
    campo_texto = driver.find_element(By.XPATH, "//div[contains(@class,'ql-editor') and @contenteditable='true']")
    time.sleep(5)
    campo_texto.send_keys("Teste de publicação")
    time.sleep(5)
    btn_publicar = driver.find_element(By.XPATH, '//span[contains(@class,"artdeco-button__text") and text()="Publicar"]/ancestor::button').click()
    time.sleep(5)
    assert campo_texto.text == "Teste de publicação"

def test_preencher_campo_texto_vazio(setup_teardown):
    driver = setup_teardown
    btn_acessar = driver.find_element(By.XPATH, '//strong[text()="Comece uma publicação"]/ancestor::button').click()
    time.sleep(5)
    campo_texto = driver.find_element(By.XPATH, "//div[contains(@class,'ql-editor') and @contenteditable='true']")
    time.sleep(5)
    campo_texto.send_keys("")
    time.sleep(5)
    btn_publicar = driver.find_element(By.XPATH, '//span[contains(@class,"artdeco-button__text") and text()="Publicar"]/ancestor::button').click()
    time.sleep(5)
    assert campo_texto.text == ""




   








