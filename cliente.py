#Importación de la clase "ErrorCliente" desde el archivo "excepciones.py" para manejar errores específicos relacionados con clientes.
from excepciones import ErrorCliente

"""
Definición de la clase cliente
Representa un cliente que ingresa en el sistema.

"""
class Cliente:
    
    #Constructor de la clase
    #Se ejecutara automaticamente cuando se crea el objeto "Cliente"
    def __init__(self, identificacion, nombre_apellido):

        #Validación de campos vacíos
        if not identificacion:
            raise ErrorCliente("❌ La identificación no puede estar vacía.")
        
        if not nombre_apellido:
            raise ErrorCliente("❌ El nombre y apellido no pueden estar vacíos.")
        
        #Encapsulación: Esto permitira proteger los datos ingresados usando doble guión(__)
        self.__identificacion = identificacion
        self.__nombre_apellido = nombre_apellido   

        #Método que permitira mostrar la información ingresada.
    def mostrar_informacion(self):
        return f"{ self.__identificacion} | {self.__nombre_apellido}"