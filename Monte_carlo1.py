""""
Importing the necessary libraries and locale to access the locale database and functionality to include currency
"""

import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_ALL, '')

"""
pv : preseent value
time_horizon: The specified time horizon in years
i : rate of return
additions : Annual addition

The savings is calculated using the loop and the mentioned formula
"""


def savings(pv, time_horizon, i, additions):
    for year in range(time_horizon):
        ending = pv * (1 + i) + additions
        print(locale.currency(ending, grouping = True))
        pv = ending


"""
Random generation of future value based on the market history. The value of Volatility and expected_return is used for the calculation 
"""

def future_value (pv, expected_return, volatility, time_horizon, annual_addition):
    print("\tReturn", "\t\tEnding Value".rjust(18))
    for year in range(time_horizon):
        market_return = np.random.normal(expected_return, volatility)
        fv = pv * (1 + market_return) + annual_addition
        print("\t{}".ljust(10).format(round(market_return, 4)),
              "\t{}".rjust(10).format(locale.currency(fv, grouping=True)))
        pv = fv

"""
Iterate multiple times to get a more representative outcome.
The first five iterations are returned to be plotted and visualized
"""

def ending_value(expected_return, volatility, time_horizon, pv, annual_investment, iterations):
    sim = DataFrame()

    for x in range(iterations):
        stream = []
        for i in range(time_horizon):
            end = round(pv * (1 + np.random.normal(expected_return, volatility)) + annual_investment, 2)

            stream.append(end)

            pv = end

        sim[x] = stream
    first_five = list(range(5))
    return sim[first_five]

"""
The mean, SD, Max and Min are calculated to provide summary statistics and describe funtion is used to calculate this
"""
def summary_statistics(s):
    sim = s
    s = s.loc[29]
    print (s.describe())

"""
The values are grouped as percentiles
"""
def percentile(s):
    p_tiles = np.percentile(s, [5, 10, 15, 25, 75, 85, 90, 95])
    for p in range(len(p_tiles)):
        l = [5, 10, 15, 25, 75, 85, 90, 95]
        print("{}%-ile: ".format(l[p]).rjust(15), "{}".format(locale.currency(p_tiles[p], grouping=True)))

"""
doctests
"""
savings(10000, 30, .07, 10000)
future_value(10000, .09, 0.18, 30, 10000)
s = ending_value(0.09, 0.18, 30, 10000, 10000, 5000)
percentile(s)
summary_statistics(s)

"""
The first five values are plotted to visualize the results
"""
print(s)
plot = plt.plot(s)
plt.show(plot)







