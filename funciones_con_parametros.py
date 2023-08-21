#FUNCIONES CON PARAMETROS

def suma():
    #INGRESA NUMEROS
    a= float(input("Ingrese el primer número:"))
    b= float(input("Ingrese el segundo número:"))
    #DEVUELVE UNA SUMA
    return a + b

def suma_lista():
    #CREA LISTA VACIA
    lista= []
    #INGRESA CANTIDAD POR TECLADO
    cantidad= int(input("¿Cuántos números desea sumar?"))
    #RECORRE
    for i in range(cantidad):
        numero=float(input("Ingrese el número {i+1}:"))
        #AGREGA A LA LISTA
        lista.append(numero)
    #DEVUELVE LA SUMA
    suma= sum(lista)
    return suma

def repetir():
    #Se ingresa una cadena de texto
    cadena= input("Ingrese la cadena de texto que desea repetir:")
    #Ingresamos el número de veces que queremos repetir
    repeticiones= int(input("Ingrese el número de veces que desea repetirla:"))
#Devuelve la cadena de texto repetida el numero de veces especificado
    return cadena* repeticiones


#PEDIMOS AL USUARIO QUE INGRESE LOS NÚMEROS
num1= int(input("Ingrese el primer número:"))
num2= int(input("Ingrese el segundo número:"))

def multiplicacion(num1,num2):
    resultado= num1* num2

    return resultado
#LLAMAMOS A LA FUNCÍON E IMPRIMIMOS EL RESULTADO
resultado= multiplicacion(num1, num2)

print("El resultado de la multiplicación es: ", resultado)

