import requests
import pickle
from bs4 import BeautifulSoup
import pandas as pd
import re
from ipwhois import IPWhois
from ipwhois.utils import get_countries
import os


def getfile(url,proxy,fn,ext=""):
    proxies = {
    #"http": "http://211.137.39.61:8080",
    "http": proxy,
    }
    headers = {'user-agent': '5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
    try:
        r = requests.get(url,headers=headers,timeout=10, proxies=proxies)
        print(r.status_code)
        if r.status_code == requests.codes.ok:
            mycontent = r.content
            html = mycontent.decode("UTF-8")
            soup = BeautifulSoup(html,'html.parser')
            listings =  soup.find_all(class_="river-block")
            #print(listings)
            linkarray = []
            for link in listings:
                linkarray.append(link.get('data-permalink'))
            print(linkarray)
            df = pd.DataFrame(data = linkarray, columns=['Link'])
            df.to_excel('excel/' + fn + '.xlsx', index=False)
        else:
            print("Failed URL: " + url)
            return "error"
    except:
        print("Connection Failed On:" + url)
        return "error"



pagelist = [616,651,658]

# for page in reversed(range(316,614)):
#     getfile('http://techcrunch.com/startups/page/'+str(page)+'/','107.151.152.210:80','myfile'+str(page))

for page in pagelist:
    getfile('http://techcrunch.com/startups/page/'+str(page)+'/','107.151.152.210:80','myfile'+str(page))


#getfile('http://techcrunch.com/startups/page/716/','107.151.142.116:80','myfile')


