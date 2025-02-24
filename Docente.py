# Clase Docente hereda de Persona
from Persona import Persona

class Docente(Persona):
    def __init__(self, nombre, edad, direccion, tipoContrato):
        super().__init__(nombre, edad, direccion)  # Llamamos al constructor de la clase base (Persona)
        self.__tipoContrato = tipoContrato  # Atributo específico de Docente

    def get_tipoContrato(self):
        return self.__tipoContrato
    
    def set_tipoContrato(self, tipoContrato):
        self.__tipoContrato=tipoContrato

    def __str__(self):
        return f"{super().__str__()}, TipoContrato: {self.get_tipoContrato}"