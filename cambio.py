
# Foi criado uma conta no FIXER.IO -- Só pode ter 1.000 acessos de usuários por mês na versão FREE

import requests
import json

url = "http://data.fixer.io/api/latest?access_key=1454bbcb8173055a6dee5046c5307d3a"
print("Acessando base de dados...")

# Fazendo requisição ao servidor onde o site está hospedado. Códigos: OK = 200, ERRO = 404
# Victor Romário utilizou no cmd: pip install requests
# 'requests' e 'json' são bibliotecas

response =  requests.get(url)
print(response)

# A resposta 200 significa que conseguiu acessar o site sem problemas

if response.status_code == 200:
    print("")
    print("Base de dados acessada com sucesso")
    print("Buscando informações das moedas...")
    dados = response.json() # Desempacotar o JSON
    
    day = dados ["date"] # Poderia ser com aspas simples também
    print ("Acesssando dados do dia %s/%s/%s" % (day [8:], day [5:7], day [0:4]))

    # O resultado do site é convertido em um formato de lista JSON
    
    print("")
    print(dados['rates']['EUR'])
    print(dados['rates']['BRL'])
    print(dados['rates']['USD'])
    print(dados['rates']['BTC'])
    print("")
    
    # Para executar somente o 'rates' ou valores da moedas. Rates é um dicionário dentro de outro

    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    print(euro_real)

    dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
    print(dollar_real)

    btc_real = dados['rates']['BRL'] / dados['rates']['BTC']
    print(btc_real)
else:
    print("Site com Problemas! Não deu 200")


