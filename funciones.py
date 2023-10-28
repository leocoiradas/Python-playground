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

'''def bigger(numOne, numTwo):
    if numOne > numTwo:
        print(f"{numOne} is bigger than {numTwo}") 
    else:
        print(f"{numTwo} is bigger than {numOne}")

bigger(48, 567)
bigger(32, 25)
bigger(583939, 9)
bigger(12, 74)'''

##Factorial: Crear una función que tome un valor positivo como parámetro y calcule su factorial

'''def factor(number):
    if number > 0:
        total = 1
        numRange = range(1, number+1)
        for i in numRange:
            total*=i
        print(f"El factorial de {number} es {total}")
        
factor(14)
factor(5)
factor(10)
factor(4)
factor(21)'''

##Números primos: Crear una funcion que permita saber si un número primo o no

'''def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} no es un número primo", n, "es divisor")
            return False
    print(f"{num} es un número primo")
    return True

es_primo(78)
es_primo(77)
es_primo(97)
es_primo(100)
es_primo(44)'''

##Revertir cadena: crear una función la cual permita invertir una cadena ingresada

'''def revertirCadena(string):
    reversedString = ""
    for char in reversed(string):
        reversedString += char
    print(reversedString)
    return reversedString

revertirCadena("Supercalifrigalisticexpialidoucious")'''

##Promedio de una lista: Crear una función que permita calcular el promedio de una lista de números

'''def promedio(arr):
    arrLength = len(arr)
    sumArr = 0
    for num in arr:
        sumArr += num
    prom = sumArr / arrLength
    prom = round(prom, 2)
    print(f"la suma de los elementos de {arr} es {sumArr} y su promedio es: {prom}")
    return prom

promedio([2, 5, 7, 8, 9, 76, 43, 12, 6, 1])'''

##Contar vocales, crear una función que reciba un string como parámetro y permita saber cuantas vocales tiene la cadena ingresada

'''def contar_vocales(string):
    vocalCount = 0
    lowerString = string.lower()
    for char in lowerString:
        if char == "a" or char == "e" or char == "i" or char == "o" or char =="u":
            vocalCount+=1
    print(f"La cadena {string} tiene en total {vocalCount} vocales")
    
contar_vocales("Superman")
contar_vocales("Superman ha salvado Metropolis")
contar_vocales("Madrid es una ciudad ubicada en España")'''

#Día de la semana: Crear una función que reciba un número del 1 al 7, y que devuelva un mensaje con el día de la semana correspondiente al número ingresado

def diaSemana(num):
    dias = ["Domingo","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado"]
    hoy = ""
    if num >=1 and num <=7:
        diasLong = len(dias)
        rango = range(1, diasLong + 1)
        for numero in rango:
            if numero == num:
                hoy = dias[numero - 1]
    else:
        print("Por favor ingrese un número entero entre 1 y 7 para ejecutar el programa")
        return hoy
    
    print(f"Hoy es {hoy}")
    return hoy

diaSemana(6)
diaSemana(5)
diaSemana(3)
diaSemana(1)