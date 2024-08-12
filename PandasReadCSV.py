'''Mini Project
Goal:
Drop script into folder/directory and use it to read basic data.
Offer user ability to perform basic statistical function on data.
Offer user visualisation of data.
'''

import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rcParams

import datetime as dt

pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("GBPUSD=X (1).csv", index_col=0)
df.index = pd.to_datetime(df.index)
#list(df.columns.values.tolist())

#Converts "Date" to a datetime object
#df["Date"] = pd.to_datetime(df["Date"])
#df.sort_values(by='Date', ascending = False, inplace = True)



Date_and_AdjClose = df[["Adj Close"]]
print(Date_and_AdjClose.head())


Date_and_AdjClose["% Change"] = Date_and_AdjClose["Adj Close"].pct_change()
Date_and_AdjClose["% Change"] = Date_and_AdjClose["% Change"].fillna(0)

print(Date_and_AdjClose.head())

#help(Date_and_AdjClose.plot)
MyPlot = Date_and_AdjClose["Adj Close"].plot(title = "GBP/USD 5 year FOREX")


MyPlot.xaxis.set_major_locator(mdates.MonthLocator(bymonth = (1,7)))
MyPlot.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
MyPlot.set_ylabel("GBP/USD Adj Close Rate")
MyPlot.legend(loc = "upper left").remove()
MyPlot.margins(x=0)

print(max(Date_and_AdjClose["% Change"]))
print(min(Date_and_AdjClose["% Change"]))

MyPlot2 = MyPlot.twinx()
MyPlot2.set_ylabel('% Change', color="orange")
MyPlot2.plot(Date_and_AdjClose["% Change"], color="orange", linewidth = 0.25)
MyPlot2.tick_params(axis="y", labelcolor="orange")
MyPlot2.margins(x=0)

rcParams['figure.figsize'] = 15, 6
plt.grid(True, linestyle = ":")
plt.show()
