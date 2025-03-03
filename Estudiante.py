# Clase Estudiante hereda de Persona
from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)  # Llamamos al constructor de la clase base (Persona)
        self.__curso = curso  # Atributo específico de Estudiante

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    def __str__(self):
        return f"{super().__str__()}, Curso: {self.curso}"


