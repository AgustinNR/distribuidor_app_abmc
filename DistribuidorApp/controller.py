from tkinter import Tk
import vista

# from modelo import *

class Controller:

    def __init__(self, root):
        self.root_controller = root
        self.objeto_vista = vista.Ventanita(self.root_controller)