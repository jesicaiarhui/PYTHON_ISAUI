#Tenemos una lista de Tuplas que representan ciertas características de una serie de productos.
#Cada tupla tiene 4 elementos:
#nombre del producto
#precio
#cantidad disponible
#marca
#Se desea obtener una lista de productos que cumplan con ciertas condiciones de búsqueda:
#precio máximo
#marca específica

lista_productos= [("Auto",1500000,5,"Honda"), ("Auto",2000000,3,"Ford"), ("Auto",3000000, 4, "Fiat"),("Auto", 5000000, 6,"Renault")]

precio= 5000000
marca= "Ford"

productos=[]

for t in lista_productos:
    if t[1]<= precio and t[3]== marca:
        productos.append(t)

print(productos)

