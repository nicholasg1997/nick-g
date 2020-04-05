import random

deck =  [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
removed_cards = []

def deal(deck):
	random.shuffle(deck)
	hand = []
	for i in range(2):
		hand.append(deck.pop(0))
	print(hand)

def action(hit_stay):
	deal(deck)
	prompt = ("would you like to 'hit' or 'stay'?")
	active = True
	while active:
		answer = input(Prompt)
		if answer == 'hit':
			hand.append(deck.pop(0))
			print(sum(hand))
		elif sum(hand) >= 22:
			print('???')

#gameplay testing

while True:
	if sum(hand_1) >= 22:
		print(f"you went bust with a {sum(hand_1)}")
		break
	elif 'hit' in hit_or_stay.values():
		hand_1.append(shuffled_cards.pop(0))
		print(f"the new sum is {sum(hand_1)}")
		strategy()
	elif 'stay' in hit_or_stay.values():
		print(f"you finished with a {sum(hand_1)}")
		break


class Play_Blackjack:
	def __init__(self, players, decks):
		self.players = int(players)
		self.decks = decks

	def shuffle_cards(self):
		

	def hit_or_stay(self):

	def auto_play(self):

game = Play_Blackjack(1,2)
card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4*game.amount_of_decks
print(game.players)
	




