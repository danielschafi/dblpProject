import requests
import json
from aufgabe21 import getKeywords
from tqdm import tqdm

class Author():

    URL = "http://127.0.0.1:5000/api/"
    #Itteration throug all Resources | currently only PHD
    PUBLICATION_TAILS = [
        ("phdthesisauthorlist", "phdthesis")
    ]

    def __init__(self, _id):
        self._id = _id
        self.name = ""
        self.orcid = ""
        #publications (PUBLICATION_TAIL_INDEX, ID)
        self.publications = []
        self.keywords = []
        self.getAttribute()
        self.getPublications()

    def getAttribute(self):
        attribs = None
        payload = {"ph":"placeholder"}
        headers = {"Content-Type": "application/json"}
        data = requests.get(f"{self.URL}/author/{self._id}",
                        headers=headers,
                        json=payload)
        if data.status_code == 200:
            attribs = json.loads(data.content)
            attribs = attribs.get(f"{self._id}")
            if attribs:
                self.name = attribs.get("name")
                self.orcid = attribs.get("orcid")

    def getPublications(self):
        payload = {"authorId":self._id}
        headers = {"Content-Type": "application/json"}
        for tail in self.PUBLICATION_TAILS:
            response = requests.get(f"{self.URL}/{tail[0]}/{self._id}",
                            headers=headers,
                            json=payload)
            if response.status_code == 200:
                data = json.loads(response.content)
                for row in data:
                    pubId = next(iter(row))
                    self.publications.append((tail,pubId[0]))
                    self.addKeywords(row, pubId[0], tail)
        self.keywords = list(set(self.keywords))
            

    def addKeywords(self, publication, pubId, tail):
        #get the publication itself from publication object
        pubId = next(iter(publication))
        data = publication.get(pubId)
        if data:
            data = data.get(tail[1])
            dataId = next(iter(data))
            title = data.get(dataId).get("title")
            #get Keywords same way as in aufgabe21
            titleKeywords = getKeywords(title)
            for keyword in titleKeywords:
                self.keywords.append(keyword)
        else:
            print(publication)
            print(pubId)
            input("go?")
        


def main():
    NUMBER_OF_AUTHORS = 1000

    author = Author(3)
    print(f"Author:\t{author.name}")
    print(f"Orcid:\t{author.orcid}")
    print(f"Keywords:\t{author.keywords}")
    print(f"PublicationsIds:\n{author.publications}")
    mostPublications = []
    mostKeywords = []
    for i in tqdm(range(NUMBER_OF_AUTHORS)):
        author = Author(i)

        numberOfKeywords = len(author.keywords)
        if len(mostKeywords) < 10:
            mostKeywords.append((i, len(author.keywords)))
        elif numberOfKeywords > mostKeywords[9][1]:
            mostKeywords[9] = (i, len(author.keywords))
            mostKeywords = sorted(mostKeywords, key=lambda x: x[1], reverse=True)

        numberOfPublications = len(author.publications)
        if len(mostPublications) < 10:
            mostPublications.append((i, len(author.publications)))
        elif numberOfPublications > mostPublications[9][1]:
            mostPublications[9] = (i, len(author.publications))
            mostPublications = sorted(mostPublications, key=lambda x: x[1], reverse=True)

    print(mostKeywords)
    print(mostPublications)

if __name__ == "__main__":
    main()

