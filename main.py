#Importación del módulo datetime para manejar fechas y horas, especialmente para registrar la fecha y hora de los errores en el archivo de logs.
from datetime import datetime
import os

#Importación de clases del sistema. 
from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva

#Importación de excepciones perzonalizadas.
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva

#Función para guardar los errores en logs.txt
def guardar_log_error(error):
    
    print(os.getcwd())

    #Obtener la fecha y hora actual para registrar cuándo ocurrió el error.
    fecha = datetime.now()

    #Guarda el error en logs.txt
    with open("logs.txt", "a", encoding= "utf-8") as archivo_log: archivo_log.write(f"[{fecha}] {error}\n")


#----------------------------------------------
#             INICIO DEL SISTEMA             
#----------------------------------------------
try:

    #------------------------------------------
    #          CREACIÓN DE CLIENTES   
    #------------------------------------------
    cliente1 = Cliente ("123456", "Juan Daza")
    cliente2 = Cliente ("346735", "Maria Gomez")
    cliente3 = Cliente ("789012", "Carlos Perez")
    
    #------------------------------------------
    #         CREACIÓN DE SERVICIOS
    #------------------------------------------
    servicio_sala = ServicioSala("Sala 101", 100, 5)
    servicio_equipo = ServicioEquipo("Proyector 03", 50, 3)
    servicio_asesoria = ServicioAsesoria("Estudiante", 200, "Estratégica")
    
    #------------------------------------------
    #          CREACIÓN DE RESERVAS
    #------------------------------------------
    reserva1 = Reserva(cliente1, servicio_sala)
    reserva2 = Reserva(cliente2, servicio_equipo)
    reserva3 = Reserva(cliente3, servicio_asesoria)

    #------------------------------------------
    #      INFORMACIÓN DE CLIENTES
    #------------------------------------------
    print("\n------------------------------------------------------------")
    print("              INFORMACIÓN DE LOS CLIENTES                 ")
    print("------------------------------------------------------------")    

    print(f"\n Cliente 1:")
    print(cliente1.mostrar_informacion())

    print(f"\n Cliente 2:")
    print(cliente2.mostrar_informacion())   

    print(f"\n Cliente 3:")
    print(cliente3.mostrar_informacion())   

    #------------------------------------------
    #       INFORMACIÓN DE SERVICIOS
    #------------------------------------------
    print("\n------------------------------------------------------------")   
    print("                DETALLES DE LOS SERVICIOS                   ")
    print("------------------------------------------------------------")  
    print(f"\n Servicio 1:")
    print(servicio_sala.detalles())

    print(f"\n Servicio 2:")
    print(servicio_equipo.detalles())

    print(f"\n Servicio 3:")
    print(servicio_asesoria.detalles())

    #------------------------------------------
    #       INFORMACIÓN DE RESERVAS
    #------------------------------------------
    print("\n------------------------------------------------------------")    
    print("                 DETALLES DE LAS RESERVAS                   ")
    print("------------------------------------------------------------")    
    print(f"\n Reserva 1:")
    print(reserva1.mostrar_detalles_reserva())

    print(f"\n Reserva 2:")
    print(reserva2.mostrar_detalles_reserva())

    print(f"\n Reserva 3:")
    print(reserva3.mostrar_detalles_reserva())   

#Bloques de manejo de excepciones encargados de capturar errores específicos relacionados con clientes, servicios y reservas.
#Además de mostrar mensajes claros en consola, los errores son almacenados automáticamente en logs.txt para mantener un registro del sistema.
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

#------------------------------------------
#          PRUEBA DE ERRORES  
#------------------------------------------
print("\n------------------------------------------------------------")    
print("                    PRUEBAS DE ERRORES                      ")
print("------------------------------------------------------------") 

#Prueba de cliente inválido
try:
    error_cliente = Cliente("", "")

except ErrorCliente as e:
    print("Error de cliente:", e)
    guardar_log_error(e)

#Prueba de servicio con precio negativo
try:
    error_servicio = ServicioSala("Sala 105", -100, 5)

except ErrorServicio as e:
    print("Error de servicio:", e)
    guardar_log_error(e)

#Prueba con precio no numérico
try:
    error_servicio = ServicioEquipo("Proyector 05", "cincuenta", 3)

except ErrorServicio as e:
    print("Error de servicio:", e)
    guardar_log_error(e)

#Prueba de reserva sin cliente
try:
    error_reserva = Reserva(None, servicio_sala)
except ErrorReserva as e:
    print("Error de reserva:", e)
    guardar_log_error(e)

#Prueba de reserva sin servicio
try:
    error_reserva = Reserva(cliente1, None)
except ErrorReserva as e:
    print("Error de reserva:", e)
    guardar_log_error(e)

#Prueba de horas de alquiler negativas
try:
    error_servicio = ServicioSala("Sala 104", 100, -6)

except ErrorServicio as e:
    print("Error de servicio:", e)
    guardar_log_error(e)

#Prueba de horas de alquiler no numéricas
try:
    error_servicio = ServicioSala("Sala 90", 100, "siete")

except ErrorServicio as e:
    print("Error de servicio:", e)
    guardar_log_error(e)