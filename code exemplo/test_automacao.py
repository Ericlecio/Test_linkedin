from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert



@pytest.fixture
def setup_teardown():
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://wcaquino.me/cypress/componentes.html")
    driver.set_window_position(2000, 0)
    # Teardown
    yield driver
    driver.quit()


def test_botao_muda_texto(setup_teardown):
    # Recuperar o driver
    driver = setup_teardown
    # Mapear o botão clique me
    btn = driver.find_element(By.ID, "buttonSimple")
    # Recuperar o texto inicial
    texto_antes = btn.get_attribute("value")
    # Clicar no botão
    btn.click()
    time.sleep(2)
    # Recuperar o texto final
    texto_depois = btn.get_attribute("value")
    # validar se os textos são diferente
    assert texto_antes != texto_depois


def test_preencher_campo_nome(setup_teardown):
    driver = setup_teardown
    campo_nome = driver.find_element(By.ID, "formNome")
    campo_nome.send_keys("Kauã")
    time.sleep(2)
    assert campo_nome.get_attribute("value") == "Kauã"


def test_preencher_checkbox(setup_teardown):
    driver = setup_teardown
    checkbox_pizza = driver.find_element(By.ID, "formComidaPizza")
    checkbox_pizza.click()
    select = checkbox_pizza.is_selected()
    assert select == True


def test_preencher_radio(setup_teardown):
    driver = setup_teardown
    radio_fem = driver.find_element(By.ID, "formSexoFem")
    radio_fem.click()
    select = radio_fem.is_selected()
    assert select == True


def test_multiplos_checkbox(setup_teardown):
    driver = setup_teardown

    carne = driver.find_element(By.ID, "formComidaCarne")
    frango = driver.find_element(By.ID, "formComidaFrango")
    pizza = driver.find_element(By.ID, "formComidaPizza")
    veg = driver.find_element(By.ID, "formComidaVegetariana")

    checkboxes = [carne, frango, pizza, veg]

    for check in checkboxes:
        if not check.is_selected():
            check.click()
        assert check.is_selected() == True, f"O checkbox {check.get_attribute('id')} deveria estar selecionado."

    
def test_drowdown(setup_teardown):
    driver = setup_teardown
    drow = driver.find_element(By.ID, "formEscolaridade")
    opcao = Select(drow)
    opcao.select_by_value("doutorado")
    time.sleep(2)
    opcao_selec = opcao.first_selected_option
    assert opcao_selec.get_attribute("value") == "doutorado"


def test_clicar_primeiro_item_tabela(setup_teardown):
    driver = setup_teardown

    primeiro_botao = driver.find_element(By.CSS_SELECTOR, '#tabelaUsuarios tr td imput[type=button]')

    primeiro_botao.click()

    alert = Alert(driver)
    assert alert.text == "Francisco"

    alert.accept()
    time.sleep(3)



def test_clicar_item_selec(setup_teardown):
    driver = setup_teardown

    botoes = driver.find_elements(By.CSS_SELECTOR, '#tabelaUsuarios tr td input[type=button]')
    print(f"Total de botões encontrados: {len(botoes)}")

    botoes[2].click()

    alert = Alert(driver)
    print(f"Texto do alerta: {alert.text}")

    assert alert.text == "Usuario A"
    alert.accept()


def test_esperar_dinamicamente(setup_teardown):
    driver = setup_teardown
    # timeout explicito -> time.sleep(n)
    # timeout implicito -> esperar condições para seguir com o fluxo

    driver.find_element(By.ID, "buttonDelay").click()
    wait = WebDriverWait(driver, 10)
    


# pytest -s -vk test_clicar_item_selec 