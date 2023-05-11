import os
from tqdm import tqdm
import requests
import json
import nltk
#How many dataPoints are searched. Be carefull with this...
NUMBER_OF_DATA=1000
URL = "http://127.0.0.1:5000/api"
URL_TAILS = [
    
    "phdthesis"
]
TEST_dict={
    "Hello": 500,
    "watchMe": 219,
    "corrupte": 121,
    "a":45,
    "b":453,
    "c":452,
    "d":245,
    "e":435,
    "f":145,
    "g":4,
    "h":452,
    "k":451,
}

def main():
    keywordSearch = {}
    #Download files for Speech recognition
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    #get entry in masterthesis
    for i in tqdm(range(NUMBER_OF_DATA)):
        for tail in URL_TAILS:
            data = getTitle(f"{URL}/{tail}/{i}", i)
            #get keywords in masterthesis
            if data:
                keywords = getKeywords(data)
                #add keywords to keywordSearch or
                #increas counter, if keyword already in dict
                for keyword in keywords:
                    if keywordSearch.get(keyword):
                        keywordSearch[keyword] += 1
                    else:
                        keywordSearch[keyword] = 1

                
    
    
    #write to file
    writeToFile(keywordSearch)

def getKeywords(title):
    words = nltk.word_tokenize(title)
    # Tag the words with their parts of speech
    tagged_words = nltk.pos_tag(words)
    # Extract the keywords(Nouns) based on their parts of speech
    keywords = [word for word, pos in tagged_words if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
    return keywords

def getTitle(url, _id):
    #Makes Get Request to API and extracts title
    data = requests.get(url)
    payload = None
    if data.status_code == 200:
        payload = json.loads(data.content)
        payload = payload.get(f"{_id}")
        if payload:
            payload = payload.get("title")
    return payload

def writeToFile(payload: dict, path="keywords.csv", header="keyword,occurence"):
    #payload is a dict with key=keyword and value=occurence of keyword
    pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", path)
    with open(pwd, "w",encoding="utf-8") as file:
        file.write(header)
        for key, value in payload.items():
            file.write(f"\n{key},{value}")



if __name__ == "__main__":
    main()