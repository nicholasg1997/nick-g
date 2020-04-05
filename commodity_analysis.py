import csv 
import matplotlib.pyplot as plt 
from datetime import datetime

filename = 'data/clv19_price-history-09-02-2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    

    for index, colomn_header in enumerate(header_row):
        print(index, colomn_header)


    #get high temp and dates
    highs, lows, opes, closes = [], [], [],[]
    for row in reader:
        try:
            high = float(row[2])
            low=float(row[3])
            ope=float(row[1])
            close=float(row[4])
        except ValueError:
            print("missing data")

        else:           
            highs.append(high)
            lows.append(low)
            opes.append(ope)
            closes.append(close)



sma_highs=highs[:10]/10
#plot highs
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(highs, c='red', alpha=0.5)
ax.plot(lows, c='blue', alpha=0.5)
ax.plot(opes,c='green',alpha=0.5)
ax.plot(closes,c='black',alpha=0.5)
#plt.fill_between(lows,highs, facecolor='blue', alpha=0.2)
#plot sma
ax.plot(sma_highs)

#format plot
plt.title('clv price', fontsize=20)
plt.xlabel('time', fontsize=16)
plt.ylabel('price', fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)
plt.style.use('seaborn')
ax.set_ylim([50,65])

plt.show()
