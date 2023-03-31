#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creating for single time upload


# import libraries
from bs4 import BeautifulSoup
import requests
import datetime
import csv

# Connect to Website and pull in data

URL = "https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Glacier-4/dp/B00KVP76G0/ref=sr_1_1?crid=3QVNRW0MHV62N&keywords=playstation+4&qid=1680181894&sprefix=playstation+4%2Caps%2C333&sr=8-1"
Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
webpage = requests.get(URL,headers = Headers)

soup = BeautifulSoup(webpage.content,'html.parser')


# Clean up the data a little bit

title = soup.find("span", attrs={"id":'productTitle'}).text.strip()
price =soup.find("span", attrs={"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find('span', attrs={'class':'a-offscreen'}).text.strip()[1:]
rating = soup.find("span", attrs={"class":'a-icon-alt'}).text

# Create a Timestamp for your output to track when data was collected
today = datetime.date.today()

header = ['Title','Price','Rating','Date']
data = [title,price,rating,today]

with open('AmazonScrape.csv','w', newline='',encoding = 'UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(header) # use header list only in creating time.
    writer.writerow(data)


# In[52]:


#Atomating the Scarping process by defining functions


# import libraries
from bs4 import BeautifulSoup
import requests
import datetime
import csv
import time

#Combine all of the above code into one function

def price_checker():

    URL = "https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Glacier-4/dp/B00KVP76G0/ref=sr_1_1?crid=3QVNRW0MHV62N&keywords=playstation+4&qid=1680181894&sprefix=playstation+4%2Caps%2C333&sr=8-1"
    Headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    try:
        webpage = requests.get(URL,headers = Headers)
        soup = BeautifulSoup(webpage.content,'html.parser')
        title = soup.find("span", attrs={"id":'productTitle'}).text.strip()
        price =soup.find("span", attrs={"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find('span', attrs={'class':'a-offscreen'}).text.strip()[1:]
        rating = soup.find("span", attrs={"class":'a-icon-alt'}).text
        today = datetime.date.today()
        header = ['Title','Price','Rating','Date']
        data = [title,price,rating,today]
        #Now we are appending data to the csv
        with open('AmazonScrape.csv','a+', newline='',encoding = 'UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        print(e)


# In[ ]:


while (True):
    price_checker()
    time.sleep(86400) #Automatically append the price and rating for each 24 hours


# In[ ]:


# read the data from folders

import pandas as pd

df = pd.read_csv(r'C:\Users\DEV\AmazonScrape.csv')

print(df)


# In[ ]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script
import smtplib

def Send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('xxxxxxxxxxxx@gmail.com','PWDxxxxxxxxxxx')
    
    subject = "The Item you want is below $40! Now is your chance to buy!"
    body = "deva, This is the moment we have been waiting for.Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here:https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Glacier-4/dp/B00KVP76G0/ref=sr_1_1?crid=3QVNRW0MHV62N&keywords=playstation+4&qid=1680181894&sprefix=playstation+4%2Caps%2C333&sr=8-1" 
    
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('xxxxxxxxxxx@gmail.com',msg)
    

