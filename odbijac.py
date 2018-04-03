from tkinter import *

class Odbijac:
    def __init__(self, igra):
        self.igra = igra
        self.sredina_odbijaca = 350
        self.odmik_odbijaca = 50
        self.ID = self.igra.platno.create_rectangle(self.sredina_odbijaca - self.odmik_odbijaca,
                                                    820,
                                                    self.sredina_odbijaca + self.odmik_odbijaca,
                                                    840,
                                                    fill='black')

        self.igra.platno.bind('<Motion>', self.premik_odbijaca)

    def premik_odbijaca(self, event):
        '''premikamo odbijač levo in desno, na začetku pa še žogico'''
        # omejimo odbijac na rob okna
        if event.x < self.odmik_odbijaca:
            self.sredina_odbijaca = self.odmik_odbijaca
        elif event.x > self.igra.sirina - self.odmik_odbijaca:
            self.sredina_odbijaca = self.igra.sirina - self.odmik_odbijaca
        else:
            self.sredina_odbijaca = event.x
        # premaknemo odbijac
        self.igra.platno.coords(self.ID,
                           self.sredina_odbijaca - self.odmik_odbijaca,
                           820,
                           self.sredina_odbijaca + self.odmik_odbijaca,
                           840)
        # nalimamo unicevalko na odbijac (če smo na začetku igre)


    def na_rob(self,event):
        '''v primeru da miška zapusti okno gre odbijač na ustrezen rob'''
        if self.sredina_odbijaca < self.igra.sirina/2:
            self.sredina_odbijaca = self.odmik_odbijaca
        #omejimo na desni rob
        else:
            self.sredina_odbijaca = self.igra.sirina - self.odmik_odbijaca
        #prestavimo odbijac
        self.igra.platno.coords(self.ID,
                           self.sredina_odbijaca - self.odmik_odbijaca,
                           820,
                           self.sredina_odbijaca + self.odmik_odbijaca,
                           840)