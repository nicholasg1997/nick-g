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
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')
		try:
			high = int(row[4])
			low=int(row[5])
		except ValueError:
			print(f"misiing data for{current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	print(highs)

#plot highs
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
if highs>lows:
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

#format plot
plt.title('daily high tempurtures', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('tempurture (F)', fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()
