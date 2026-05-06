#Sistema de Gestión de Servicios y Reservas.

##📌Descripción del proyecto:
- Este proyecto fue desarrollado en Python aplicando la Programación Orientada a Objetos (POO). El sistema permite gestionar clientes, servicios y reservas, utilizando conceptos como herencia, encapsulación, abstracción, polimorfismo y un buen manejo de excepciones. Por otra parte, el sistema permite registrar automaticamente errores que se generen enviandolos automaticamente a un archivo de logs. 

##📌Tecnologías que han sido utilizadas:
- Python
-Git
- GitHub
- Visual Studio Code 

#📌Estructura del proyecto:
sistema-gestion-software-FJ/ 
- cliente.py 
- servicio.py 
- reserva.py 
- excepciones.py 
- main.py 
- logs.txt 
- README.md 
- .gitignore 
- LICENSE

##📌Descripción de los archivos del proyecto:

- cliente.py

Contiene la clase Cliente, la cual esta encargada de almacenar la infornación de todos los clientes que ingresen al sistema. 

- servicio.py

Contiene la clase abstracta Servicio, y las clases derivadas (o clases hijas) llamadas:

 - ServicioSala
 - ServicioEquipo
 - ServicioAsesoria

En este archivo se implementa la herencia, abstracción y polimorfismo. 

- reserva.py

Se relacionan los clientes con los servicios para luego generar las reservas dentro del sistema. 

- excepciones.py

Contiene excepciones personalizadas dependiendo del servicio:

 - ErrorCliente
 - ErrorServicio
 - ErrorReserva

Encargada de capturar los errores dentro del sistema.

- main.py

Achico principal del proyecto. Es el encargado de ejecutar e integrar todo el sistema.

- logs.txt

Archivo donde se guardaran automáticamente los errores que se generen durante la ejecución del programa.

##📌Funcionalidades que contiene el Sistema:

- Registrar clientes.
- Gestionar servicios.
- Crear reservas.
- Validar datos.
- Manejar excepciones completamente personalizadas.
- Guardar los errores en logs.
- Integración del sistema completo.

##📌Conceptos aplicados:

- Programación Orientada a Objetos (POO)
- Herencia
- Abstracción
- Polimorfismo
- Manejo de excepciones
- Modularidad

##📌Como se debe ejecutar el proyecto:

- Clonar el repositorio:

git clone https://github.com/LineOsp/sistema-gestion-software-FJ

- Ingresar a la carpeta de proyecto:

cd sistema-gestion-software-FJ

- Ejecutar el sistema:

python main.py

##📌Ejemplo de ejecución del sistema:

- Ejemplo de clientes registrados:

              INFORMACIÓN DE LOS CLIENTES                 

 Cliente 1:
123456 | Juan Daza

 Cliente 2:
346735 | Maria Gomez


- Ejemplo de servicios registrados:
 
                DETALLES DE LOS SERVICIOS                 
 
 Servicio 1:
Sala 101, con un costo de 500 por 5 horas de alquiler.

 Servicio 2:
Proyector 03, con un costo de 150 por 3 días de alquiler.
 

- Ejemplo de reservas registradas:
 
                DETALLES DE LAS RESERVAS                  
 
 Reserva 1:
123456 | Juan Daza 
Sala 101, con un costo de 500 por 5 horas de alquiler..

 Reserva 2:
346735 | Maria Gomez 
Proyector 03, con un costo de 150 por 3 días de alquiler..
 

- Ejemplo de manejo de errores:

Error de cliente: ❌ La identificación no puede estar vacía.

- Ejemplo de registro en logs.txt

[2026-05-06 12:25:54.272349] ❌ La identificación no puede estar vacía.

##📌Validaciones del sistema:

El sistema crea validaciones que permite detectar errores como son:
 - Campos vacíos
 - Precios negativos
 - Cantidades inválidas
 - Reservas incorrectas

Cada error que sea detectado sera almacenado directamente en el archivo logs.txt

##📌Evidencia del desarrollo del sistema:

El proyecto ha sido creado utilizando Git y GitHub, dejando evidencias constantes por medio de commits y actualizaciones para mejoras de repositorio.

##📌Autores:

Liney Paola Ospino Vergel

##📌Estado actual del proyecto:

¡Proyecto en fase final! 
Se estan integrando pruebas y documentación. 