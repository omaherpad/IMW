# UT1-A3: Trabajo con virtual hosts

Vamos a configurar 4 sitios web (virtual hosts) en nuestro servidor web Nginx.

## Sitio web 1

Vamos a mostrar una página con la imagen de "Diagrama de unidades de trabajo"

Primero vamos al fichero que hay en **sites-available** de imw y lo modificamos para que nos salga el contenido que hay en la carpeta que hemos creado **/mec** situada en el directorio imw.

![img](img/imagen1.png)

Nos bajamos la imagen en la máquina real y luego la movemos a la máquina de producción con el comando **scp**

![img](img/imagen3.png)

Creamos el index.html dentro de **mec** para visualizar la img.

![img](img/imagen4.png)

Actualizamos los cambios y comprobamos:

![img](img/imagen6.png)

Vemos que la imagen se nos ve perfectamente.

![img](img/imagen7.png)

Ahora vamos mostrar una página con un enlace al Real decreto del título de Administración de Sistemas Informáticos.

Nos bajamos en la máquina real el pdf y luego lo pasamos a la máquina de producción con el comando **scp** :

![img](img/imagen8.png)

En el index.html ponemos el enlace al pdf

![img](img/imagen9.png)

Actualizamos y comprobamos:

![img](img/imagen10.png)

Aqui nos muestra el enlace al fichero pdf :

![img](img/imagen20.png)

## Sitio web 2

Vamos mostrar ahora el listado de ficheros y directorios de /var/lib de la máquina de producción.

Para eso creamos el siguiente fichero varlib en sites-available hacemos el enlace simbólico y actualizamos:   

![img](img/imagen11.png)

Como podemos ver nos sale toda la información del directorio de /var/lib

![img](img/imagen12.png)

## Sitio web 3

Vamos mostrar una página web que nos pida usuario y contraseña con el nombre de todo el alumnado de clase y el certificado de seguridad ssl.

Creamos el dirrectorio students

![img](img/imagen24.png)

Vamos al archivo **ssl** en **sites-available** y añadimos la config para students, para que nos pida usuario-contraseña y prohibir explícitamente el acceso al fichero .htpasswd

![img](img/imagen23.png)

Creamos el fichero .htpasswd usando el siguiente comando:
**perl -le 'print crypt("aula108", "salt-hash")'**

y echo **"usuario1:saePqpXJa/sVk" > .htpasswd**

![img](img/imagen26.png)

![img](img/imagen25.png)

Comprobamos con contraseña y usuario

![img](img/imagen27.png)

Y como podemos ver funciona correctamente:

![img](img/imagen28.png)

## Sitio web 4

**Redirecciones**

Se debe redirigir cualquier petición de esta dirreción http://redirect.alu5627.me a http://target.alu5627.me

http://redirect.alu5627.me/test/ -> http://target.alu5627.me
http://www.redirect.alu5627.me/probando/ -> http://target.alu5627.me
http://www.redirect.alu5627.me/hola/ -> http://target.alu5627.me

Creamos el fichero redirect con la siguiente config:

![img](img/imagen15.png)

Creamos el fichero target con la siguiente config:

![img](img/imagen16.png)

Y creamos el enlace simbolico target

![img](img/imagen21.png)

Movemos el contenido de initializr de la máquina real a la máquina de producción con el comando **scp** y con esto mostraremos en http://target.alu5627.me su contenido.

![img](img/imagen13.png)

![img](img/imagen14.png)

Creamos el dirrectorio redirect en /var/log/nginx para tener estas rutas :

    /var/log/nginx/redirect/access.log
    /var/log/nginx/redirect/error.log


![img](img/imagen17.png)

![img](img/imagen18.png)

Entramos en el dominio http://redirect.alu5627.me y vemos que nos redirreciona a http://target.alu5627.me

![img](img/imagen22.png)

![img](img/imagen19.png)
