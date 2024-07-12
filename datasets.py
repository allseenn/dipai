import os
import gzip
import json
import shutil
import requests
from tokens import DATA_MOS_RU

datasets = ["2072", "2263", "2457"]
step = 1000

url = "https://apidata.mos.ru/v1"
folder = "/datasets/"
params = {
    "api_key": DATA_MOS_RU,
    "$skip": 0
}

for dataset in datasets:
    count = int(requests.get(url + folder + dataset + "/count", params=params).text)
    all_data = []
    
    while count > params["$skip"]:
        response = requests.get(url + folder + dataset + "/rows", params=params)
        data = response.json()
        all_data.extend(data)
        params["$skip"] += step
    
    params["$skip"] = 0
    count = 0
    
    with open(f"data-{dataset}.json", "w", encoding="utf-8", errors="ignore") as outfile:
        json.dump(all_data, outfile, ensure_ascii=False, separators=(',', ':'))
    
    with open(f"data-{dataset}.json", "rb") as f_in, gzip.open(f"data-{dataset}.json.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    
    os.remove(f"data-{dataset}.json")








