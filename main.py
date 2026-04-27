#Importación de la clase Cliente desde el archivo cliente.py
from cliente import Cliente

#Bloque de código para manejar errores al crear un objeto de la clase Cliente
try:
    #Creación de un objeto de la clase Cliente con datos de ejemplo
    cliente1 = Cliente ("123456", "Juan", "Daza")
    
    #Prueba con datos invalidos
    cliente2 = Cliente ("", "Camilo", "Guette")

    #Mostrar la información del cliente utilizando el método mostrar_informacion
    print(cliente1.mostrar_informacion())
    print(cliente2.mostrar_informacion())

#Si se intenta crear un cliente con campos vacíos, se lanzará una excepción y se mostrará 
#el mensaje de error correspondiente.
except Exception as e:
    
    #Mostrar el mensaje de error en caso de que ocurra una excepción
    print("Error", e)