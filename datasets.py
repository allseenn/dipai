from tokens import DATA_MOS_RU
import requests
import json


url = "https://apidata.mos.ru/v1"

folder = "/datasets/"
dataset = "2263"
file = "/rows" # действие

params = {
    "api_key": DATA_MOS_RU,
    "top": "1000000",
}

# filename = "datasets.json"
# filename = "data-2072-count.json" # ЕГЭ
filename = "data-2263.json" # Список школ
# filename = "data-2457-count.json" # Экология
response = requests.get(url+folder+dataset+file, params=params)
data = json.loads(response.text)
with open(filename, "w", encoding="utf-8", errors="ignore") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)

