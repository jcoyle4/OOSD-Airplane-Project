import unittest, os
from Aircraft import *


class AircraftTest(unittest.TestCase):

    def setUp(self):
        self.known_values = (("A319", 3750, "Airbus"), ("737", 9012.304, "Boeing"), ("BAE146", 2909, "BAE"))
        self.testAircraft1 = Aircraft("A319")
        self.testAircraft2 = Aircraft("737")
        self.testAircraft3 = Aircraft("BAE146")

    def testDescription(self):
        Aircraft_2_maker = self.testAircraft2.getMaker()
        Aircraft_1_maker = self.testAircraft1.getMaker()
        Aircraft_1_range = self.testAircraft1.getRange()
        Aircraft_2_range = self.testAircraft2.getRange()
        Aircraft_3_code = self.testAircraft3.getCode()

        self.assertEqual(self.known_values[0][2], Aircraft_1_maker)
        self.assertEqual(self.known_values[1][2], Aircraft_2_maker)
        self.assertEqual(self.known_values[1][1], Aircraft_2_range)
        self.assertEqual(self.known_values[2][0], Aircraft_3_code)
        self.assertEqual(self.known_values[0][1], Aircraft_1_range)
        os.remove("aircraft.json")


if __name__ == '__main__':
    unittest.main()

