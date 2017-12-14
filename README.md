# Title: Monte Carlo Simulation in Stock Portfolio

## Team Member(s):
Gopikrishnan Pararath Radhakrishnan, Shivank Mishra, Hemanth Prabhakar

# Monte Carlo Simulation Scenario & Purpose: 

We decided to explore the stock market environment as the scenario to implement the Monte Carlo Simulation. We provide inputs for all variables such as 

Strike price
Spot Value
Expiry date of future
Volatility
Number of simulations
We are trying to analyze the stock portfolios through the simulation of uncertain variables that affect their values and find a way to reduce the risk in their investment.

 
### Hypothesis before running the simulation:
Best estimation of call or put option. 
### Simulation's variables of uncertainty

In the case of a standard European call option we used Black-Scholes and Monte Carlo to generate answers 

The equation that randomizes the stock price is
St =So * exp((r-0.5(sigma)^2)T+ sigma* sqrt(T*z))
So = Current stock price
St = Future stock price
T  = Expiry date
z  = standard normal random numbers
sigma^2 = variance
(sigma^2)/2 = volatility


List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). 
For each such variable, how did you decide the range and which probability distribution to use?  
Do you think it's a good representation of reality?

## Instructions on how to use the program:
Import the folder and run the program on Python 3. 
Run client.py and input all the variables into the rogram for equation.

## Sources Used:
https://en.wikipedia.org/wiki/Risk_neutral
https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model
https://en.wikipedia.org/wiki/Risk-neutral_measure#Example_2_.E2.80.94_Brownian_motion_model_of_stock_prices
Stochastic Calculus for Finance II - Continuous Time Models by Steven Shreve
https://www.investopedia.com/articles/investing/032415/how-investment-risk-quantified.asp
https://www.advisorperspectives.com/articles/2014/08/26/the-power-and-limitations-of-monte-carlo-simulations
