#uvoz knjiznic
from tkinter import *
from math import *

#uvoz datotek
from unicevalka import *
from odbijac import *
from kamn import *

class Unicevalec:
    def __init__(self, master):

        #splošne lastnosti
        self.sirina = 700
        self.visina = 900

        #ustvarimo lastnosti za začetni in koncni meni
        self.zacetni_meni = Frame(master, width=self.sirina, height=self.visina)
        self.zacetni_meni.pack()
        self.koncni_meni = Frame(master, width=self.sirina, height=self.visina)

        #premiki za začetni meni
        self.zacetni_meni.bind('<Button-1>', self.zacetek)

        #ustvarjanje lastnosti za platno
        self.platno = Canvas(master, width = self.sirina, height =self.visina)
        self.unicevalka = Unicevalka(self)
        self.odbijac = Odbijac(self)
        self.zacetek = True
        self.kamni = []
        #ustvarjanje kamnov
        self.kamn_sirina_pol = 30
        self.kamn_visina_pol = 10
        dim = (self.kamn_sirina_pol, self.kamn_visina_pol)
        sredisce = [70 + self.kamn_sirina_pol, 40 + self.kamn_visina_pol]
        for i in range(1, 8):
            for j in range(1, 10):
                self.kamni.append(Kamn(self, sredisce, 1, dim))
                sredisce[0] = sredisce[0] + self.kamn_sirina_pol*2 + 5
            sredisce[1] = sredisce[1] + self.kamn_visina_pol*2 + 5
            sredisce[0] = 70 + self.kamn_sirina_pol





        #premiki za platno
        self.platno.bind('<Leave>', self.na_rob)
        self.platno.bind('<Button-1>', self.unicevalka.izstrel)
        self.platno.bind('<Motion>', self.sledi_miski)



    def zacetek(self, event):
        '''prehod z začetnega menija na igro'''
        #zapremo začetni meni
        self.zacetni_meni.pack_forget()
        #odpremo platno
        self.platno.pack()

    def sledi_miski(self, event):
        '''Na začetku igre odbijac in uničevalka sledita miški, po izstrelu samo še odbijac'''
        self.odbijac.premik_odbijaca(event)
        self.unicevalka.premik_unicevalke_zacetek(event)


    def na_rob(self, event):
        '''v primeru, da z miško uidemo iz platna, se odbijač prestavi na ustrezni rob'''
        #ce smo na zacetku premikamo se unicevalko
        self.odbijac.na_rob(event)
        self.unicevalka.na_rob(event)

    def poisci_kamn(self, ID):
        '''poišče kamen z njegovim id'''
        for kamn in self.kamni:
            if kamn.ID == ID:
                ind = self.kamni.index(kamn)
                return kamn, ind








okno = Tk()
app = Unicevalec(okno)

okno.mainloop()