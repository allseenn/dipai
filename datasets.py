from tokens import DATA_MOS_RU
import requests
import json


url = "https://apidata.mos.ru/v1"

folder = "/datasets/"
dataset = "2072"
params = {
    "api_key": DATA_MOS_RU,
}

# filename = "datasets.json"
filename = "data-2072.json" # ЕГЭ
# filename = "data-2263.json" # Список школ
# filename = "data-2457.json" # Экология
response = requests.get(url+folder+dataset, params=params)
data = json.loads(response.text)
with open(filename, "w", encoding="utf-8", errors="ignore") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)

