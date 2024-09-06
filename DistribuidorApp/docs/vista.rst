.. module:: vista
   :platform: Python
   :synopsis: Módulo que define la interfaz gráfica de usuario (GUI) de la aplicación.

Módulo Vista
============

El módulo "vista" se encarga de definir y gestionar la interfaz gráfica de usuario (GUI) de la aplicación. Proporciona la estructura y los elementos visuales que permiten a los usuarios interactuar con la funcionalidad principal de la aplicación.

Clase Ventanita
---------------

La clase `Ventanita` representa la ventana principal de la aplicación y se encarga de las siguientes tareas:

- Crear y configurar la ventana principal de la aplicación.
- Definir etiquetas, entradas de texto, botones y vistas de árbol necesarios para la GUI.
- Gestionar la interacción del usuario y las acciones realizadas en la interfaz.

Métodos de la Clase Ventanita
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **__init__(self, window)**:
   - Descripción: Constructor de la clase `Ventanita`. Recibe la ventana principal (`window`) como argumento y configura la interfaz gráfica de la aplicación.
   - Parámetros:
     - `window` (Tk): La ventana principal de la aplicación.

2. **alta(self)**:
   - Descripción: Método para realizar la operación de alta, que agrega un nuevo registro a la base de datos con los valores ingresados por el usuario.
   - Retorna: Un diccionario con una respuesta (`True` si se completó con éxito, `False` si ocurrió un error) y un mensaje informativo.

3. **borrar(self)**:
   - Descripción: Método para realizar la operación de baja, que elimina un registro seleccionado de la base de datos.
   - Retorna: `True` si se eliminó con éxito, `False` si ocurrió un error.

4. **modificar(self)**:
   - Descripción: Método para realizar la operación de modificación, que actualiza los valores de un registro existente en la base de datos.
   - Retorna: `None`.

5. **consultar(self)**:
   - Descripción: Método para realizar la operación de consulta, que busca registros que coincidan con una descripción proporcionada y los muestra en la vista de árbol.
   - Retorna: `None`.

6. **actualizar(self)**:
   - Descripción: Método para actualizar la vista de árbol con los datos más recientes de la base de datos.
   - Retorna: `None`.

.. note::

   La clase `Ventanita` se encarga principalmente de la lógica relacionada con la interfaz gráfica y la interacción del usuario. La comunicación con la base de datos y la lógica de negocio generalmente se delegan a otros módulos, como el módulo "modelo.py" y el módulo "controller.py".

Asegúrate de proporcionar información detallada sobre la funcionalidad de la interfaz gráfica, cómo se realizan las operaciones CRUD y cómo los métodos de la clase `Ventanita` interactúan con otros componentes de la aplicación en tu documentación.

.. admonition:: Ejemplo

   A continuación, se muestra un ejemplo hipotético de cómo podría ser la clase `Ventanita` en el módulo "vista.py":

   .. code-block:: python

      from tkinter import Tk, StringVar, DoubleVar, Frame, Entry, Label, Button, ttk
      from modelo import Abmc
      from tkinter.messagebox import showinfo

      class Ventanita:
          def __init__(self, window):
              # Configuración y creación de la interfaz gráfica
              # Definición de etiquetas, entradas de texto, botones, y vista de árbol
              # Configuración de eventos y acciones del usuario

          def alta(self):
              # Lógica para realizar la operación de alta

          def borrar(self):
              # Lógica para realizar la operación de baja

          def modificar(self):
              # Lógica para realizar la operación de modificación

          def consultar(self):
              # Lógica para realizar la operación de consulta

          def actualizar(self):
              # Lógica para actualizar la vista de árbol

Si tienes otros métodos en la clase `Ventanita`, asegúrate de documentarlos adecuadamente en tu documentación.


.. automodule:: vista
   :members:
   :undoc-members:
   :show-inheritance:
