####couldnt get this to work sadly!!! span with data-reactid = 34 does not show up for some reason??


import requests
import pandas as pd
import bs4


url = 'https://finance.yahoo.com/quote/HOG?p=HOG'


def get_webpage(url):
    response = requests.get(url)  #  Get the url
    return bs4.BeautifulSoup(response.text, 'html.parser')

webpage = get_webpage(url)
spans = webpage.find_all("span")

for span in spans:
    span = str(span)
    #print(span)
    if 'data-reactid="34"' in span:
        print(span)


#print(spans)
#print(type(spans[0]))


hogdata = pd.read_html(url)

#print(hogdata[1])