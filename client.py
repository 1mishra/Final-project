from Server import Server
import client
import random
import math
from numpy import zeros
from scipy.stats import norm
from six.moves import input
import matplotlib.pyplot as plt

def main():
    ch='y'
    while(ch=='y'):
        reply = int(input("Press 1 for choosing default values or 2 to input your data :  "))
        if reply == 1:
            expiry = 252
            strike = 3500
            spot = 2700
            vol = 0.02
            rate = 0.06
            mc_paths = 10000
            ch='n'
            call = Server(expiry, strike, spot, vol, rate, mc_paths)
            call.display()
            print("Monte Carlo Result: ", call.monte_carlo_pricer())
            print("Black Scholes Model: ", call.black_scholes())

        elif reply == 2:
            expiry = float(input("Option expiry: "))
            strike = float(input("Option strike price: "))
            spot = float(input("Spot Value: "))
            vol = float(input("Volatility for a number between 1-100: ")) / 100
            rate = float(input("Interest Rate for a number between 1-100: ")) / 100
            mc_paths = int(input("Number paths for Monte Carlo: "))
            ch='n'
            call = Server(expiry, strike, spot, vol, rate, mc_paths)
            call.display()
            print("Monte Carlo Result: ", call.monte_carlo_pricer())
            print("Black Scholes Model: ", call.black_scholes())
        else:
            ch=str(input("Sorry wrong input, do you want to try again? (y/n) :  "))

    # print("-----: ", call.Price_calculation())


if __name__ == '__main__':
    main()