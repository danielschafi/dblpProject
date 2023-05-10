import matplotlib.pyplot as plt
import pandas as pd
import os


def main():
    #read data to df
    pwd = os.path.join(os.getcwd(), "aufgabenblatt_5", "keywords.csv")
    df = pd.read_csv(pwd)
    plt.bar(df.iloc[:,0], df.iloc[:,1])
    plt.show()

if __name__ == "__main__":
    main()