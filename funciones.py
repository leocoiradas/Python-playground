import math
#Functions

##Crear una función que acepte un nombre como parametro e imprima un saludo
'''def greeting(name):
    print(f"Hi {name} I hope that you're having an amazing day!!")

greeting("Alan")'''

##Función para calcular el área de un círculo. toma radio como argumento y calcula el área con la fórmula pi * radio^2

'''def area(radius):
    pi = math.pi
    circleArea =  pi * math.pow(radius, 2)
    "math.pow es un metodo de la librería math que se usa para calcular potencias, recibe 2 parámetros:" 
    "el primero es la base y el segundo el exponente al que se va a elevar la base para calcular la potencia"
    
    print(circleArea)

area(34)'''

##Función para verificar el número mayor, recibe 2 números como parámetro y devuelve el mayor

def bigger(numOne, numTwo):
    if numOne > numTwo:
        print(f"{numOne} is bigger than {numTwo}") 
    else:
        print(f"{numTwo} is bigger than {numOne}")

bigger(48, 567)
bigger(32, 25)
bigger(583939, 9)
bigger(12, 74)