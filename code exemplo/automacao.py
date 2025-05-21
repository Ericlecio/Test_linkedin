from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def recupera_texto(botao):
    return botao.get_attribute("value")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://wcaquino.me/cypress/componentes.html")

time.sleep(5)
campo_nome = driver.find_element(By.ID, "formNome")
campo_nome.send_keys("Kauã")

driver.find_element(By.CSS_SELECTOR, "#formSobrenome").send_keys("Gabriel")

btn = driver.find_element(By.ID, "buttonSimple")
print(recupera_texto(btn))

btn.click()

print(recupera_texto(btn))

time.sleep(5)

driver.quit()


