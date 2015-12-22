import unittest
from Itinerary import *
from AirportAtlas import *


class ItineraryTest(unittest.TestCase):

    def setUp(self):
        self.testAtlas = AirportAtlas("airport.csv")
        self.todaysItinerary = GenerateItinerary("testroutes.csv", self.testAtlas)

        """ testroutes.csv used in this test looks like the following
                DUB,LHR,SYD,JFK,AAL,777
                SNN,ORK,MAN,CDG,SIN,A330
                BOS,DFW,ORD,SFO,ATL,737
        """
        self.knownValues = (('DUB', "LHR", "SYD", "JFK", "AAL", "777"), ('SNN', "ORK", "MAN", "CDG", "SIN", "A330"),
                            ("BOS", "DFW", "ORD", "SFO", "ATL", "737"))

    def testDescription(self):

        self.assertIn(self.todaysItinerary.getItinAircraft(0), self.knownValues[0][5])
        self.assertEqual(self.todaysItinerary.getItinHome(1), self.knownValues[1][0])
        self.assertEqual(self.todaysItinerary.getItinStops(2, 3), self.knownValues[2][3])
        os.remove('aircraft.json')

if __name__ == '__main__':
    unittest.main()
