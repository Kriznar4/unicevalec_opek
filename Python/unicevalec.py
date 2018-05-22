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
        self.master = master
        self.sirina = 700
        self.visina = 900
        self.igramo = False
        self.zmaga = False

        #ustvarimo lastnosti za začetni in koncni meni
        self.zacetni_meni = Frame(master, width=self.sirina, height=self.visina)
        self.zacetni_meni.pack()
        self.koncni_meni = Frame(master, width=self.sirina, height=self.visina)

        #začetni frame
        Label(self.zacetni_meni, text='Uničevalec opek', bg='pink', anchor='center', font=("Courier", 44)).pack(fill = X)
        Button(self.zacetni_meni, text='Začni igro', command=self.zacetek, height=11, width=20, font=("Courier", 44)).pack()
        self.izhod = PhotoImage(file ='ugasni.gif')
        Button(self.zacetni_meni, image = self.izhod, command=master.destroy, height=100, width=100).pack()

        #končni frame
        self.napis = Label(self.koncni_meni, text=' ', bg='pink', anchor='center', font=("Courier", 44))
        self.napis.pack(fill=X)
        Button(self.koncni_meni, text='Poskusi ponovno', command=self.zacetek, height=11, width=20,
               font=("Courier", 44)).pack()
        Button(self.koncni_meni, image=self.izhod, command=master.destroy, height=100, width=100).pack()

        #ustvarjanje lastnosti za platno
        # self.platno = Canvas(master, width = self.sirina, height =self.visina)
        # self.unicevalka = Unicevalka(self)
        # self.odbijac = Odbijac(self)
        # self.zacetek = True
        # self.kamni = []
        #####preselil v funkcijo ustvarjanje objektov

        #ustvarjanje kamnov
        self.kamn_sirina_pol = 30
        self.kamn_visina_pol = 10

        #####Ta del kode premaknil v funkcijo ustvarjanje kamnov





        #premiki za platno
        # self.platno.bind('<Leave>', self.na_rob)
        # self.platno.bind('<Button-1>', self.unicevalka.izstrel)
        # self.platno.bind('<Motion>', self.sledi_miski)



    def zacetek(self):
        '''prehod z začetnega menija na igro'''
        #zapremo začetni meni
        self.igramo = True
        self.ustvarjanje_objektov()
        self.zacetni_meni.pack_forget()
        self.koncni_meni.pack_forget()
        #odpremo platno
        self.platno.pack()

    def konec(self):
        '''konec igre'''
        if self.zmaga:
            self.napis.config(text='Odlično!')
        else:
            self.napis.config(text='Zelo slabo!')
        self.platno.pack_forget()
        self.platno.delete('all')
        self.igramo = False
        self.koncni_meni.pack()

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

    def ustvarjanje_kamnov(self):
        '''Ustvari kamne na začetku igre'''
        dim = (self.kamn_sirina_pol, self.kamn_visina_pol)
        sredisce = [70 + self.kamn_sirina_pol, 40 + self.kamn_visina_pol]
        for i in range(1, 8):  # 1, 8
            for j in range(1, 10):  # 1, 10
                self.kamni.append(Kamn(self, sredisce, 1, dim))
                sredisce[0] = sredisce[0] + self.kamn_sirina_pol * 2 + 5
            sredisce[1] = sredisce[1] + self.kamn_visina_pol * 2 + 5
            sredisce[0] = 70 + self.kamn_sirina_pol

    def ustvarjanje_objektov(self):
        '''ustvari objekte na začetku igre'''
        self.platno = Canvas(self.master, width=self.sirina, height=self.visina)
        self.unicevalka = Unicevalka(self)
        self.odbijac = Odbijac(self)
        self.zacetek = True
        self.kamni = []
        self.ustvarjanje_kamnov()
        self.ukazi_za_platno()

    def ukazi_za_platno(self):
        '''veže ukaze za platno z dogodki'''
        self.platno.bind('<Leave>', self.na_rob)
        self.platno.bind('<Button-1>', self.unicevalka.izstrel)
        self.platno.bind('<Motion>', self.sledi_miski)

    def unici(self):
        '''na koncu igre unici vse nepotrebne elemente'''
        self.platno.destroy()








okno = Tk()
okno.resizable(width=False, height=False)
app = Unicevalec(okno)

okno.mainloop()