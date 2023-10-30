#Clases y objetos


##Clase persona: Crear una clase persona con atributos como nombre edad y género. Crear varios objetos de esta clase

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad_valor = None
        self.genero_valor = None
        print(f"Hola!! Mi nombre es {nombre}")
    def edad(self, edad):
        self.edad_valor = edad
        print(f"Tengo {edad} años")
    def genero(self, genero):
        self.genero_valor = genero
        print(f"Mi género es {genero}")
        
personaOne = Persona("Tadeo")
personaOne.edad(20)
personaOne.genero("Masculino")

personaTwo = Persona("Lucila")
personaTwo.edad(32)
personaTwo.genero("Femenino")
