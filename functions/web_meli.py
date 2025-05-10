from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from bs4 import BeautifulSoup

import time

# Importações Locais
from converters_data import convert_bs4_to_float

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

def search(ean):
    gtin = str(ean)
    # Acessando o Mercado Livre
    driver.get("https://www.mercadolivre.com.br/")
    time.sleep(3)

    # Encontrando a caixa de pesquisa e realizando uma ação
    search_box = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]') # Identificação da Barra de Pesquisa
    search_box.send_keys(gtin) # Introdução do Dado no Campo - Barra de Pesquisa
    search_box.submit() # Efetivação da Pesquisa

    time.sleep(3) # Espera do Carregamento

    div_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root-app"]/div')) #<div class="ui-search">
    )
    html_content = div_search.get_attribute('outerHTML') #  Captura o Código Fonte HTML do Elemento

    soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8') # Cria um Objeto BeautifulSoup, que Facilita a Navegação e Extração de Dados Específicos dessa Estrutura HTML.

    return soup

def preco_padrao(soup):
    element = 's'
    class_name = 'andes-money-amount andes-money-amount--previous andes-money-amount--cents-comma'

    list_prices = soup.find_all(element, class_=class_name)

    return convert_bs4_to_float(list_prices)

def preco_oferta(soup):
    element = 'span'
    class_name = 'andes-money-amount andes-money-amount--cents-superscript'

    list_prices = soup.find_all(element, class_=class_name)

    return convert_bs4_to_float(list_prices)

def desconto_aplicado(soup):
    element = 'span'
    class_name = 'andes-money-amount__discount poly-price__disc_label'

    list_discount = soup.find_all(element, class_=class_name)

    return list_discount

def titulo(soup):
    element = 'h3'
    class_name = 'poly-component__title-wrapper'

    list_titles = soup.find_all(element, class_=class_name)

    return list_titles



 
