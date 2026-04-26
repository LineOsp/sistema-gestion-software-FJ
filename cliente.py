"""
Definición de la Clase Cliente. 
La cual representa el cliente que usa el sistema 
(persona que quiere hacer reservas).
"""

class Cliente:

    #Constructor: Se ejecutara cuando ingrese cada cliente.
    def __init__(self, identificacion, nombre, apellido):

        #Validación de los campos vacios.
        if not identificacion:
            raise ValueError("Identificación no ingresada.Ingrese su identificación si desea continuar.")
        
        if not nombre:
            raise ValueError("Nombre no ingresado.Ingrese su nombre si desea continuar.")
        
        if not apellido:
            raise ValueError("Apellido no ingresado.Ingrese su apellido si desea continuar.")
        
        #Encapsulación: Se crean los atibutos privados, los cuales no se podran 
        # modificar directamente.
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__apellido =apellido

        #Metodo para mostrar la información ingresada. 
        def mostrar_información(self):
            return f"{self.__identificacion} | {self.__nombre} | {self.__apellido}"
        