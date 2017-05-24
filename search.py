#!/usr/bin/python

################################
#Written By Ari Perez
#Search for groceries in the area
#Date: May 23, 2017
#################################

import requests, re
from bs4 import BeautifulSoup

#This should be chaned to use google maps to find local store websites
#/search/?search-bar=asdfsd\
#Walmart -->/search/item

websites = ["https://www.walmart.ca/", "https://www.loblaws.ca/", "https://www.zehrs.ca/"]
#"https://www.nofrills.ca/"
search_param = "search/?search-bar="
search_param1 = "/search/"
item = raw_input("What are you looking for: ")

cl = {'class' : re.compile('.*price.*')}


for i in websites:
    print(i)
    get_data = requests.get(i + search_param + item)
    print(get_data.cookies)
    #clean = ""

    try:
        try:
            clean = BeautifulSoup(get_data.content, "html.parser").find_all(**cl)[0].get_text()

            print (clean)
        except:
            print ("test")
            get_data = requests.get(i + search_param1 + item)
            print(get_data.content)

            clean1 = BeautifulSoup(get_data.content, "html.parser").find_all(**cl) #[0]
            print (clean1)
    except:
        print("Woops")

    '''
    try:
        #clean = BeautifulSoup(get_data.content, "html.parser").find_all(**cl)[0].get_text()
        if ('$' in clean):
            pass
        else:
            print("test")
            get_data = requests.get(i + search_param1 + item)
            clean = BeautifulSoup(get_data.content, "html.parser").find_all(**cl)[0].get_text()
        print(clean)
    except:
        print("Pass")
        pass
    '''
    get_data.connection.close()

    print("--------------------------")
