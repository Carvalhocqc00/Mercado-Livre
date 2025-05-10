from bs4 import BeautifulSoup

def convert_bs4_to_float(bs4_object_list):
# Converter para float (removendo 'R$', pontos e trocando ',' por '.')
    converted_prices = []
    for price in bs4_object_list:
        text = price.get_text().strip()  # Ex: 'R$ 1.299,99'
        text = text.replace('R$', '').replace('.', '').replace(',', '.').strip()  # '1299.99'
        number = float(text)
        converted_prices.append(number)

    return converted_prices # [1299.99, 2499.50, 999.00]

def convert_bs4_to_string(bs4_object_list):
    # Converter para string
    converted_title = []
    for price in bs4_object_list:
        text = price.get_text()
        number = str(text)
        converted_title.append(number)

    return converted_title

def convert_bs4_to_int(bs4_object_list):
    # Converter para lista
    converted_int = []
    for price in bs4_object_list:
        text = price.get_text().strip()  # Ex: 'R$ 1.299,99'
        #text = text.replace('R$', '').replace('.', '').replace(',', '.').strip()  # '1299.99'
        number = int(text)
        converted_int.append(number)

    return converted_int # [1299.99, 2499.50, 999.00]