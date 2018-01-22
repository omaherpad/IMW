# WordPress

Lo primero, si estamos trabajando con una máquina de producción con poca memoria RAM, en este caso, sólo 512MB, debemos activar el Swap para no tener problemas con los servicios.

Entramos en mysql.

![imagen](./img/imagen1.png)

Creamos la base de datos, el usuario y asignamos privilegios:

![imagen](./img/imagen2.png)

Descargamos el código fuente de Wordpress desde su página web:

![imagen](./img/imagen3.png)

A continuación descomprimimos el código y lo copiamos en /usr/share:

![imagen](./img/imagen4.png)

![imagen](./img/imagen5.png)

Ahora tenemos que establecer los permisos necesarios para que el usuario web www-data pueda usar estos ficheros:

![imagen](./img/imagen6.png)

Vamos a editar ficheros de configuración.

Debemos especificar el nombre de la base de datos, el usuario y la contraseña, para que Wordpress pueda usarlos:

![imagen](./img/imagen8.png)

![imagen](./img/imagen7.png)

Para que nuestro sitio Wordpress sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del servidor web Nginx.

![imagen](./img/imagen9.png)

Enlazamos la configuración para que el virtual host esté disponible:

![imagen](./img/imagen10.png)

![imagen](./img/imagen11.png)

Reiniciamos el servicio Nginx:

![imagen](./img/imagen12.png)

Ahora podemos acceder a la dirección de nuestro servidor para configurar nuestro Wordpress vía web.

Realizamos las configuraciones correspondientes:

![imagen](./img/imagen13.png)

![imagen](./img/imagen14.png)

![imagen](./img/imagen15.png)

Accedemos a la interfaz administrativa de Wordpress tras inicio de sesión:

![imagen](./img/imagen16.png)

Por defecto, el límite de subida de archivos para aplicaciones PHP suele ser bastante bajo, en torno a los 2MB.

Para incrementarlo, debemos hacer lo siguiente, como root en la máquina de producción:

![imagen](./img/imagen20.png)

![imagen](./img/imagen17.png)

![imagen](./img/imagen18.png)

![imagen](./img/imagen19.png)

Ahora reiniciamos el servicio php-fpm:

![imagen](./img/imagen21.png)

Además de esto, debemos añadir una línea en el fichero de configuración de Nginx y reiniciar el servicio:

![imagen](./img/imagen23.png)

![imagen](./img/imagen22.png)

**Ajuste de permalinks**

En primer lugar activamos esta opción dentro de la interfaz administrativa de Wordpress:

![imagen](./img/imagen24.png)

Ahora debemos indicar a Nginx que procese estas URLs:

![imagen](./img/imagen26.png)

![imagen](./img/imagen25.png)

Entramos en nuestro **Wordpress**:

Instalamos y activamos un tema gratuito.

![imagen](./img/imagen27.png)

![imagen](./img/imagen28.png)

![imagen](./img/imagen29.png)

Escribimos un post con las estadísticas de uso de Wordpress vistas en clase y entramos a dicho post.

![imagen](./img/imagen30.png)

![imagen](./img/imagen31.png)
