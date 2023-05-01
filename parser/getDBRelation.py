import requests
import json

url = "127.0.0.1:5000/api"
headers = {'Content-type': 'application/json'}



def getJournalID(journal):
    # TODO endpoint doesen't exist yet to get by journalName /journal/(str)
    response = requests.get(f"{url}/journal/{journal[0]}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None

def createJournal(journal):
    response = requests.post(url=url+"/journal/1/", data=journal, headers=headers)
    return response.status_code
        
def getAuthorID(author):
    response = requests.get(f"{url}/author/{author}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None

def createAuthor(author):
    response = requests.post(url=url+"/author/1/", data=author, headers=headers)
    return response.status_code

def createArticle(article):
    response = requests.post(url=url+"/article/1/", data=article, headers=headers)
    return response.status_code
