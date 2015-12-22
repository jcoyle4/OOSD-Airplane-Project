import csv
import os
from Aircraft import *
import itertools


class Itinerary:  # class to store an individual itinerary

    def __init__(self, route, aircraft):
        self.route = route
        self.aircraft = Aircraft(aircraft)
        self.returnToHomeAirport()

    def returnToHomeAirport(self):  # method to put the home airport on the end of the route

        home = self.route[0]
        self.route.append(home)

    def errorMessage(self):  # method to return/print when aircraft has not enough range
        print("Sorry, your", self.aircraft.getCode(), "is not able to complete the given journey due to its range")
        print("--------------------------------------------------------------------")
        return "Sorry, your {} is not able to complete the given journey due to its range"\
            .format(self.aircraft.getCode())

    def permutate(self):  # method to generate all route options
        option_storage = []
        middleOfJourney = self.route[1:len(self.route)-1]
        listOfPermutations = list(itertools.permutations(middleOfJourney))

        for x in range(len(listOfPermutations)):  # for loop to ensure not dealing with a list within a list
            list_generator = []
            list_generator.append(self.route[0])
            for y in range(len(middleOfJourney)):
                list_generator.append(listOfPermutations[x][y])
            list_generator.append(self.route[len(self.route)-1])
            option_storage.append(list_generator)

        return option_storage  # return a list of lists

    def getShortestRoute(self, atlas):  # method to cycle through the list of lists and return the shortest distance
        ans_storage = {}
        bestOption = []

        option_storage = self.permutate()

        for i in range(len(option_storage)):
            total_distance = 0
            for j in range(len(option_storage[i])):
                try:
                    distance = atlas.getDistBetween(option_storage[i][j], option_storage[i][j+1])
                    if distance < self.aircraft.getRange():
                        total_distance += distance
                        tuple_option = tuple(option_storage[i])
                        ans_storage[tuple_option] = total_distance
                    else:
                        return self.errorMessage()
                except IndexError:  # if it gets to the end of the list, do nothing
                    pass


        minimum = min(ans_storage, key=ans_storage.get)
        reversed_minimum = minimum[::-1]
        bestOption.append(minimum)
        bestOption.append(reversed_minimum)
        bestOption.append(ans_storage[minimum])

        return bestOption

    def getCheapestRoute(self, atlas):  # method to cycle through the list of lists and return the cheapest option

        ans_storage = {}
        bestOption = []

        option_storage = self.permutate()
        # assumptions for this calculation detailed in the documentation
        for i in range(len(option_storage)):
            cost = 0

            for j in range(len(option_storage[i])):
                try:
                    distance = atlas.getDistBetween(option_storage[i][j], option_storage[i][j+1])
                    if distance < self.aircraft.getRange():  # see if the plane can make the given leg
                        if self.aircraft.seeFuelLevel() < self.aircraft.MIN_FUEL:
                                neededfuel = self.aircraft.MIN_FUEL - self.aircraft.seeFuelLevel()
                                self.aircraft.addFuel(neededfuel)
                                cost += neededfuel * option_storage[i][j+1].currency.rateFromEuro

                        if distance > self.aircraft.seeFuelLevel():
                            currentFuel = self.aircraft.seeFuelLevel()  # see how much fuel is in the plane
                            inputFuel = (distance - currentFuel) * 1.1
                            # calculate the amount of fuel to input, with 10% extra
                            cost += inputFuel * option_storage[i][j].currency.rateFromEuro * 1.1  # calculate cost
                            self.aircraft.addFuel(inputFuel)  # add the necessary amount of fuel
                        self.aircraft.fly(distance)  # make the plane fly to decrease the fuel level

                    else:
                        return self.errorMessage()

                except IndexError:  # if it gets to the end of the list, do nothing
                    continue
            tuple_option = tuple(option_storage[i])
            ans_storage[tuple_option] = round(cost, 2)

        minimum = min(ans_storage, key=ans_storage.get)
        bestOption.append(minimum)
        bestOption.append(ans_storage[minimum])
        return bestOption

    # the next 3 methods are used for finding and printing the optimum re-fuelling strategy,
    #  assuming infinite fuel capacity
    def whatOption(self, number, airport1, airport2, airport3, airport4, airport5):
        if number == "opt1":
            print("Refuel at:", airport1, ",", airport2, ",", airport3, ",", airport4, "and", airport5)
        elif number == "opt2":
            print("Refuel at:", airport1, ",", airport2, ",", airport3, "and", airport4)
        elif number == "opt3":
            print("Refuel at:", airport1, ",", airport2, ",", airport3, "and", airport5)
        elif number == "opt4":
            print("Refuel at:", airport1, ",", airport2, ",", airport4, "and", airport5)
        elif number == "opt5":
            print("Refuel at:", airport1, ",", airport3, ",", airport4, "and", airport5)
        elif number == "opt6":
            print("Refuel at:", airport1, ",", airport4, "and", airport5)
        elif number == "opt7":
            print("Refuel at:", airport1, ",", airport3, "and", airport4)
        elif number == "opt8":
            print("Refuel at:", airport1, ",", airport2, "and", airport3)
        elif number == "opt9":
            print("Refuel at:", airport1, ",", airport2, "and", airport4)
        elif number == "opt10":
            print("Refuel at:", airport1, ",", airport3, "and", airport5)
        elif number == "opt11":
            print("Refuel at:", airport1, ",", airport2, "and", airport5)
        elif number == "opt12":
            print("Refuel at:", airport1, "and", airport5)
        elif number == "opt13":
            print("Refuel at:", airport1, "and", airport4)
        elif number == "opt14":
            print("Refuel at:", airport1, "and", airport3)
        elif number == "opt15":
            print("Refuel at:", airport1, "and", airport2)
        elif number == "opt16":
            print("Only fuel at:", airport1)
        else:
            print("ERROR")

    def calcOptRoute(self, atlas):
        answers = {}

        home = self.route[0]
        stop1 = self.route[1]
        stop2 = self.route[2]
        stop3 = self.route[3]
        stop4 = self.route[4]
        stop5 = self.route[5]

        leg1 = atlas.getDistBetween(home, stop1)
        leg2 = atlas.getDistBetween(stop1, stop2)
        leg3 = atlas.getDistBetween(stop2, stop3)
        leg4 = atlas.getDistBetween(stop3, stop4)
        leg5 = atlas.getDistBetween(stop4, stop5)

        opt1 = (leg1 * home.currency.rateFromEuro) + (leg2 * stop1.currency.rateFromEuro) +\
               (leg3 * stop2.currency.rateFromEuro) + (leg4 * stop3.currency.rateFromEuro) + \
               (leg5 * stop4.currency.rateFromEuro)
        answers["opt1"] = opt1

        opt2 = (leg1 * home.currency.rateFromEuro) + (leg2 * stop1.currency.rateFromEuro) +\
               (leg3 * stop2.currency.rateFromEuro) + ((leg4 + leg5) * stop3.currency.rateFromEuro)
        answers["opt2"] = opt2

        opt3 = (leg1 * home.currency.rateFromEuro) + (leg2 * stop1.currency.rateFromEuro) +\
               ((leg3+leg4) * stop2.currency.rateFromEuro) + (leg5 * stop4.currency.rateFromEuro)
        answers["opt3"] = opt3

        opt4 = (leg1 * home.currency.rateFromEuro) + ((leg2 + leg3) * stop1.currency.rateFromEuro) + \
               (leg4 * stop3.currency.rateFromEuro) + (leg5 * stop4.currency.rateFromEuro)
        answers["opt4"] = opt4

        opt5 = ((leg1 + leg2) * home.currency.rateFromEuro) + (leg3 * stop2.currency.rateFromEuro) + \
               (leg4 * stop3.currency.rateFromEuro) + (leg5 * stop4.currency.rateFromEuro)
        answers["opt5"] = opt5

        opt6 = ((leg1 + leg2 + leg3) * home.currency.rateFromEuro) + (leg4 * stop3.currency.rateFromEuro) + \
               (leg5 * stop4.currency.rateFromEuro)
        answers["opt6"] = opt6

        opt7 = ((leg1 + leg2) * home.currency.rateFromEuro) + (leg3 * stop2.currency.rateFromEuro) + \
               ((leg4 + leg5) * stop3.currency.rateFromEuro)
        answers["opt7"] = opt7

        opt8 = (leg1 * home.currency.rateFromEuro) + (leg2 * stop1.currency.rateFromEuro) + \
               ((leg3 + leg4 + leg5) * stop2.currency.rateFromEuro)
        answers["opt8"] = opt8

        opt9 = (leg1 * home.currency.rateFromEuro) + ((leg2 + leg3) * stop1.currency.rateFromEuro) + \
               ((leg4 + leg5) * stop3.currency.rateFromEuro)
        answers["opt9"] = opt9

        opt10 = ((leg1 + leg2) * home.currency.rateFromEuro) + ((leg3 + leg4) * stop2.currency.rateFromEuro) + \
                (leg5 * stop4.currency.rateFromEuro)
        answers["opt10"] = opt10

        opt11 = (leg1 * home.currency.rateFromEuro) + ((leg2 + leg3 + leg4) * stop1.currency.rateFromEuro) + \
                (leg5 * stop4.currency.rateFromEuro)
        answers["opt11"] = opt11

        opt12 = ((leg1 + leg2 + leg3 + leg4) * home.currency.rateFromEuro) + (leg5 * stop4.currency.rateFromEuro)
        answers["opt12"] = opt12

        opt13 = ((leg1 + leg2 + leg3) * home.currency.rateFromEuro) + ((leg4 + leg5) * stop3.currency.rateFromEuro)
        answers["opt13"] = opt13

        opt14 = ((leg1 + leg2) * home.currency.rateFromEuro) + ((leg3 + leg4 + leg5) * stop2.currency.rateFromEuro)
        answers["opt14"] = opt14

        opt15 = (leg1 * home.currency.rateFromEuro) + ((leg2 + leg3 + leg4 + leg5) * stop1.currency.rateFromEuro)
        answers["opt15"] = opt15

        opt16 = ((leg1 + leg2 + leg3 + leg4 + leg5) * home.currency.rateFromEuro)
        answers["opt16"] = opt16

        minimum = min(answers, key=answers.get)
        #print(minimum, round(answers[minimum], 2))
        #self.whatOption(minimum, home, stop1, stop2, stop3, stop4)
        return [minimum, round(answers[minimum], 2)]

    def getOptimumRoute(self, atlas):

        ans_storage = {}
        bestOption = []

        option_storage = self.permutate()

        for i in range(len(option_storage)):
            cost = 0
            cost += self.aircraft.MIN_FUEL
            self.aircraft.addFuel(self.aircraft.MIN_FUEL)

            for j in range(len(option_storage[i])):
                try:
                    optRoutes = self.calcOptRoute(atlas)
                    #print(type(optRoutes))
                    #print(optRoutes)
                    optRoutes = tuple(optRoutes)
                    list_option = tuple(option_storage[i])
                    ans_storage[list_option] = optRoutes
                except IndexError:  # if it gets to the end of the list, do nothing
                    continue

        minimum = min(ans_storage, key=ans_storage.get)
        # bestOption.append(minimum)
        # bestOption.append(ans_storage[minimum])
        # print(minimum)
        # print(ans_storage[minimum][0])
        print("Take route -", minimum)
        self.whatOption(ans_storage[minimum][0], self.route[0], self.route[1], self.route[2], self.route[3],
                        self.route[4])
        print("Cost of", ans_storage[minimum][1], "Euro")
        # return bestOption

    def getHomeAirport(self):  # method to return the home airport
        return self.route[0]

    def getStops(self, stop):
        if stop == 1:
            return self.route[1]
        elif stop == 2:
            return self.route[2]
        elif stop == 3:
            return self.route[3]
        elif stop == 4:
            return self.route[4]

    def getAircraft(self):
        return self.aircraft.getCode()

    def __str__(self):
        return "Plane: {} -- Route: {}".format(self.aircraft.getCode(), self.route)


