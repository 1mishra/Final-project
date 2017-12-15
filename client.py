from Server import Server
import client
import random
import math
from numpy import zeros
from scipy.stats import norm
from six.moves import input
import matplotlib.pyplot as plt

def main():
    expiry = float(input("Option expiry: "))
    strike = float(input("Option strike price: "))
    spot = float(input("Spot Value: "))
    vol = float(input("Volatility for a number between 1-100: ")) / 100
    rate = float(input("Interest Rate for a number between 1-100: ")) / 100
    mc_paths = int(input("Number paths for Monte Carlo: "))
    call = Server(expiry, strike, spot, volatility, interest_rate, mc_paths)
    print("Monte Carlo Result: ", call.monte_carlo_pricer())
    print("Black Scholes Model: ", call.black_scholes())
    # print("-----: ", call.Price_calculation())



if __name__ == '__main__':
    main()