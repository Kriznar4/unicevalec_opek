#uvoz knjiznic
from tkinter import *

#uvoz datotek
from unicevalka import *


class Unicevalec:
    def __init__(self, master):

        #ustvarjanje lastnosti
        self.sirina = 700
        self.visina = 900
        self.platno = Canvas(master, width = self.sirina, height =self.visina)
        self.platno.pack()
        self.sredina_odbijaca = 350
        self.odmik_odbijaca = 50
        self.odbijac = self.platno.create_rectangle(self.sredina_odbijaca - self.odmik_odbijaca, 820, self.sredina_odbijaca + self.odmik_odbijaca, 840)
        self.unicevalka = Unicevalka(self.platno,350,812)
        self.zacetek = True


        #premiki
        self.platno.bind('<Motion>', self.premik_odbijaca)
        self.platno.bind('<Leave>', self.na_rob)

    #metode
    def premik_odbijaca(self, event):
        # omejimo odbijac na rob okna
        if event.x < self.odmik_odbijaca:
            self.sredina_odbijaca = self.odmik_odbijaca
        elif event.x > self.sirina - self.odmik_odbijaca:
            self.sredina_odbijaca = self.sirina - self.odmik_odbijaca
        else:
            self.sredina_odbijaca = event.x
        # premaknemo odbijac
        self.platno.coords(self.odbijac ,self.sredina_odbijaca - self.odmik_odbijaca, 820, self.sredina_odbijaca + self.odmik_odbijaca, 840)
        # nalimamo unicevalko na odbijac (če smo na začetku igre)
        if self.zacetek == True:
            self.platno.coords(self.unicevalka.ID, self.sredina_odbijaca - self.unicevalka.polmer, self.unicevalka.y - self.unicevalka.polmer, self.sredina_odbijaca + self.unicevalka.polmer, self.unicevalka.y + self.unicevalka.polmer)

    def na_rob(self, event):
        if self.sredina_odbijaca < self.sirina/2:
            self.sredina_odbijaca = self.odmik_odbijaca
        else:
            self.sredina_odbijaca = self.sirina - self.odmik_odbijaca
        self.platno.coords(self.odbijac, self.sredina_odbijaca - self.odmik_odbijaca, 820,
                           self.sredina_odbijaca + self.odmik_odbijaca, 840)
        if self.zacetek == True:
            self.platno.coords(self.unicevalka.ID, self.sredina_odbijaca - self.unicevalka.polmer, self.unicevalka.y - self.unicevalka.polmer, self.sredina_odbijaca + self.unicevalka.polmer, self.unicevalka.y + self.unicevalka.polmer)










okno = Tk()
app = Unicevalec(okno)

okno.mainloop()