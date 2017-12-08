import random 
import math
from numpy import zeros
from scipy.stats import norm
from six.moves import input
import matplotlib.pyplot as plt

class VanillaOption:
    def __init__(self, expiry, strike, spot, volatility, interest_rate, number_of_paths):
        #self.option_type = option_type
        self.expiry = expiry
        self.strike = strike
        self.spot = spot
        self.volatility = volatility
        self.interest_rate = interest_rate
        self.number_of_paths = number_of_paths


    def black_scholes(self):
        d_1 = math.log(self.spot / self.strike) + ((self.interest_rate + (self.volatility * self.volatility)/2) *
                self.expiry)
        d_2 = d_1 - self.volatility * math.sqrt(self.expiry)
       # if self.option_type.lower() == 'call':
        result = self.spot * norm.cdf(d_1) - self.strike * math.exp(-self.interest_rate * self.expiry) * norm.cdf(d_2)
        return result
        #elif self.option_type.lower() == 'put':
         #   result = self.strike * math.exp(-self.interest_rate * expiry) * norm.cdf(-d_2) - self.spot * norm.cdf(-d_1)
          #  return result
            
def main():
   # option_type = str(input("Enter 'call' for call options or 'put' for put options: "))
    expiry = float(input("Enter the expiry of the option: "))
    strike = float(input("Enter the strike price of the option: "))
    spot = float(input("Enter the spot value of the option: "))
    volatility =  float(input("Enter the volatility value of the option as a rate: ")) / 100
    interest_rate = float(input("Enter the risk free interest rate as a rate: ")) / 100
    number_of_paths = int(input("Enter the number of paths you want to run the simulation for: "))
    call = VanillaOption(expiry, strike, spot, volatility, interest_rate, number_of_paths) 
    print ("Monte Carlo Result: ", call.monte_carlo_pricer())
    #up_factor = float(input("Enter the up factor: " ))
    #print "SS Binomial Model without dividends: ", call.ss_binomial_model_no_dividends(up_factor)
    #print "Reg Binomial Model without dividends: ", call.reg_binomial_model_no_dividends()
    #dividends = float(input("Enter the dividend value: "))
    #print "Reg Binomial Model with dividends: ", call.reg_binomial_model_with_dividends(dividends)
    print ("Black Scholes Model: ", call.black_scholes())
    # call.visulization()
        
if __name__ == '__main__':
    main()
