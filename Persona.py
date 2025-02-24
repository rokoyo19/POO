class Persona:
    def __init__(self, nombre, edad, direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion=direccion
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre=nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad=edad
    
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion=direccion

    def __str__(self):
        return f"Nombre: {self.set_nombre}, Edad: {self.set_edad}, Direccion: {self.set_direccion}"

# Clase Estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base (Persona)
        self.curso = curso  # Atributo específico de Estudiante

    def __str__(self):
        return f"{super().__str__()}, Curso: {self.curso}"
    
class Docente(Persona):
    def __init__(self, nombre, edad, tipoContrato):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base (Persona)
        self.tipoContrato = tipoContrato  # Atributo específico de Docente

    def __str__(self):
        return f"{super().__str__()}, TipoContrato: {self.tipoContrato}"
