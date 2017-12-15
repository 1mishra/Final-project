from Server import Server
import client
import random
import math
from numpy import zeros
from scipy.stats import norm
from six.moves import input
import matplotlib.pyplot as plt

def main():
    # option_type = str(input("Enter 'call' for call options or 'put' for put options: "))
    expiry = float(input("Enter the expiry of the option: "))
    strike = float(input("Enter the strike price of the option: "))
    spot = float(input("Enter the spot value of the option: "))
    volatility = float(input("Enter the volatility value of the option as a rate: ")) / 100
    interest_rate = float(input("Enter the risk free interest rate as a rate: ")) / 100
    number_of_paths = int(input("Enter the number of paths you want to run the simulation for: "))
    call = Server(expiry, strike, spot, volatility, interest_rate, number_of_paths)
    print("Monte Carlo Result: ", call.monte_carlo_pricer())
    print("Black Scholes Model: ", call.black_scholes())
    # print("-----: ", call.Price_calculation())



if __name__ == '__main__':
    main()