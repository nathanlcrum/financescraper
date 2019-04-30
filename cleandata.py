
import pandas as pd
from io import StringIO
from datetime import datetime
from csv import writer
import re

#TODO:
# handle empty values


def turnmillionsandbillions(y):

    x = re.split('(M|B)', y)
    num = float(x[0])
    letter = x[1]

    if letter == 'M':
        num *= 1000000
    elif letter == 'B':
        num *= 1000000000

    return num


def cleanpercent(z):

    per = re.split('%', z)
    return float(per[0])/100


def main():

    df = pd.read_csv('sp1500data.csv')

    #df[] is a series and uses apply
    #df[[]] is a dataframe and uses applymap

    # clean up millions and billions
    df['Shares Outstanding'] = df['Shares Outstanding'].apply(lambda x: turnmillionsandbillions(x))
    df['Market Cap'] = df['Market Cap'].apply(lambda x: turnmillionsandbillions(x))

    # clean up percents
    df['Expected Growth - 5 Year'] = df['Expected Growth - 5 Year'].apply(lambda x: cleanpercent(x))
    df['Last 12 Month Return'] = df['Last 12 Month Return'].apply(lambda x: cleanpercent(x))

    print(df)


if True:
    main()


