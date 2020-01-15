# 2019-2-DropTable----T4

Aquí se implementa los requisitos pedidos para la Tarea 4 del curso
CC4401. El repositorio contiene lo siguiente: implementación del
modelo de datos, formularios de autentificación para iniciar
sesión/registrarse en el sistema, y la posibilidad de cambiar los
datos del usuario, tales como la contraseña y foto de perfil.


Para instalar los requerimientos necesarios para ejecutar la
aplicación, escribir el siguiente comando desde una terminal:

`$ pip install -r requirements.txt`


Para probar la funcionalidad de la aplicación, se debe seguir los siguientes pasos:

* Levantar el servidor con ```python manage.py runserver``` desde el
  directorio raíz del proyecto.

* Visitar localhost:8000 desde el navegador.

* Si el usuario ya se encuentra registrado, ir a la pestaña *Inicia sesión*.

* Si no, ir a la pestaña *Registrarse* e ingresar los datos de
  registro. Una vez finalizado el proceso, se podrá iniciar sesión al
  igual que en el paso anterior.

* Una vez iniciada la sesión, se puede ir a la pestaña *Perfil -> Mi
  Perfil* para revisar los datos personales y cambiar la imagen del
  usuario. Desde la pestaña *Seguridad* se puede cambiar la
  contraseña.
