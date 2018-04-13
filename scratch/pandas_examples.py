import pandas_datareader.data as web
from datetime import datetime

start = datetime(2017, 4, 12)
end = datetime(2018, 4, 12)

nok = web.DataReader('nok', 'morningstar', start, end)

# diff(args ==> period); If period = 'n' Gives a difference with respect to nth previous index value for every index in a series
nok['Close'].diff(1)

# For rolling mean over a period window
import pandas
pandas.rolling_mean(nok['Close'],2)['nok']['2018-04-12']

# For average
nok["Close"]["nok"].mean()

#For High
nok["Close"]["nok"].max()

#For Min
nok["Close"]["nok"].min()

#For Median
nok["Close"]["nok"].median()

