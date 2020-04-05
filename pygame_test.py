import pygame
import sys


class BlueScreen:

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption('blue screen')
		self.bg_color = (0, 0, 230)
		self.ship = Ship(self)

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type ==pygame.QUIT:
					sys.exit()
			self.screen.fill(self.bg_color)
			self.ship.blitme

			pygame.display.flip()
class Ship:
	"""manage ship"""

	def __init__(self, ai_game):
		
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#load ship image
		self.image = pygame.image.load('images/superman.bmp')
		self.rect = self.image.get_rect()

		#start ship in middle bottom
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""draw ship at current location"""
		self.screen.blit(self.image, self.rect)
if __name__ == '__main__':
	ai = BlueScreen()
	ai.run_game()



