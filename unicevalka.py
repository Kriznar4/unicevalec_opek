from tkinter import *
from math import *

class Unicevalka:
    def __init__(self, igra):

        # ustvarjanje lastnosti
        self.igra = igra
        self.polmer = 7
        self.x = 350
        self.y = 820 - self.polmer
        self.premik_x = 1
        self.premik_y = 1
        self.hitrost = 7
        self.ID = self.igra.platno.create_oval(self.x - self.polmer,
                                     self.y - self.polmer,
                                     self.x + self.polmer,
                                     self.y + self.polmer)



    #metode
    def premik_unicevalke_zacetek(self, event):
        '''Unicevalka do izstrela sledi miški'''
        if self.igra.zacetek == True:
            self.igra.platno.coords(self.ID, event.x - self.polmer,
                                       self.y - self.polmer,
                                       event.x + self.polmer,
                                       self.y + self.polmer)
            self.x = event.x
            if event.x <= self.igra.odbijac.sredina_odbijaca \
                or event.x >= self.igra.sirina - self.igra.odbijac.sredina_odbijaca:
                self.na_rob(event)

    def na_rob(self, event):
        '''v primeru da miška zapusti okno gre unicevalka na ustrezen rob'''
        if self.igra.zacetek == True:
            self.igra.platno.coords(self.ID,
                               self.igra.odbijac.sredina_odbijaca - self.polmer,
                               self.y - self.polmer,
                               self.igra.odbijac.sredina_odbijaca + self.polmer,
                               self.y + self.polmer)
            self.x = self.igra.odbijac.sredina_odbijaca

    def izstrel(self, event=None):
        '''ob kliku izstreli žogico skozi točko (350, 550)'''
        x = self.x
        y = self.y
        #alfa je kot med vodoravnico in tocko (350, 550)
        if event.x < self.igra.sirina/2:
            self.premik_x *= -1
        self.alfa = atan(abs(262)/abs(350 - x)) #####točko bi prestavil malo nižje
        self.igra.zacetek = False
        self.dx = cos(self.alfa)*self.hitrost
        self.dy = sin(self.alfa)*self.hitrost
        self.premikanje()

    def premikanje(self):
        '''premikanje žogice'''
        self.odboj_od_sten()
        self.igra.platno.coords(self.ID,
                           (self.x - self.polmer - self.dx*self.premik_x),
                           (self.y - self.polmer - self.dy*self.premik_y),
                           (self.x + self.polmer - self.dx*self.premik_x),
                           (self.y + self.polmer - self.dy*self.premik_y))
        self.x -= self.dx*self.premik_x
        self.y -= self.dy*self.premik_y
        if self.y + self.polmer > 820:
            self.odboj_od_odbijaca()
        self.igra.platno.after(20, self.premikanje)

    def odboj_od_sten(self):
        '''odbijanje zogice od vseh elementov'''
        if (self.x - self.polmer - self.dx*self.premik_x) < 0\
                or (self.x + self.polmer - self.dx * self.premik_x) > self.igra.sirina:#nasledni 2 if stavki so za odboj
            self.premik_x *= -1
        if (self.y - self.polmer - self.dy*self.premik_y) < 0:
            self.premik_y *= -1
        if (self.y + self.polmer - self.dy*self.premik_y) > self.igra.visina: #za konec igre žogica pade pod odbijača
            self.igra.platno.pack_forget()
            self.igra.koncni_meni.pack()

    def odboj_od_odbijaca(self):
        '''ko se žogica dotakne odbijača se odbije'''
        if self.igra.odbijac.sredina_odbijaca + self.igra.odbijac.odmik_odbijaca >= \
            self.x >= \
            self.igra.odbijac.sredina_odbijaca - self.igra.odbijac.odmik_odbijaca:
            self.premik_y *= -1


