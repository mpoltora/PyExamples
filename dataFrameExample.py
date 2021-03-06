# General syntax to import specific functions in a library:
##from (library) import (specific library function)

import sys  # only needed to determine Python version number

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import pandas as pd  # this is how I usually import pandas

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

Location = "./BLPAPI_Data.csv"

'''
df = pd.io.parsers.read_csv(Location, header=[0,1], parse_dates=[['Security'],['Field']])

print df.dtypes

print df[0:5]

'''
df = pd.read_csv(Location, parse_dates=['Security'])
#df.rename(columns = {'Security':'Date'}, inplace=True)
#df.interpolate(method='linear', axis=0, inplace=True)
print (df[0:30])
print("")



print (df.dtypes)
print("")

mavg = df['10_MA'] = df['MXUS Index'].rolling(window=10, min_periods=10, center=False).mean()
df['10_MA'].tail()
print (df[0:60])
print("")

mavg = df['30_MA'] = df['MXUS Index'].rolling(window=20,min_periods=20,center=False).mean()
df['30_MA'].tail()
print (df[0:30])
