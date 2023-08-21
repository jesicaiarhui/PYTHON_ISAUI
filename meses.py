#Crear una tupla con los meses del año, pide numeros al usuario, si el numero está entre 1 y la longitud maxima de la tupla, muestra el
#Contenido de esa posicion, sino muestra un mensaje de error
#El programa termina cuando el usuario ingresa un cero (0)

import os
salir = False

meses_del_año = ("ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE")


while salir == False:
    print ("\n"*1)
    num = int(input ("ingrese un Numero (1-12) "))
    
    if num == 0:
        salir = True
    else: 
        if num >= 1 and num <= len(meses_del_año):
            print ("el mes seleccionado es: ")
            print (meses_del_año[num-1])
            print ("\n"*1)
            print ("si desea salir ingrese cero (0)")
        else:
            print ("el numero que ingresó es incorrecto.","\n"*2,"porfavor ingrese un numero entre el 1 y", len(meses_del_año))
            os.system ("cls")