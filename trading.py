import math
import numpy as np 
import pandas as pd

SO = 100 #initial index level
K = 105 #strike price
T = 1.0 #time to maturity
r = 0.05 #riskless short rate
sigma = 0.2 #volatility

I = 100000 #number of simulations

z = np.random.standard_normal(I) #psuedo-random numbers

ST = SO * np.exp((r - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * z)
hT = np.maximum(ST - K, 0) #payoff at maturity
CO = math.exp(-r * T) * np.mean(hT) # monte carlo estimator

print('value of european call option %5.3f.' % CO)