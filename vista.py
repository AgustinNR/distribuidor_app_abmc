from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from modelo import Abmc
from tkinter import ttk
from tkinter import END
from tkinter.messagebox import showinfo

class Ventanita:
    def __init__(self, window):
        self.root = window
        self.descripcion = StringVar()
        self.cantidad = DoubleVar()
        self.precio = DoubleVar()
        self.a_buscar = StringVar()
        self.frame = Frame(self.root)
        self.tree = ttk.Treeview(self.frame)
        self.objeto_base = Abmc()
        # Frame
        self.root.title("Distribuidora Sega Genesis")
        self.root.configure(bg="#333333")
        self.frame.config(width=1000, height=850)
        self.frame.grid(row=10, column=0, columnspan=5)
        
        self.frame_negro = Frame(self.root,width=30, height=110, bg="#262626", relief="sunken", borderwidth=2)
        self.frame_negro.grid(column=4, row=1, rowspan=3, padx=3, pady=3, sticky="w" + "e")      

        # Etiquetas
        self.superior = Label(
            self.root, text="Ingrese los datos de su compra:", bg="#1A8CE1", fg="white", font=("Helvetica", 14, "bold"), width=40
        )
        self.descripcion = Label(self.root, text="Producto", bg="#333333", fg="white", font=("Helvetica", 12, "bold"))
        self.cantidad = Label(self.root, text="Cantidad", bg="#333333", fg="white", font=("Helvetica", 12, "bold"))
        self.precio = Label(self.root, text="Precio",  bg="#333333", fg="white", font=("Helvetica", 12, "bold"))
        
        self.superior.grid(
            row=0, column=0, columnspan=5, padx=1, pady=1, sticky="w" + "e"
        )
        self.descripcion.grid(row=1, column=0, sticky="w" + "e")
        self.cantidad.grid(row=2, column=0, sticky="w" + "e")
        self.precio.grid(row=3, column=0, sticky="w" + "e")

        # Entradas
        w_ancho = 20
        self.entrada_descripcion = Entry(self.root, textvariable=self.descripcion, width=w_ancho, bg="#555555", fg="white", font=("Helvetica", 12))
        self.entrada_descripcion.grid(row=1, column=1)
        self.entrada_cantidad = Entry(self.root, textvariable=self.cantidad, width=w_ancho, bg="#555555", fg="white", font=("Helvetica", 12))
        self.entrada_cantidad.grid(row=2, column=1)
        self.entrada_precio = Entry(self.root, textvariable=self.precio, width=w_ancho, bg="#555555", fg="white", font=("Helvetica", 12))
        self.entrada_precio.grid(row=3, column=1)
        self.entrada_a_buscar = Entry(self.root, textvariable=self.a_buscar, width=w_ancho, bg="#303030", fg="white", font=("Helvetica", 12))
        self.entrada_a_buscar.grid(row=1, column=4)
        
        # Botones
        self.boton_alta = Button(
            self.root, text="Alta", command=lambda: self.alta(),
            bg="#555555", fg="white", font=("Helvetica", 10), width=15
        )
        self.boton_alta.grid(row=1, column=3, pady=5)

        self.boton_borrar = Button(
            self.root, text="Borrar", command=lambda: self.borrar(),
            bg="#555555", fg="white", font=("Helvetica", 10), width=15
        )
        self.boton_borrar.grid(row=2, column=3, pady=5)

        self.boton_modificar = Button(
            self.root, text="Modificar", command=lambda: self.modificar(), 
            bg="#555555", fg="white", font=("Helvetica", 10), width=15
        )
        self.boton_modificar.grid(row=3, column=3, pady=5)
         
        self.boton_consultar = Button(
            self.root, text="Buscar", command=lambda: self.consultar(), 
            bg="#303030", fg="white", font=("Helvetica", 10), width=15
        )
        self.boton_consultar.grid(row=2, column=4, pady=5)

        self.boton_actualizar = Button(
            self.root, text="Mostrar todos", command=lambda: self.actualizar(), 
            bg="#303030", fg="white", font=("Helvetica", 10), width=15,
        )
        self.boton_actualizar.grid(row=3, column=4, pady=5)
        


        # Tree
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="Cantidad")
        self.tree.heading("col3", text="Precio")
        self.tree.grid(row=10, column=0, columnspan=5, padx=10, pady=10)

    def alta(
        self,
    ):
        alta_resultado=self.objeto_base.alta(self.entrada_descripcion, self.entrada_cantidad, self.entrada_precio, self.tree)
        if alta_resultado["respuesta"]:
            self.entrada_cantidad.delete(0,END)
            self.entrada_precio.delete(0,END)
            self.entrada_descripcion.delete(0,END)
            self.entrada_descripcion.focus()
        else:
            showinfo("Error",alta_resultado["mensaje"])
                
    def borrar(
        self,
    ):
        if self.objeto_base.baja(self.tree):
            showinfo("Baja Confirmada", "Se ha eliminado el registro seleccionado.")
        else:
            showinfo("Error", "Metiste la pata.")
    
    def modificar(
        self,
    ):
        self.objeto_base.modificar(self.entrada_descripcion, self.entrada_cantidad, self.entrada_precio, self.tree)
    
    def consultar(
        self,
    ):
        self.objeto_base.consultar(self.entrada_a_buscar, self.tree)
    
    def actualizar(
        self,
    ):
        self.objeto_base.actualizar_treeview(self.tree)
