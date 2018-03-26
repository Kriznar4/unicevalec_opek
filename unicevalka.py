from tkinter import *

class Unicevalka:
    def __init__(self, platno, x, y):

        # ustvarjanje lastnosti
        self.platno = platno
        self.x = x
        self.y = y
        self.premik_x = 1
        self.premik_y = 1
        self.smer = None
        self.hitrost = 10
        self.polmer = 7
        self.ID = self.platno.create_oval(self.x - self.polmer,
                                     self.y - self.polmer,
                                     self.x + self.polmer,
                                     self.y + self.polmer)



        #metode





