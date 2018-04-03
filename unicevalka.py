from tkinter import *
from math import *

class Unicevalka:
    def __init__(self, igra):

        # ustvarjanje lastnosti
        self.igra = igra
        self.polmer = 10
        self.x = 350
        self.y = 820 - self.polmer
        self.premik_x = 1
        self.premik_y = 1
        self.hitrost = 7
        self.ID = self.igra.platno.create_oval(self.x - self.polmer,
                                     self.y - self.polmer,
                                     self.x + self.polmer,
                                     self.y + self.polmer,
                                               fill='red')



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
        self.igra.platno.unbind('<Button-1>')
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
        if self.y > 780:
            self.odboj_od_odbijaca()
        if self.y < 400:
            self.odboj_od_kamnov()
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
        sez_id = self.igra.platno.find_closest(self.x, self.y, halo=self.polmer)
        if sez_id[0] != self.ID:
            prejsni_x = self.x
            prejsni_y = self.y
            self.x += self.dx * self.premik_x
            self.y += self.dy * self.premik_y
            if self.igra.odbijac.sredina_odbijaca - self.igra.odbijac.odmik_odbijaca\
                    <= prejsni_x <= \
                            self.igra.odbijac.sredina_odbijaca + self.igra.odbijac.odmik_odbijaca:
                self.premik_y *= -1
                delez = (self.igra.odbijac.sredina_odbijaca + self.igra.odbijac.odmik_odbijaca - prejsni_x)\
                        /self.igra.odbijac.odmik_odbijaca*2
                self.alfa = delez*pi*14/3 + pi/3
                self.dx = cos(self.alfa) * self.hitrost
                self.dy = sin(self.alfa) * self.hitrost
            elif 790 <= prejsni_y <= 810:
                self.premik_x *= - 1
            else:
                self.premik_y *= -1
                self.premik_x *= - 1
        #if self.igra.odbijac.sredina_odbijaca + self.igra.odbijac.odmik_odbijaca >= \
        #    self.x >= \
        #    self.igra.odbijac.sredina_odbijaca - self.igra.odbijac.odmik_odbijaca:
        #    self.premik_y *= -1

    def odboj_od_kamnov(self):
        '''žogica se odbije od kamnov'''
        sez_id = self.igra.platno.find_closest(self.x, self.y, halo=self.polmer)
        if sez_id[0] != self.ID:
            prejsni_x = self.x
            prejsni_y = self.y
            self.x += self.dx * self.premik_x
            self.y += self.dy * self.premik_y
            kamn, ind = self.igra.poisci_kamn(sez_id[0])
            if kamn.sredisce_x - kamn.sirina_pol <= prejsni_x <= kamn.sredisce_x + kamn.sirina_pol:
                self.premik_y *= -1
            elif kamn.sredisce_y - kamn.visina_pol <= prejsni_y <= kamn.sredisce_y + kamn.visina_pol:
                self.premik_x *= - 1
            else:
               self.premik_y *= -1
               self.premik_x *= - 1
            kamn.zadet(ind)





