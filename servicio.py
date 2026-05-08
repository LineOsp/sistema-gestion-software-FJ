#Importación de la clase "ErrorServicio" desde el archivo "excepciones.py" para manejar errores específicos relacionados con servicios.
from excepciones import ErrorServicio

"""
Clase abstracta Servicio que define la estructura básica para los servicios ofrecidos 
por el sistema de gestión de software.
"""
from abc import ABC, abstractmethod

class Servicio(ABC):

    #Validación del constructor para asegurar que los campos no estén vacíos 
    # y que el precio sea un valor positivo.
    def __init__(self, nombre_apellido, precio):
        
        if not nombre_apellido.strip():
            raise ErrorServicio("❌ El nombre y apellido del servicio no pueden estar vacíos.")
        
        if not isinstance(precio, (int, float)):
            raise ErrorServicio("❌ El precio del servicio debe ser un valor numérico válido.")
        
        if precio <= 0:
            raise ErrorServicio("❌ El precio del servicio debe ser un valor positivo, mayor a cero.")
        
        
        #Atributos protegidos para almacenar el nombre, apellido y su precio.
        self._nombre_apellido = nombre_apellido
        self._precio = precio

    #Métodos abstractos que deben ser implementados por las clases hijas 
    # para calcular el costo y mostrar los detalles del servicio.
    @abstractmethod
    def calcular_costo(self):
         pass

    @abstractmethod
    def detalles(self):
         pass

#Clase ServicioSala que hereda de la clase Servicio y representa un servicio de alquiler de sala.
class ServicioSala(Servicio):
    def __init__(self, nombre_apellido, precio, horas_alquiler):
          #Llamada al constructor de la clase padre para inicializar los atributos comunes.
          super().__init__(nombre_apellido, precio)
          
          if not isinstance(horas_alquiler, (int, float)):
               raise ErrorServicio("❌ Las horas de alquiler deben ser un valor numérico válido.")
          
          if horas_alquiler <= 0:
               raise ErrorServicio("❌ Las horas de alquiler deben ser un valor numérico válido.")
          
          
          self._horas_alquiler = horas_alquiler
    
    #Calcula el costo total del servicio multiplicando el precio por las horas de alquiler.
    def calcular_costo(self):
            return self._precio * self._horas_alquiler
    
    #Describe los detalles del servicio, incluyendo el nombre del cliente, el costo total y las horas de alquiler.
    def detalles(self):
            return f"Alquiler de {self._nombre_apellido}, con un costo de {self.calcular_costo()} por {self._horas_alquiler} horas."
     

#Clase ServicioEquipo que hereda de la clase Servicio y representa un servicio de alquiler de equipo.
class ServicioEquipo(Servicio):
    def __init__(self, nombre_apellido, precio, dias_alquiler):
        #Llamada al constructor de la clase padre para inicializar los atributos comunes.
        super().__init__(nombre_apellido, precio)
        
        if not isinstance(dias_alquiler, (int, float)):
            raise ErrorServicio("❌ Los días de alquiler deben ser un número positivo.")
        
        if dias_alquiler <= 0:
            raise ErrorServicio("❌ Los días de alquiler deben ser un valor numérico válido.")

        self._dias_alquiler = dias_alquiler

    #Calcula el costo total del servicio multiplicando el precio por los días de alquiler.
    def calcular_costo(self):
         return self._precio * self._dias_alquiler
    
    #Describe los detalles del servicio, incluyendo el nombre del cliente, el costo total y los días de alquiler.
    def detalles(self):
         return f"Alquiler de {self._nombre_apellido}, con un costo de {self.calcular_costo()} por {self._dias_alquiler} días."


#Clase ServicioAsesoria que hereda de la clase Servicio y representa un servicio de asesoría.
class ServicioAsesoria(Servicio):
    def __init__(self, nombre_apellido, precio, tipo_asesoria):
        #Llamada al constructor de la clase padre para inicializar los atributos comunes.
        super().__init__(nombre_apellido, precio)

        if not isinstance(tipo_asesoria, str):
            raise ErrorServicio("❌ El tipo de asesoría debe ser una cadena de texto.") 
        
        if not tipo_asesoria.strip():
            raise ErrorServicio("❌ Especifique el tipo de asesoría.")
          
        self._tipo_asesoria = tipo_asesoria
 
    #Calcula el costo del servicio de asesoría basado en el tipo de asesoría.
    def calcular_costo(self):
        if self._tipo_asesoria == "Técnica":
            return self._precio
        elif self._tipo_asesoria == "Estratégica":
            return self._precio * 2
        elif self._tipo_asesoria == "Personalizada":
            return self._precio * 3
        else:
            raise ErrorServicio("❌ Tipo de asesoría no reconocido. Use 'Técnica', 'Estratégica' o 'Personalizada'.")

    #Describe los detalles del servicio de asesoría, incluyendo el nombre del cliente, el tipo de asesoría y el costo total.     
    def detalles(self):
            return f"Asesoria {self._tipo_asesoria} para {self._nombre_apellido}, con un costo de {self.calcular_costo()}."
 