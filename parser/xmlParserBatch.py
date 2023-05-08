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


def parseElement(element):
    if element.tag == "article":
        par.parseArticle(element)
    elif element.tag == "inproceedings":
        par.parseInproceedings(element)
    elif element.tag == "proceedings":
        par.parseProceedings(element)
    elif element.tag == "book":
        par.parseBook(element)
    elif element.tag == "incollection":
        par.parseIncollection(element)
    elif element.tag == "phdthesis":
        par.parsePhdthesis(element)
    elif element.tag == "mastersthesis":
        par.parseMastersthesis(element)
    elif element.tag == "www":
        par.parseWww(element)
    elif element.tag == "data":
        par.parseData(element)

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