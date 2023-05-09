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


limit = 10

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

def parseElement(element):
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
        
    

def process_chunk(chunk):
    for element in chunk:
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

def parseXML():
    # get number of xml files in xml_chunks folder
    num_xml_files = len(os.listdir("xml_chunks"))
    cores = 10

    #with mp.Pool(cores) as pool:
    #    for _ in tqdm(pool.imap_unordered(parallel_parse_xml_chunkwise, range(num_xml_files)), total=num_xml_files):
    #        pass

    ###TEST DATA
    parse_xml_chunkwise("dblp.xml", 10000)

if __name__ == "__main__":
    parseXML()


#TO CREATE CHUNKS DO THIS:
#run python xml_split.py -o xml_chunks -M 1024 dblp.xml