import os, csv
from math import *
from Airport import Airport


class AirportAtlas:  # class to generate a dictionary of all airports
    __airportDict = {}

    def __init__(self, csvFileName):
        self.loadData(csvFileName)

    def loadData(self, csvFileName):  # get the data from a csv file
        try:
            with open(os.path.join(csvFileName), "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        self.__airportDict[line[4]] = Airport(line[4], line[1], line[3], line[2], line[6], line[7])

                    except UnicodeEncodeError:
                        #   If country isn't found, the airport wont be added to the dictionary
                            continue

        except FileNotFoundError:
            print("No CSV file found - airport atlas not generated")

    def printDict(self):
        for key in self.__airportDict:
            try:
                print("KEY =", key, "- Airport =", self.__airportDict[key].description())
            except UnicodeEncodeError:
                continue

    @staticmethod
    def askForAirport():
        code = input("Enter airport: \n")
        return code

    def getInputAirport(self):  # method that asks user for an airport, and returns the airport object
        while True:
            try:
                code = self.askForAirport().upper()
                return self.__airportDict[code]
            except KeyError:
                print("Code does not exist")

    def getAirport(self, code):  # method that takes in an airport code, and returns the object
        code = code.upper()
        return self.__airportDict[code]

    @staticmethod
    def getDist(lat1, lat2, long1, long2):  # distance calculator
        if lat1 > 0:
            lat1 = 90 - lat1
        else:
            lat1 = 90 + abs(lat1)

        if lat2 > 0:
            lat2 = 90 - lat2
        else:
            lat2 = 90 + abs(lat2)

        lat1 *= ((2 * pi) / 360)
        lat2 *= ((2 * pi) / 360)
        long1 *= ((2 * pi) / 360)
        long2 *= ((2 * pi) / 360)

        return int(acos((sin(lat1) * sin(lat2) * cos((long1 - long2))) + (cos(lat1) * cos(lat2))) * 6371)

    def getDistBetween(self, code_1, code_2):  # code that takes in 2 codes and returns the distance between them
        return self.getDist(code_1.lat, code_2.lat, code_1.long, code_2.long)

    def updateAirport(self, currency_dict):  # method to attach currency objects to airport objects
        for key in self.__airportDict:  # cycle through the airport dictionary (key is the airport code)
            country = self.__airportDict[key].country.upper()  # get the country of the airport
            currency_dict.addCurrencyToAirport(self.__airportDict[key], country)  # move to currency dictionary
            # bring the airport object and the country of the airport with you

    def getDetailsOfGivenAirport(self, airport):
        for key in self.__airportDict:
            if airport == key:
                self.__airportDict[key].description()
                self.__airportDict[key].getCurrencyDetails()
                return True
        else:
            print("'", airport, "', is not in our atlas of airports", sep='')
            return False





