from tkinter import *

class Odbijac:
    def __init__(self, platno):
        self.platno = platno
        self.sredina_odbijaca = 350
        self.odmik_odbijaca = 50
        self.ID = self.platno.create_rectangle(self.sredina_odbijaca - self.odmik_odbijaca,
                                                    820,
                                                    self.sredina_odbijaca + self.odmik_odbijaca,
                                                    840)