
import pandas as pd
from datetime import datetime
import numpy as np


#TODO: check for  periods and change to dashes
# check for 2020 as well


def main():

    year = str(datetime.now().year)

    sp1500 = pd.read_csv('sp1500list.csv')
    sp1500symbols = sp1500[['Symbol']]  # get the symbols for searching on yahoo finance

    urlbase = 'https://finance.yahoo.com/quote/'
    columns = ['Ticker', 'Price', 'Shares Outstanding', 'Market Cap', 'Expected Growth - 5 Year',
               'Last 12 Month Return',
               'Beta', 'Avg Current Estimate']
    df = pd.DataFrame(index=np.arange(1510), columns=columns)

    for index, row in sp1500symbols.iterrows():
        symbol = row['Symbol']
        print(symbol + str(index))

        urlmain = urlbase + symbol + '?p=' + symbol
        urlstats = urlbase + symbol + '/key-statistics?p=' + symbol
        urla = urlbase + symbol + '/analysis?p=' + symbol

        na = 'N/A'
        expectedepsfiveyear = na
        avgcurrest = na
        beta = na
        price = na
        marketcap = na
        twelvemonthreturn = na
        sharesos = na

        try:
            # read home url and get price and marketcap
            maindata = pd.read_html(urlmain)
            price = maindata[0][1][1]  # open price of the day
            marketcap = maindata[1][1][0]

            # read stats url
            statdata = pd.read_html(urlstats)
            beta = statdata[7][1][0]
            twelvemonthreturn = statdata[7][1][1]
            sharesos = statdata[8][1][2]

            # read analysis url
            adata = pd.read_html(urla)
            avgcurrest = adata[0]['Current Year (' + year + ')'][1]  # get the current year
            expectedepsfiveyear = adata[5][symbol][4]  # need to replace the HOG with the ticker symbol here

        except (ValueError, KeyError, IndexError) as e:
            print(str(e) + ' with ' + symbol)

        # append to some dataframe
        stocklist = [symbol, price, sharesos, marketcap, expectedepsfiveyear, twelvemonthreturn, beta, avgcurrest]
        df.loc[index] = stocklist

    # combine df and sp1500 for your final thingy
    sp1500 = pd.concat([sp1500, df], axis=1, join='inner')  # join and merge the two dataframes
    sp1500.to_csv('sp1500data.csv')


if __name__ == "__main__":
    main()


