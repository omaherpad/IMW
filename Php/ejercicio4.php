<!doctype html>
<html>
  <body>
     <form action="index.php" method="post">
      <label for="filas">Filas:</label>
      <input type="text" name="filas"/><br>

      <label for="columnas">Columnas:</label>
        <input type="text" name="columnas"/><br>

      <input type="submit" value="Enviar"/>
     </form>
     <table border="1">
     <?php
       if (isset($_POST["filas"]) and isset($_POST["columnas"])) {
         $filas = (float)$_POST["filas"];
         $columnas = (float)$_POST["columnas"];
         $i_c = 1;
         $i_f = 1;
         if ($filas >= 1 and $columnas >= 1) {
           echo("<p>Tablas y columnas:</p>");
           while ($i_f<=$filas) {
             $i_f++;
             echo("<tr>");
             while ($i_c<=$columnas) {
               $i_c++;
               echo("<td>Prueba</td>");
             }
             $i_c = 1;
             echo("</tr>");
           }
         }
         else{
           echo("Dato incorrecto");
         }
       }
    ?>
    </table>
  </body>
</html>

