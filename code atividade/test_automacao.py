from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time


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
    input_username.send_keys("linkedinteste579@gmail.com")
    time.sleep(1)
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("testeequipe@")

    # clicar no botão de entrar da page login
    btn_login = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    btn_login.click()
    time.sleep(1)
    
    return driver


def test_busca_vagas_remoto(setup_teardown):

    driver = test_fazer_login_sucesso(setup_teardown)

    wait = WebDriverWait(driver, 15)

    links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.global-nav__primary-link")))
    vagas_link = next(
        link for link in links
        if link.find_element(By.TAG_NAME, "span").text.strip() == "Vagas"
    )
    vagas_link.click()

    location_input = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input.jobs-search-box__text-input[aria-label='Cidade, estado ou código postal']")
        )
    )

    location_input.clear()
    location_input.click()
    location_input.send_keys("Remoto")

    time.sleep(0.5)

    actions = ActionChains(driver)
    actions.send_keys_to_element(location_input, Keys.ENTER).perform()
    time.sleep(5)


def test_busca_perfil(setup_teardown):
    
    driver = test_fazer_login_sucesso(setup_teardown)

    wait = WebDriverWait(driver, 15)

    # Espera o campo de busca
    search_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.search-global-typeahead__input"))
    )

    perfil_nome = "Ericlécio Thiago"
    search_input.clear()
    search_input.send_keys(perfil_nome)
    search_input.send_keys(Keys.ENTER)

    # Espera a URL conter "search"
    wait.until(lambda d: "search" in d.current_url or "profile" in d.current_url)

    time.sleep(5)

    url_atual = driver.current_url
    assert "search" in url_atual or "profile" in url_atual, "Não foi carregada a página de resultados ou perfil."

    resultados = driver.find_elements(By.CSS_SELECTOR, "div.search-results-container, div.profile-detail")
    assert len(resultados) > 0, "Nenhum resultado ou perfil foi exibido após a busca."