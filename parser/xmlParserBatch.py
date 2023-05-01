import lxml.etree as etree
import json
from getDBRelation import *
import parseElement as par
import requests

url = "127.0.0.1:5000/api/"
threshold = 1000


articleList = []
authorList = []

"""
These get inserted as they are found
- journal
- author

"""


for event, element in etree.iterparse("testData.xml", dtd_validation=True):
    if event == "end":
        if element.tag == "article":
            articleDict = par.parseArticle(element)
            articleList.append(articleDict)
            
            """
                "ee" : element.find("ee").text,
                "authors" : element.findall("author"),
            """
            
            
            
            if len(articleList) > threshold:
                articleList.clear()
                #articleList = 
                
                # TODO postRequest with batch of ArticleList
                
            
            
            
# When iterator is finished with xml, post the rest of the data

# TODO postRequests with all lists that are not empty

    
        
        
        
        
print(json.dumps(articleList))