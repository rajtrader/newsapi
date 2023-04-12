# GoogleNews1.6.5 python lib is used ***
# Reference from: https://pypi.org/project/GoogleNews/ ***

# To prevent from blocking IP, run the program in parts. Tetsed with 50 parameters(input compnanies)***

from GoogleNews import GoogleNews
googlenews = GoogleNews()
import pandas as pd
import os
from io import StringIO
import json 
import time
import gspread 
from datetime import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def remove_punctuation_stopwords(sentence: str) -> list:
    # tokenize the sentence
    tokens=word_tokenize(sentence)
    # remove stop words
    stop_words = set(stopwords.words('english'))
    
    # remove punctuation and numbers
    words = [word for word in tokens if word.isalpha() or '-' in word]
     # remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [word for word in words if word.lower() not in stop_words ]
    
#     filtered_sentence = [word for word in tokens if word.lower() and word.isalpha() not in stop_words or '-' in word ]

    return filtered_sentence


gc = gspread.service_account(filename='newsscraper_credential.json')
open_sheet = gc.open('PD')
sh= open_sheet.worksheet('News stream PD')
sh1 = open_sheet.worksheet('PD')
sh.batch_clear(['A2:AX1000'])

googlenews = GoogleNews(lang='en', region='IN')

# Optional choose period #
googlenews = GoogleNews(period='5d')
#googlenews = GoogleNews(start='09/10/2022',end='10/10/2022')

# csv file for input parameters

#data = pd.read_csv(r'C:\Users\Lenovo\Documents\News Data\EP_3Oct.csv')
#company = data['Name'].tolist()
#company_list = ["business"]

company_list= sh1.col_values(1)
symbol_list = sh1.col_values(2)
group_list = sh1.col_values(3)
percent_list = sh1.col_values(4)
date_list =  sh1.col_values(5)
tradingview_list = sh1.col_values(6)
peaker_list = sh1.col_values(7)


#print (company_list)


for i, company in enumerate (company_list):
    # Clear result list before doing another search with the same object
    googlenews.clear()
    #googlenews.get_news(i)
    time.sleep(1)
    name = company_list[i+1]
    symbol = symbol_list[i+1]
    date = date_list[i+1]
    group = group_list[i+1]
    percent = percent_list[i+1]
    tradingview = tradingview_list[i+1]
    peaker = peaker_list[i+1]
    googlenews.search(name)
#     sh.insert_row([name],index=2)
#     sh.append_row([name],value_input_option='RAW',insert_data_option=None,table_range='A:A')
    
    news_list= googlenews.results(sort=True)
    
   # remove key from the dict, i.e. rows from from the data  
    remove_key =['desc','img']
    for n in news_list:
        for key in remove_key:
            n.pop(key)
    
            
    # append row wise values in the google sheet 
    # using a temp list to dump data before writing in the sheet to reduce API request(100 is the limit) 
    
#     print (news_list)

    temp=[]
    media = ['Business Standard', 'Moneycontrol','The Economic Times','Mint','Zee Business','IndiaInfoline','CNBCTV18.com',
             'EquityBulls.com','Inshorts','MarketScreener','The Financial Express','CNN']
    
    
    for n in news_list:
        values=[n['title'],n['date'],n['media'],n['link'],str(n['datetime']),name,symbol,date,group,percent,tradingview,peaker]
        filtered_words = remove_punctuation_stopwords(values[0])
        temp.append(values)
        values.extend(filtered_words)
#         for m in media:
#             if values[2]==m:
#                 if values[4]!="None" and values[1] not in ('1 month ago', '4 weeks ago','3 weeks ago' ):
#                     filtered_words = remove_punctuation_stopwords(values[0])
#                     temp.append(values)
#                     values.extend(filtered_words)
                    
#     print(temp)
#     print(index)
#     sh.append_rows(temp,insert_data_option='INSERT_ROWS')
#     sh.insert_rows(temp)
    sh.append_rows(temp,table_range='A1:A')
    if i==90: # terminate program at the last row to avoid out of index error#
#     if i==len(company_list)-2: # terminate program at the last row to avoid out of index error#
        break
    
