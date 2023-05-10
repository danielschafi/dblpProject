import os
#How many dataPoints are searched. Be carefull with this...
NUMBER_OF_DATA=500
TEST_dict={
    "Hello": 500,
    "watchMe": 219,
    "corrupte": 121
}
def main():
    keywordSearch = {}
    #get entry in masterthesis
    #get keywords in masterthesis
    #add keyword to keywordSearch or
    #increas counter, if keyword already in dict
    #write to file
    writeToFile(TEST_dict)

def writeToFile(payload: dict, path="keywords.csv", header="keyword,occurence"):
    #payload is a dict with key=keyword and value=occurence of keyword
    pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", path)
    with open(pwd, "w",encoding="utf-8") as file:
        file.write(header)
        for key, value in payload.items():
            file.write(f"\n{key},{value}")



if __name__ == "__main__":
    main()