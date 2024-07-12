import requests

address = "Адрес организации"
url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"

response = requests.get(url)
data = response.json()

if len(data) > 0:
    latitude = data[0]['lat']
    longitude = data[0]['lon']
    print(f"Координаты организации: {latitude}, {longitude}")
else:
    print("Координаты организации не найдены")
