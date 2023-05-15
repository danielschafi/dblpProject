from urllib.request import urlretrieve
import xml_split
import shutil
import os
import gzip
import parser.xmlParser as dblpParser
# Remove old files
outputDir = "newData"
outputDirChunks = f"{outputDir}/xml_chunks"

if os.path.exists(outputDir):
    shutil.rmtree(outputDir)

# Create destination folders
if not os.path.exists(outputDirChunks):
    os.makedirs(outputDirChunks)

else:
    exit()
 



# # dblp.dtd
dtdUrl = "https://dblp.org/xml/dblp.dtd"
dtdDest = f"{outputDir}/dblp.dtd"

# # dblp.xml.gz
dblpgzUrl = "https://dblp.org/xml/dblp.xml.gz"
dblpgzDest = f"{outputDir}/dblp.xml.gz"




# get files from url
urlretrieve(dtdUrl, dtdDest)
urlretrieve(dblpgzUrl, dblpgzDest)

#unzip .gz file
dblpDest = f"{outputDir}/dblp.xml"
buffer_size = 4096

with gzip.open(dblpgzDest, 'rb') as gz_file:
    with open(dblpDest, 'wb') as xml_file:
        shutil.copyfileobj(gz_file, xml_file, length=buffer_size)

print("File extracted successfully.")

xml_split.main(dblpDest, outputDirChunks)


#when xml split finished

# dont clear database


dblpParser.parseXML()

