from AirportAtlas import *


class Currency:

    def __init__(self, name, code, country):
        self.name = name
        self.code = code
        self.country = country
        self.rateToEuro = 1
        self.rateFromEuro = 1

    def inputRateToEuro(self, rate):
        self.rateToEuro = float(rate)

    def inputRateFromEuro(self, rate):
        self.rateFromEuro = float(rate)

    def getName(self):
        return self.name

    def __str__(self):
        return "Code: {}, Name: {}, Country: {}, Rate To Euro: {}, Rate From Euro: {}".format(self.code, self.name,
                                                                                              self.country,
                                                                                              self.rateToEuro,
                                                                                              self.rateFromEuro)


class CurrencyAtlas:
    __currencyAtlas = {}

    def __init__(self, csvFileName):
        self.loadData(csvFileName)
        self.getConversionRates('currencyrates.csv')

    def loadData(self, csvFileName):
        try:
            with open(os.path.join(csvFileName), "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        self.__currencyAtlas[line[0].upper()] = Currency(line[17], line[14], line[0].upper())
                    except UnicodeEncodeError:
                        #   If country isn't found, the airport wont be added to the dictionary
                            continue
        except FileNotFoundError:
            print("No CSV file found - currency dictionary not generated")

    def printDict(self):
        list_of_dict = list(self.__currencyAtlas.values())
        for row in list_of_dict:
            try:
                print(row)
            except UnicodeEncodeError:
                continue

    def getConversionRates(self, csvFileName = 'currencyrates.csv'):  # search through the conversion rate file
        try:
            with open(os.path.join(csvFileName), "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        toEuro = line[2]
                        fromEuro = line[3]
                        for key in self.__currencyAtlas:
                            code = self.__currencyAtlas[key].code
                            if line[1] == code:
                                self.__currencyAtlas[key].inputRateToEuro(toEuro)  # attach correct conversion code to
                                self.__currencyAtlas[key].inputRateFromEuro(fromEuro)  # the currency object
                    except UnicodeEncodeError:
                        continue
        except FileNotFoundError:
            print("No CSV file found - exchange rates not recorded")

    def addCurrencyToAirport(self, airportObject, country):

        for key in self.__currencyAtlas:  # cycle through the currency atlas
            if self.__currencyAtlas[key].country == country:  # see of the country of the currency matches the country
                # of the airport
                airportObject.uploadCurrency(self.__currencyAtlas[key])  # move to the airport object and attach the
                # currency object

    def getCurrencyDetails(self, country):
        for key in self.__currencyAtlas:
            if key.upper() == country:
                print(self.__currencyAtlas[key])
                return True




