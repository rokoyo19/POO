class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Clase Estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base (Persona)
        self.carrera = carrera  # Atributo específico de Estudiante

    def __str__(self):
        return f"{super().__str__()}, Carrera: {self.carrera}"
    
class Docente(Persona):
    def __init__(self, nombre, edad, tipoContrato):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base (Persona)
        self.tipoContrato = tipoContrato  # Atributo específico de Docente

    def __str__(self):
        return f"{super().__str__()}, TipoContrato: {self.tipoContrato}"
