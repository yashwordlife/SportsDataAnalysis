import requests
from bs4 import BeautifulSoup

topic = "soccer"
#Change topic according to the subtopic
url_file = open(topic,"r")
cnt = 0
for url in url_file:
    output = open("../Data/NYT/soccer/soccernyt" + str(cnt),"w+")
    url.replace("https://","http://")
    print url
    article = requests.get(url.strip())
    soup = BeautifulSoup(article.content, 'html5lib')
    for p in soup.find_all("p"):
        print p.get_text()
        if (p.get_text() != 'Advertisement'):
            output.write(p.get_text().encode('ascii', 'ignore').decode('ascii'))
            output.write("\n")
url_file.close()