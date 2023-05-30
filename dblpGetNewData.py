from urllib.request import urlretrieve
import pandas as pd

from sqlalchemy import create_engine, text
import xml_split
import shutil
import os
import gzip
import sys
# import parser
sys.path.insert(0, "parser")
import xmlParser as dblpParser
import logging



def getData(year=None, count=10, art=None):
    
    # create a logger list
    
    
    logging.basicConfig(level=logging.INFO,  # Set the minimum level for log messages
                        format='%(asctime)s - %(levelname)s - %(message)s')  # Define the log format
    logger = logging.getLogger(__name__)


    # Remove old files
    outputDir = "newData"

    if os.path.exists(outputDir):
        shutil.rmtree(outputDir)

    loggerList = []
    loggerList.append(f"Old files and directory removed from directory: {outputDir}")
    logger.info(f"Old files and directory removed from directory: {outputDir}")

    # Create destination folders
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    else:
        exit()
    
    loggerList.append(f"Folders for new Data created: {outputDir}")
    logger.info(f"Folders for new Data created: {outputDir}")




    # dblp.dtd
    dtdUrl = "https://dblp.org/xml/dblp.dtd"
    dtdDest = f"{outputDir}/dblp.dtd"

    # dblp.xml.gz
    dblpgzUrl = "https://dblp.org/xml/dblp.xml.gz"
    dblpgzDest = f"{outputDir}/dblp.xml.gz"



    # get files from url
    loggerList.append("dblp.dtd started download")
    logger.info("dblp.dtd started download")
    urlretrieve(dtdUrl, dtdDest)
    loggerList.append("dblp.dtd finished download")
    logger.info("dblp.dtd finished download")

    loggerList.append("dblp.xml.gz started download")
    logger.info("dblp.xml.gz started download")
    urlretrieve(dblpgzUrl, dblpgzDest)
    loggerList.append("dblp.xml.gz finished download")
    logger.info("dblp.xml.gz finished download")

    loggerList.append("dblp.xml.gz file start unzipping")
    logger.info("dblp.xml.gz file start unzipping")
    #unzip .gz file
    dblpDest = f"{outputDir}/dblp.xml"
    buffer_size = 4096

    with gzip.open(dblpgzDest, 'rb') as gz_file:
        with open(dblpDest, 'wb') as xml_file:
            shutil.copyfileobj(gz_file, xml_file, length=buffer_size)

    loggerList.append("dblp.xml.gz file finished unzipping")
    logger.info("dblp.xml.gz file finished unzipping")


    loggerList.append("started parsing dblp.xml and inserting into database")
    logger.info("started parsing dblp.xml and inserting into database")
    # Parse, insert into database
    dblpParser.parseXML(dblpDest, year, count, art)
    loggerList.append("finished parsing dblp.xml and inserting into database")
    logger.info("finished parsing dblp.xml and inserting into database")
    return loggerList

def getDataCSV(year, count, art):
    loggerlist = []
    engine = create_engine('postgresql://postgres:1234@localhost/dblp')
    if art != None:
        loggerlist.append("Exporting data to csv")
        conn = engine.connect()
        query = text(f"SELECT * FROM {art} LIMIT :count".format(art))
        query = query.bindparams(count=count)
        result = conn.execute(query)
        #get all rows in datafram
        loggerlist.append("Exporting data to csv dataframe")
        df = result.fetchall()
        df = pd.DataFrame(df)
        df.columns = result.keys()
        loggerlist.append("Exporting data to csv dataframe finished")
        loggerlist.append("Exported data {} entries of type {} from year {}".format(count, art, year))
        return df, loggerlist
            
    return None
            
   