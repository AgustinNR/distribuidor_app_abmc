from tkinter import Tk
import vista
import observador


class Controller:

    def __init__(self, root):
        self.root_controller = root
        self.objeto_vista = vista.Ventanita(self.root_controller)
        self.el_observador = observador.ConcreteObserverA(self.objeto_vista.objeto_base)      
