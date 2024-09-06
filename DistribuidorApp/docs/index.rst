.. DistribuidorApp documentation master file, created by
   sphinx-quickstart on Mon Sep 11 16:44:10 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _pagina_principal:
¡Bienvenido a la documentación de DistribuidorApp!
==================================================

Descripción
-----------

La aplicación «DistribuidorApp» es una herramienta de registro y gestión de compras de productos diseñada para facilitar el seguimiento de las transacciones comerciales. Permite a los usuarios ingresar información detallada sobre las compras realizadas, incluyendo el nombre del producto, la cantidad y el precio unitario. Con DistribuidorApp, los usuarios pueden llevar un registro organizado de sus compras y realizar diversas operaciones relacionadas con la gestión de productos.

Funcionamiento
--------------

DistribuidorApp ofrece las siguientes funcionalidades clave:

**Alta de una compra:** Permite a los usuarios agregar una nueva compra al sistema, ingresando el nombre del producto, la cantidad y el precio. Los datos se almacenan en una base de datos para su posterior consulta.

**Baja de una compra:** Los usuarios pueden eliminar una compra específica de la base de datos, lo que resulta útil para eliminar registros incorrectos o innecesarios.

**Modificación de una compra:** Permite a los usuarios actualizar la información de una compra existente, como el nombre del producto, la cantidad o el precio.

**Consulta de productos:** Los usuarios pueden buscar compras específicas por nombre de producto y ver los resultados en una lista.

**Mostrar todos:** DistribuidorApp ofrece la capacidad de mostrar todas las compras registradas en una vista de lista, lo que facilita la revisión de todas las transacciones.

Interfaz de Usuario
-------------------

La interfaz de usuario de DistribuidorApp se basa en la biblioteca Tkinter de Python, lo que proporciona una experiencia gráfica amigable y fácil de usar. Los elementos de la interfaz incluyen etiquetas, entradas de texto, botones y una vista de árbol (treeview) para mostrar los registros de compras de manera organizada.

Uso de la Interfaz
-------------------

Los usuarios pueden interactuar con la interfaz de DistribuidorApp de la siguiente manera:

1. Iniciar la aplicación: Ejecutar la aplicación inicia la ventana principal de DistribuidorApp.

2. Alta de una compra: Para registrar una nueva compra, el usuario debe ingresar el nombre del producto, la cantidad y el precio en los campos correspondientes y hacer clic en el botón "Alta".

3. Baja de una compra: Para eliminar una compra existente, el usuario debe seleccionar la compra deseada en la vista de árbol y hacer clic en el botón "Borrar".

4. Modificación de una compra: Para actualizar los detalles de una compra, el usuario debe seleccionar la compra deseada en la vista de árbol, realizar las modificaciones necesarias en los campos de entrada y hacer clic en el botón "Modificar".

5. Consulta de productos: Para buscar compras específicas por nombre de producto, el usuario debe ingresar el nombre en el campo de búsqueda y hacer clic en el botón "Buscar".

6. Mostrar todos: El botón "Mostrar todos" permite al usuario ver todas las compras registradas en la vista de árbol.

Ejecución de la Aplicación
---------------------------

Para ejecutar DistribuidorApp, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.

2. Abre una terminal o línea de comandos.

3. Navega al directorio donde se encuentra el código fuente de DistribuidorApp.

4. Ejecuta el módulo principal, por ejemplo:

   .. code-block:: shell

      python main.py

   Esto iniciará la aplicación y abrirá la ventana principal de DistribuidorApp.

   ¡Ahora estás listo para comenzar a utilizar DistribuidorApp y gestionar tus compras de productos de manera eficiente!

.. note::

   Asegúrate de tener la biblioteca Tkinter y el ORM peewee instalados en tu entorno de Python antes de ejecutar la aplicación.


.. toctree::
   :maxdepth: 4
   :caption: Contents:

   controller
   main
   modelo
   validar
   vista


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
