import lxml.etree as etree
import json
from getDBRelation import *
import parseElement as par
import requests
from numba import jit
import multiprocessing as mp
import tqdm


url = "http://127.0.0.1:5000/api"


def parseElement(args):
    config, i = args
    element = config.elements[i]
    element = etree.fromstring(element)
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

def parseXML(config):
    counter = 0
    pool = mp.Pool()
    tasks = []
    elements= []
    #do a loading bar with tqdm
    for event, element in etree.iterparse("testData.xml", dtd_validation=True):
        if event == "end":
            tasks.append((config, counter))
            elements.append(etree.tostring(element, encoding='utf8', method='xml'))
            counter += 1
    config.elements = elements
    for _ in tqdm.tqdm(pool.imap_unordered(parseElement, tasks), total=len(tasks)):
        pass

if __name__ == "__main__":
    manager = mp.Manager()
    config = manager.Namespace()
    config.elements = []
    parseXML(config)
