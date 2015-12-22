from currency import *
import unittest


class CurrencyTest(unittest.TestCase):

    def setUp(self):

        self.testAtlas = AirportAtlas("airport.csv")
        self.testCurrency = CurrencyAtlas("countrycurrency.csv")
        self.testAirport = self.testAtlas.getAirport("GCW")
        self.knownValueUSDRateFromEur = 1.0541

    def testDescription(self):

        self.assertIsNone(self.testAirport.currency)
        self.testAtlas.updateAirport(self.testCurrency)
        self.assertIsNotNone(self.testAirport.currency)
        self.assertEqual(self.knownValueUSDRateFromEur, self.testAirport.currency.rateFromEuro)

if __name__ == '__main__':
    unittest.main()
