#Clase base para representar errores en el sistema de gestión de servicios.
class ErrorSistema(Exception):
    pass

#Excepción específica para cada tipo de error de cliente, heredando de la clase base ErrorSistema.
class ErrorCliente(ErrorSistema):
    pass

#Excepción específica para cada tipo de error de servicio, heredando de la clase base ErrorSistema.
class ErrorServicio(ErrorSistema):
    pass

#Excepción específica para cada tipo de error de reserva, heredando de la clase base ErrorSistema.
class ErrorReserva(ErrorSistema):
    pass