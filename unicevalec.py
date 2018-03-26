#uvoz knjiznic
from tkinter import *
from math import *

#uvoz datotek
from unicevalka import *
from odbijac import *


class Unicevalec:
    def __init__(self, master):

        #splošne lastnosti
        self.sirina = 700
        self.visina = 900

        #ustvarimo lastnosti za začetni meni
        self.zacetni_meni = Frame(master, width=self.sirina, height=self.visina)
        self.zacetni_meni.pack()

        #premiki za začetni meni
        self.zacetni_meni.bind('<Button-1>', self.zacetek)

        #ustvarjanje lastnosti za platno
        self.platno = Canvas(master, width = self.sirina, height =self.visina)
        self.odbijac = Odbijac(self.platno)
        self.unicevalka = Unicevalka(self.platno,350,812)
        self.zacetek = True
        self.zacetna_tocka = self.platno.create_oval(345, 545, 355, 555)#####dodal zgolj za orientacijo


        #premiki za platno
        self.platno.bind('<Motion>', self.premik_odbijaca)
        self.platno.bind('<Leave>', self.na_rob)
        self.platno.bind('<Button-1>', self.izstrel)









    def zacetek(self, event):
        '''prehod z začetnega menija na igro'''
        #zapremo začetni meni
        self.zacetni_meni.pack_forget()
        #odpremo platno
        self.platno.pack()

    #metode
    def premik_odbijaca(self, event):
        '''premikamo odbijač levo in desno, na začetku pa še žogico'''
        # omejimo odbijac na rob okna
        if event.x < self.odbijac.odmik_odbijaca:
            self.odbijac.sredina_odbijaca = self.odbijac.odmik_odbijaca
        elif event.x > self.sirina - self.odbijac.odmik_odbijaca:
            self.odbijac.sredina_odbijaca = self.sirina - self.odbijac.odmik_odbijaca
        else:
            self.odbijac.sredina_odbijaca = event.x
        # premaknemo odbijac
        self.platno.coords(self.odbijac.ID,
                           self.odbijac.sredina_odbijaca - self.odbijac.odmik_odbijaca,
                           820,
                           self.odbijac.sredina_odbijaca + self.odbijac.odmik_odbijaca,
                           840)
        # nalimamo unicevalko na odbijac (če smo na začetku igre)
        if self.zacetek == True:
            self.platno.coords(self.unicevalka.ID, self.odbijac.sredina_odbijaca - self.unicevalka.polmer,
                               self.unicevalka.y - self.unicevalka.polmer,
                               self.odbijac.sredina_odbijaca + self.unicevalka.polmer,
                               self.unicevalka.y + self.unicevalka.polmer)
            self.unicevalka.x = self.odbijac.sredina_odbijaca

    def na_rob(self, event):
        '''v primeru, da z miško uidemo iz platna, se odbijač prestavi na ustrezni rob'''
        #omejimo na levi rob
        if self.odbijac.sredina_odbijaca < self.sirina/2:
            self.odbijac.sredina_odbijaca = self.odbijac.odmik_odbijaca
        #omejimo na desni rob
        else:
            self.odbijac.sredina_odbijaca = self.sirina - self.odbijac.odmik_odbijaca
        #prestavimo odbijac
        self.platno.coords(self.odbijac.ID,
                           self.odbijac.sredina_odbijaca - self.odbijac.odmik_odbijaca,
                           820,
                           self.odbijac.sredina_odbijaca + self.odbijac.odmik_odbijaca,
                           840)
        #ce smo na zacetku premikamo se unicevalko
        if self.zacetek == True:
            self.platno.coords(self.unicevalka.ID,
                               self.odbijac.sredina_odbijaca - self.unicevalka.polmer,
                               self.unicevalka.y - self.unicevalka.polmer,
                               self.odbijac.sredina_odbijaca + self.unicevalka.polmer,
                               self.unicevalka.y + self.unicevalka.polmer)
            self.unicevalka.x = self.odbijac.sredina_odbijaca


    def izstrel(self, event=None):
        '''ob kliku izstreli žogico skozi točko (350, 550)'''
        x = self.unicevalka.x
        y = self.unicevalka.y
        #alfa je kot med vodoravnico in tocko (350, 550)
        if event != None: #####dodan if stavek
            self.alfa = atan(abs(262)/abs(350 - x)) #####točko bi prestavil malo nižje
            self.zacetek = False
        dx = cos(self.alfa)*self.unicevalka.hitrost#####odstranil radiane saj
        dy = sin(self.alfa)*self.unicevalka.hitrost#####atan vrne radiane < >
        if (x - self.unicevalka.polmer - dx*self.unicevalka.premik_x) < 0:#####nasledni 4 if stavki so za odboj
            self.unicevalka.premik_x *= -1
        elif (x + self.unicevalka.polmer - dx*self.unicevalka.premik_x) > self.sirina:
            self.unicevalka.premik_x *= -1
        if (y - self.unicevalka.polmer - dy*self.unicevalka.premik_y) < 0:
            self.unicevalka.premik_y *= -1
        elif (y + self.unicevalka.polmer - dy*self.unicevalka.premik_y) > self.visina:#####spremeni posledico tega pogoja
            self.unicevalka.premik_y *= -1
        self.platno.coords(self.unicevalka.ID, #####spodaj sem premaknil zaklepaje ki so bili za dx oz. dy
                           (x - self.unicevalka.polmer - dx*self.unicevalka.premik_x),
                           (y - self.unicevalka.polmer - dy*self.unicevalka.premik_y),
                           (x + self.unicevalka.polmer - dx*self.unicevalka.premik_x),
                           (y + self.unicevalka.polmer - dy*self.unicevalka.premik_y))
        self.unicevalka.x = x - dx*self.unicevalka.premik_x
        self.unicevalka.y = y - dy*self.unicevalka.premik_y
        self.platno.after(20, self.izstrel)













okno = Tk()
app = Unicevalec(okno)

okno.mainloop()