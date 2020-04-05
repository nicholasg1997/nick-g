alien_o = {'x_location': 0, 'y_position': 25, 'speed': 'fast'}
print(f"original position is {alien_o['x_location']}")

if alien_o['speed'] == 'slow':
	x_increment = 1
elif alien_o['speed'] == 'medium':
	x_increment = 2 
else:
	x_increment = 3

alien_o['x_location'] = alien_o['x_location'] + x_increment
print(f"new location is {alien_o['x_location']}")