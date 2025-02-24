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

# Pedir datos al usuario
nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))
carrera = input("Ingresa la carrera del estudiante: ")

# Crear un objeto Estudiante
estudiante = Estudiante(nombre, edad, carrera)

# Mostrar los datos del estudiante
print(estudiante)
