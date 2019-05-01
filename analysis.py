
import pandas as pd
import numpy as np

import re


#TODO
# calculate all of the fields that rick wants
# put them in excel

rf = .024 # assumptions of the market
mrp = .062
newcolumns = ['Equity COC', 'PVEPS', 'EPS1', 'EPS2', 'EPS3', 'EPS4', 'EPS5', 'Known Growth', 'Unknown Growth',
              '% Present', '% Known', '% Unknown']


def npv(series):
    return np.npv(float(series['Equity COC']), [series['EPS1'], series['EPS2'],
                                                series['EPS3'], series['EPS4'], series['EPS5']])


def main():

    # read in the clean data csv
    df = pd.read_csv('sp1500clean.csv')
    df = df.replace('-', pd.np.nan).dropna(axis=0, how='any')

    df[newcolumns[0]] = df['Beta'].apply(lambda x: rf+(float(x)*mrp)) # do Equity COC
    df[newcolumns[1]] = pd.to_numeric(df['Avg Current Estimate'])/pd.to_numeric(df['Equity COC']) #calc PVEPS
    df[newcolumns[2]] = (pd.to_numeric(df['Expected Growth - 5 Year'])+1)* pd.to_numeric(df['EPS'])
    df[newcolumns[3]] = (pd.to_numeric(df['Expected Growth - 5 Year'])+1)* pd.to_numeric(df['EPS1'])
    df[newcolumns[4]] = (pd.to_numeric(df['Expected Growth - 5 Year'])+1)* pd.to_numeric(df['EPS2'])
    df[newcolumns[5]] = (pd.to_numeric(df['Expected Growth - 5 Year'])+1)* pd.to_numeric(df['EPS3'])
    df[newcolumns[6]] = (pd.to_numeric(df['Expected Growth - 5 Year'])+1)* pd.to_numeric(df['EPS4'])
    df[newcolumns[7]] = df.apply(lambda x: npv(x), axis=1)  #this is hard to calculate npv
    df[newcolumns[8]] = pd.to_numeric(df['Price']) - pd.to_numeric(df['PVEPS']) - pd.to_numeric(df['Known Growth'])
    df[newcolumns[9]] = 100 * pd.to_numeric(df['PVEPS'])/pd.to_numeric(df['Price'])
    df[newcolumns[10]] = 100 * pd.to_numeric(df['Known Growth'])/pd.to_numeric(df['Price'])
    df[newcolumns[11]] = 100 * pd.to_numeric(df['Unknown Growth'])/pd.to_numeric(df['Price'])

    df.to_csv('sp1500analyzed.csv')


if True:
    main()
