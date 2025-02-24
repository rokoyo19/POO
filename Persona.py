class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Permitir que el usuario ingrese el nombre y la edad
nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))

persona = Persona(nombre, edad)

# Mostrar los datos de la persona
print(f'Nombre: {persona.nombre}, Edad: {persona.edad}')
