import os
import csv
import json


class Vehicle:  # parent vehicle class

    code = ""
    units = ""
    type = ""
    maker = ""
    range = 0.0
    maxFuel = 0.0

    def __init__(self, aircraftType):

        if not os.path.isfile('aircraft.json'):  # if the json file is already created, do not create it again
            self.csvToJson()

        self.fillDetails(aircraftType)  # fill the aircraft attributes with details from the json file
        if self.units == "imperial":  # convert imperial range to metric range
            self.imperialToMetric()
        self.maxFuel = self.range

    def csvToJson(self, fileName = "aircraft.csv"):  # convert the csv file to a json file
        csvfile = open(fileName, 'r')
        jsonfile = open('aircraft.json', 'w')
        fieldnames = ("code", "type", "units", "maker", "range")
        reader = csv.DictReader(csvfile, fieldnames)
        out = json.dumps([row for row in reader])
        jsonfile.write(out)

    def fillDetails(self, aircraftType, fileName = 'aircraft.json'):
        # cycle through the json file, filling attributes when appropriate
        with open(fileName) as f:
            data = json.load(f)
        for list in data:
            for key in list:
                if aircraftType == list[key]:
                    for key2 in list:
                        if key2 == "code":
                            self.code = list[key2]
                        if key2 == "maker":
                            self.maker = list[key2]
                        if key2 == "units":
                            self.units = list[key2]
                        if key2 == "type":
                            self.Type = list[key2]
                        if key2 == "range":
                            self.range = float(list[key2])

    def imperialToMetric(self):
        self.range *= 1.60934

    def addFuel(self, volume):  # fuel the vehicle
        unusedFuel = 0

        if self.fuel + volume <= self.maxFuel:
            self.fuel = self.fuel + volume
        elif self.fuel + volume > self.maxFuel:
            self.fuel = self.maxFuel
            unusedFuel = volume - self.fuel

        return unusedFuel

    def seeFuelLevel(self):
        return self.fuel

