# importing tkinter module
import tkinter.ttk
from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        # Creating the window
        self.master = master # reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("800x400")


        # Overskrift
        Label(self.payWindow, text="Indbetal penge", font=("Arial", 40)).pack(pady=20)




        # dropdown menu af deltagere
        # frame:
        self.dropdownFrame = Frame(self.payWindow, width=200, height=50, borderwidth=self.master.borderwidth,
                                   relief=tkinter.GROOVE)
        self.dropdownFrame.pack()

        # label for dropdown
        self.dropdownLabel = Label(self.dropdownFrame, text="Vælg en deltager:")
        self.dropdownLabel.pack(side=LEFT)

        def clicked(event):
            self.selected_user = self.selected_option.get()

        # dropdown
        names = self.master.fodboldtur.keys()
        self.selected_option = StringVar()
        self.selected_option.set("Navn")
        self.selected_user = self.selected_option
        self.dropdown = OptionMenu(self.dropdownFrame, self.selected_option, *names, command=clicked)
        self.dropdown.config(width=10)
        self.dropdown.pack(side=RIGHT)




        # indbetalings felt
        self.money = Entry(self.payWindow, width=5)
        self.money.pack(pady=20)



        # frame for betal og tilbage knap
        self.buttonFrame = Frame(self.payWindow, width=200, height=100, borderwidth=self.master.borderwidth,
                                 relief=tkinter.GROOVE)
        self.buttonFrame.pack_propagate(False)
        self.buttonFrame.pack()

        # betal knap
        self.button = Button(self.buttonFrame, text="Betal", width=5, command= self.addMoney)
        self.button.pack(pady=20, side=LEFT)

        # tilbage knap
        self.back = Button(self.buttonFrame, text="Tilbage", width=5) # should save and close window
        self.back.pack(side=RIGHT)


    def addMoney(self):
        # Tjek om der er intastet et tal
        try:
            amount = abs(int(self.money.get())) # abs funktionen virker kun på tal
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        # Tjek om der er indtastet et negativt tal
        try:
            1/(abs(int(self.money.get()))+int(self.money.get()))  # hvis der intastes et negativt tal divideres der med 0 og dermed er der en fejl
        except:
            messagebox.showerror(parent=self.payWindow, title="Indtastnings fejl!", message="Prøv igen.\nKun positive tal!")
            return

        # Tjek om der er valgt en deltager
        try:
            self.master.fodboldtur[self.selected_user] += amount
        except:
            messagebox.showerror(parent=self.payWindow, title="Manglende Deltager", message="Prøv igen.\n Husk at vælge en deltager!")
            return

        #  Tjek om der er inbetalt for meget
        if self.master.fodboldtur[self.selected_user] > self.master.price_pr_person:

            messagebox.showerror(parent=self.payWindow, title="For høj inbetaling!", message="Prøv igen.\nDu har indbetalt mere end nødvendigt!")
            self.master.fodboldtur[self.selected_user] -= amount  # delete paid amount
            return



        self.master.save()

        # TODO: Informere bruger om at betaling er gemt

        self.master.total = sum(self.master.fodboldtur.values())

        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
