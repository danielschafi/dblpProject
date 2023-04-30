import lxml.etree as etree
import psycopg2
from getDBRelation import getJournalID


conn = psycopg2.connect("dbname=dblp user=postgres password=Sahana15! host=localhost port=5432")
cur = conn.cursor()


for event, element in etree.iterparse("testData.xml",dtd_validation=True):
    if event == "end" and element.tag == "article":
        title = element.find("title").text
        pages = element.find("pages").text
        year = element.find("year").text
        volume = element.find("volume").text
        journal = element.find("journal").text
        if getJournalID(journal) != None:
            journalID = getJournalID(journal)
        else:
            insertJournal = "INSERT INTO journal (name) VALUES (%s)"
            cur.execute(insertJournal,(journal,))
            conn.commit()
            journalID = getJournalID(journal)

        
        number = element.find("number").text
        ee = element.find("ee").text
        url = element.find("url").text
        year = element.find("year").text
        authors = element.findall("author")