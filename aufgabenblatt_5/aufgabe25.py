import os
import pandas as pd
import numpy as np
import requests
import json
from tqdm import tqdm
import matplotlib.pyplot as plt

URL = "http://127.0.0.1:5000/api"
URL_TAILS = [
    
    "phdthesis"
]

def main():
    #get 100 to keywords
    #read dataframe
    pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", "keywords.csv")
    df = pd.read_csv(pwd)
    #get Top ten keywords
    top100 = df.nlargest(100, "occurence").reset_index()
    print(top100)
    #create keyword - parring
    x = np.arange(0,100)
    y = np.arange(0,100)
    numberOfOccurences = np.zeros((100,100))
    #call API for all IDs with parring
    for tail in URL_TAILS:
        for i in tqdm(x):
            for j in y:
                numberOfOccurences[i,j] += getOccurences(top100.iloc[i,1], top100.iloc[j,1], tail)
    #create plot
    barchart3D(numberOfOccurences)

def barchart3D(occurencesArray):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Define the x, y, and z coordinates for the bars
    x = np.arange(occurencesArray.shape[0])
    y = np.arange(occurencesArray.shape[1])
    xpos, ypos = np.meshgrid(x, y, indexing='ij')
    zpos = np.zeros_like(xpos)

    dx = 0.5
    dy = 0.5
    dz = occurencesArray.flatten()

    ax.bar3d(xpos.flatten(), ypos.flatten(), zpos.flatten(), dx, dy, dz)
    plt.show()


def getOccurences(keyword, keywordTwo, tail):
    payload = {"keyword":keyword,"keywordTwo":keywordTwo}
    headers = {"Content-Type": "application/json"}

    response = requests.get(f"{URL}/{tail}/10", headers=headers, json=payload)
    if response.status_code == 200:
        data = json.loads(response.content)
        return len(data)
    else:
        print(response.status_code)

if __name__ == "__main__":
    main()