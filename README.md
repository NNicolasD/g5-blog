# PROYECTO FINAL INFORMATORIO 2023 GRUPO 5

_El objetivo de este proyecto fue crear una aplicación web utilizando el framework Django y aplicando los conocimientos adquiridos durante el curso. El blog permitirá a los visitantes leer artículos, filtrar el contenido por categorías, antigüedad y orden alfabético. Los usuarios registrados, además, podrán comentar en los artículos, editar y eliminar sus comentarios . Los usuarios colaboradores podrán crear, editar y eliminar artículos, categorías y comentarios._

## Comenzando 🚀

_Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones_


### Pre-requisitos 📋

_Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:_


```
virtualenv nombre-entorno

```
_Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):_


```
nombre_del_entorno\Scripts\activate.bat

```

_Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto._


_Luego, con el entorno activado, no dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecuta el siguiente comando en la consola._

```
pip install -r requirements.txt

```
_Este comando instalará en nuestro entorno, todo lo necesario para que el proyecto funcione funciona correctamente._

### SETTINGS 🔧

Luego tenes que crear un archivo de configuraciones en la carpeta proyecto/settings/ y llamala "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

```
from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

```

## Construido con 🛠️

_Las herramientas utilizadas para el desarrollo fueron:_

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.


## Autor ✒️

_Proyecto desarrollado por:_ 


**Alejandro Lencina**,
**Carlos Fernando Maciel**,
**Hector Carlos Larre**,
**Lucas Gabriel Gomez**,
**Matheo Cardozo**,
**Miguel Angel Ivanoff**,
**Nicolas Dellamea**



También puedes mirar la lista de todos los [contribuyentes](https://github.com/matheosc/g5-blog/graphs/contributors) quíenes han participado en este proyecto. 

## Link de la pagina 

* [DeFi Blog](https://triclion01.pythonanywhere.com)


---
