from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from bs4 import BeautifulSoup

import time

# Configurações para a não abertura da janela
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ativa o modo headless
chrome_options.add_argument("--disable-gpu")  # Melhora a compatibilidade
chrome_options.add_argument("--no-sandbox")  # Útil em ambientes Linux
chrome_options.add_argument("--window-size=1920,1080")  # Define um tamanho de tela virtual


# Inicializando o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) # Aplicação com Vizualização em Janela
#driver = webdriver.Chrome(service=service, options=chrome_options) # Aplicação sem Vizualização em Janela

# Acessando o Google
driver.get("https://www.mercadolivre.com.br/")
time.sleep(3)

# Encontrando a caixa de pesquisa e realizando uma ação
search_box = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]')
search_box.send_keys("7891000329665") #7890856209329
search_box.submit()

time.sleep(3)

div_search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root-app"]/div')) #<div class="ui-search">
)
html_content = div_search.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')

div_priceNormal_products = soup.find_all('s', class_='andes-money-amount andes-money-amount--previous andes-money-amount--cents-comma')
div_price_products = soup.find_all('span', class_='andes-money-amount andes-money-amount--cents-superscript')
div_description_products = soup.find_all('h3', class_='poly-component__title-wrapper')
div_discont_products = soup.find_all('span', class_='andes-money-amount__discount poly-price__disc_label')

price = div_price_products[5].get_text()
print(price)
print(type(div_price_products))
print(len(div_price_products))

#i = 0
#while i < len(div_price_products):
#    print(div_price_products[i].get_text())
#    i += 1

# Converter para float (removendo 'R$', pontos e trocando ',' por '.')
converted_prices = []
for price in div_price_products:
    text = price.get_text().strip()  # Ex: 'R$ 1.299,99'
    text = text.replace('R$', '').replace('.', '').replace(',', '.').strip()  # '1299.99'
    number = float(text)
    converted_prices.append(number)

print(converted_prices)  # [1299.99, 2499.50, 999.00]

#print(soup.prettify())
#search_price = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[12]/ol/li[2]/div/div/div/div[2]/div[1]/div/span[1]/span[2]').text

#print(search_price)

# Fechando o navegador
#driver.quit() 