#CALCULADORA
import math
from fractions import Fraction

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b!=0:
        return a / b
    else:
        return "Error. No se puede dividir por cero"

def potencia(base, exponente):
    return math.pow(base, exponente)

def raiz_cuadrada(numero):
    if numero>=0:
        return math.sqrt(numero)
    
def logaritmo(n,base):
    if n>0 and base>0 !=1:
        return math.log(n,base)
    
def decimal_a_fraccion(decimal):
    return Fraction(decimal).limit_denominator()
    
def raiz_nesima (numero,indice):
    if numero>=0:
        return numero** (1/indice)
    else:
        return("Error. No se puede calcular la raiz de un numero negativo")
    
def seno(angulo):
    return math.sin(math.radians(angulo))

def coseno(angulo):
    return math.cos(math.radians(angulo))

def tangente(angulo):
    return math.tan(math.radians(angulo))

def calculadora():
    print("CALCULADORA CIENTÍFICA")
    print("-------------------------------------")
    print("OPERACIONES")
    print("-------------------------------------")
    print("\n"*1)
    print("1) SUMA")
    print("2) RESTA")
    print("3) MULTIPLICACIÓN")
    print("4) DIVISIÓN")
    print("5) POTENCIA")
    print("6) RAIZ CUADRADA")
    print("7) LOGARITMO")
    print("8) DECIMAL A FRACIÓN")
    print("9) RAIZ NESIMA")
    print("10) SENO")
    print("11) COSENO")
    print("12) TANGENTE")
    print("\n"*1)

    opcion= input("INGRESE LA OPERACIÓN QUE DESEA CALCULAR (1-12):")

    if opcion in ['1', '2', '3', '4', '5', '6', '7','8','9','10','11', '12' ]:
        if opcion in ['1', '2', '3', '4', '5', '7']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        else:
            num1 = float(input("Ingresa el número: "))
        
        if opcion == '1':
            print("Resultado:", suma(num1, num2))
            calculadora()
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
            calculadora()
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
            calculadora()
        elif opcion == '4':
            print("Resultado:", division(num1, num2))
            calculadora()
        elif opcion == '5':
            print("Resultado:", potencia(num1, num2))
            calculadora()
        elif opcion == '6':
            print("Resultado:", raiz_cuadrada(num1))
            calculadora()
        elif opcion == '7':
            base = float(input("Ingresa la base del logaritmo: "))
            print("Resultado:", logaritmo(num1, base))
            calculadora()
        elif opcion == '8':
            decimal = float(input("Ingresa el número decimal: "))
            fraccion = decimal_a_fraccion(decimal)
            print("Fracción:", fraccion)
            calculadora()
        elif opcion == '9':
            num1 = float(input("Ingresa el número: "))
            indice = float(input("Ingresa el índice de la raíz: "))
            print("Resultado:", raiz_nesima(num1, indice))
            calculadora()
        elif opcion == '10':
            angulo = float(input("Ingresa el ángulo en grados: "))
            print("Seno:", seno(angulo))
            calculadora()
        elif opcion == '11':
            angulo = float(input("Ingresa el ángulo en grados: "))
            print("Coseno:", coseno(angulo))
            calculadora()
        elif opcion == '12':
            angulo = float(input("Ingresa el ángulo en grados: "))
            print("Tangente:", tangente(angulo))
            calculadora()
    else:
        print("Opción no válida. Elija una opcion correcta")

calculadora()

