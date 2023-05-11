import pandas as pd
import os
import requests
import json
from tqdm import tqdm

URL = "http://127.0.0.1:5000/api"
URL_TAILS = [
    
    "phdthesis"
]

def main():
    #read dataframe
    pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", "keywords.csv")
    df = pd.read_csv(pwd)
    #get Top ten keywords
    top10 = df.nlargest(10, "occurence")
    print(top10)
    splitFile(top10)
    
def splitFile(top10):
    for row in tqdm(range(len(top10))):
        keyword = top10.iloc[row,0]
        pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", f"{keyword}.csv")
        #Get Occurences-ID from db (TypeOfResource, id)
        keywordIds = []
        for tail in URL_TAILS:
            ids = getId(keyword, tail)
            for _id in ids:
                keywordIds.append((tail, _id))
        #saveFile
        saveFile(keywordIds,pwd)

def getId(keyword, tail):

    payload = {"keyword":keyword}
    headers = {"Content-Type": "application/json"}

    response = requests.get(f"{URL}/{tail}/10", headers=headers, json=payload)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    else:
        print(response.status_code)

def saveFile(payload,path, header="table,id"):
    with open(path, "w", encoding="utf-8") as file:
        file.write(header)
        for item in payload:
            file.write(f"\n{item[0]},{item[1]}")


if __name__ == "__main__":
    main()