import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk(5000)
	rw.fill_walk()

	plt.style.use('classic')
	fig, ax = plt.subplots(figsize = (15,9))
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values,rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s=1)
	ax.scatter(0,0, c='green', edgecolors='none', s= 100)
	ax.plot(rw.x_values[-1], linewidth = 10)
	plt.show()


	keep_running = input("make another plot? y/n:")
	if keep_running == 'n':
		break