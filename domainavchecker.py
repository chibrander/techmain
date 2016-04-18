# These code snippets use an open-source library. http://unirest.io/python

import requests
import json
import pandas as pd

domainlist = pd.read_excel("list.xlsx")
mylist = domainlist.values.tolist()
#domain = 'ctichicago.com'

def checker(domain):
    try:
        response = requests.get("https://is-domain-available.p.mashape.com/rest.php?d=" + str(domain),
          headers={
            "X-Mashape-Key": "AItwKac89apmshxQvFZIUew3JX89Lp1TZ7WRjsnh5pQ9ZMInUJD",
            "Accept": "application/json"
          }
        )
        mycontent = response.content
        html = mycontent.decode("UTF-8")
        jsonlist = json.loads(html)


        if jsonlist['status'] == "AVAILABLE":
            print(domain)
        else:
            pass
            #print(domain + "Is Not Avalable")

    except:
        print("API Error")

for d in mylist:
    checker(d)
