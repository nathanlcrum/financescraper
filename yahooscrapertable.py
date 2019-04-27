import requests
import pandas as pd
import bs4
from datetime import datetime

sp1500 = pd.read_csv('sp1500list.csv')
sp1500symbols = sp1500[['Symbol']] #get the symbols for searching on yahoo finance

print(sp1500symbols)

url = 'https://finance.yahoo.com/quote/HOG?p=HOG'

urlstats = 'https://finance.yahoo.com/quote/HOG/key-statistics?p=HOG'
urla = 'https://finance.yahoo.com/quote/HOG/analysis?p=HOG'


# read home url and get price and marketcap

hogdata = pd.read_html(url)

price = hogdata[0][1][1]  # open price of the day
marketcap = hogdata[1][1][0]


# read stats url

statdata = pd.read_html(urlstats)

beta = statdata[7][1][0]
twelvemonthreturn = statdata[7][1][1]
sharesos = statdata[8][1][2]

# read analysis url

adata = pd.read_html(urla)

avgcurrest = adata[0]['Current Year (' + str(datetime.now().year) +')'][1]  #get the current year
expectedepsfiveyear= adata[5]['HOG'][4]  # need to replace the HOG with the ticker symbol here

#print(expectedepsfiveyear)

print(adata[0])

