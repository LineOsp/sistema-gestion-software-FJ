#Importación de la clase Cliente desde el archivo cliente.py
from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria

#Bloque de código para manejar errores al crear un objeto de la clase Cliente
try:
    #Prueba de creación de un cliente con datos válidos
    cliente1 = Cliente ("123456", "Juan Daza")
    
    #Prueva de los servicios
    servicio_sala = ServicioSala("Sala 101", 100, 5)
    servicio_equipo = ServicioEquipo("Equipo 1003", 50, 3)
    servicio_asesoria = ServicioAsesoria("Asesoría 1", 200, "estratégica")


    #Mostrar la información del cliente utilizando el método mostrar_informacion
    print(cliente1.mostrar_informacion())
    
    #Mostrar los detalles de los servicios
    print(servicio_sala.detalles())
    print(servicio_equipo.detalles())
    print(servicio_asesoria.detalles())

#Si se intenta crear un cliente con campos vacíos, se lanzará una excepción y se mostrará 
#el mensaje de error correspondiente.
except Exception as e:
    
    #Mostrar el mensaje de error en caso de que ocurra una excepción
    print("Error", e)