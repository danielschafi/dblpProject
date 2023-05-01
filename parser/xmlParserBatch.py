import lxml.etree as etree
import json
from getDBRelation import *
import parseElement as par
import requests

url = "127.0.0.1:5000/api/"



"""
These get inserted as they are found
- journal
- author

"""


for event, element in etree.iterparse("testData.xml", dtd_validation=True):
    if event == "end":
        if element.tag == "article":
            par.parseArticle(element)
            
            
            """
                "ee" : element.find("ee").text,
                "authors" : element.findall("author"),
            """
            
            