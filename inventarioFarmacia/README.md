# Inventario de Farmacia

Este proyecto utiliza Flask y Microsoft Access para gestionar el inventario de una farmacia.

## Estructura del Proyecto

/inventarioFarmacia
|-- app.py
|-- /database
| |-- __init__.py
| |-- views.py
|-- /medicamentos
| |-- __init__.py
| |-- views.py
|-- /precios
| |-- __init__.py
| |-- views.py
|-- /templates
| |-- agregar.html
| |-- editar.html
| |-- index.html
|-- requirements.txt


- **app.py:** Archivo principal de la aplicación Flask.
- **/database:** Módulo para interactuar con la base de datos Access.
- **/medicamentos:** Módulo para manejar la lógica relacionada con los medicamentos.
- **/precios:** Módulo para manejar la lógica relacionada con los precios.
- **/templates:** Contiene las plantillas HTML para las páginas web.
- **requirements.txt:** Lista de dependencias del proyecto.

## Instalación

1. Clona este repositorio: `git clone https://github.com/tu_usuario/inventarioFarmacia.git`
2. Entra al directorio del proyecto: `cd inventarioFarmacia`
3. Instala las dependencias: `pip install -r requirements.txt`

## Configuración de la Base de Datos

Asegúrate de tener una base de datos Microsoft Access con la siguiente estructura:

Id  medicamento  cantidad  precio  presentacion
1   Paracetamol    200     1000     Tableta
2   Ibuprofeno     150     3000     Tableta


## Uso

1. Ejecuta la aplicación: `python app.py`
2. Abre tu navegador y visita [http://localhost:5000/](http://localhost:5000/)

## Funcionalidades

- **Agregar Medicamento:** Permite agregar nuevos medicamentos al inventario.
- **Editar Medicamento:** Permite editar la cantidad, precio y presentación de un medicamento existente.
- **Visualizar Inventario:** Muestra la lista de medicamentos en el inventario.

## Contribuciones

Si encuentras algún error o tienes sugerencias para mejorar el proyecto, no dudes en abrir un issue o enviar un pull request.






