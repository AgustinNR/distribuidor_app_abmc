from tkinter import Tk
from controller import Controller


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)

    application.objeto_vista.actualizar()
    root_tk.mainloop()