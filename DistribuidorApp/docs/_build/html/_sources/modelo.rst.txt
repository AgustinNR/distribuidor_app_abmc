.. module:: modelo
   :platform: Python
   :synopsis: Módulo que maneja la interacción con la base de datos SQLite y las operaciones CRUD.

Módulo Modelo
=============

El módulo "modelo" contiene la clase `Abmc`, que se encarga de interactuar con una base de datos SQLite y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la tabla "Productos". Esta clase facilita el acceso y la gestión de los datos almacenados en la base de datos.

Clase Abmc
----------

La clase `Abmc` proporciona una interfaz para llevar a cabo las siguientes operaciones:

- Alta de un nuevo registro en la tabla "Productos" con información sobre un producto.
- Baja de un registro existente en la tabla "Productos" según el ID seleccionado.
- Modificación de los valores de un registro existente en la tabla "Productos".
- Consulta de registros que coinciden con una descripción proporcionada.
- Actualización de una vista de árbol (treeview) con los datos de la tabla "Productos".

Métodos de la Clase Abmc
~~~~~~~~~~~~~~~~~~~~~~~~~

1. **alta(descripcion, cantidad, precio, tree)**:
   - Descripción: Agrega un nuevo registro a la tabla "Productos" con los valores proporcionados.
   - Parámetros:
     - `descripcion` (str): La descripción del producto.
     - `cantidad` (float): La cantidad de unidades del producto.
     - `precio` (float): El precio del producto.
     - `tree` (ttk.Treeview): La vista de árbol donde se mostrarán los registros actualizados.
   - Retorna: Un diccionario con una respuesta (`True` si se completó con éxito, `False` si ocurrió un error) y un mensaje informativo.

2. **baja(tree)**:
   - Descripción: Elimina el registro seleccionado de la tabla "Productos".
   - Parámetros:
     - `tree` (ttk.Treeview): La vista de árbol donde se mostrarán los registros actualizados.
   - Retorna: `True` si se eliminó con éxito, `False` si ocurrió un error.

3. **modificar(descripcion, cantidad, precio, tree)**:
   - Descripción: Actualiza los valores de un registro existente en la tabla "Productos".
   - Parámetros:
     - `descripcion` (str): La nueva descripción del producto.
     - `cantidad` (float): La nueva cantidad de unidades del producto.
     - `precio` (float): El nuevo precio del producto.
     - `tree` (ttk.Treeview): La vista de árbol donde se mostrarán los registros actualizados.

4. **consultar(descripcion, tree)**:
   - Descripción: Realiza una consulta en la tabla "Productos" y muestra los resultados en la vista de árbol.
   - Parámetros:
     - `descripcion` (str): La descripción a buscar.
     - `tree` (ttk.Treeview): La vista de árbol donde se mostrarán los resultados de la consulta.

5. **actualizar_treeview(tree)**:
   - Descripción: Actualiza la vista de árbol con los datos más recientes de la tabla "Productos".
   - Parámetros:
     - `tree` (ttk.Treeview): La vista de árbol a actualizar.

.. note::

   La clase `Abmc` se utiliza para gestionar la interacción con la base de datos y no contiene métodos para la creación o configuración de la base de datos en sí, ya que se asume que la base de datos se ha creado previamente.

.. automodule:: modelo
   :members:
   :undoc-members:
   :show-inheritance:
