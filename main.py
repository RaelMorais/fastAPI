from fastapi import FastAPI, Query
import requests
import json

app = FastAPI()

@app.get('/api/hello')

def hello_world():
    joao = {
        'hello':'world',
        'hello1':'world2'
    }
    return joao

@app.get('/api/restaurantes')
def restaurante(restaurante: str = Query(None)):  
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        dados_restaurante = []
        for item in dados_json:
            if item['Company'].lower() == restaurante.lower(): 
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else: 
        print(f'O erro foi {response.status_code}')

@app.get('/api/dollar/')
def dolar():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
            data = response.json()
            lista = {
                  'bid': data['USDBRL']['bid'],
                  'high': data['USDBRL']['high'],
                  'low':data['USDBRL']['low'],
            }
    return lista

        
    


