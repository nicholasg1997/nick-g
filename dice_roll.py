from random import choice

def get_winning_ticket(possibilities):
	winning_ticket = []
	while len(winning_ticket) < 4:
		pulled_item = choice(possibilities)
		
		if pulled_item not in winning_ticket:
			winning_ticket.append(pulled_item)
	return winning_ticket

def check_ticket(played_ticket, winning_ticket):
	if played_ticket != winning_ticket:
			return False

	return True

def make_rand_ticket(possibilities):
	ticket = []
	while len(ticket) < 4:
		pulled_item = choice(possibilities)

		if pulled_item not in ticket:
			ticket.append(pulled_item)
	return ticket	

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0 
won = False

while not won:
	new_ticket = get_winning_ticket(possibilities)
	won = check_ticket(new_ticket,winning_ticket)
	plays += 1

if won:
	print(f"your ticket: {new_ticket}")
	print(f"winning ticet: {winning_ticket}")
	print(f"it took {plays} tries")