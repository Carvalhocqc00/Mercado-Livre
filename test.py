from functions.web_meli import search,titulo,preco_oferta,preco_padrao,desconto_aplicado

soup = search("7891000329665")

#print(titulo(soup)[3].get_text())
#print(preco_oferta(soup))
print(titulo(soup))