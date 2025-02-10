from fastapi import FastAPI, Query
import requests
from typing import Optional

from fastapi.responses import JSONResponse

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
@app.get('/api/cars')
def all_cars():
    url = "https://raelmorais.github.io/api/api_car.json"
    response = requests.get(url)
    print(response)
    data = response.json()
    print(data)
    return data 

def fetch_filtered_cars(model: str = None, brand: str = None, year: str = None):
    url = "https://raelmorais.github.io/api/api_car.json"
    response = requests.get(url)
    return response

@app.get('/api/cars/filtered')
def get_filtered_cars(model: str = Query(None), brand: str = Query(None), year: str = Query(None)):
    response = fetch_filtered_cars(model, brand, year)

    if response.status_code == 200:
        data = response.json()
        filtered_cars = [car for car in data if
                         (model is None or car['model'].lower() == model.lower()) and
                         (brand is None or car['brand'].lower() == brand.lower()) and
                         (year is None or car['year'] == year)]
        if not filtered_cars:
            return {'message': 'Nenhum carro encontrado com os parâmetros fornecidos.'}
        
        return {'Carro Filtrado': filtered_cars[0]}  

    else:
        return {'error': f'Ocorreu um erro ao acessar a API externa. Código: {response.status_code}'}