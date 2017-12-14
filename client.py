from Server import Server

def main():
    # option_type = str(input("Enter 'call' for call options or 'put' for put options: "))
    expiry = float(input("Enter the expiry of the option (Total days for option): "))
    strike = float(input("Enter the strike price of the option (The price you are willing to pay for a future): "))
    spot = float(input("Enter the spot value of the option (Stock price currently): "))
    volatility = float(input("Enter the volatility value of the option as a rate: ")) / 100
    interest_rate = float(input("Enter the risk free interest rate as a rate: ")) / 100
    number_of_paths = int(input("Enter the number of paths you want to run the simulation for: "))
    call = VanillaOption(expiry, strike, spot, volatility, interest_rate, number_of_paths)
    print("Monte Carlo Result: ", call.monte_carlo_pricer())
    print("Black Scholes Model: ", call.black_scholes())
    # call.visulization()

if __name__ == '__main__':
    main()
else:
    print("run from import")