class GenerateItinerary:  # class to generate all itineraries from a file

    def __init__(self, csvFileName, atlas):
        self.__itineraryList = []
        self.__listOfShortestRoutes = []
        self.__listOfCheapestRoute = []
        self.__listOfOptimumRoutes = []
        self.atlas = atlas
        self.loadData(csvFileName)

    def loadData(self, csvFileName):  # get data from the file
        try:
            with open(os.path.join(csvFileName), "rt", encoding="utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        self.__itineraryList.append(Itinerary([self.atlas.getAirport(line[0]),
                                                               self.atlas.getAirport(line[1]),
                                                               self.atlas.getAirport(line[2]),
                                                               self.atlas.getAirport(line[3]),
                                                               self.atlas.getAirport(line[4])], line[5]))
                    except (UnicodeEncodeError, IndexError):
                        #   If route is in incorrect format, it won't be added to the dictionary
                            continue

        except FileNotFoundError:
            print("File not found - Itinerary not generated")

    def printItinerary(self):
        if len(self.__itineraryList) != 0:
            for x in range(len(self.__itineraryList)):
                print("Route", x+1, "--", self.__itineraryList[x])
            return True
        else:
            return False

    def findShortestRoutes(self):  # method to aid calculating shortest distance of multiple itineraries

        for i in range(len(self.__itineraryList)):
            bestRoute = self.__itineraryList[i].getShortestRoute(self.atlas)
            self.__listOfShortestRoutes.append(bestRoute)

        for i in range(len(self.__listOfShortestRoutes)):
            try:
                if type(self.__listOfShortestRoutes[i]) != str:  # the error message is in a string
                    print("For Route", i+1, "the shortest options will be", self.__listOfShortestRoutes[i][0], "or",
                        self.__listOfShortestRoutes[i][1], "with a distance of", self.__listOfShortestRoutes[i][2], "KM")
                    print("------------------------------------")
            except TypeError:
                continue

    def findCheapestRoute(self):  # method to aid calculating cheapest option of multiple itineraries
        for i in range(len(self.__itineraryList)):
            cheapestRoute = self.__itineraryList[i].getCheapestRoute(self.atlas)
            self.__listOfCheapestRoute.append(cheapestRoute)

        for j in range(len(self.__listOfCheapestRoute)):
            distance = 0
            try:
                if type(self.__listOfCheapestRoute[j]) != str:  # the error message is in a string
                    print("For Route", j+1, "the cheapest option will be", self.__listOfCheapestRoute[j][0],
                          "with a cost of", self.__listOfCheapestRoute[j][1], "Euro")
                    for k in range(len(self.__listOfCheapestRoute[j][0])):
                        try:
                            distance += self.atlas.getDistBetween(self.__listOfCheapestRoute[j][0][k],
                                                                  self.__listOfCheapestRoute[j][0][k+1])
                        except IndexError:
                            pass
                    print("For Route", j+1, "the cheapest option has a distance of", distance, "km")
                    print("-----------------------------------------")
            except TypeError:
                continue

    def writeItinerary(self, option):  # method to write the cheapest itinerary to a file
        csvfilename = ""
        # Check if file has correct extension
        while True:
            csvfilename = input("Name of the file to write to: \n")

            if csvfilename[len(csvfilename)-4:] == ".csv":
                break
            else:
                print("Incorrect file extension. Must be .csv, Please try again")

        try:
            with open(os.path.join(csvfilename), "w", newline='') as f:
                writer = csv.writer(f, delimiter=",")
                routesToWrite = []

                if option == "C":  # write cheapest option
                    for item in self.__listOfCheapestRoute:
                        routesToWrite.append(item)

                    for itinerary in routesToWrite:
                        csvrow = []
                        csvrow.append(itinerary)
                        writer.writerow(csvrow)

                elif option == "S":  # write shortest option
                    for item in self.__listOfShortestRoutes:
                        routesToWrite.append(item)

                    for itinerary in routesToWrite:
                        csvrow = []
                        csvrow.append(itinerary)
                        writer.writerow(csvrow)
                return True

        except FileNotFoundError:
            print("There is something wrong with how you named your file, check symbols and try again")
            return False

    def getItinAircraft(self, routeNumber):
        return self.__itineraryList[routeNumber].getAircraft()

    def getItinHome(self, routeNumber):
        return str(self.__itineraryList[routeNumber].getHomeAirport())

    def getItinStops(self, routeNumber, stop):
        return str(self.__itineraryList[routeNumber].getStops(stop))