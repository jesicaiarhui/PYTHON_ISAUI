#Crea una tupla con valores predefinidos del 1 al 10, pide al usuario 
#un indice por teclado y muestra los valores de la tupla.
#RESUELVE EN CASO DE QUE NO EXISTA ESE INDICE EN LA TUPLA

tupla = (1,2,3,4,5,6,7,8,9,10)

indice = int(input("ingrese un indice: "))

if indice >=0 and indice< len (tupla):
    print (tupla [indice])
else:
    print ("indice ingresado INCORRECTO.")