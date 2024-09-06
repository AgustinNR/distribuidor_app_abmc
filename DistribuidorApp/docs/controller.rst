.. module:: controller
   :platform: Python
   :synopsis: Módulo que se encarga de controlar la lógica de la aplicación y la interacción entre la interfaz gráfica y la lógica de negocio.

Módulo Controller
=================

El módulo "controller" contiene la lógica principal de la aplicación y actúa como intermediario entre la interfaz gráfica de usuario (GUI) y la lógica de negocio subyacente. Su objetivo principal es coordinar las acciones realizadas por el usuario a través de la interfaz con las operaciones y la gestión de datos de la aplicación.

Clase Controller
---------------

La clase `Controller` representa el controlador principal de la aplicación y se encarga de las siguientes tareas:

- Crear y gestionar la ventana principal de la aplicación.
- Coordinar la comunicación entre la interfaz gráfica y la lógica de negocio.
- Iniciar la lógica de la aplicación y sus componentes.

Métodos de la Clase Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **__init__(self, root)**:
   - Descripción: Constructor de la clase `Controller`. Recibe la ventana principal (`root`) como argumento y crea una instancia de la ventana principal de la aplicación.
   - Parámetros:
     - `root` (Tk): La ventana principal de la aplicación.

2. **otros_métodos(self)**:
   - Descripción: Aquí puedes listar y describir otros métodos específicos que estén presentes en tu clase `Controller`, si los tienes. Detalla la funcionalidad de cada uno de estos métodos y cómo se utilizan en la aplicación.

.. admonition:: Nota

   El contenido y la funcionalidad de la clase `Controller` pueden variar según la estructura y la lógica específica de tu aplicación. Asegúrate de proporcionar información detallada sobre cómo se coordina la interacción entre la interfaz gráfica y la lógica de negocio en tu documentación.

.. admonition:: Ejemplo

   A continuación, se muestra un ejemplo hipotético de cómo podría ser la clase `Controller` en el módulo "controller.py":

   .. code-block:: python

      from tkinter import Tk
      from vista import Ventanita

      class Controller:
          def __init__(self, root):
              # Crea la ventana principal de la aplicación
              self.root_controller = root
              # Crea una instancia de la interfaz gráfica
              self.application = Ventanita(self.root_controller)

              # Acá podrían añadirse métodos y lógica adicional de control

          def otro_metodo(self):
         
            # Acá podrían añadirse más métodos y lógica. 

          # ...



.. automodule:: controller
   :members:
   :undoc-members:
   :show-inheritance:
