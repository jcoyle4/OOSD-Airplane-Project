import os


class Airport:  # class for airport objects

    def __init__(self, id, name, country, city,  lat, long):
        self.name = name
        self.id = id
        self.lat = float(lat)
        self.long = float(long)
        self.country = country
        self.city = city
        self.currency = None  # will be used to store the currency object, not available at instantiation

    def description(self):   # returns a description of the airport
        print(self.name, ", with code of ", self.id, ", is in the country of ", self.country, ", which has currency ",
              self.currency.getName(), sep="")

    def getCountry(self):  # returns the country of the airport
        return self.country

    def uploadCurrency(self, currency):  # attaches the currency object to the airport
        self.currency = currency

    def getCurrencyDetails(self):  # returns currency details of a given airport
        try:
            print("The currency of ", self.currency.getName(), " has conversion rates of ", self.currency.rateToEuro,
                  " to euro and ", self.currency.rateFromEuro, " from euro", sep='')
        except AttributeError:
            pass

    def __str__(self):
        return "{}".format(self.id)

    def __repr__(self):
        return "{}".format(self.id)


