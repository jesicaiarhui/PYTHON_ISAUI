#Crea una tupla con numeros, pide al usuario un numero por teclado e indica
#cuantas veces se repite segun lo halle en la tupla creada

#VALIDAR LOS INGRESOS DEL USUARIO
cont = 0
numeros = (3,4,8,3,2,0,3,2,5,5,1,9,0,5,4,8,2,8,2,3,3)

ingreso = int(input("Ingrese el número que desea consultar: "))

if ingreso != len(numeros) and ingreso > len(numeros):
    print ("El número ingresado inexistente.")
else:
   for e in numeros:
      if ingreso == e:
        cont = cont + 1

print ("El número ingresado se repite", cont, "veces")