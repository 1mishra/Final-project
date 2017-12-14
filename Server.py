import client
import random
import math
from numpy import zeros
from scipy.stats import norm
from six.moves import input
import matplotlib.pyplot as plt

client.main()
# print("Executing MCS in {} ".format(__name__))
class VanillaOption:
    def __init__(self, expiry, strike, spot, volatility, interest_rate, number_of_paths):
        #self.option_type = option_type
        self.expiry = expiry
        self.strike = strike
        self.spot = spot
        self.volatility = volatility
        self.interest_rate = interest_rate
        self.number_of_paths = number_of_paths

    def monte_carlo_pricer(self):
        variance = self.volatility * self.volatility * self.expiry
        standard_deviation = math.sqrt(variance)
        ito_correction = -0.5 * variance
        spot_changed = self.spot * math.exp(self.interest_rate * self.expiry + ito_correction)
        sum = 0
        stock_list = []
        for i in range(0, self.number_of_paths):
            normal = random.normalvariate(0, 1)
            stock_val = spot_changed * math.exp(standard_deviation * normal)
            stock_list.append(stock_val)
            sum += max(stock_val - self.strike, 0.0)
        result = sum / self.number_of_paths
        plot = plt.plot(stock_list)
        plt.show(plot)
        result *= math.exp(-self.interest_rate * self.expiry)
        return result

    def black_scholes(self):
        d_1 = math.log(self.spot / self.strike) + ((self.interest_rate + (self.volatility * self.volatility)/2) *
                self.expiry)
        d_2 = d_1 - self.volatility * math.sqrt(self.expiry)
       # if self.option_type.lower() == 'call':
        result = self.spot * norm.cdf(d_1) - self.strike * math.exp(-self.interest_rate * self.expiry) * norm.cdf(d_2)
        return result