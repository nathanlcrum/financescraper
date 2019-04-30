from selectolax.parser import HTMLParser
import pandas as pd
import requests
import time
import re
import numpy as np


s = time.time()
columns = ['Symbol', 'Security', 'Sector', 'Subsector']
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_Component_Stocks'
htmlcontent = requests.get(url).text

dom = HTMLParser(htmlcontent)
table = dom.tags('table')[0]
table = HTMLParser(table.html)
th = table.tags('th')

#print(re.match('^\n(\w{3})','\nWWWX').group(1))
# for row in th:
#     #print(row.text())
#
tr = table.tags('tr')
df = pd.DataFrame(index=np.arange(1510), columns=columns)
i=0
for row in tr:
    #print(row.text())
    symbol = row.text().split('\n')[1]
    company = row.text().split('\n')[3]
    sector = row.text().split('\n')[5]
    subsector = row.text().split('\n')[6]

    #print(row.text().split('\n')[3])
    #symbol = re.match("^\n(\w{1,5}|^\n(\w{3}.\w))", row.text()).group(1)
    df.loc[i]=[symbol, company, sector, subsector]
    i+=1
print(df)

#print(table.text(separator='%%'))
#print(type(table.text()))

