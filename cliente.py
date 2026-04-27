"""
Definición de la clase cliente
Representa un cliente que ingresa en el sistema.

"""

class Cliente:
    
    #Constructor de la clase
    #Se ejecutara automaticamente cuando se crea el objeto "Cliente"
    def __init__(self, identificacion, nombre, apellido):

        #Validación de campos vacíos
        if not identificacion:
            raise ValueError("❌ La identificación no puede estar vacía.")
        
        if not nombre:
            raise ValueError("❌ El nombre no puede estar vacío.")
        
        if not apellido:
            raise ValueError("❌ El apellido no puede estar vacío.")
        
        #Encapsulación: Esto permitira proteger los datos ingresados usando doble guión(__)
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__apellido = apellido

        #Método que permitira mostrar la información ingresada.
    def mostrar_informacion(self):
        return f"{ self.__identificacion} | {self.__nombre} | {self.__apellido}"
        
