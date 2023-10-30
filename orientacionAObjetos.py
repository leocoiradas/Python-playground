#Clases y objetos


##Clase persona: Crear una clase persona con atributos como nombre edad y género. Crear varios objetos de esta clase

'''class Persona:
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
personaTwo.genero("Femenino")'''

##Clase coche: Crear clase coche con atributos y metodos como marca modelo y año. Crear objetos instanciando dicha clase

class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    def coche_marca(self):
        print(f"La marca del auto es {self.marca}")
    def coche_modelo(self):
        print(f"El modelo del auto es {self.modelo}")
    def coche_anio(self):
        print(f"El año de este coche es {self.anio}")
        
ferrari = Coche("Ferrari", "Deportivo", "2023")
ferrari.coche_anio()
ferrari.coche_modelo()
ferrari.coche_marca()
    
