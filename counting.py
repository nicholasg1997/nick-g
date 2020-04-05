prompt = "please enter age to determin price"
prompt += "\ntype 'quit when done: "

while True:
	age = input(prompt)
	if age == 'quit':
		break

	age = int(age)

	if age <= 3:
		print('  you get in free')
	elif age <= 12:
		print('  your ticket is $12')
	else:
		print('  your ticket is $18')