import unittest
from AirportAtlas import *


class AtlasDistanceTest(unittest.TestCase):

    def setUp(self):
        self.known_values = (("DUB", "JFK", 5103), ("DUB", "AAL", 1096), ("CDG", "SYD", 16944))
        self.testAtlas = AirportAtlas("airport.csv")

    def test_getDistBetween_known_values(self):
        for code_1, code_2, dist in self.known_values:
            code_1 = self.testAtlas.getAirport(code_1)
            code_2 = self.testAtlas.getAirport(code_2)

            result = self.testAtlas.getDistBetween(code_1, code_2)

            self.assertEqual(dist, result)

if __name__ == '__main__':
    unittest.main()
