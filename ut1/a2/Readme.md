# Listado de directorios

En esta práctica utilizaremos **autoindex** y nos permite listar el contenido del directorio actual, pudiendo implementar una especie de **FTP** a través del navegador.

Creadmos el dirrectorio Shared en webapps y nos situamos en el.

![img](img/imagen1.png)

Ahora vamos a crear un virtual host para servir esta carpeta compartida shared con el siguiente comando:
cd etc/nginx/sites-available y luego sudo nano alu5627

![img](img/imagen2.png)

Enlazamos los directorios en el virtual host para que estén disponibles

Ahora recargamos el servidor para que los cambios tengan efecto:

![img](img/imagen3.png)

Y comprobamos que funciona todo correctamente.

![img](img/imagen4.png)
