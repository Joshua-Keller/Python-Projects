#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd


# #### User Input
#user_input = int(input("What is the zipcode you are looking for? "))
user_input = 28409


#Getting Date
today = datetime.date.today()


#collecting & sorting the data

def check_zipcode():
    ###pulling information from site
    def website(page):
        url = f"https://www.realtor.com/realestateandhomes-search/{user_input}"

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"}

        page = requests.get(url, headers = headers)

        soup1 = BeautifulSoup(page.content, "html.parser")

        soup3 = BeautifulSoup(soup1.prettify(),"html.parser")

        return soup3


    def extract(soup3):
        ###Extracting desired information
        info = soup3.find_all('div',{'class':"jsx-11645185 detail-wrap fixed-wrapper-ldp-redesign has-cta"})
        for item in info:
            #summary = item.find('div',{'class': 'jsx-11645185 prop-meta'}).text.strip().replace('\n','') 
            address = item.find('div',{'class': 'jsx-11645185 address ellipsis srp-page-address srp-address-redesign'}).text.strip().replace('  ','').replace('\n','')
            price = item.find('span',{'class': 'rui__x3geed-0 kitA-dS'}).text.replace('$','')      
            try:
                beds = item.find('li',{'data-label': 'pc-meta-beds'}).text.strip()[0:26]
            except:
                beds = ''
            try:
                baths = item.find('li',{'data-label': 'pc-meta-baths'}).text.strip()[0:26]
            except:
                baths = ''
            try:
                sqrFt = item.find('li',{'data-label': 'pc-meta-sqft'}).text.strip()[0:26]
            except:
                sqrFt = ''
            try:
                acres = item.find('li',{'data-label': 'pc-meta-sqftlot'}).text.strip()[0:26]
            except:
                acres = ''

            housing = {'address': address,
                       'price': price, 
                       'beds': beds, 
                       'baths': baths,
                       'sqrFt': sqrFt,
                       'acres': acres,
                       'today': today}
            housinglist.append(housing)
        return


    housinglist = []
###Statement for range of pages (0-4)
    for i in range(0,4):
        c = website(0)
        extract(c)

    df = pd.DataFrame(housinglist)
    df.to_csv('House.csv')

   

#Automatic refreshing

while(True):
    check_zipcode()
    time.sleep(2)


