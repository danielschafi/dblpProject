import requests
import json

url = "http://127.0.0.1:5000/api"
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
         


def createJournal(journal):
    response = requests.post(url=url, data=journal, headers=headers)
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

def createArticleAuthorList(articleAuthor):
    response = requests.post(url=url+"/articleauthorlist/1/", data=articleAuthor, headers=headers)
    return response.status_code

def createArticleEeList(articleEe):
    response = requests.post(url=url+"/articleeelist/1/", data=articleEe, headers=headers)
    return response.status_code