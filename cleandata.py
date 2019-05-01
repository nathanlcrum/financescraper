
import pandas as pd
import re

#TODO:
# handle empty values


def turnmillionsandbillions(y):

    if y == '-':
        return y
    if y == str(0):
        return y
    #print(y)
    x = re.split('(M|B)', str(y))
    num = float(x[0])
    letter = x[1]

    if letter == 'M':
        num *= 1000000
    else:
        num *= 1000000000

    return num


def cleanpercent(z):

    if z == '-':
        return z
    print(z)
    per = re.split('%', z)
    print(per[0])
    if per[0][0].isdigit() or per[0][0] == '-':
        return float(per[0]) / 100
    return '-'



def emptytodash(a):

    if a == 'NaN':
        a = '-'
    elif a == 'nan':
        a = '-'
    elif a == '':
        a = '-'
    elif a != a:
        a = '-'
    elif a is None:
        return '-'
    elif a == '\N{infinity}':
        a = '-'
    return a


def main():

    df = pd.read_csv('sp1500data.csv')

    #df[] is a series and uses apply
    #df[[]] is a dataframe and uses applymap

    df = df.applymap(lambda x: emptytodash(x))

    # clean up millions and billions
    df['Shares Outstanding'] = df['Shares Outstanding'].apply(lambda x: turnmillionsandbillions(x))
    df['Market Cap'] = df['Market Cap'].apply(lambda x: turnmillionsandbillions(x))

    # clean up percents
    df['Expected Growth - 5 Year'] = df['Expected Growth - 5 Year'].apply(lambda x: cleanpercent(x))
    df['Last 12 Month Return'] = df['Last 12 Month Return'].apply(lambda x: cleanpercent(x))

    df.to_csv('sp1500clean.csv')


if True:
    main()


