# importing tkinter module
import operator
from collections import OrderedDict
from tkinter import *

class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("800x400")

        # Overskrift
        Label(self.listWindow, text="Deltager liste", font=("Arial", 40)).pack(pady=15)

        # sort fodboldtur alphabeticly
        self.sorted_fodboldtur = self.master.fodboldtur

        def list_deltagere():
            # frame til deltager liste
            self.listFrame = Frame(self.listWindow, width=200, height=200, borderwidth=self.master.borderwidth,
                                   relief=GROOVE)
            self.listFrame.pack(ipadx=10, ipady=10)

            # frame til deltagernavne
            self.deltagerListeFrame = Frame(self.listFrame, borderwidth=self.master.borderwidth, relief=GROOVE)
            self.deltagerListeFrame.pack(side=LEFT)

            # Underoverskrift og deltager liste
            Label(self.deltagerListeFrame, text="Deltager:", font=("Arial", 12, 'bold')).pack(anchor='w')
            for key in self.sorted_fodboldtur.keys():
                Label(self.deltagerListeFrame, text=key).pack(side=TOP, anchor='w')

            #frame til deltagers indbetalte beløb
            self.beløbListeFrame = Frame(self.listFrame, borderwidth=self.master.borderwidth, relief=GROOVE)
            self.beløbListeFrame.pack(side=RIGHT)

            # underoverskrift og beløbsliste
            Label(self.beløbListeFrame, text="Betalt beløb:", font=("Arial", 12, 'bold')).pack(anchor='w')
            for value in self.sorted_fodboldtur.values():
                textvar = StringVar()
                textvar.set(f"{value} kr")
                Label(self.beløbListeFrame,textvariable=textvar).pack(side=TOP,anchor='w')

        list_deltagere()




        # frame til ny deltager knap og tilbage knap
        self.ny_deltager_frame = Frame(self.listWindow, width=self.listWindow.winfo_screenwidth(), height=30,
                                 borderwidth= self.master.borderwidth, relief=GROOVE)
        self.ny_deltager_frame.pack_propagate(False)
        self.ny_deltager_frame.pack(side=BOTTOM, padx=10, pady=10)

        # ny deltager knap
        self.ny_deltager_button = Button(self.ny_deltager_frame, text="Tilføj deltager")
        self.ny_deltager_button.pack(side=RIGHT)

        # tilbage knap
        self.tilbage_button = Button(self.ny_deltager_frame, text="Tilbage", command=self.listWindow.destroy)
        self.tilbage_button.pack(side=LEFT)



        def clicked(event):
            self.selected_user = self.selected_option.get()
            print(self.selected_user)

            if self.selected_user == choices[0]:
                self.sorted_fodboldtur = OrderedDict(sorted(self.master.fodboldtur.items()))
            elif self.selected_user == choices[1]:
                self.sorted_fodboldtur = OrderedDict(sorted(self.master.fodboldtur.items(), reverse=True))
            elif self.selected_user == choices[2]:
                self.sorted_fodboldtur = dict(sorted(self.master.fodboldtur.items(), key=operator.itemgetter(1)))
            elif self.selected_user == choices[3]:
                self.sorted_fodboldtur = dict(sorted(self.master.fodboldtur.items(), key=operator.itemgetter(1), reverse=True))

            self.listFrame.destroy()

            list_deltagere()





        choices = ["A-Z", "Z-A", "Mindst til størst", "Størst til mindst"]
        self.selected_option = StringVar()
        self.selected_option.set(choices[0])
        self.selected_user = self.selected_option
        self.dropdown = OptionMenu(self.listWindow, self.selected_option, *choices, command=clicked)
        self.dropdown.config(width=10)
        self.dropdown.pack(side=BOTTOM)
