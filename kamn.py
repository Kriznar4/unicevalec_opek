from tkinter import *


class Kamn:
    def __init__(self, igra, sredisce, st_zadetkov, dim):
        self.igra = igra
        self.sirina_pol = dim[0]
        self.visina_pol = dim[1]
        self.sredisce_x = sredisce[0]
        self.sredisce_y = sredisce[1]
        self.st_zadetkov = 1
        self.ID = self.igra.platno.create_rectangle(self.sredisce_x - self.sirina_pol,
                                                    self.sredisce_y - self.visina_pol,
                                                    self.sredisce_x + self.sirina_pol,
                                                    self.sredisce_y + self.visina_pol,
                                                    fill='pink')


    def zadet(self, ind):
        '''kamen je zadet in se izbriše'''
        if self.st_zadetkov > 1:
            self.st_zadetkov -= 1
        else:
            self.igra.platno.delete(self.ID)
            self.igra.kamni.pop(ind)
