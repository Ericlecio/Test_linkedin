from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar conexão com driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def recupera_texto(botao):
    return botao.get_attribute("value")

# Acessar página
driver.get("https://wcaquino.me/cypress/componentes.html")

# Escrever em um elmento utilizando o By.ID
time.sleep(5)
campo_nome = driver.find_element(By.ID, "formNome")
campo_nome.send_keys("David")

# Escrever em um elemento utilizando o By.CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "#formSobrenome").send_keys("Brandão")

# Clicar em um botão - radio button - checkbox
btn_click_me = driver.find_element(By.ID, "buttonSimple")
print(recupera_texto(btn_click_me))

btn_click_me.click()
print(recupera_texto(btn_click_me))

time.sleep(5)
driver.quit()