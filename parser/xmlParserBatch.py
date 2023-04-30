import lxml.etree as etree
import psycopg2
import json
from getDBRelation import *
import requests

url = "127.0.0.1:5000/api/"
threshold = 1000


articleList = []
authorList = []


for event, element in etree.iterparse("testData.xml", dtd_validation=True):
    if event == "end" and element.tag == "article":
        
        journal = element.find("journal").text,
        journalID = getJournalID(journal)
        
        if journalID is None:
            createJournal(journal)
            journalID = getJournalID(journal)   
        
            
                
        articleDict = {
            "title" : element.find("title").text,
            "number" : element.find("number").text,
            "pages" : element.find("pages").text,
            "url" : element.find("url").text,
            "year" : element.find("year").text,
            "journalid" : journalID,
        }
        
        """
            Not needed here, these get inserted in separate table (other than volume)
            "volume" : element.find("volume").text, No volume?
            "ee" : element.find("ee").text,
            "authors" : element.findall("author"),
        """
        
        articleList.append(articleDict)
        print(json.dumps(articleList))
        
        
        if len(articleList) > threshold:
            articleList.clear()
            #articleList = 
            pass
            # TODO postRequest with batch of ArticleList
            
            
            
            
# When iterator is finished with xml, post the rest of the data

# TODO postRequests with all lists that are not empty

    
        
        
        
        
print(json.dumps(articleList))