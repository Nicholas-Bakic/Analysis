#I would recommend running this in a Jupyter lab notebook in order for all of the graphs to form properly.

import matplotlib.pyplot as plt
import yfinance as yf
import ta 
from matplotlib.pyplot import figure
choice = input("Enter a stock symbol:")
choice = choice.upper()

msft = yf.Ticker(choice)

e = msft.earnings
if e.iloc[3,0] > e.iloc[2,0]:
    print("Revenue increased since last year")
else:
    print("Revenue decreased since last year")
if e.iloc[3,1] > e.iloc[2,1]:
    print("Earnings increased since last year")
else:
    print("Earnings decreased since last year")
#########

msft = yf.Ticker(choice).history(period="100d").reset_index()[["Date", "Close"]]

bol = ta.volatility.BollingerBands(msft["Close"], window=14)

msft["lband"] = bol.bollinger_lband() #
msft["hband"] = bol.bollinger_hband()
plt.style.use('seaborn')
figure(figsize=(13, 4.8), dpi=80)
plt.plot(msft["Date"], msft["Close"], label="Stock price") ,plt.plot(msft["Date"], msft["lband"], label="Lower band")
plt.plot(msft["Date"], msft["hband"], label="Higher band")
plt.legend(loc="upper left") #legend location uppper left,using the names from label="" when plotting, above ^.
plt.title("Bollinger Bands around stock price"), plt.xlabel("Dates"), plt.ylabel("Stock price") #setting a title and axes labels.
plt.fill_between(msft["Date"], msft["lband"], msft["hband"], alpha = 0.2)
#line above means to fill in between the 2 bands with colour, but with an alpha
#value of 0.2 which means it is quite transparent.


msft = yf.Ticker(choice).history(period="100d").reset_index()[["Date", "Close"]]
msft["rsi"] = ta.momentum.RSIIndicator(msft["Close"], window=14).rsi()
figure(figsize=(13.1, 4.8), dpi=80)
plt.xlabel("Date"), plt.ylabel("RSI value"), plt.title("RSI values")
plt.plot(msft["Date"], msft["rsi"])
######


msft = yf.Ticker(choice)

hist = msft.history(period="100d")
y = []
volumetotal = hist.shape[0]
for i in range(0,volumetotal):
    vol = hist.iloc[i,4]
    y.append(vol)

temphist = yf.Ticker(choice).history(period="100d").reset_index()[["Date"]]
figure(figsize=(13.2, 4.8), dpi=80)
plt.plot(temphist["Date"],y), plt.ylabel("Volume traded"), plt.xlabel("Date"), plt.title("Volume traded values on a graph")
#######

bal = msft.balance_sheet
if bal.iloc[-3,0] > bal.iloc[-3,1]:
    print("Their long term debt has grown since last year")
else:
    print("Their long term debt has shrunk from last year")
#####

print("The forward PE ratio is:", msft.info["forwardPE"], ", The trailing PE ratio is:", msft.info["trailingPE"])
