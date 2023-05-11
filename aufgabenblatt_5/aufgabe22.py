import matplotlib.pyplot as plt
import pandas as pd
import os

#minimum number of occurence to be displayed in plot
DF_THRESH = 20

def main():
    #read data to df
    pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", "keywords.csv")
    df = pd.read_csv(pwd)
    df = df.loc[df.occurence >= DF_THRESH]
    plt.bar(df.iloc[:,0], df.iloc[:,1])
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()