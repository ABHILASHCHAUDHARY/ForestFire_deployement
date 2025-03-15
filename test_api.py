import requests

url = 'http://127.0.0.1:5000/predict'

data = [
    {
        "Temperature": 32.5,
        "RH": 35,
        "Ws": 14.2,
        "Rain": 0.0,
        "FFMC": 90.2,
        "DMC": 30.6,
        "ISI": 7.5,
        "Classes": 1,      # 1 = fire, 0 = not fire (you mentioned this earlier)
        "Region": 1
    }
]

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
