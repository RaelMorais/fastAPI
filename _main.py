from fastapi import FastAPI, Query
import requests
from typing import Optional

app = FastAPI()

@app.get('/api/cars')#All cars, no filtred
def all_cars():
    url = "https://raelmorais.github.io/api/api_car.json"
    response = requests.get(url)
    print(response)
    data = response.json()
    return data 

def fetch_filtered_cars(model: str = None, brand: str = None, year: str = None):
    url = "https://raelmorais.github.io/api/api_car.json"
    response = requests.get(url)
    return response
"""
    Fetches car data from an external API.

    Sends a GET request to retrieve car data in JSON format.
    The function does not filter the data but returns the full API response.

    Returns:
    response (Response): The API response object.
"""

@app.get('/api/cars/filtered')#Endpoint for research
def get_filtered_cars(model: str = Query(None), brand: str = Query(None), year: str = Query(None)):
    response = fetch_filtered_cars(model, brand, year)
    """
    Filters car data based on model, brand, and/or year.

    This FastAPI endpoint allows filtering of cars by model, brand, and year through query parameters.
    It returns the filtered car(s) in a JSON response. 

    Parameters:
    model (str): Optional filter for car model.
    brand (str): Optional filter for car brand.
    year (str): Optional filter for car year.

    Returns:
    dict: A dictionary with:
          - The first filtered car if found.
          - A 'No cars found 😓' message if no matches are found.
          - An error message if the API request fails.
    """

    if response.status_code == 200:
        data = response.json()
        filtered_cars = [car for car in data if
                         (model is None or car['model'].lower() == model.lower()) and
                         (brand is None or car['brand'].lower() == brand.lower()) and
                         (year is None or car['year'] == year)]
        if not filtered_cars:
            return {'message': 'No cars found 😓'}
        
        return {'Cars filtered': filtered_cars[0]}  

    else:
        return {'error': f'API Error. CODE: {response.status_code}'}