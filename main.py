import pickle

# importing tkinter module
import tkinter
from tkinter import *
from tkinter.ttk import * #progressbar

from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass

class mainWindow:
    def __init__(self):
        # global border width
        self.borderwidth = 2

        # load fil
        self.filename = 'betalinger.pk'

        infile = open(self.filename, 'rb')
        self.fodboldtur = pickle.load(infile)
        infile.close()

        # udregn værdier fra filen
        self.total = sum(self.fodboldtur.values())
        self.price_pr_person = 4500
        self.num_persons = len(self.fodboldtur)
        self.target = self.price_pr_person * self.num_persons

        # creating tkinter window
        self.root = Tk()
        self.root.geometry('800x400')


        # frame for the menu
        menuFrame = tkinter.Frame(self.root, width=150, height=self.root.winfo_screenheight(),
                                  borderwidth=self.borderwidth, relief=tkinter.GROOVE)
        menuFrame.pack_propagate(False)
        menuFrame.pack(padx=10, pady=10, side=LEFT)

        # frame for the visualized content
        contentFrame = tkinter.Frame(self.root, width=self.root.winfo_screenwidth(),
                                     height=self.root.winfo_screenheight(),
                                     borderwidth=self.borderwidth,
                                     relief=tkinter.GROOVE)
        contentFrame.pack_propagate(False)
        contentFrame.pack(padx=10, pady=10, side=RIGHT)

        # Overskrift
        velkomst = Label(contentFrame, text="Fodboldtur Prisoversigt", font = ("Arial", 40))
        velkomst.pack(pady=30)

        # TODO: Cirkel diagram

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(contentFrame, textvariable=self.progressLabelText)
        self.progress = Progressbar(contentFrame, orient = HORIZONTAL,
                    length = 300, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100

        self.progress.pack(padx= 20, pady= 20, side=BOTTOM)
        self.progressLabel.pack(side=BOTTOM)





        #  Buttons
        listButton = Button(menuFrame,text ="Deltager overblik", width = menuFrame.winfo_screenwidth(), command = lambda: listWindowClass(self))
        listButton.pack(pady = 5) # textwrap


        payButton = Button(menuFrame,text ="Indbetal penge", width = menuFrame.winfo_screenwidth(), command = lambda: payWindowClass(self))
        payButton.pack(pady = 5)

        bottom3Button = Button(menuFrame,text ="Mindste betalere", width = menuFrame.winfo_screenwidth(), command = lambda: worstWindowClass(self))
        bottom3Button.pack(pady = 5)

        # TODO: Developer mode switch - synlig frames

        # infinite loop
        mainloop()

    def save(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()
        print("Gemt!")
        return

if __name__ == '__main__':
    main = mainWindow()
