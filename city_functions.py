import unittest

def name_city(city, country, population=''):
	"""format name of city and country"""
	if population:
		location = f"{city}, {country}: {population}"
	else:
		location = f"{city}, {country}"
	return location.title()





class CityCountryTest(unittest.TestCase):

	def test_city_country(self):
		place = name_city('calgary','canada')
		self.assertEqual(place, 'Calgary, Canada')

	def test_city_country_pop(self):
		place = name_city('calgary', 'canada', 1000)
		self.assertEqual(place, "Calgary, Canada: 1000")
if __name__ == '__main__':
	unittest.main()
