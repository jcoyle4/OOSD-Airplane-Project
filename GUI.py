from currency import *
from Itinerary import *
from AirportAtlas import *
from tkinter import *


class MyGUI(Frame):  # class to create the GUI

    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.geometry("770x400+450+125")  # size and position
        parent.title("Route Planner")  # title
        parent.wm_iconbitmap('plane.ico')  # icon in top left corner
        label = Label(text='Plane Sailing Route Planner', font=("Helvetica", 14))  # header size and font
        label.place(x=250, y=25)  # place header

        # attributes to work with
        self.aircraft = ""
        self.airport1 = None
        self.airport2 = None
        self.airport3 = None
        self.airport4 = None
        self.airport5 = None
        self.solution = ""

        # necessary objects
        self.atlas = AirportAtlas("airport.csv")
        self.currency = CurrencyAtlas("countrycurrency.csv")
        self.atlas.updateAirport(self.currency)

        # airport labels and entry boxes
        L1 = Label(text='Home Airport')
        self.E1 = Entry(bd=5)
        L2 = Label(text='Airport 1')
        self.E2 = Entry(bd=5)
        L3 = Label(text='Airport 2')
        self.E3 = Entry(bd=5)
        L4 = Label(text='Airport 3')
        self.E4 = Entry(bd=5)
        L5 = Label(text='Airport 4')
        self.E5 = Entry(bd=5)
        L1.place(x=250, y=75)
        self.E1.place(x=355, y=75)
        L2.place(x=250, y=100)
        self.E2.place(x=355, y=100)
        L3.place(x=250, y=125)
        self.E3.place(x=355, y=125)
        L4.place(x=250, y=150)
        self.E4.place(x=355, y=150)
        L5.place(x=250, y=175)
        self.E5.place(x=355, y=175)
        self.var = IntVar()
        # aircraft radio buttons (so only 1 can be selected)
        P1 = Radiobutton(parent, text="A319", variable=self.var, value=1, command=self.sel)
        P2 = Radiobutton(parent, text="A320", variable=self.var, value=2, command=self.sel)
        P3 = Radiobutton(parent, text="A321", variable=self.var, value=3, command=self.sel)
        P4 = Radiobutton(parent, text="A330", variable=self.var, value=4, command=self.sel)
        P5 = Radiobutton(parent, text="737", variable=self.var, value=5, command=self.sel)
        P6 = Radiobutton(parent, text="747", variable=self.var, value=6, command=self.sel)
        P7 = Radiobutton(parent, text="757", variable=self.var, value=7, command=self.sel)
        P8 = Radiobutton(parent, text="767", variable=self.var, value=8, command=self.sel)
        P9 = Radiobutton(parent, text="777", variable=self.var, value=9, command=self.sel)
        P10 = Radiobutton(parent, text="BAE146", variable=self.var, value=10, command=self.sel)
        P11 = Radiobutton(parent, text="DC8", variable=self.var, value=11, command=self.sel)
        P12 = Radiobutton(parent, text="F50", variable=self.var, value=12, command=self.sel)
        P13 = Radiobutton(parent, text="MD11", variable=self.var, value=13, command=self.sel)
        P14 = Radiobutton(parent, text="A400M", variable=self.var, value=14, command=self.sel)
        P15 = Radiobutton(parent, text="C212", variable=self.var, value=15, command=self.sel)
        P16 = Radiobutton(parent, text="V22", variable=self.var, value=16, command=self.sel)
        P1.place(x=175, y=200)
        P2.place(x=225, y=200)
        P3.place(x=275, y=200)
        P4.place(x=325, y=200)
        P5.place(x=375, y=200)
        P6.place(x=425, y=200)
        P7.place(x=475, y=200)
        P8.place(x=525, y=200)
        P9.place(x=175, y=225)
        P10.place(x=225, y=225)
        P11.place(x=290, y=225)
        P12.place(x=335, y=225)
        P13.place(x=380, y=225)
        P14.place(x=435, y=225)
        P15.place(x=495, y=225)
        P16.place(x=550, y=225)

        # Calculate and Clear buttons
        calc = Button(text='Calculate', command=self.OnClickCalc)
        calc.place(x=325, y=250)
        clear = Button(text='Clear', command=self.OnClickClear)
        clear.place(x=390, y=250)
        self.solVar = StringVar()
        self.solLabel = Label(parent, textvariable=self.solVar, relief=RAISED)

    # method to return the aircraft depending on the radio button that was selected
    def sel(self):
        value = self.var.get()
        if value == 1:
            self.aircraft = "A319"
        elif value == 2:
            self.aircraft = "A320"
        elif value == 3:
            self.aircraft = "A321"
        elif value == 4:
            self.aircraft = "A330"
        elif value == 5:
            self.aircraft = "737"
        elif value == 6:
            self.aircraft = '747'
        elif value == 7:
            self.aircraft = '757'
        elif value == 8:
            self.aircraft = '767'
        elif value == 9:
            self.aircraft = '777'
        elif value == 10:
            self.aircraft = 'BAE146'
        elif value == 11:
            self.aircraft = 'DC8'
        elif value == 12:
            self.aircraft = 'F50'
        elif value == 13:
            self.aircraft = 'MD11'
        elif value == 14:
            self.aircraft = 'A400M'
        elif value == 15:
            self.aircraft = 'C212'
        elif value == 16:
            self.aircraft = 'V22'

    # method to perform the calculation using given airports
    def OnClickCalc(self):

        try:
            self.airport1 = self.atlas.getAirport(self.E1.get().upper())
            self.airport2 = self.atlas.getAirport(self.E2.get().upper())
            self.airport3 = self.atlas.getAirport(self.E3.get().upper())
            self.airport4 = self.atlas.getAirport(self.E4.get().upper())
            self.airport5 = self.atlas.getAirport(self.E5.get().upper())

            customItinerary = Itinerary([self.airport1, self.airport2, self.airport3, self.airport4, self.airport5],
                                        self.aircraft)

            shortest = customItinerary.getShortestRoute(self.atlas)
            cheapest = customItinerary.getCheapestRoute(self.atlas)

            if type(cheapest) == list:
                cheapestToPrint = "For the given stops, the cheapest route will be {}, with a cost of {} Euro".format(
                    cheapest[0], cheapest[1])
                distance = 0
                for k in range(len(cheapest[0])):
                    try:
                        distance += self.atlas.getDistBetween(cheapest[0][k], cheapest[0][k+1])
                    except IndexError:
                        pass
                cheapest_distance = "For the given stops, the cheapest route has a distance of {}km".format(distance)
            else:
                cheapestToPrint = "Sorry, the selected airplane does not have the range to travel this distance"
                cheapest_distance = ""

            if type(shortest) == list:
                shortestToPrint = "For the given route, the shortest option will be {}, or {}, with a distance of {} " \
                                  "KM".format(shortest[0], shortest[1], shortest[2])
            else:
                shortestToPrint = ""
        except KeyError:
            cheapestToPrint = 'One or more of your airports is invalid'
            cheapest_distance = ''
            shortestToPrint = "Please Clear and Try again.."

        # write the solution and place it in a widget
        self.solution = "{} \n {} \n {}".format(cheapestToPrint, cheapest_distance, shortestToPrint)
        self.solVar.set(self.solution)
        self.solLabel.place(relx=0.5, rely=0.8, anchor=CENTER)

    #   method to clear all widgets on the gui
    def OnClickClear(self):

        self.E1.delete(0, 'end')
        self.E2.delete(0, 'end')
        self.E3.delete(0, 'end')
        self.E4.delete(0, 'end')
        self.E5.delete(0, 'end')
        self.solLabel.place_forget()


def launch_gui():  # method to launch the gui
    root = Tk()
    MyGUI(root)
    root.mainloop()

if __name__ == '__main__':
    launch_gui()
