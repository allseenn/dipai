from tokens import DATA_MOS_RU
import requests
import json


url = "https://apidata.mos.ru/v1"

folder = "/datasets/"
params = {
    "api_key": DATA_MOS_RU,
}

response = requests.get(url+folder, params=params)
data = json.loads(response.text)
with open("datasets.json", "w", encoding="utf-8", errors="ignore") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)

