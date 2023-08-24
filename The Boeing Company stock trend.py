import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

data = yf.download("BA", start="2023-01-09", end="2023-08-31")


Q1 = data['Close'].quantile(0.25)
Q3 = data['Close'].quantile(0.75)
IQR = Q3 - Q1


lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


extreme_values = data[(data['Close'] < lower_bound) | (data['Close'] > upper_bound)]


plt.figure(figsize=(19, 6))
sns.lineplot(data=data, x=data.index, y='Close')
plt.title("Historical Trend Of The Boeing Company")


plt.scatter(extreme_values.index, extreme_values['Close'], color='red', s=50, label='Peak Value')


plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
plt.xticks(rotation=45) 
plt.ylabel('Closing Price')
plt.legend()

plt.tight_layout()  
plt.show()
