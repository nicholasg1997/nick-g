import random

#card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
dealer_first_card = []
hand = []
hit_or_stay = {'action': ''}
dealer_cards = []
class Play_Blackjack:
	"""attempting to create auto card countin"""
	
	def __init__(self, players, decks):
		self.players = players
		self.amount_of_decks = decks
		self.bust_count = 0
		self.games_won = 0
		self.games_lost = 0
		self.games_drawn = 0

	def shuffle_cards(self):
		random.shuffle(card_deck)
	
	def starting_hand(self):
		
		for i in range(2):
			hand.append(card_deck.pop(0))
		print(hand)

	def dealer_starting_hand(self):
		
		for i in range(2):
			dealer_cards.append(card_deck.pop(0))
		dealer_first_card.append(dealer_cards.pop(0))



	def hit_or_stay(self):
		if 2 in dealer_first_card:
			if sum(hand) <= 12:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'	

		if 3 in dealer_first_card:
			if sum(hand) <= 12:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 4 in dealer_first_card:
			if sum(hand) <= 11:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 5 in dealer_first_card:
			if sum(hand) <= 11:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 6 in dealer_first_card:
			if sum(hand) <= 11:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 7 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 8 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 9 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 10 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 1 in dealer_first_card:
			if sum(hand) <= 17:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'
		print(hit_or_stay.values())

	def auto_play(self):
		while True:
			if sum(hand) >= 22:
				print(f"you went bust with a {sum(hand)}")
				self.bust_count += 1
				break
			elif 'hit' in hit_or_stay.values():
				hand.append(card_deck.pop(0))
				print(f"the new sum is {sum(hand)}")
				self.hit_or_stay()
			elif 'stay' in hit_or_stay.values():
				print(f"you finished with a {sum(hand)}")
				break
	def dealer_auto_play(self):
		while True:
			if sum(dealer_cards) == 21:
				print("the dealer got a blackjack")
				break
			if sum(dealer_cards) <=17:
				dealer_cards.append(card_deck.pop(0))
				
			if sum(dealer_cards) >= 22:
				print("dealer went bust")
				break
			else:
				break
		print(f"the dealer finished with a {sum(dealer_cards)}")

	def who_won(self):
		
		if sum(hand) <= 21:
			if sum(dealer_cards) <= 21:
				if sum(hand) - sum(dealer_cards) > 0:
					print("you win")
					self.games_won += 1
					
				if sum(hand) - sum(dealer_cards) < 0:
					print("you lose")
					self.games_lost += 1
					
				if sum(hand) - sum(dealer_cards) == 0:
					print("you tied")
					self.games_drawn += 1
						
			elif sum(dealer_cards) >= 22:
				print("you won")
				self.games_won += 1
					
		elif sum(hand) >= 22:
			print("you won")
			self.games_lost += 1
				


	
	def play_blackjack(self):
		game.starting_hand()
		game.dealer_starting_hand()
		dealer_cards.extend(dealer_first_card)
		game.hit_or_stay()
		game.auto_play()
	
		print(f"dealers starting hand was{dealer_cards}")
		print(f"dealer has a {dealer_first_card} to start")
		game.dealer_auto_play()
		game.who_won()
		while dealer_first_card:
			dealer_first_card.pop()
		while dealer_cards:
			dealer_cards.pop()
		while len(hand) >= 1:
			hand.pop()
		


game = Play_Blackjack(1,2)
card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4*game.amount_of_decks
game.shuffle_cards()
game.play_blackjack()
game.play_blackjack()
game.play_blackjack()
game.play_blackjack()
game.play_blackjack()



print(f"you went bust {game.bust_count} times")
print(f"won {game.games_won} times")
print(f"lost {game.games_lost} times")
print(f"tied {game.games_drawn} times")
