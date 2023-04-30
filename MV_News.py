
# GoogleNews1.6.5 python lib is used ***
# Reference from: https://pypi.org/project/GoogleNews/ ***

# To prevent from blocking IP, run the program in parts. Tetsed with 50 parameters(input compnanies)***

from GoogleNews import GoogleNews
googlenews = GoogleNews()
import time
import gspread

credentials = {
  "type": "service_account",
  "project_id": "newsscraper-367610",
  "private_key_id": "8e3313f883ed4e319db32e10826497fdddef52f5",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCq+F6SUwEqwmEj\nsssVMf9JyJSFNOTGqVMgKKjr2rzkQVz+O2HBIUq5JVSQVia8G8Uy7qyV5NR//Xeu\nHeQBechC+VHeODONUhwgLk81Lcs+0TWr3G4uyLqNw0cXx8Yx3R064YTbD8BP87Jf\nIaLZ3FYyXz0GbnGiU155Tbz/aK5JDYUpPlmE7dp+3RYF6yG4pQ2M35MnIPSOZUd9\nPnonM1S13fFh9kGj6JfaFSWT3bpYLjTm88m8Y2rBbFUoAGr0jc6Cp8MeWKx6kRva\nNQ0J1shO5VqagdEJn5ogDdcsOM94jbTL6PLDdhJICjhuRmzvkjHXjE3QfvVRjy/l\nPcIQj4OdAgMBAAECggEAJTvxlrLqjGYoUya3WT6Z/zbmd4sxLr3GG3kXbsQkwp4k\nkz6Z975ZIHDLlaKZjXqLzB+UKRHcoKIyLBKY6yRbU5CqPnflbEffVbfYKrf2LVBR\nPMRFH725+TE33Ks2k/n4iW//Z9jqlE75wAOajJFSmWZJ60pmx4gaCVd/i21AFar3\nkuqOnvLm1sIJI6CfgsoB0r4T0up1FyUxHBe/h4hegsYJvt1BP64YrLsPa3w70FpR\nBqe+3xnozPy6SbpRLRan8SX2tsO9haYYuPpl7W5df1etEQWCxhjHW7UM5Pa44OaE\nK7KUrzpKeo2bcXnaFHKe0yQqBjNL9HiGQe5bnEUUYQKBgQDedEHfadGv2I1pi7at\nUHITQzIUL9Cp/5ti6KQd266dCDOhNy/TW/4TuEmc2AlUv9b1H+aPbfYybt5AEdNM\n3CMmlUR1eG8JFsZkZMuZ2I8K15adHOWb+Dv+5b5l/eECoaxq8D1ab3B0DwqzBazW\nxo7SXbaWlrUUC0wWZ4+bkUT5PQKBgQDEwJj+JMlHJJ7ouhSLKShDYxmFPm9Vl1pG\nfVC1Ho74xomcSTHuCacvmx3GEzCmthA5QPSHbjxvYlxgQiQB9aQlSrwF6Y9lS+F0\nAy2W3u32Gua4a40r4M2iCzc9YXx10uVE4sp85xBhb1bKRyXiFD+TXq3z2AREzE4E\nx6JLM5eZ4QKBgQCLOMdhQ6DwJN+cBsy1e3tpgsx8xdAaFNby+BZ+eVa3AMMPSrKr\n3Q8O2G95sdtlJwspLmXlrjQ/LBP8lSthFwUIyLKnslALqC1R96NVDau4ZWTlv4gU\nLS+fP7oBqvp/4x89bk13o/cFK8TOdebOJEaOcggsBvYdLVTZUMcX3bsFIQKBgDQU\nEqr6i7hkDhfl4TgwjbLAkWm+a/PI2yFbXDiEvS1GR/hxO2EZdwJX2ZqrS65k9Ihj\nFBag7ChDbdYgy60lGuywCnK6LrWOTz/I85FCstP4rOdVuIlLuMJSm62Il0wMpZkF\nOrmy45gWw29JQ9LCr01Pu1WW8RJQzbngKaokHtWhAoGARDPEY2hI4G+gZxWZsRRx\nZC1VNN7s9i3GtH9Wd9Uu8l+SChyM/DlYSSVV8gB+u2Ej+39n0raocH5690ecxq3B\n6h4xJHucUnVtAgb3Q2sxR8gmRWHmL9uPs23icU2z848jXFm7yckG3bO7NWZVAAUY\nWWKZE+Hdfe3nUudeXxgMfQ8=\n-----END PRIVATE KEY-----\n",
  "client_email": "newsscraper@newsscraper-367610.iam.gserviceaccount.com",
  "client_id": "108256613622716515423",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/newsscraper%40newsscraper-367610.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(credentials)


open_sheet = gc.open('Daily News')
sh= open_sheet.worksheet('News Stream')
sh1 = open_sheet.worksheet('Sheet9')
# sh.batch_clear(['A2:F1000'])

googlenews = GoogleNews(lang='en', region='IN')

# Optional choose period #
googlenews = GoogleNews(period='5d')
#googlenews = GoogleNews(start='09/10/2022',end='10/10/2022')


company_list= sh1.col_values(2)
symbol_list = sh1.col_values(1)
date_list =  sh1.col_values(3)
type_list = sh1.col_values(5)
group_list = sh1.col_values(6)
tradingview_list = sh1.col_values(8)
peaker_list = sh1.col_values(9)



for i, company in enumerate (company_list[:85]):
# for i, company in enumerate (company_list[86:170],86):
# for i, company in enumerate (company_list[171:250],171):
# for i, company in enumerate (company_list[251:330],251):
# for i, company in enumerate (company_list[331:420],331):
    # Clear result list before doing another search with the same object
    googlenews.clear()
    #googlenews.get_news(i)
    time.sleep(1)
    name = company
    symbol = symbol_list[i]
    date = date_list[i]
    types =  type_list[i]
    group = group_list[i]
    tradingview = tradingview_list[i]
    peaker = peaker_list[i]

    googlenews.search(name)


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
        values=[n['title'],n['date'],n['media'],n['link'],str(n['datetime']),symbol,name,date,types,group,tradingview,peaker]
        if values[4]!="None" and len(values[4])>20:
            if values[1] not in ('1 month ago', '4 weeks ago','3 weeks ago','2 weeks ago','1 week ago' ):
                temp.append(values)

        # for m in media:
        #     if values[2]==m:
        #         if values[4]!="None" and values[1] not in ('1 month ago', '4 weeks ago','3 weeks ago','2 weeks ago','1 week ago' ):
        #             temp.append(values)

#     print(temp)
#     print(index)
#     sh.append_rows(temp,insert_data_option='INSERT_ROWS')
#     sh.insert_rows(temp)
    sh.append_rows(temp,table_range='A1:A')
