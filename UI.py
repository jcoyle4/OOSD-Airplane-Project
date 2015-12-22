from currency import *
from Itinerary import *
from AirportAtlas import *
from GUI import launch_gui

# objects needed for calculations
atlas = AirportAtlas("airport.csv")
currency = CurrencyAtlas("countrycurrency.csv")
atlas.updateAirport(currency)


def mainMenu():  # menu functiond

    print("MAIN MENU")
    print("----------------------")
    print("----------------------")
    print("A: PLANE DETAILS")  # done
    print("B: AIRPORT DETAILS")  # done
    print("C: CURRENCY DETAILS")  # done
    print("D: INPUT ROUTE FILE")  # done
    print("E: INPUT ROUTE MANUALLY")  # done
    print("F: LAUNCH GUI")
    print("G: TRY OUR NEW BETA VERSION")  # done
    print("H: TURN OFF MACHINE")  # done

    print("----------------------")


def main():  # UI main block

    turnOff = False  # bool to get things to loop

    print("Hello, Welcome to the Plane Sailing route planner")
    print("----------------------")
    while not turnOff:  # master loop
        mainMenu()

        answer = input("ENTER AN OPTION \n")
        answer = answer.upper()

        if answer == "A":  # Plane Details

            loopA = False
            while not loopA:  # option A loop
                print("Launching plane details section...")
                print("----------------------")
                again = False
                again2 = False
                while not again:
                    plane = input("Which plane would you like to inspect: \n")
                    plane = plane.upper()
                    plane = Aircraft(plane)
                    again = plane.getDetails()  # returns a bool
                    del plane
                # due to the way my aircraft/vehicle class is set up
                # I need to delete plane objects after creation for this option in the UI
                print("----------------------")

                while not again2:  # return to main menu or turn off loop
                    response = input("Return to main menu? (Y/N) \n")

                    response = response.upper()
                    if response == "Y":
                        loopA = True
                        again2 = True
                    elif response == "N":
                        Exit = input("Turn Off Machine? (Y/N) \n")
                        Exit = Exit.upper()
                        if Exit == "Y":
                            loopA = True
                            turnOff = True
                            again2 = True
                            print("Turning off Machine\nHave a nice day")
                            if os.path.isfile("aircraft.json"):
                                os.remove("aircraft.json")
                        elif Exit == "N":
                            again2 = True

        elif answer == "B":  # Airport details

            loopB = False
            while not loopB:

                print("Launching Airport details section...")
                print("----------------------")
                again = False
                again2 = False
                while not again:
                    airport = input("Enter code of airport you would like to inspect: \n")
                    airport = airport.upper()
                    again = atlas.getDetailsOfGivenAirport(airport)  # this returns a bool
                print("----------------------")

                while not again2:  # return to main menu or turn off loop
                    response = input("Return to main menu? (Y/N) \n")
                    response = response.upper()
                    if response == "Y":
                        loopB = True
                        again2 = True
                    elif response == "N":
                        Exit = input("Turn Off Machine? (Y/N) \n")
                        Exit = Exit.upper()
                        if Exit == "Y":
                            loopB = True
                            turnOff = True
                            again2 = True
                            print("Turning off Machine\nHave a nice day")
                            if os.path.isfile("aircraft.json"):
                                os.remove("aircraft.json")
                        elif Exit == "N":
                            again2 = True

        elif answer == "C":  # Currency details
            loopC = False
            while not loopC:
                print("Launching Currency details...")
                print("----------------------")
                again = False
                again2 = False
                while not again:
                    country = input("Enter the country of the currency you would like to inspect \n")
                    country = country.upper()
                    again = currency.getCurrencyDetails(country)  # returns a bool
                    if not again:
                        print("Sorry, no country with the name", country, "in our records, Please Try Again...")

                while not again2:  # return to main menu or turn off loop
                    response = input("Return to main menu? (Y/N) \n")
                    response = response.upper()
                    if response == "Y":
                        loopC = True
                        again2 = True
                    elif response == "N":
                        Exit = input("Turn Off Machine? (Y/N) \n")
                        Exit = Exit.upper()
                        if Exit == "Y":
                            loopC = True
                            turnOff = True
                            again2 = True
                            print("Turning off Machine\nHave a nice day")
                            if os.path.isfile("aircraft.json"):
                                os.remove("aircraft.json")
                        elif Exit == "N":
                            again2 = True

        elif answer == "D":  # File Input
            loopD = False
            while not loopD:
                print("Launching File Input UI...")
                print("----------------------")
                again = False
                again2 = False
                while not again:
                    again_a = False
                    while not again_a:
                        fileName = input("Please enter the route csv file: \n")
                        itinerary = GenerateItinerary(fileName, atlas)
                        again_a = itinerary.printItinerary()
                    optionWhile = False
                    while not optionWhile:
                        option = input("Would you like the (C)heapest or (S)hortest route? \n")
                        option = option.upper()
                        if option == "C":
                            itinerary.findCheapestRoute()
                            print("Outputting results to csv file....")
                            optionWhile = itinerary.writeItinerary(option)
                            again = True

                        elif option == "S":
                            itinerary.findShortestRoutes()
                            print("Outputting results to csv file....")
                            optionWhile = itinerary.writeItinerary(option)
                            again = True

                        else:
                            print("Sorry, invalid option...")
                print("----------------------")

                while not again2:  # return to main menu or turn off loop
                    response = input("Return to main menu? (Y/N) \n")
                    response = response.upper()
                    if response == "Y":
                        loopD = True
                        again2 = True
                    elif response == "N":
                        Exit = input("Turn Off Machine? (Y/N) \n")
                        Exit = Exit.upper()
                        if Exit == "Y":
                            loopD = True
                            turnOff = True
                            again2 = True
                            print("Turning off Machine\nHave a nice day")
                            if os.path.isfile("aircraft.json"):
                                os.remove("aircraft.json")
                        elif Exit == "N":
                            again2 = True

        elif answer == "E":  # Manual input
            loopE = False
            print("Launching Manual Route Input.......")
            print("----------------------")
            while not loopE:
                again = False
                again2 = False
                while not again:
                    code1 = atlas.getInputAirport()
                    code2 = atlas.getInputAirport()
                    code3 = atlas.getInputAirport()
                    code4 = atlas.getInputAirport()
                    code5 = atlas.getInputAirport()
                    aircraft = input("Which plane would you like to fly with: \n")
                    aircraft = aircraft.upper()
                    customItinerary = Itinerary([code1, code2, code3, code4, code5], aircraft)
                    option = input("Would you like the (C)heapest or (S)hortest route? \n")
                    option = option.upper()

                    if option == "C":
                        result = customItinerary.getCheapestRoute(atlas)
                        distance = 0
                        try:
                            if type(result) == list:
                                print("For the given route, the cheapest option will be", result[0],
                                      "with a cost of", result[1], "Euro")
                                for k in range(len(result[0])):
                                    try:
                                        distance += atlas.getDistBetween(result[0][k], result[0][k+1])
                                    except IndexError:
                                        pass
                                print("For the given route, the cheapest option has a distance of", distance, "km")
                                print("-----------------------------------------")
                            else:
                                print("Sorry, there was a problem with your aircraft input...")
                        except TypeError:
                            continue
                        again = True

                    if option == "S":
                        result = customItinerary.getShortestRoute(atlas)
                        try:
                            if type(result) == list:
                                print("For the given route, the shortest option will be", result[0], "or",
                                      result[1], "with a distance of", result[2], "KM")
                                print("------------------------------------")
                            else:
                                print("Sorry, there was a problem with your aircraft input...")
                        except TypeError:
                            continue
                        again = True

                while not again2:  # return to main menu or turn off loop
                    response = input("Return to main menu? (Y/N) \n")
                    response = response.upper()
                    if response == "Y":
                        loopE = True
                        again2 = True
                    elif response == "N":
                        Exit = input("Turn Off Machine? (Y/N) \n")
                        Exit = Exit.upper()
                        if Exit == "Y":
                            loopE = True
                            turnOff = True
                            again2 = True
                            print("Turning off Machine\nHave a nice day")
                            if os.path.isfile("aircraft.json"):
                                os.remove("aircraft.json")
                        elif Exit == "N":
                            again2 = True

        elif answer == "F":  # GUI
            launch_gui()

        elif answer == "G":  # Beta calculator
            loopG = False
            print("Launching BETA Calculator.......")
            print("----------------------")
            print("This will calculate the optimum strategy for the refuelling of the aircraft \n"
                  "N.B. This calculation assumes the given aircraft has INFINITE range \n"
                  "DISCLAIMER: The algorithm for this section is far from perfect")
            while not loopG:
                again = False
                again2 = False
                while not again:
                    code1 = atlas.getInputAirport()
                    code2 = atlas.getInputAirport()
                    code3 = atlas.getInputAirport()
                    code4 = atlas.getInputAirport()
                    code5 = atlas.getInputAirport()
                    aircraft = input("Which plane would you like to fly with: \n")
                    aircraft = aircraft.upper()
                    customItinerary = Itinerary([code1, code2, code3, code4, code5], aircraft)
                    customItinerary.getOptimumRoute(atlas)
                    again = True

                while not again2:  # return to main menu or turn off loop
                    response = input("Return to main menu? (Y/N) \n")
                    response = response.upper()
                    if response == "Y":
                        loopG = True
                        again2 = True
                    elif response == "N":
                        Exit = input("Turn Off Machine? (Y/N) \n")
                        Exit = Exit.upper()
                        if Exit == "Y":
                            loopG = True
                            turnOff = True
                            again2 = True
                            print("Turning off Machine\nHave a nice day")
                            if os.path.isfile("aircraft.json"):
                                os.remove("aircraft.json")
                        elif Exit == "N":
                            again2 = True

        elif answer == "H":  # Turn off machine
            print("Turning off Machine\nHave a nice day")
            if os.path.isfile("aircraft.json"):
                os.remove("aircraft.json")
            return 0

if __name__ == '__main__':
    main()
