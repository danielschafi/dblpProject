import requests
import json

url = "127.0.0.1:5000/api"
headers = {'Content-type': 'application/json'}


#TODO: create get methods for all endpoints
def getJournalID(journal):
    # TODO endpoint doesen't exist yet to get by journalName /journal/(str)
    response = requests.get(f"{url}/journal/{journal[0]}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None
         
def getAuthorID(author):
    response = requests.get(f"{url}/author/{author}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None
    
def getPublisherID(publisher):
    response = requests.get(f"{url}/publisher/{publisher}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None
    
def getCiteID(cite):
    response = requests.get(f"{url}/cite/{cite}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None
    
def getEeID(ee):
    response = requests.get(f"{url}/ee/{ee}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None

def getEeType(ee):
    response = requests.get(f"{url}/ee/{ee}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None

def getSchoolID(school):
    response = requests.get(f"{url}/school/{school}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None
    
def getEditorID(editor):
    response = requests.get(f"{url}/editor/{editor}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['name']
    else:
        return None


# TODO: create post methods for all endpoints
def createJournal(journal):
    response = requests.post(url=url+"/journal/1/", data=journal, headers=headers)
    return response.status_code

def createPublisher(publisher):
    response = requests.post(url=url+"/publisher/1/", data=publisher, headers=headers)
    return response.status_code

def createAuthor(author):
    response = requests.post(url=url+"/author/1/", data=author, headers=headers)
    return response.status_code

def createCite(cite):
    response = requests.post(url=url+"/cite/1/", data=cite, headers=headers)
    return response.status_code

def createEe(ee):
    response = requests.post(url=url+"/ee/1/", data=ee, headers=headers)
    return response.status_code

def createSchool(school):
    response = requests.post(url=url+"/school/1/", data=school, headers=headers)
    return response.status_code

def createEditor(editor):
    response = requests.post(url=url+"/editor/1/", data=editor, headers=headers)
    return response.status_code

def createArticle(article):
    response = requests.post(url=url+"/article/1/", data=article, headers=headers)
    return response.status_code
