import lxml.etree as etree
import os
import json
from getDBRelation import *
import parseElement as par
import requests
from numba import jit
import multiprocessing as mp
from tqdm import tqdm


url = "http://127.0.0.1:5000/api"

tags = ["article", "inproceedings", "proceedings", "book", "incollection", "phdthesis", "mastersthesis", "www", "data"]

# Define limits for each tag to Import
# 100 takes a time about 2:20 minutes
# 1000 takes a time about 7:30 minutes
limit = 1000

eLimits = {
    "article" : limit,
    "inproceedings" : limit,
    "proceedings" : limit,
    "book" : limit,
    "incollection" : limit,
    "phdthesis" : limit,
    "mastersthesis" : limit,
    "www" : limit,
    "data" : 4,
    }

eCounts = {
    "article" : 0,
    "inproceedings" : 0,
    "proceedings" : 0,
    "book" : 0,
    "incollection" : 0,
    "phdthesis" : 0,
    "mastersthesis" : 0,
    "www" : 0,
    "data" : 0,
    "fullECount" : 0
    }

def parseElement(element, startDate="2023-01-01", endDate="2023-12-31"):
    mDate = element.get("mDate")
    if mDate is not None and startDate <= mDate <= endDate:
        return
    if element.tag == "article" and eCounts["article"] < eLimits["article"]:
        par.parseArticle(element)
        eCounts["article"] +=1
        if eCounts["article"] == eLimits["article"] : eCounts["fullECount"] += 1
        
    elif element.tag == "inproceedings" and eCounts["inproceedings"] < eLimits["inproceedings"]:
        par.parseInproceedings(element)
        eCounts["inproceedings"] +=1
        if eCounts["inproceedings"] == eLimits["inproceedings"] : eCounts["fullECount"] += 1

    elif element.tag == "proceedings" and eCounts["proceedings"] < eLimits["proceedings"]:
        par.parseProceedings(element)
        eCounts["proceedings"] +=1
        if eCounts["proceedings"] == eLimits["proceedings"] : eCounts["fullECount"] += 1

    elif element.tag == "book" and eCounts["book"] < eLimits["book"]:
        par.parseBook(element)
        eCounts["book"] +=1
        if eCounts["book"] == eLimits["book"] : eCounts["fullECount"] += 1
        
    elif element.tag == "incollection" and eCounts["incollection"] < eLimits["incollection"]:
        par.parseIncollection(element)
        eCounts["incollection"] +=1
        if eCounts["incollection"] == eLimits["incollection"] : eCounts["fullECount"] += 1
        
    elif element.tag == "phdthesis" and eCounts["phdthesis"] < eLimits["phdthesis"]:
        par.parsePhdthesis(element)
        eCounts["phdthesis"] +=1
        if eCounts["phdthesis"] == eLimits["phdthesis"] : eCounts["fullECount"] += 1
        
    elif element.tag == "mastersthesis" and eCounts["mastersthesis"] < eLimits["mastersthesis"]:
        par.parseMastersthesis(element)
        eCounts["mastersthesis"] +=1
        if eCounts["mastersthesis"] == eLimits["mastersthesis"] : eCounts["fullECount"] += 1
        
    elif element.tag == "www" and eCounts["www"] < eLimits["www"]:
        par.parseWww(element)
        eCounts["www"] +=1
        if eCounts["www"] == eLimits["www"] : eCounts["fullECount"] += 1
        
    elif element.tag == "data" and eCounts["data"] < eLimits["data"]:
        par.parseData(element)
        eCounts["data"] +=1
        if eCounts["data"] == eLimits["data"] : eCounts["fullECount"] += 1
        
    if eCounts["fullECount"]  >= len(tags):
        print("Parsing finished")
        exit()
        
    

def process_chunk(chunk):
    for element in tqdm(chunk):
        parseElement(element)

def parse_xml_chunkwise(xml_file_path, chunk_size):
    context = etree.iterparse(xml_file_path, events=("start", "end"), dtd_validation=True, load_dtd=True)
    _, root = next(context)  # get root element

    def map_chunk_to_processes(mapped_chunk):
        process_chunk(mapped_chunk)

    chunk = []
    for event, elem in context:
        if event == "end" and elem.tag in tags:
            chunk.append(elem)

            if len(chunk) >= chunk_size:
                map_chunk_to_processes(chunk)
                root.clear()
                chunk = []

    if chunk:
            map_chunk_to_processes(chunk)

def parallel_parse_xml_chunkwise(suffix):
    parse_xml_chunkwise("xml_chunks/" + "{:04d}".format(suffix) + "/dblp.xml", 10000)
    print("part %d Done" % suffix)


def parseXML(dblpXmlPath = "dblp.xml"):
    parse_xml_chunkwise(dblpXmlPath, 10000)

if __name__ == "__main__":
    parseXML()


#TO CREATE CHUNKS DO THIS:
#run python xml_split.py -o xml_chunks -M 1024 dblp.xml