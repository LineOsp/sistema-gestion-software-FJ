#Importación de la clase "ErrorReserva" desde el archivo "excepciones.py" para manejar errores específicos relacionados con reservas.
from excepciones import ErrorReserva

#Impotación de las clases Cliente y Servicio para establecer la relación entre un cliente y el servicio que desea reservar.
from cliente import Cliente 
from servicio import Servicio

#Clase Reserva
# Representa la relación que existe entre un cliente y el servicio que desea.
class Reserva:
    def __init__(self, cliente, servicio):
        
        #Validación para asegurarse de que se ingrese un cliente y un servicio válidos.
        if not isinstance (cliente, Cliente):
            raise ErrorReserva("❌ Debe ingresar un cliente válido.")
        
        if not isinstance (servicio, Servicio):
            raise ErrorReserva("❌ Debe ingresar un servicio válido.")
        
        #Asociación entre el cliente y el servicio
        self._cliente = cliente
        self._servicio = servicio

    #Creación de un método para mostrar los detalles de la reserva, incluyendo la información del cliente y los detalles del servicio.
    def mostrar_detalles_reserva(self):
        return f"{self._cliente.mostrar_informacion()} \n{self._servicio.detalles()}"
