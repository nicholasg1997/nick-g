
hit_stay = {'action': ''}
class Blackjack:
	"""blackjack strategy generator"""

	def __init__(self):
		"""blackjack settings"""
		self.amount_of_decks = 0
		self.amount_of_players = 0
		self.deck = []
		self.hand = []
		self.discarded = []
		self.dealer_face_up = []
		self.bet2 = 0
		self.bet3 = 0
		self.bet4 = 0
		self.bet5 = 0
		self.bet6 = 0
		self.bet7 = 0
		self.bet8 = 0
		self.bet9 = 0
		self.bet10 = 0
		self.total_bet = 0
		


	def amount_players(self):
		players = input("how many players: ")
		players = int(players)
		self.amount_of_players = players
		return self.amount_of_players

	def beggining_deck(self):
		decks = input("how many decks: ")
		decks = int(decks)
		self.deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4*decks
		return self.deck



	def starting_hands(self):
		#card face up for dealer
		dealer_card = input("what card is dealer showing: ")
		dealer_card = int(dealer_card)
		self.discarded.append(dealer_card)
		self.dealer_face_up.append(dealer_card)
		self.deck.remove(dealer_card)
		
		for i in range(2):
			#cards dealt to me
			card = input("what card were you dealt: ")
			card = int(card)
			self.hand.append(card)
			self.deck.remove(card)

		for i in range(self.amount_of_players-1):
			#cards dealt to other players
			for i in range(2):
				card = input("what card was dealt to other player: ")
				card = int(card)
				self.discarded.append(card)
				self.deck.remove(card)

	def hit_stay(self):
		# hit or stay depeding on cards and changing hit_stay dictionary
		
		
		sum_hand = sum(self.hand)
		
	
		if sum(self.dealer_face_up) == 1:
			if sum(self.hand) <= 17:
				hit_stay['action'] = 'hit'
			else:
				hit_stay['action'] = 'stay'
		if sum(self.dealer_face_up) <= 3:
			if sum(self.hand) <= 12:
				hit_stay['action'] = 'hit'
			else:
				hit_stay['action'] = 'stay'
		if sum(self.dealer_face_up) <= 6:
			if sum(self.hand) <= 11:
				hit_stay['action'] = 'hit'
			else:
				hit_stay['action'] ='stay'
		if sum(self.dealer_face_up) <= 10:
			if sum(self.hand) <= 16:
				hit_stay['action'] = 'hit'
			else:
				hit_stay['action'] = 'stay'
		print(hit_stay['action'])

	def betting(self):
				# 2 count
		if self.deck.count(2) >= 1:
			count_2 = (len(self.deck)-self.deck.count(2))/self.deck.count(2)
		else:
			count_2 = 50
		# bet for 2 count
		if count_2 <= 9:
			self.bet2 = 6
		elif count_2 <= 15:
			self.bet2 = 4
		elif count_2 > 15:
			self.bet2 = 0
		#3 count
		if self.deck.count(3) >= 1:
			count_3 = (len(self.deck)-self.deck.count(3))/self.deck.count(3)
		else:
			count_3 = 50
		# bet for 3 count
		if count_3 <= 14:
			self.bet3 = 6
		elif count_3 <= 19:
			self.bet3 = 4
		elif count_3 <= 30:
			self.bet3 = 2
		elif count_3 > 30:
			self.bet3 = 1
		#4 count
		if self.deck.count(4) >= 1:
			count_4 = (len(self.deck)-self.deck.count(4))/self.deck.count(4)
		else:
			count_4 = 50
		# bet for 4 count
		if count_4 <= 14:
			self.bet4 = 5
		elif count_4 <= 19:
			self.bet4 = 4
		elif count_4 <= 30:
			self.bet4 = 2
		elif count_4 > 30:
			self.bet4 = 2
		#5 count
		if self.deck.count(5) >= 1:
			count_5 = (len(self.deck)-self.deck.count(5))/self.deck.count(5)
		else:
			count_5 = 50
		# bet for 5 count
		if count_5 <= 9:
			self.bet5 = 6
		elif count_5 <= 15:
			self.bet5 = 4
		elif count_5 <= 19:
			self.bet5 = 1
		elif count_5 > 19:
			self.bet5 = 0
		#6 count
		if self.deck.count(6) >= 1:
			count_6 = (len(self.deck)-self.deck.count(6))/self.deck.count(6)
		else:
			count_6 = 50
		# bet for 6 count
		if count_6 <= 14:
			self.bet6 = 5
		elif count_6 <= 19:
			self.bet6 = 4
		elif count_6 <= 30:
			self.bet6 = 2
		elif count_6 > 30:
			self.bet6 = 1
		#7 count
		if self.deck.count(7) >= 1:
			count_7 = (len(self.deck)-self.deck.count(7))/self.deck.count(7)
		else:
			count_7 = 50
		# bet for 7 count
		if count_7 <= 9:
			self.bet7 = 2
		elif count_7 <= 14:
			self.bet7 = 4
		elif count_7 <= 19:
			self.bet7 = 6
		elif count_7 > 19:
			self.bet7 = 8
		#8 count
		if self.deck.count(8) >= 1:
			count_8 = (len(self.deck)-self.deck.count(8))/self.deck.count(8)
		else:
			count_8 = 50
		# bet for 8 count
		if count_8 <= 9:
			self.bet8 = 2
		elif count_8 <= 14:
			self.bet8 = 2
		elif count_8 <= 19:
			self.bet8 = 3
		elif count_8 > 19:
			self.bet8 = 5
		#9 count
		if self.deck.count(9) >= 1:
			count_9 = (len(self.deck)-self.deck.count(9))/self.deck.count(9)
		else:
			count_9 = 50
		# bet for 9 count
		if count_9 <= 9:
			self.bet9 = 4
		elif count_9 <= 14:
			self.bet9 = 5
		elif count_9 <= 19:
			self.bet9 = 7
		elif count_9 > 19:
			self.bet9 = 10
		#10 count
		if self.deck.count(10) >= 1:
			count_10 = (len(self.deck)-self.deck.count(10))/self.deck.count(10)
		else:
			count_10 = 50
		# bet for 10 count
		if count_10 <= 4:
			self.bet10 = 5
		elif count_10 < 6:
			self.bet10 = 5
		elif count_10 < 9:
			self.bet10 = 15
		elif count_10 >= 9:
			self.bet10 = 30



		#calculating total bet
		self.total_bet = (self.bet2+self.bet3+self.bet4+self.bet5+self.bet6+self.bet7+self.bet8+self.bet9+self.bet10)
		print(f"bet: {self.total_bet/2}")

	def dealt_card(self):
		card = input("what other card were you dealt: ")
		card = int(card)
		self.hand.append(card)
		self.deck.remove(card)

	def play_blackjack(self):
		self.amount_players()
		self.beggining_deck()
		while True:
			self.betting()
			self.starting_hands()
			self.hit_stay()
			while 'hit' in hit_stay.values():
				#discarding cards dealt to me
				print(f"sum of your hand: {sum(self.hand)}")
				self.dealt_card()
				self.hit_stay()
			while True:
				if self.amount_of_players > 1:
					#dicarding cards dealt to other players
					card = input("what card was dealt to other player 'quit' when done: ")
				
					if card == "quit":
						break
					else:
						card = int(card)
						self.deck.remove(card)
				else:
					break
			while True:
				#discarding cards dealt to dealer
				card = input("what was dealer dealt 'quit' when done: ")	
				if card == 'quit':
					break
				else: 
					card = int(card)
					self.deck.remove(card) 
			shuffle = input("shuffled? 'y/n: ")
			if shuffle == 'y':
				break
			if shuffle == 'n':
				self.hand = []
				self.dealer_face_up = []


black = Blackjack()
black.play_blackjack() 