import numpy as np 
import math
from scipy.stats import norm
import datetime as dt
import time
import yfinance as yf

# Black–Scholes formulas
def call_option(S,K,T,r,sigma):
    d1 = (math.log(S/K) + (r+ (sigma**2)/2)*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    Call = S*norm.cdf(d1)-K*math.exp(-r*T)*norm.cdf(d2)
    return Call

def put_option(S,K,T,r,sigma):
    d1 = (math.log(S/K) + (r+ (sigma**2)/2)*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    Put = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return Put

ticker = yf.Ticker("BLK")

time.sleep(5)  # avoid rate limit
expiration = ticker.options
print("\nAvailable Expiration Dates:")
for i, date in enumerate(expiration):
    print(f"{i}: {date}")

choice = int(input("\nSelect expiration (enter number): "))
expiry = expiration[choice]
print(f"\nYou selected expiry: {expiry}")

options_chain = ticker.option_chain(expiry)
calls = options_chain.calls
puts = options_chain.puts

# first 10 strikes
print("\nAvailable Strike Prices:")
for i, strike in enumerate(calls["strike"].head(10)):
    print(f"{i}: {strike}")

strike_choice = int(input("\nSelect strike (enter number): "))
K = calls["strike"].iloc[strike_choice]
print(f"\nYou selected Strike Price: {K}")

# latest close
S = ticker.history(period="1d")["Close"].iloc[-1]
print(f"\nLatest Stock Price (S): {S}")

# Compute volatility from last 10 daily closes
hist = ticker.history(period="10d")["Close"]
log_returns = np.log(hist / hist.shift(1)).dropna()
sigma = np.std(log_returns) * np.sqrt(252)  # annualized volatility
print(f"Estimated Volatility (σ): {sigma:.4f}")

# Risk-free rate 
r = float(input("\nEnter risk-free rate (e.g., 0.05 for 5%): "))

# Time to maturity
expiry_date = dt.datetime.strptime(expiry, "%Y-%m-%d")
today = dt.datetime.today()
T = (expiry_date - today).days / 365
print(f"Time to Maturity (T): {T:.4f} years")

call_price = call_option(S,K,T,r,sigma)
put_price = put_option(S,K,T,r,sigma)

print(f"\n Black Scholes Prices for BlackRock ") 
print(f"Call Option Price: {call_price:.2f}")
print(f"Put Option Price:  {put_price:.2f}")
