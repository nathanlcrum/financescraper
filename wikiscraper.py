import pandas as pd


def get_sp_1500():

    sp500url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_Component_Stocks'
    sp1000url = 'https://en.wikipedia.org/wiki/List_of_S%26P_1000_companies'

    sp500 = pd.read_html(sp500url)  # list of dataframes from the url
    sp500 = sp500[0]  # the correct table is the first table in the list of dataframes

    sp1000 = pd.read_html(sp1000url)
    sp1000 = sp1000[3]  # the fourth table on the sp1000 wiki url

    sp500 = sp500[['Security', 'Symbol', 'GICS Sector', 'GICS Sub Industry']]  # extract the relevant stockinfo
    sp1000 = sp1000[['Company', 'Ticker Symbol', 'GICS Economic Sector', 'GICS Sub-Industry']]
    sp1000.rename(inplace=True, columns={'Company': 'Security', 'Ticker Symbol': 'Symbol',
                                         'GICS Economic Sector': 'GICS Sector', 'GICS Sub-Industry': 'GICS Sub Industry'})

    sp1500 = sp500.append(sp1000)
    sp1500.reset_index(inplace=True, drop=True)

    sp1500.to_csv('sp1500list.csv')

    return sp1500

# sp1500symbols = sp1500[['Symbol']] #get the symbols for searching on yahoo finance


if __name__ == "__main__":
    get_sp_1500()






