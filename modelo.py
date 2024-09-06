import sqlite3
from peewee import *
from validar import Validar
from observador import Sujeto
from client import send_message

db = SqliteDatabase("mi_base.db")

class BaseModel(Model):
    class Meta:
        database = db

class Productos(BaseModel):
    descripcion = CharField()
    cantidad = FloatField()
    precio = FloatField()

db.connect()
db.create_tables([Productos])

def log_decorator(action):
    def decorator(function):
        def wrap(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                send_message(f"{action} ejecutada con exito.")
                return result
            except Exception as e:
                send_message(f"{action} no pudo completarse - Error: {str(e)}")
                raise
        return wrap

    return decorator


class Abmc(Sujeto):
    def __init__(
        self,
    ): pass

    @log_decorator("Alta de producto")    
    def alta(self, descripcion, cantidad, precio, tree):
        productos=Productos()
        productos.descripcion=descripcion.get()
        productos.cantidad=cantidad.get()
        productos.precio=precio.get()
        patron = r'^[a-zA-Z0-9]+$'
        validar=Validar()
        validacion=validar.regex(patron, productos.descripcion)
        if validacion:
            try: 
                productos.save()
                self.actualizar_treeview(tree)
                self.notificar(descripcion.get(), cantidad.get(), precio.get())
                return {"respuesta":True, "mensaje":"Registro ingresado con éxito"}
            except:
                return {"respuesta":False, "mensaje":"Error de guardado."}
        else:
            return {"respuesta":False, "mensaje":"Has ingresado caracteres inválidos."}

  
    def actualizar_treeview(self, tree):
        # limpieza de tabla
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        # Consiguiendo datos
        for fila in Productos.select():
            tree.insert("", 0, text=fila.id, values=(fila.descripcion, fila.cantidad, fila.precio))


    @log_decorator("Baja de producto")  
    def baja(self, tree):
        try:
            item_seleccionado = tree.focus()
            valor_id = tree.item(item_seleccionado)
            borrar=Productos.get(Productos.id==valor_id["text"])
            borrar.delete_instance()
            self.actualizar_treeview(tree)
            return True
        except:
            return False

    @log_decorator("Modificación de producto") 
    def modificar(self, descripcion, cantidad, precio, tree):
        item_seleccionado = tree.focus()
        valor_id = tree.item(item_seleccionado)
        actualizar=Productos.update(descripcion=descripcion.get(), cantidad=cantidad.get(), precio=precio.get()).where(Productos.id==valor_id["text"])
        actualizar.execute()
        self.actualizar_treeview(tree)
        
    def consultar(self, descripcion, tree):
        # limpieza de tabla
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        
        resultado=Productos.select().where(Productos.descripcion**f"%{descripcion.get()}%")
        print(str(resultado))
        
        for fila in resultado:
            tree.insert("", 0, text=fila.id, values=(fila.descripcion, fila.cantidad, fila.precio))
