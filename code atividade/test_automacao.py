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


def test_fazer_login_sucesso(setup_teardown):
    driver = setup_teardown
    # Botão page inicial
    btn_entrar = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    btn_entrar.click()
    time.sleep(2)

    # Page de login
    # Os inputs
    input_username = driver.find_element(By.ID, "username")
    input_username.send_keys("evertontestex@gmail.com")
    time.sleep(1)
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("Testequipe2025@")

    # clicar no botão de entrar da page login
    btn_login = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    btn_login.click()
    time.sleep(1)
    return driver
    
    
def test_alterar_nome_perfil(setup_teardown):
    driver = test_fazer_login_sucesso(setup_teardown)
    href = driver.find_element(By.CSS_SELECTOR, ".profile-card-member-details a").get_attribute("href")
    driver.get(f"{href}")
    time.sleep(2)
    btn_edit = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Editar introdução']")
    btn_edit.click()
    time.sleep(2)
    campo_nome = driver.find_element(By.ID, "single-line-text-form-component-profileEditFormElement-TOP-CARD-profile-ACoAAFsFkiQBZQ6oIDAM97mmQBcvcF-87kN-S-E-firstName")
    campo_nome.clear()
    campo_nome.send_keys("Teste")
    btn_salvar = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button")
    assert campo_nome.get_attribute("value") == "Teste"
    btn_salvar.click()
    time.sleep(2)


def test_alterar_sobrenome_perfil(setup_teardown):
    driver = test_fazer_login_sucesso(setup_teardown)
    href = driver.find_element(By.CSS_SELECTOR, ".profile-card-member-details a").get_attribute("href")
    driver.get(f"{href}")
    time.sleep(2)
    btn_edit = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Editar introdução']")
    btn_edit.click()
    time.sleep(2)
    campo_sobrenome = driver.find_element(By.ID, "single-line-text-form-component-profileEditFormElement-TOP-CARD-profile-ACoAAEXolgUBioTMw30o3-ldjk-H64-P6SrD0yU-lastName")
    campo_sobrenome.clear()
    campo_sobrenome.send_keys("Automatizado")
    btn_salvar = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button")
    assert campo_sobrenome.get_attribute("value") == "Automatizado"
    btn_salvar.click()
    time.sleep(2)

