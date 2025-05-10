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
