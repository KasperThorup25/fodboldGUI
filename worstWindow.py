# importing tkinter module
import operator
from tkinter import *

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("800x400")

        # Overskrift
        Label(self.worstWindow, text="De værste betalere", font=("Arial", 40)).pack()

        # sort dict after values
        self.sorted_fodboldtur = dict(sorted(self.master.fodboldtur.items(), key=operator.itemgetter(1)))

        # frame til deltager liste
        self.worstListFrame = Frame(self.worstWindow, width=200, height=200, borderwidth=self.master.borderwidth,
                               relief=GROOVE)
        self.worstListFrame.pack(ipadx=10, ipady=10)

        # frame til deltagernavne
        self.deltagerListeFrame = Frame(self.worstListFrame, borderwidth=self.master.borderwidth, relief=GROOVE)
        self.deltagerListeFrame.pack(side=LEFT)

        # Underoverskrift og deltager liste
        Label(self.deltagerListeFrame, text="Deltager:", font=("Arial", 12, 'bold')).pack(anchor='w')
        for key in self.sorted_fodboldtur.keys():
            Label(self.deltagerListeFrame, text=key).pack(side=TOP, anchor='w')

        # frame til deltagers indbetalte beløb
        self.beløbListeFrame = Frame(self.worstListFrame, borderwidth=self.master.borderwidth, relief=GROOVE)
        self.beløbListeFrame.pack(side=RIGHT)

        # underoverskrift og beløbsliste
        Label(self.beløbListeFrame, text="Manglende beløb:", font=("Arial", 12, 'bold')).pack(anchor='w')
        for value in self.sorted_fodboldtur.values():
            textvar = StringVar()
            textvar.set(f"{self.master.price_pr_person - value} kr")
            Label(self.beløbListeFrame, textvariable=textvar).pack(side=TOP, anchor='w')

        self.ny_deltager_frame = Frame(self.worstWindow, width=self.worstWindow.winfo_screenwidth(), height=30,
                                       borderwidth=self.master.borderwidth, relief=GROOVE)
        self.ny_deltager_frame.pack_propagate(False)
        self.ny_deltager_frame.pack(side=BOTTOM, padx=10, pady=10)

        # tilbage knap
        self.tilbage_button = Button(self.ny_deltager_frame, text="Tilbage", command=self.worstWindow.destroy)
        self.tilbage_button.pack(side=LEFT)

