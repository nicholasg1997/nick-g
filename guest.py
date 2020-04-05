file_name = 'guest_book.txt'

print("enter 'quit' when done:")
while True:
	name = input("what is you name: ")
	if name == 'quit':
		break
	else:
		with open(file_name, 'f') as f:
			f.write(f"{name}\n")
		print(f"{name} has been added to list")