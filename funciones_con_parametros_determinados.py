 #FUNCIONES CON PARAMETROS PREDETERMINADOS

def multiplicacion(num1,num2=2):
    #PEDIMOS AL USUARIO QUE INGRESE LOS NÚMEROS
    num1= int(input("Ingrese el segundo número:"))
    return num1* num2
resultado= multiplicacion(0) 
print(resultado)

def hipotenusa_triangulo_rectangulo(cateto1=4, cateto2=6):
    hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
    return hipotenusa
resultado= hipotenusa_triangulo_rectangulo()
print(resultado) 

def calcular_edad(anio_nacimiento):
    anio_actual = 2023  # Se puede cambiar a un valor actualizado
    edad = anio_actual - anio_nacimiento
    print(edad)

calcular_edad(int(input("Ingrese un año:")))

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

celsius_a_fahrenheit(int(input("Ingrese la temperatura en °C:")))

def cuadrado_binomio(a, b=5):
    resultado = a**2 + 2*a*b + b**2
    print(resultado)

cuadrado_binomio(int(input("Ingrese un numero para calcular el cuadrado de un binomio:")))
