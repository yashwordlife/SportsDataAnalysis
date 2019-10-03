import gzip
import requests
import io
import json 
from StringIO import StringIO
from contextlib import closing
import gzip
import warc
import requests
from bs4 import BeautifulSoup
import re 

dataList = open("urldata/cricketUrls","w+")
listOfUrls = set()

keywords = "cricket-news"
n_rec = 0

def addValidUrls(url,urlKey):
    soup = BeautifulSoup(markup)
    links = soup.find_all('a')
    for link in links:
        href = link.attrs.get('href')
        if href is not None:
            if keyword in href and href.startswith("http"):
                dataList.write(url)
                dataList.write('\n')
    
    if (keywords in url or keywords in urlKey):
        listOfUrls.add(url)
        dataList.write(url)
        dataList.write('\n')

indices = ["2019-13","2019-09","2019-04"]
mid = "CC-MAIN-"
prefix = "http://index.commoncrawl.org/"
end = "-index?url=cricbuzz.com&matchType=domain&output=json"
records_list=[]

for index in indices:
    url = prefix+mid+index+end
    resp = requests.get(url)
    if resp.status_code == 200:
        records = resp.content.splitlines()
        for record in records:
            x = json.loads(record)
            records_list.append(x)

dataprefixUrl = "https://commoncrawl.s3.amazonaws.com/"
counter = 0
for record in records_list:
    recStartIndex = int(record['offset'])
    recLength = int(record['length'])
    recEndIndex = recStartIndex + recLength - 1
    resp = requests.get(dataprefixUrl + record['filename'], headers={'Range': 'bytes={}-{}'.format(recStartIndex, recEndIndex)})
    raw_data = StringIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)
    data = f.read()
       try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
            addValidUrls(record['url'],record['urlkey'])
        except:
            pass
    if len(listOfUrls) > 200:
        break

dataList.close()