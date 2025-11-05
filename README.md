# BlackScholes
A simple Python script that fetches live option chain data from Yahoo Finance and computes theoretical call and put prices using the Black–Scholes model

Our objective here is to basically find a fair price say "C" as a function of variables s,t where s is stock price and t is time to expiration of the option contract.
Here, fair implies no arbitrage.
We’ll basically build a riskless portfolio using the stock and the option, and then require that its return must equal the risk-free rate "r".

This was theorized, in 1973 by Fischer Black, Myron Scholes and Robert C. Merton. 
