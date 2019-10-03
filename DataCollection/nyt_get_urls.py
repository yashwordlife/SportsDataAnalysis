import requests
import datetime
import time

#Set makes sure urls are unique
url_list = set()
stop = 0
prefix = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q='
end_date = datetime.date(2019,1,1)
#Change topic according to the subtopic - Cricket, NBA, NFL
topic = "cricket"
output = open(topic+"urls","a+")
for page in range(0,100):
    time.sleep(20)
    #Get the latest articles
    url = prefix +topic+'&page='+str(page)+'&sort=newest&api-key=m4L2vXs100SXvd0JBIQOFm1QmWSEAZGF&fl=response,web_url,pub_date,meta&fq=section_name:(\"Sports\")'
    reply = requests.get(url).json()
    response = requests.get(url).json()['response']
    for doc in response['docs']:
        date_strings = doc['pub_date'][0:10].split("-")
        web_url = doc['web_url']
        date_published = datetime.date(int(date_strings[0]),int(date_strings[1]),int(date_strings[2]))
        if (date_published <= end_date):
            stop = 1
            break
        url_list.add(web_url)
        output.write(web_url)
        output.write("\n")
    if stop == 1:
        break
all_urls = list(url_list)
print len(all_urls)
output.close()