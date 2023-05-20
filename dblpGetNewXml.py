from urllib.request import urlretrieve
import xml_split
import shutil
import os
import gzip
import sys
# import parser
sys.path.insert(0, "parser")
import xmlParser as dblpParser
import logging

logging.basicConfig(level=logging.INFO,  # Set the minimum level for log messages
                    format='%(asctime)s - %(levelname)s - %(message)s')  # Define the log format
logger = logging.getLogger(__name__)


# Remove old files
outputDir = "newData"
outputDirChunks = f"{outputDir}/xml_chunks"

if os.path.exists(outputDir):
    shutil.rmtree(outputDir)

logger.info(f"Old files and directory removed from directory: {outputDir}")

# Create destination folders
if not os.path.exists(outputDirChunks):
    os.makedirs(outputDirChunks)

else:
    exit()
 
logger.info(f"Folders for new Data created: {outputDirChunks}")




# dblp.dtd
dtdUrl = "https://dblp.org/xml/dblp.dtd"
dtdDest = f"{outputDir}/dblp.dtd"

# dblp.xml.gz
dblpgzUrl = "https://dblp.org/xml/dblp.xml.gz"
dblpgzDest = f"{outputDir}/dblp.xml.gz"



# get files from url
logger.info("dblp.dtd started download")
urlretrieve(dtdUrl, dtdDest)
logger.info("dblp.dtd finished download")

logger.info("dblp.xml.gz started download")
urlretrieve(dblpgzUrl, dblpgzDest)
logger.info("dblp.xml.gz finished download")


logger.info("dblp.xml.gz file start unzipping")
#unzip .gz file
dblpDest = f"{outputDir}/dblp.xml"
buffer_size = 4096

with gzip.open(dblpgzDest, 'rb') as gz_file:
    with open(dblpDest, 'wb') as xml_file:
        shutil.copyfileobj(gz_file, xml_file, length=buffer_size)

logger.info("dblp.xml.gz file finished unzipping")



logger.info("started parsing dblp.xml and inserting into database")
# Parse, insert into database
dblpParser.parseXML(dblpDest)

logger.info("finished parsing dblp.xml and inserting into database")
