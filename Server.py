"""
Parameters
variance: square of the standared deviation from the mean 
expiry: The period of contract
volatlity: The fluctuation of stock price
mean: mean of the stock price
strike: price at which the stocks can be sold or bought (at expiry)
spot: The current market price when the stock is bought or sold
interst rate: Interst charged per year
number_of_paths: Number of simulted paths
"""

import client
import random
import math
from numpy import zeros
from scipy.stats import norm
from six.moves import input
import matplotlib.pyplot as plt
import matlab.engine
eng = matlab.engine.start_matlab()

client.main()
# print("Executing MCS in {} ".format(__name__))
class VanillaOption:
    def __init__(self, expiry, strike, spot, volatility, interest_rate, number_of_paths):
        #self.option_type = option_type
        self.expiry = expiry
        self.strike = strike
        self.spot = spot
        self.mean = mean
        self.volatility = volatility
        self.interest_rate = interest_rate
        self.number_of_paths = number_of_paths

"""
Monte carlo method is unique compared to the other pricing techniques because they generate future assset prices. 
The function plots the stock_list after iterating through the number of paths by using the formula for calculating the stock value.
It also returns the exponenent of the product of interest_rate and expiry with the math module.
"""

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
        plt.title('Simulations of Stock Price)
        plt.ylabel('Stock Price')
        result *= math.exp(-self.interest_rate * self.expiry)
        return result
"""
The model assumes the price of heavily traded assets follows a geometric Brownian motion with constant volatility.
The Black Scholes call option formula is calculated by multiplying the stock price by the cumulative standard normal probability distribution function.
"""

    def black_scholes(self):
        d_1 = math.log(self.spot / self.strike) + ((self.interest_rate + (self.volatility * self.volatility)/2) *
                self.expiry)
        d_2 = d_1 - self.volatility * math.sqrt(self.expiry)
       # if self.option_type.lower() == 'call':
        result = self.spot * norm.cdf(d_1) - self.strike * math.exp(-self.interest_rate * self.expiry) * norm.cdf(d_2)
        return result
    
""" 
Calculating the put_price and call_price values using the matlab module and the assetpaths function
"""
                  
     def Price_calculation:
          standard_deviation = self.variance ** (0.5)
          time_steps = 1/365
          Asset_path = eng.AssetPaths(self.spot, self.mean, standard_deviation, self.expiry, self.number_of_paths);
          option = input("Mention your choice (call or put) : ")
          if option == "call"
            call_pay = max(mean(Asset_path-self.spot,0)
            callPrice = mean(call_pay)*exp(-self.interest_rate * self.expiry)
          else
             put_pay = max(self.spot - mean(Asset_path))
             putPrice = mean(put_pay)*exp(-self.interest_rate * self.expiry)
                     
                  
    
    
    
    
    
    
    
    
    
