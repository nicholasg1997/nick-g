from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt

#create two d6
die_1 = Die()
die_2 = Die()
die_3 = Die()

#store results
results = []
for roll_num in range(50_000):
	result = die_1.roll()+die_2.roll()+die_3.roll()
	results.append(result)

#analyze results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides+ die_3.num_sides
for value in range(3,max_results+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#visualize results
x_values = list(range(3, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'results', 'dtick': 1}
y_axis_config = {'title' : 'frequency of results'}
my_layout = Layout(title='results of rolling two D6 1000 times',xaxis = x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,"layout":my_layout,},filename='d6_d6_d6.html')

