from io import StringIO
from csv import writer
import pandas as pd

output = StringIO()
csv_writer = writer(output)

sp1500 = pd.read_csv('sp1500list.csv')
sp1500symbols = sp1500[['Symbol']]  # get the symbols for searching on yahoo finance


for index, row in sp1500symbols.iterrows():
    print(row['Symbol'])
    csv_writer.writerow(row)

output.seek(0)  # we need to get back to the start of the StringIO
df = pd.read_csv(output, header=None)

df.reset_index(inplace=True, drop=True)
df.to_csv('test.csv')
print(df)

