#Impotación de las clases Cliente y Servicio
from cliente import Cliente 
from servicio import Servicio

#Clase Reserva
# Representa la relación que existe entre un cliente y el servicio que desea.
class Reserva:
    def __init__(self, cliente, servicio):
        
        #Validación para asegurarse de que se ingrese un cliente y un servicio válidos.
        if not isinstance (cliente, Cliente):
            raise ValueError("❌ Debe ingresar un cliente válido.")
        
        if not isinstance (servicio, Servicio):
            raise ValueError("❌ Debe ingresar un servicio válido.")
        
        #Asociación entre el cliente y el servicio
        self._cliente = cliente
        self._servicio = servicio

    #Creación de un método para mostrar los detalles de la reserva, incluyendo la información del cliente y los detalles del servicio.
    def mostrar_detalles_reserva(self):
        return f"Reserva para {self._cliente.mostrar_informacion()} | {self._servicio.detalles()}."
