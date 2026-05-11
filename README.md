# Sistema de Gestión de Servicios y Reservas.

## 📌Descripción del proyecto:

Este proyecto fue desarrollado en Python aplicando la Programación Orientada a Objetos (POO). El sistema permite gestionar clientes, servicios y reservas, utilizando conceptos como herencia, encapsulación, abstracción, polimorfismo y un buen manejo de excepciones. Por otra parte, el sistema permite registrar automáticamente errores que se generen enviandolos automáticamente a un archivo de logs. 

Se enfoca en la robustez operativa mediante el uso de:

- Abstracción: Definición de moldes base para servicios.

- Herencia y Polimorfismo: Especialización de categorías con comportamientos únicos.

- Encapsulación: Protección de datos sensibles de clientes y costos.

- Gestión de Excepciones: Un sistema de control de errores que garantiza que la aplicación no se detenga ante entradas inválidas, derivando los fallos a un archivo de logs para su posterior auditoría.

## 📌Objetivo del proyecto:

Aplicar conceptos de programación orientada a objetos por medio de el lenguaje de programación Python capaz de gestionar clientes, servicios y reservas, incorporando validaciones, excepciones personalizadas 
y registro de errores para fortalecer organización y confiabilidad del sistema. 

## 📌Tecnologías que han sido utilizadas:
- Python
- Git
- GitHub
- Visual Studio Code 

## 📌Estructura del proyecto:
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

## 📌Descripción de los archivos del proyecto:

- cliente.py

Implementa la clase Cliente, actuando como el repositorio de atributos para los usuarios (ID, Nombre). Permite la instanciación de perfiles únicos dentro de la memoria del sistema.

- servicio.py

Contiene la clase abstracta Servicio, y las clases derivadas (o clases hijas) llamadas:

 - ServicioSala: Especializado en gestión de espacios físicos.
 - ServicioEquipo: Orientado a prestamos de equipos electronicos.
 - ServicioAsesoria: Enfocado en horas de consultoría profesional.

En este archivo se implementa la herencia, abstracción y polimorfismo. 

- reserva.py

Actúa como el motor de vinculación. Se encarga de instanciar objetos que conectan un objeto Cliente con un objeto Servicio, generando un registro de transacción válido.

- excepciones.py

Contiene excepciones personalizadas dependiendo del servicio:

 - ErrorCliente
 - ErrorServicio
 - ErrorReserva

Encargada de capturar los errores dentro del sistema.

- main.py

Es el núcleo ejecutable. Implementa el menú interactivo, gestiona el flujo de datos entre clases y contiene el bloque try-except principal para la captura de errores globales.

- logs.txt

Funciona como una base de datos de texto plano donde se anexan (append) las trazas de error con fecha y hora, facilitando el mantenimiento preventivo.

## 📌Funcionalidades del proyecto:

- Registrar clientes: Alta validación de clientes.
- Gestionar servicios: Gestión de servicios con diferentes lógicas de cobro.
- Crear reservas: Generación de comprobantes de servicio vinculados.
- Validar datos: Verificación de tipos de datos y rangos numéricos.
- Manejar excepciones completamente personalizadas: Tratamiento de errores personalizado por módulo.
- Integración del sistema completo: Escritura automatizada de fallos en disco.
- Guardar los errores en logs: Conexión fluida entre todos los componentes del software.

## 📌Conceptos aplicados:

- Programación Orientada a Objetos (POO): Organización basada en objetos que interactúan entre sí.
- Herencia: Reutilización de código de Servicio en clases hijas.
- Abstracción: Uso de métodos abstractos para definir contratos de código.
- Polimorfismo: Capacidad de ejecutar calcular_costo() de diferentes maneras según el objeto.
- Manejo de excepciones: Uso de raise y catch para control de flujo.
- Modularidad: Separación de archivos para facilitar el escalamiento.

## 📌Cómo se debe ejecutar el proyecto:

- 1️⃣Clonar el repositorio:

git clone https://github.com/LineOsp/sistema-gestion-software-FJ

- 2️⃣Ingresar a la carpeta de proyecto:

cd sistema-gestion-software-FJ

- 3️⃣Ejecutar el sistema:

python main.py

## 📌Ejemplo de ejecución del sistema:

- ➡️Ejemplo de clientes registrados:

              INFORMACIÓN DE LOS CLIENTES                 

 Cliente 1:

123456 | Juan Daza

 Cliente 2:

346735 | Maria Gomez


- ➡️Ejemplo de servicios registrados:
 
                DETALLES DE LOS SERVICIOS                 
 
 Servicio 1:

Sala 101, con un costo de 500 por 5 horas de alquiler.

 Servicio 2:

Proyector 03, con un costo de 150 por 3 días de alquiler.
 

- ➡️Ejemplo de reservas registradas:
 
                DETALLES DE LAS RESERVAS                  
 
 Reserva 1:

123456 | Juan Daza 

Sala 101, con un costo de 500 por 5 horas de alquiler..

 Reserva 2:

346735 | Maria Gomez 

Proyector 03, con un costo de 150 por 3 días de alquiler..
 

- ➡️Ejemplo de manejo de errores:

Error de cliente: ❌ La identificación no puede estar vacía.

- ➡️Ejemplo de registro en logs.txt

[2026-05-06 12:25:54.272349] ❌ La identificación no puede estar vacía.

## 📌Validaciones del sistema:

El sistema implementa diferentes validaciones que permite detectar errores relacionados con clientes, servicios y reservas.

Tales como:
 - Campos vacíos
 - Precios negativos
 - Cantidades inválidas
 - Reservas incorrectas

Cada error que sea detectado será almacenado directamente en el archivo logs.txt

## 📌Evidencia del desarrollo del sistema:

El proyecto ha sido creado utilizando Git y GitHub, dejando evidencias constantes por medio de commits y actualizaciones para mejoras de repositorio.

## 📌Registro de errores en logs.txt

El proyecto cuenta con un archivo llamado logs.txt, encargado de almacenar automáticamente todos los errores que presente el sistema durante la ejecución del 
proyecto. Cada registro incluye fecha, hora y descripción del error para facilitar el seguimineto y control de fallos en el sistema. 

## 📌Autores:

Liney Paola Ospino Vergel

Edwin Yair Barreto Bertel

## 📌Conclusión
 
El desarrollo de este proyecto permitió aplicar los principales conceptos de programación orientada a objetos en Python, fortaleciendo el manejo de clases, herencia, excepciones personalizadas y trabajo colaborativo mediante Git y GitHub. Además, se logró construir un sistema organizado y funcional capaz de gestionar servicios, clientes y reservas de manera eficiente.
