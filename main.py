#Importación del módulo datetime para manejar fechas y horas, especialmente para registrar la fecha y hora de los errores en el archivo de logs.
from datetime import datetime
import os

#Importación de las clases Cliente, ServicioSala, ServicioEquipo, ServicioAsesoria y Reserva desde sus respectivos módulos.
from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva

#Importación de excepciones para manejar errores específicos relacionados con clientes, servicios y reservas.
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva

#Función que permitira guardar los errores en logs.txt
def guardar_log_error(error):
    
    #
    print(os.getcwd())

    #Obtener la fecha y hora actual para registrar cuándo ocurrió el error.
    fecha = datetime.now()

    #Abrir el archivo logs.txt en modo de escritura (append) para agregar nuevos errores sin sobrescribir los existentes, y escribir el mensaje de error 
    # junto con la fecha y hora en que ocurrió el error.
    with open("logs.txt", "a", encoding= "utf-8") as archivo_log: archivo_log.write(f"[{fecha}] {error}\n")


#Bloque de código principal del programa, donde se crean clientes, servicios y reservas, y se muestran sus detalles. Además, se maneja cualquier excepción que pueda ocurrir durante la ejecución del programa para garantizar que los errores se registren adecuadamente en el archivo de logs.
try:

    #Creación de clientes validos con identificaciones y nombres completos, y validando que los campos no estén vacíos para evitar errores relacionados con datos incompletos.
    cliente1 = Cliente ("123456", "Juan Daza")
    cliente2 = Cliente ("346735", "Maria Gomez")
    cliente3 = Cliente ("789012", "Carlos Perez")
    
    #Creación de servicios, incluyendo validaciones para asegurarse de que los datos ingresados 
    #sean correctos y que los valores numéricos sean positivos.
    servicio_sala = ServicioSala("Sala 101", 100, 5)
    servicio_equipo = ServicioEquipo("Proyector 03", 50, 3)
    servicio_asesoria = ServicioAsesoria("Estudiante", 200, "Estratégica")

    #Creación de reservas, asociando cada cliente con un servicio específico, y validando que se ingresen objetos válidos para cliente y servicio.
    reserva1 = Reserva(cliente1, servicio_sala)
    reserva2 = Reserva(cliente2, servicio_equipo)
    reserva3 = Reserva(cliente3, servicio_asesoria)

    #Mostrar la información de los clientes.
    print("------------------------------------------------------------")
    print("\n              INFORMACIÓN DE LOS CLIENTES                 ")
    print("------------------------------------------------------------")    

    print("\n Clientes registrados en el sistema: ")
    print("------------------------------------------------------------")  
    print(f"\n Cliente 1:")
    print(cliente1.mostrar_informacion())

    print(f"\n Cliente 2:")
    print(cliente2.mostrar_informacion())   

    print(f"\n Cliente 3:")
    print(cliente3.mostrar_informacion())   
    print("------------------------------------------------------------")   

    print("\n                DETALLES DE LOS SERVICIOS                 ")
    print("------------------------------------------------------------")  
    print(f"\n Servicio 1:")
    print(servicio_sala.detalles())

    print(f"\n Servicio 2:")
    print(servicio_equipo.detalles())

    print(f"\n Servicio 3:")
    print(servicio_asesoria.detalles())

    print("------------------------------------------------------------")    
    print("\n                DETALLES DE LAS RESERVAS                  ")
    print("------------------------------------------------------------")    
    print(f"\n Reserva 1:")
    print(reserva1.mostrar_detalles_reserva())

    print(f"\n Reserva 2:")
    print(reserva2.mostrar_detalles_reserva())

    print(f"\n Reserva 3:")
    print(reserva3.mostrar_detalles_reserva())   
    print("------------------------------------------------------------")    

    print("\n        PRUEBA DE ERROR PARA CLIENTES INVALIDOS           ") 
    print("------------------------------------------------------------")
    #Prueba de error para clientes con campos vacíos, lo que debería generar una excepción y mostrar un mensaje de error claro.
    cliente_invalido = Cliente("", "")


#Manejo de excepciones para capturar errores específicos relacionados con clientes, servicios y reservas, y mostrar 
# mensajes de error claros en caso de que ocurra una excepción.
except ErrorCliente as e:
    print(f"Error de cliente:", e)
    guardar_log_error(e)

except ErrorServicio as e:
    print(f"Error de servicio:", e)
    guardar_log_error(e)

except ErrorReserva as e:
    print(f"Error de reserva:", e)
    guardar_log_error(e)

except Exception as e:
    print(f"Error inesperado:", e)
    guardar_log_error(e)