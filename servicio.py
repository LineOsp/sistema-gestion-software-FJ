from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre_apellido, precio):
        if not nombre_apellido:
            raise ValueError("❌ El nombre y apellido del servicio no pueden estar vacíos.")
        
        if precio <= 0:
            raise ValueError("❌ El precio del servicio debe ser un valor positivo.")
        
        self._nombre_apellido = nombre_apellido
        self._precio = precio

    @abstractmethod
    def calcular_costo(self):
         pass

    @abstractmethod
    def detalles(self):
         pass

class ServicioSala(Servicio):
    def __init__(self, nombre_apellido, precio, horas_alquiler):
          super().__init__(nombre_apellido, precio)
          
          if horas_alquiler <= 0:
               raise ValueError("❌ Las horas de alquiler deben ser un valor positivo, mayor a cero.")
          
          self._horas_alquiler = horas_alquiler

    def calcular_costo(self):
            return self._precio * self._horas_alquiler
    def detalles(self):
            return f"Servicio de sala para {self._nombre_apellido}, con un costo de {self.calcular_costo()} por {self._horas_alquiler} horas de alquiler."
     

class ServicioEquipo(Servicio):
    def __init__(self, nombre_apellido, precio, dias_alquiler):
        super().__init__(nombre_apellido, precio)
        
        if dias_alquiler <= 0:
            raise ValueError("❌ Los días de alquiler deben ser un valor positivo, mayor a cero.")

        self._dias_alquiler = dias_alquiler

    def calcular_costo(self):
         return self._precio * self._dias_alquiler

    def detalles(self):
         return f"Servicio de equipo para {self._nombre_apellido}, con un costo de {self.calcular_costo()} por {self._dias_alquiler} días de alquiler."
      
class ServicioAsesoria(Servicio):
    def __init__(self, nombre_apellido, precio, tipo_asesoria):
        super().__init__(nombre_apellido, precio)
        
        if not tipo_asesoria:
            raise ValueError("❌ Especifique el tipo de asesoría.")
              
        self._tipo_asesoria = tipo_asesoria

    def calcular_costo(self):
        if self._tipo_asesoria == "tecnica":
            return self._precio
        elif self._tipo_asesoria == "estratégica":
            return self._precio * 1.5
        elif self._tipo_asesoria == "personalizada":
            return self._precio * 2
        else:
            raise ValueError("❌ Tipo de asesoría no reconocido. Use 'tecnica', 'estratégica' o 'personalizada'.")
            
    def detalles(self):
            return f"Servicio de asesoría {self._tipo_asesoria} para {self._nombre_apellido}, con un costo de {self.calcular_costo()}."
