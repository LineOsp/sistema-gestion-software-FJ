#Importación de las clases Cliente, ServicioSala, ServicioEquipo, ServicioAsesoria y Reserva desde sus respectivos módulos.
from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva

#Importación de excepciones para manejar errores específicos relacionados con clientes, servicios y reservas.
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva

#Bloque de código para manejar errores al crear un objeto de la clase Cliente
try:

    #Creación de clientes.
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


#Manejo de excepciones para capturar errores específicos relacionados con clientes, servicios y reservas, y mostrar 
# mensajes de error claros en caso de que ocurra una excepción.
except ErrorCliente as e:
    print(f"Error de cliente: {e}")

except ErrorServicio as e:
    print(f"Error de servicio: {e}")

except ErrorReserva as e:
    print(f"Error de reserva: {e}")

except Exception as e:
    print(f"Error inesperado: {e}")