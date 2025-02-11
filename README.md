
# 🚀 Api Docs 
A simple FastAPI application to learn about Fastapi and API Docs.

:pushpin: Json data font: https://raelmorais.github.io/api/api_car.json

### 1. `/api/cars`
Fetch all cars from the external API without any filtering.
#### Request
**Method**: `GET`

### :bomb: Endpoint
**URL**: `/api/cars`

#### Response
- **Status Code**: `200 OK`  	:heavy_check_mark:
- **Body**: A JSON array containing all the cars from the external API.

#### :warning: Example Response
```json
[
    {
        "model": "Onix",
        "brand": "Chevrolet",
        "year": "2012"
    },
    {
        "model": "Cherry Tiggo 5",
        "brand": "Cherry",
        "year": "2020"
    },
    {
    },
]

```
### 2. `/api/cars/filtered`
Filter cars by model, brand, and/or year. This endpoint accepts query parameters for filtering and returns the matching car(s).
#### Request
**Method**: `GET`
### :bomb: Endpoint
**URL**: `/api/cars/filtered`

### Query Parameters (all optional):
- ***model***: The model of the car to filter by.
- ***brand***: The brand of the car to filter by.
- ***year***: The manufacturing year of the car to filter by.

### Request example:

```bash
http://127.0.0.1:8000/api/cars/filtered?model=Onix&brand=Chevrolet&year=2012
```
#### Response
- **Status Code**: `200 OK (If cars are found)`  	:heavy_check_mark:
- **Body**: A JSON object containing the first filtered car.
- 
#### :warning: Example Response
```json
{
  "Cars filtered": {
    "model": "Onix",
    "brand": "Chevrolet",
    "year": "2012",
    "fuel": "flex",
    "car_class": "compact"
  }
}
```
## :bangbang: CODES :bangbang:

#### Response
- **Status Code**: `200 OK (If no cars match the criteria)`  	:heavy_check_mark:
- **Body**: A message indicating no cars were found.
  
```bash
 {
    "message": "No cars found 😓"
}
```

- **Status Code**: `500 Internal Server Error (If Api requests falls`:x:
- **Body**: An error message with the status code.

```json
{
    "error": "API Error. CODE: 500"  	
}
```




<h1> :thinking: How to run?</h1>
1. Clone repository ⭐

 ````bash
>>>git clone https://github.com/RaelMorais/fastAPI.git
````

2. Create virtual environment 💻
````bash
>>>python -m venv env
````

3. Active virtual environment ✔️
```
>>>.\env\Scripts\activate
```

4. install requirements 😄

````bash
>>>pip install -r requirements.txt
````

5. Run 🚀
````bash
>>>puvicorn _main:app --reload
````
Use ```http://127.0.0.1:8000/docs/``` to documentation API. To deactivate venv use ````deactivate```` in shell. 

:brazil: :rage3:

