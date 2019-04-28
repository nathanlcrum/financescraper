
import pandas as pd
from io import StringIO
from datetime import datetime
from csv import writer
import re

#TODO:



def main():

    year = datetime.now().year
    output = StringIO()
    csv_writer = writer(output)

    sp1500 = pd.read_csv('sp1500list.csv', index_col=0) #make sure you dont have a duplicate index
    sp1500symbols = sp1500[['Symbol']].applymap(lambda x: re.sub("[.]", '-', str(x)))  # get the symbols for searching on yahoo finance

    urlbase = 'https://finance.yahoo.com/quote/'
    columns = ['Ticker', 'Price', 'Shares Outstanding', 'Market Cap', 'Expected Growth - 5 Year',
               'Last 12 Month Return', 'Beta', 'Avg Current Estimate']
    csv_writer.writerow(columns)

    for index, row in sp1500symbols.iterrows():
        symbol = row['Symbol']
        print('Index: ' + str(index) + ' Symbol: ' + symbol)

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

            try:
                # read analysis url
                adata = pd.read_html(urla)
                avgcurrest = adata[0]['Current Year (' + str(year) + ')'][1]  # get the current year
                expectedepsfiveyear = adata[5][symbol][4]
            except KeyError:
                avgcurrest = adata[0]['Current Year (' + str(year+1) + ')'][1]  # get the current year +1 cuz yahoo is messed up

        except (ValueError, KeyError, IndexError) as e:
            print(str(e) + ' with ' + symbol)

        # write to csv_writer
        stocklist = [symbol, price, sharesos, marketcap, expectedepsfiveyear, twelvemonthreturn, beta, avgcurrest]
        csv_writer.writerow(stocklist)

    # combine df and sp1500 for your final thingy
    output.seek(0)
    df = pd.read_csv(output)
    sp1500 = pd.concat([sp1500, df], axis=1, join='inner')  # join and merge the two dataframes
    sp1500.to_csv('sp1500data.csv')
    print("Success")


if __name__ == "__main__":
    main()


