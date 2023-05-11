import pandas as pd
import os

def main():
    #read dataframe
    pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", "keywords.csv")
    df = pd.read_csv(pwd)
    #get Top ten keywords
    top10 = df.nlargest(10, "occurence")
    splitFile(top10)
    
def splitFile(top10):
    for row in range(len(top10)):
        keyword = top10.iloc[row,0]
        pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", f"{keyword}.csv")
        #Get Occurences-ID from db (TypeOfResource, id)
        ids = [("master",1),("master",2),("master",3),("phd",4)]#TODO
        #saveFile
        saveFile(ids,pwd)

def getId(keyword):
    pass

def saveFile(payload,path, header="table,id"):
    with open(path, "w", encoding="utf-8") as file:
        file.write(header)
        for item in payload:
            file.write(f"\n{item[0]},{item[1]}")


if __name__ == "__main__":
    main()