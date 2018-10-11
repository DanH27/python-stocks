import requests
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


teslaHighs = []
microsoftHighs = []
appleHighs = []
facebookHighs = []
zyngaHighs = []


#Tesla Section
tesla = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TSLA&outputsize=full&apikey=")

teslaHighs.append(tesla.json()["Monthly Time Series"]["2018-10-10"]["2. high"])
teslaHighs.append(tesla.json()["Monthly Time Series"]["2017-12-29"]["2. high"])
teslaHighs.append(tesla.json()["Monthly Time Series"]["2016-12-30"]["2. high"])
teslaHighs.append(tesla.json()["Monthly Time Series"]["2015-12-31"]["2. high"])
teslaHighs.append(tesla.json()["Monthly Time Series"]["2014-12-31"]["2. high"])

#Microsoft Section
microsoft = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MSFT&outputsize=full&apikey=")
microsoftHighs.append(microsoft.json()["Monthly Time Series"]["2018-10-10"]["2. high"])
microsoftHighs.append(microsoft.json()["Monthly Time Series"]["2017-12-29"]["2. high"])
microsoftHighs.append(microsoft.json()["Monthly Time Series"]["2016-12-30"]["2. high"])
microsoftHighs.append(microsoft.json()["Monthly Time Series"]["2015-12-31"]["2. high"])
microsoftHighs.append(microsoft.json()["Monthly Time Series"]["2014-12-31"]["2. high"])

#Apple
apple = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&outputsize=full&apikey=")
appleHighs.append(apple.json()["Monthly Time Series"]["2018-10-10"]["2. high"])
appleHighs.append(apple.json()["Monthly Time Series"]["2017-12-29"]["2. high"])
appleHighs.append(apple.json()["Monthly Time Series"]["2016-12-30"]["2. high"])
appleHighs.append(apple.json()["Monthly Time Series"]["2015-12-31"]["2. high"])
appleHighs.append(apple.json()["Monthly Time Series"]["2014-12-31"]["2. high"])

#Facebook
facebook = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=FB&outputsize=full&apikey=")
facebookHighs.append(facebook.json()["Monthly Time Series"]["2018-10-10"]["2. high"])
facebookHighs.append(facebook.json()["Monthly Time Series"]["2017-12-29"]["2. high"])
facebookHighs.append(facebook.json()["Monthly Time Series"]["2016-12-30"]["2. high"])
facebookHighs.append(facebook.json()["Monthly Time Series"]["2015-12-31"]["2. high"])
facebookHighs.append(facebook.json()["Monthly Time Series"]["2014-12-31"]["2. high"])

#Zynga
zynga = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=ZNGA&outputsize=full&apikey=")
zyngaHighs.append(zynga.json()["Monthly Time Series"]["2018-10-10"]["2. high"])
zyngaHighs.append(zynga.json()["Monthly Time Series"]["2017-12-29"]["2. high"])
zyngaHighs.append(zynga.json()["Monthly Time Series"]["2016-12-30"]["2. high"])
zyngaHighs.append(zynga.json()["Monthly Time Series"]["2015-12-31"]["2. high"])
zyngaHighs.append(zynga.json()["Monthly Time Series"]["2014-12-31"]["2. high"])

names = ["2018-10-10", "2017-12-29", "2016-12-30", "2015-12-31", "2014-12-31"]
values = teslaHighs
values.sort()


plt.subplot(131)
plt.bar(names, values)
plt.xticks(rotation=90)
plt.xlabel('Years')
plt.ylabel('Stock Prices (High)')
plt.show()

names = ["2018-10-10", "2017-12-29", "2016-12-30", "2015-12-31", "2014-12-31"]
values = microsoftHighs
values.sort()


plt.subplot(131)
plt.bar(names, values)
plt.xticks(rotation=90)
plt.xlabel('Years')
plt.ylabel('Stock Prices (High)')
plt.show()


names = ["2018-10-10", "2017-12-29", "2016-12-30", "2015-12-31", "2014-12-31"]
values = facebookHighs
values.sort()


plt.subplot(131)
plt.bar(names, values)
plt.xticks(rotation=90)
plt.xlabel('Years')
plt.ylabel('Stock Prices (High)')
plt.show()


names = ["2018-10-10", "2017-12-29", "2016-12-30", "2015-12-31", "2014-12-31"]
values = zyngaHighs
values.sort()


plt.subplot(131)
plt.bar(names, values)
plt.xticks(rotation=90)
plt.xlabel('Years')
plt.ylabel('Stock Prices (High)')
plt.show()


names = ["2018-10-10", "2017-12-29", "2016-12-30", "2015-12-31", "2014-12-31"]
values = appleHighs
values.sort()


plt.subplot(131)
plt.bar(names, values)
plt.xticks(rotation=90)
plt.xlabel('Years')
plt.ylabel('Stock Prices (High)')
plt.show()
