import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
response = requests.get(url)
print(response)
if response.status_code == 200:
    data = response.json()
    cotacao = float(data['USDBRL']['bid'])
    valorAlta = float(data['USDBRL']['high'])
    valorBaixa = float(data['USDBRL']['low'])
    num = 20.00
    valordolar = num * cotacao
    print(f"U$ 1 dólar corresponde a R$ {cotacao:.2f}\nNa baixa vale R$ {valorBaixa:.2f}\nNa alta R$ {valorAlta:.2f}\n {num} = {valordolar:.2f}")
    
else:
    print(f"A requisição falhou com o código de status {response.status_code}") 