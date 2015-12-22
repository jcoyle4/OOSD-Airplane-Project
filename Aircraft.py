from Vehicle import Vehicle


class Aircraft(Vehicle):  # class that inherits from the Vehicle class

    MIN_FUEL = 1000

    def __init__(self, planeCode = '747', tailNumber = ''):
        super().__init__(planeCode)
        self.tailNumber = tailNumber
        self.fuel = 0.0

    def fly(self, distance):  # decreases the fuel level depending on distance flown
        if distance <= self.range:
            self.fuel -= distance
        else:
            print("distance too far")
            return self.range

    def getCode(self):  # returns aircraft code
        return self.code

    def getMaker(self):  # returns aircraft maker
        return self.maker

    def getRange(self):  # returns the max distance the aircraft can fly
        return self.range

    def getDetails(self):  # returns aircraft details
        if self.maxFuel == 0:  # if there is no aircraft object, it will not have a maxFuel attribute
            print("Sorry, there is no airplane with that code in our system!")
            return False
        else:
            print(self)
            return True

    def __str__(self):
        return "Code: {} - Max Range {} - Maker {}".format(self.code, self.maxFuel, self.maker)

    def __repr__(self):
        return "Code: {} - Max Range {}KM - Maker {}".format(self.code, self.maxFuel, self.maker)
