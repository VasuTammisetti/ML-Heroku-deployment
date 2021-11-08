import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'sepallength':5, 'sepalwidth':3, 'petallength':1,'petalwidth':1})

print(r.json())