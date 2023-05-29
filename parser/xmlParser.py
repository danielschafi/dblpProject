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

def parseElement(element, year=None, limit=10, art=None):
    if year:
        startDate=f"{year}-01-01"
        endDate=f"{year}-12-31"

        
    mDate = element.get("mdate")
    if mDate is None or not (year is None or startDate <= mDate <= endDate):
        return
    
    
    if (art == "article" or art is None) and element.tag == "article" and eCounts["article"] < limit:
        par.parseArticle(element)
        eCounts["article"] +=1
        if eCounts["article"] == limit : eCounts["fullECount"] += 1
        
    elif (art == "inproceedings" or art is None) and element.tag == "inproceedings" and eCounts["inproceedings"] < limit:
        par.parseInproceedings(element)
        eCounts["inproceedings"] +=1
        if eCounts["inproceedings"] == limit : eCounts["fullECount"] += 1

    elif (art == "proceedings" or art is None) and element.tag == "proceedings" and eCounts["proceedings"] < limit:
        par.parseProceedings(element)
        eCounts["proceedings"] +=1
        if eCounts["proceedings"] == limit : eCounts["fullECount"] += 1

    elif (art == "book" or art is None) and element.tag == "book" and eCounts["book"] < limit:
        par.parseBook(element)
        eCounts["book"] +=1
        if eCounts["book"] == limit : eCounts["fullECount"] += 1
        
    elif (art == "incollection" or art is None) and element.tag == "incollection" and eCounts["incollection"] < limit:
        par.parseIncollection(element)
        eCounts["incollection"] +=1
        if eCounts["incollection"] == limit : eCounts["fullECount"] += 1
        
    elif (art == "phdthesis" or art is None) and element.tag == "phdthesis" and eCounts["phdthesis"] < limit:
        par.parsePhdthesis(element)
        eCounts["phdthesis"] +=1
        if eCounts["phdthesis"] == limit : eCounts["fullECount"] += 1
        
    elif (art == "mastersthesis" or art is None) and element.tag == "mastersthesis" and eCounts["mastersthesis"] < limit:
        par.parseMastersthesis(element)
        eCounts["mastersthesis"] +=1
        if eCounts["mastersthesis"] == limit : eCounts["fullECount"] += 1
        
    elif (art == "www" or art is None) and element.tag == "www" and eCounts["www"] < limit:
        par.parseWww(element)
        eCounts["www"] +=1
        if eCounts["www"] == limit : eCounts["fullECount"] += 1
        
    elif (art == "data" or art is None) and element.tag == "data" and eCounts["data"] < (min(limit, 4)):
        par.parseData(element)
        eCounts["data"] +=1
        if eCounts["data"] == (min(limit, 4)) : eCounts["fullECount"] += 1
        
    if eCounts["fullECount"]  >= len(tags) or (art is not None and eCounts["fullECount"] == 1):
        print("Parsing finished")
        exit()
        
    

def process_chunk(chunk, year=None, limit=10, art=None):
    for element in tqdm(chunk):
        parseElement(element, year, limit, art)

def parse_xml_chunkwise(xml_file_path, chunk_size, year=None, limit=10, art=None):
    
    context = etree.iterparse(xml_file_path, events=("start", "end"), dtd_validation=True, load_dtd=True)
    _, root = next(context)  # get root element

    def map_chunk_to_processes(mapped_chunk):
        process_chunk(mapped_chunk, year, limit, art)

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


def parseXML(dblpXmlPath = "dblp.xml", year=2023, limit=10, art=None):
    parse_xml_chunkwise(dblpXmlPath, 10000, year, limit, art)

if __name__ == "__main__":
    parseXML()


#TO CREATE CHUNKS DO THIS:
#run python xml_split.py -o xml_chunks -M 1024 dblp.xml