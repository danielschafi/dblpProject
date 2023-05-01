import requests
import json

url = "127.0.0.1:5000/api"



def getJournalID(journal):
    # TODO endpoint doesen't exist yet to get by journalName /journal/(str)
    response = requests.get(f"{url}/journal/{journal[0]}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None

def createJournal(journal):
    response = requests.post(url+"/journal/1", journal)
    return response.status_code
        
def getAuthorID(author):
    response = requests.get(f"{url}/author/{author}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None

def createAuthor(author):
    response = requests.post(url+"/author/1", author)
    return response.status_code