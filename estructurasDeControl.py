#sentencia if else elsif

##Comparar 2 numeros y verificar si uno es mayor al otro e imprimir el mayor

'''print("Ingrese un número")
numOne = input()
print("Ingrese otro número")
numTwo = input()

if numOne>numTwo:
    print(str(numOne) + " es el mayor")
else:
    print(str(numTwo) + " es el mayor")'''
    

##ingresar una edad e imprimir si es niño (0 a 12) adolescente (13 a 17) adulto (18 a 59) o adulto mayor (+60)

'''print("ingrese su edad")
edad = int(input())
if edad < 12:
    print(f"Usted tiene {edad} años, por tanto es un niño")
elif edad >13 and edad<18:
    print(f"Usted tiene {edad} años, por tanto es un adolescente")
elif edad > 18 and edad <=59:
    print(f"Usted tiene {edad} años, por tanto es un adulto")
else:
    print(f"Usted tiene {edad} años, por tanto es un adulto mayor")'''
    
##Ingresar una calificación y darle una letra (F de 0 a 20) (D 21 a 40) (C 41 a 60) (B 61 a 80) (A 81 a 100)

'''print("Ingrese un número del 1 al 100")

calificacion = int(input())
if calificacion >= 0 and calificacion <=20:
    print("Usted sacó una F")
elif calificacion >=21 and calificacion <=40:
    print("Usted sacó una D")
elif calificacion >=41 and calificacion <=60:
    print("Usted sacó una C")
elif calificacion >=61 and calificacion <=80:
    print("Usted sacó una B")
elif calificacion >=81 and calificacion <=100:
    print("Usted sacó una A")
else:
    print("El numero de calificación que ingresó no es válido, intente otra vez con otro número del 0 al 100.")'''
    
##Año bisiesto: el usuario ingresa un año, y si este número de año es divisible por 4 entonces es un año bisiesto

'''print("Ingrese un número correspondiente a un año.")

year = int(input())

if year%4==0 and year % 100 != 0 or year %400 == 0:
    print(f"{year} es un año bisiesto")
else:
    print(f"{year} no es un año bisiesto")'''





#Bucles for

##Ingresar un numero y mostar su tabla de multiplicar del 1 al 10

'''print("Ingrese un número")

num = int(input())

tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tablaNum = []

for element in tabla:
    result = 0
    result = element * num
    tablaNum.append(result)

print(tablaNum)'''

##Ingresar un número par y sumar todos los números pares desde 2 al número ingresado

'''print("Ingrese un número par")
numero = int(input())
sumTotal = 0
if numero % 2 == 0:
    rango = range(2, numero + 1)
    
    for i in rango:
        if i % 2 == 0:
            sumTotal+= i
    print(sumTotal)'''
    
    
##Factorial: el usuario ingresa un número y se calcula el factorial del mismo

'''print("Ingrese un número")

number = int(input())

rangeNum = range(1, number+1)
result = 1
for i in rangeNum:
    result*=i
print(f"El factorial de {number} es: {result}")'''

##Números primos: El usuario ingresa un número y se verifica que sea un número primo
    