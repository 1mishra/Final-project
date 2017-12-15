"""
Parameters
var: square of the standared deviation from the mean 
expiry: The period of contract
volatlity: The fluctuation of stock price
mean: mean of the stock price
strike: price at which the stocks can be sold or bought (at expiry)
spot: The current market price when the stock is bought or sold
interst rate: Interst charged per year
mc_paths: Number of simulted paths
"""

import random
import math
from numpy import zeros
from scipy.stats import norm
from six.moves import input
import matplotlib.pyplot as plt
# import matlab.engine
# eng = matlab.engine.start_matlab()

class Server:
    def __init__(self, expiry, strike, spot, vol, rate, mc_paths):
        self.expiry = expiry
        self.strike = strike
        self.spot = spot
        self.vol = vol
        self.rate = rate
        self.mc_paths = mc_paths

    def display(self):
        print("expiry                   :  ",self.expiry)
        print("Strike price             :  ",self.strike)
        print("Spot value               :  ",self.spot)
        print("Volatility               :  ",self.vol)
        print("Rate of interest         :  ",self.rate)
        print("Number of iterations     :  ",self.mc_paths)

    def monte_carlo_pricer(self):
        """
        Monte carlo method is unique compared to the other pricing techniques because they generate future assset prices.
        The function plots the stock_list after iterating through the number of paths by using the formula for calculating the stock value.
        It also returns the exponenent of the product of rate and expiry with the math module.
        """
        var = self.vol * self.vol * self.expiry
        std_dev = math.sqrt(var)
        ito = -0.5 * var
        spot_changed = self.spot * math.exp(self.rate * self.expiry + ito)
        sum = 0
        stock_list = []
        for i in range(0, self.mc_paths):
            normal = random.normalvariate(0, 1)
            stock_val = spot_changed * math.exp(std_dev * normal)
            stock_list.append(stock_val)
            sum += max(stock_val - self.strike, 0.0)
        result = sum / self.mc_paths
        plot = plt.plot(stock_list)
        result *= math.exp(-self.rate * self.expiry)
        return result

        var = np.square(vol)

    def black_scholes(self):
        """
        The model assumes the price of heavily traded assets follows a geometric Brownian motion with constant vol.
        The Black Scholes call option formula is calculated by multiplying the stock price by the cumulative standard normal probability distribution function.
        """
        d_1 = math.log(self.spot / self.strike) + ((self.rate + (self.vol * self.vol)/2) *
                self.expiry)
        d_2 = d_1 - self.vol * math.sqrt(self.expiry)
       # if self.option_type.lower() == 'call':
        result = self.spot * norm.cdf(d_1) - self.strike * math.exp(-self.rate * self.expiry) * norm.cdf(d_2)
        return result
        #elif self.option_type.lower() == 'put':
         #   result = self.strike * math.exp(-self.rate * expiry) * norm.cdf(-d_2) - self.spot * norm.cdf(-d_1)
          #  return result
          
    # def Price_calculation():
    #     standard_deviation = self.variance ** (0.5)
    #     time_steps = 1/365
    #     Asset_path = eng.AssetPaths(self.spot, self.mean, standard_deviation, self.expiry, self.number_of_paths);
    #     # option = input("Mention your choice (call or put) : ")
    #     # option == "call"
    #     call_pay = max(mean(Asset_path-self.spot,0)
    #     callPrice = mean(call_pay)*math.exp(-self.interest_rate * self.expiry)
    #     return callPrice
    #     # else
    #     #   put_pay = max(self.spot - mean(Asset_path))
    #     #   putPrice = mean(put_pay)*exp(-self.interest_rate * self.expiry)
    #     #   return putPrice


