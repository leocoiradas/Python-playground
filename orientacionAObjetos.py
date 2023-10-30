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

'''class Coche:
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
ferrari.coche_marca()'''

##Clase libro: Crear una clase libro con atributos como titulo, autor y genero. Crear objetos en base a dicha clase
'''
class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    def libro_titulo(self):
        print(f"El título de este libro es: {self.titulo}")
    def libro_autor(self):
        print(f"El autor de este libro es: {self.autor}")
    def libro_genero(self):
        print(f"El género de este libro es: {self.genero}")

harryPotter = Libro("Harry Potter", "J.K Rowling", "Fantasía")
harryPotter.libro_titulo()
harryPotter.libro_autor()
harryPotter.libro_genero()    '''    

##Herencia de clases

##Crear una clase empleado que herede de la clase persona. Agregar atributos específicos de empleado, como salario y cargo
    
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        print(f"Hola!! Mi nombre es {self.nombre}")
    def edad_valor(self):
        print(f"Tengo {self.edad} años")
    def genero_valor(self):
        print(f"Mi género es {self.genero}")
        
class Empleado(Persona):
    def __init__(self, nombre, edad, genero, salario, cargo):
        self.salario = salario
        self.cargo = cargo
        super().__init__(nombre, edad, genero) 
    def salario_valor(self):
        print(f"Mi salario es de: {self.salario}")
    def cargo_valor(self):
        print(f"Mi cargo es el de: {self.cargo}")
        
luciano = Empleado("Luciano", 34, "Masculino", 30000, "Arquitecto")
luciano.genero_valor()
luciano.edad_valor()
luciano.salario_valor()
luciano.cargo_valor()