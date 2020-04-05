import matplotlib.pyplot as plt

input_values = range(1,5001) 
squares = [x**3 for x in input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()


ax.scatter(input_values, squares, c = input_values,cmap = plt.cm.twilight, s=3)
ax.set_title('square numbers', fontsize=23)
ax.set_xlabel('value', fontsize=23)
ax.set_ylabel('square of value', fontsize=23)

ax.tick_params(axis='both', labelsize=14)

plt.show()