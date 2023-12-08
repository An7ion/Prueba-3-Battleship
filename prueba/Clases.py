class vehiculo:

    def __init__(self, Patente,Marca,Modelo,Color,NumeroMotor) -> None:
        self.__Patente = Patente 
        self.__Marca  = Marca
        self.__Modelo = Modelo
        self.__Color = Color
        self.__NumeroMotor = NumeroMotor
  
    def getPatente(self):
        return self.__Patente
    
    def getMarca(self):
        return self.__Marca
    
    def getModelo(self):
        return self.__Modelo
    
    def getColor(self):
        return self.__Color

    def getNumeroMotor(self):
        return self.__NumeroMotor
    
class Mecanico:

    def __init__(self, Rut,Nombre,Telefono,Direccion) -> None:
        self.__Rut = Rut
        self.__Nombre  = Nombre
        self.__Telefono = Telefono
        self.__Direccion = Direccion
  
    def getRut(self):
        return self.__Rut
    
    def getNombre(self):
        return self.__Nombre
    
    def getTelefono(self):
        return self.__Telefono
    
    def getDireccion(self):
        return self.__Direccion

class Reparaciones:

    def __init__(self, Cod_Reparaciones,Fecha,DescripcionFalla,VehiculoReparado,RutMecanico,DetalleReparacion,ValorReparacion) -> None:
        self.__Cod_Reparaciones = Cod_Reparaciones
        self.__Fecha  = Fecha
        self.__DescripcionFalla = DescripcionFalla
        self.__VehiculoReparado = VehiculoReparado
        self.__RutMecanico = RutMecanico
        self.__DetalleReparacion = DetalleReparacion
        self.__ValorReparacion = ValorReparacion
  
    def getCod_Reparaciones(self):
        return self.__Cod_Reparaciones
    
    def getFecha(self):
        return self.__Fecha
    
    def getDescripcionFalla(self):
        return self.__DescripcionFalla
    
    def getVehiculoReparado(self):
        return self.__VehiculoReparado

    def getRutMecanico(self):
        return self.__RutMecanico
    
    def getDetalleReparacion(self):
        return self.__DetalleReparacion
    
    def getValorReparacion(self):
        return self.__ValorReparacion