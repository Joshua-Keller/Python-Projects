#!/usr/bin/env python
# coding: utf-8

# In[137]:


import requests
import pandas as pd


### Collecting User input

x = input("Would you like information on multiple stocks (yes or no): ")

###User Choice for Single Stock 
if x.lower() == 'no':
    ticker = input("Enter ticker: ")
    ticker = ticker.upper()
    print("use this api for general use: LsDZryZe1tGqOtyP4oGi10l0sclfsaLs",
          "/ Please acknolwedge that this api was merely created for this project.")
    api = input("Please enter your API: ")
   

 ####Collecting api information
    base_url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey={api}"
    response = requests.get(base_url)
    
    ###Checking Status Code 
    if response.status_code != 200:
        print("Error!")
    elif response.status_code == 200:
        ###Collecting Desired Data
        data = response.json()
        stock = data['ticker']
        info1 = data['results'][0]['vw']
        info2 = data['results'][0]['o']
        info3 = data['results'][0]['c']
        info4 = data['results'][0]['h']
        info5 = data['results'][0]['l']
        if info1 == 0 or info2 == 0 or info3 == 0 or info4 == 0 or info5 == 0:
            print(0)
        else:
            print("Stock:", stock)
            print("Information:")
            print("Vol/weigh/avg/price", info1)
            print("Opening price", info2)
            print("Closing price", info3)
            print("Highest price", info4)
            print("Lowest price", info5)
            
            
            
###User Choice for Multiple Stocks 
            
elif x== 'yes':
    print("use this api for general use: LsDZryZe1tGqOtyP4oGi10l0sclfsaLs",
          "/ Please acknolwedge that this api was merely created for this project.")
    api = input("Please enter your API: ")
    date =input("Please enter your date of choice in year-month-day format (0000-00-00): ")
    
    base_url2 = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{date}?adjusted=true&apiKey={api}"
    response2 = requests.get(base_url2)
    if response2.status_code == 200:
        Stocks_List = []
        data2 = response2.json()
        tic = data2['results']
        for i in tic:
            try:
                x = i['T']
            except:
                x = ''
            try:
                x1 = i['v']
            except:
                x1 = ''
            try:
                x2 = i['vw']
            except:
                x2 = ''
            try:
                x3 = i['o']
            except:
                x3 = ''
            try:
                x4 =i['c']
            except:
                x4 = ''
            try:
                x5 = i['h']
            except:
                x5 = ''
            try:
                x6 = i['l']
            except:
                x6 = ''
            try:
                x7 = i['n']
            except:
                x7 = ''
            info= {'Ticker': x,'Trading Volume' : x1,'Volume Weighted Avg. Price': x2,
                   'Opening Price': x3,'Closing Price': x4,'Highest Price': x5, 'Lowest Price': x6,
                   'Number of Transactions': x7}
            Stocks_List.append(info)
        ### Uploading to a csv file.           
        df = pd.DataFrame(Stocks_List)
        df.to_csv('AllStocks.csv')
        print("You now can view stock information in your files under AllStocks.csv")
        print(df.head())
    else: 
        print("I am sorry but there was an error. Please try again.")
        











