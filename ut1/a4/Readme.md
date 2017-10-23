# Sirviendo aplicaciones Php y Python

Enlace php:  http://php.alu5627.me

Enlace python: http://now.alu5627.me

## Sitio web 1

Primero nos descargamos el archivo **demo_php.zip** en la maquina real y luego
lo movemos a la máquina de producción con el siguiente comando:

![img](img/imagen3.png)

Creamos el directorio php y dentro de este utilizamos el siguiente comando para descomprimir el archivo:

![img](img/imagen1.png)

![img](img/imagen2.png)

A continuación vamos a crear un nuevo archivo en sites-available llamado php con la siguiente configuración:

![img](img/imagen4.png)

Luego hacemos el enlace simbolico.  

![img](img/imagen5.png)

Reiniciamos el sistema nginx:

![img](img/imagen23.png)

Vamos a comprobar que poniendo la dirrecion http://php.alu5627.me nos sale el contenido de **demo_php** correctamente.

![img](img/imagen6.png)


## Sitio web 2

Vamos a crear un entorno virtual para **now** y luego lo vamos a activar :

![img](img/imagen8.png)

Ahora vamos a instalar un mini-framework de desarrollo web denominado flask

![img](img/imagen10.png)

A continuación creamos un pequeño fichero en python que va a contener el código de la aplicación web:

![img](img/imagen9.png)

Lanzamos el proceso para comprobar que va correcto hasta el momento:

![img](img/imagen12.png)

Creamos un fichero de configuración para **UWSGI**:


![img](img/imagen11.png)

![img](img/imagen17.png)

Ahora tenemos que crear un pequeño script que será el encargado de activar el entorno virtual de nuestra aplicación y de lanzar el proceso uwsgi para que escuche peticiones en el socket especificado:

![img](img/imagen14.png)

Le damos permisos de ejecución al script que hemos creado:

![img](img/imagen13.png)

Vamos a crear un virtual host para nuestra aplicación python. Para ello creamos un archivo sites-available:

![img](img/imagen15.png)

Creamos el enlace simbolico y reiniciamos el sistema:

![img](img/imagen16.png)

Lanzamos nuestra aplicación UWSGI para que escuche en el socket especificado y devuelva el sencillo html que hemos preparado en nuestra aplicación python:

![img](img/imagen18.png)

Para mantener nuestra aplicación "viva" y poder gestionar su arranque/parada de manera sencilla, necesitamos un proceso coordinador. Para este cometido, se ha desarrollado supervisor (nosotros ya lo tenemos instalado en nuestra máquina de producción).

Vamos a realizar el siguiente paso para que nuestro programa now sea gestionado por supervisor, tenemos que añadir un fichero de configuración:

![img](img/imagen19.png)

Reiniciamos el servicio para que surtan efectos los cambios realizados y comprabamos el status de este:

![img](img/imagen20.png)

Vemos que esta funcionando correctamente nuestra aplicación :

![img](img/imagen21.png)

Y comprobamos entrando en la siguiente dirreción http://now.alu5627.me si funciona correctamente:

![img](img/imagen22.png)
