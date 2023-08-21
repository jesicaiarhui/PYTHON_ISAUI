#DICCIONARIO CON LOS PRODUCTOS DE LA TIENDA

productos= {
    "001":{"Nombre":"IPHONE 6s ","marca":"APPLE","precio $": 30000,"stock":10,"color":"Silver","caracteristicas":" Memoria: 16 GB"},
    "002":{"Nombre":"IPHONE 6s plus","marca":"APPLE","precio $": 40000,"stock":20,"color":"Gold","caracteristicas":"Memoria: 32 GB"},
    "003":{"Nombre":"IPHONE 7", "marca":"APPLE", "precio $": 55000,"stock": 30, "color":"Black","caracteristicas":"Memoria: 32 GB"},
    "004":{"Nombre":"IPHONE 7 plus","marca":"APPLE","precio $": 60000,"stock": 40, "color":"Silver","caracteristicas":"Memoria: 64 GB"},
    "005":{"Nombre":"IPHONE 8","marca":"APPLE","precio $": 80000,"stock": 50, "color":"Rose gold","caracteristicas":"Memoria: 32 GB"},
    "006":{"Nombre":"IPHONE 8 plus","marca":"APPLE","precio $": 85000,"stock": 60,"color":"Black","caracteristicas":"Memoria: 128 GB"},
    "007":{"Nombre":"IPHONE X","marca":"APPLE","precio $": 95000, "stock": 70,"color":"Red","caracteristicas":"Memoria: 64 GB"},
    "008":{"Nombre":"IPHONE 11 pro max","marca":"APPLE", "precio $": 140000,"stock": 80,"color":"Green","caracteristicas":"Memoria: 128 GB"},
    "009":{"Nombre":"IPHONE 12","marca":"APPLE","precio $": 215000,"stock": 90,"color":"White","caracteristicas":"Memoria: 64 GB"},
    "010":{"Nombre":"IPHONE 13","marca":"APPLE","precio $": 300000,"stock": 95,"color":"Black","caracteristicas":"Memoria: 128 GB"},
    
}

#CARRITO DE COMPRAS
carrito=[]

def mostrar_product_detalle (productos):
    for codigo, producto in productos.items():
        print("\n"*1)
        print("Código", codigo)
        print("Nombre", producto["Nombre"])
        print("Marca", producto["marca"])
        print("Precio",producto["precio $"])
        print("Stock", producto["stock"])
        print("Color", producto["color"])
        print("Características", producto["caracteristicas"])
        print("--------------------------------------------")
        print("\n"*1)
        

def info_breve_product(productos):
    for codigo,producto in productos.items():
        print("\n"*1) 
        print("Código:", codigo)
        print("Nombre:", producto["Nombre"])
        print("Precio: {:.2f}".format(producto["precio $"]))
        print("Cantidad disponible:", producto["stock"])
        print("---------------------------------------------")
        print("\n"*1)

def buscar_product_por_codigo():
    print("\n"*1)
    codigo= input("Ingrese el código del producto a buscar:")
    
    while codigo not in productos:
        print("PRODUCTO NO ENCONTRADO. INTENTA NUEVAMENTE")
        print("\n"*1) 
    producto= productos[codigo]
    print("\n"*1) 
    print("---------------------")
    print("BUSCASTE")
    print("---------------------")
    print("\n"*1) 
    print("Nombre del producto:", producto["Nombre"])
    print("\n"*1)
    print("INFORMACIÓN DEL PRODUCTO")
    print("\n"*1)
    print("Código", codigo)
    print("Marca", producto["marca"])
    print("Precio",producto["precio $"])
    print("Stock", producto["stock"])
    print("Color", producto["color"])
    print("Características", producto["caracteristicas"])
    print("--------------------------------------------")
    print("\n"*1)

def realizar_compra(carrito):
    codigo=input("Ingrese el código del producto:")
    if codigo in productos:
        producto=productos[codigo]
        cantidad=int(input("Ingrese la cantidad a comprar:"))
        if cantidad>0:
            if cantidad<= producto["stock"]:
                precio = float(producto["precio $"])
            # Calculo el costo total por la cantidad que compró
                costo_total = precio * cantidad

                #AGREGAMOS PRODUCTO AL CARRITO
                carrito.append({"nombre": producto["Nombre"], "cantidad": cantidad, "precio $": producto["precio $"],"costo total": costo_total})
                #ACTUALIZAR STOCK
                producto["stock"]-= cantidad

                print("Producto añadido al carrito")
            else:
                print("No hay suficiente stock disponible")
        else:
            print("La cantidad debe ser MAYOR a cero")
    else:
        print("El producto no ha sido encontrado o no existe")

def mostrar_carrito(carrito):
    if len(carrito)==0:
        print("El carrito está vacío")
    else:
        print("Ver carrito:")
        for item in carrito:
            print("Nombre:", item["nombre"])
            print("Cantidad:", item["cantidad"])
            print("Precio por unidad:", item["precio $"])
            print("Costo total:", item["costo total"])   
            print("----------------------------------------------")

def finalizar_compra():
    mostrar_carrito(carrito)
    while True:
        opcion= input("¿Desea modificar el carrito? (SI/NO)")
        if opcion.lower()== "si":
            modificar_carrito(carrito)
            break
        elif opcion.lower()== "no":
            confirmar_compra(carrito)
            break
        else:
            print("Opción inválida.")
            print("Por favor seleccione SI para modificar carrito o NO para confirmar compra")
def modificar_carrito(carrito):
    while True:
        print("1) Agregar cantidad de un producto")
        print("2) Disminuir cantidad de un producto")
        print("3) Eliminar producto del carrito")
        print("4) Volver al menú anterior")

        opcion= input("Ingrese una opción:")

        if opcion== "1":
            agregar_cantidad(carrito)
        elif opcion== "2":
            disminuir_cantidad(carrito)
        elif opcion=="3":
            eliminar_product(carrito)
        elif opcion== "4":
            break
        else:
            print("Opción inválida. Por favor ingrese una opción válida")

def agregar_cantidad(carrito):
    #Mostrar productos con sus cantidades
    for i,item in enumerate(carrito):
        print(f"{i+1}.{item['nombre']}- Cantidad: {item['cantidad']}")
    #Solicitar al usuario la cantidad que desea agregar
    indice=int(input("Ingrese el código del producto que desea agregar:"))

    #Verificamos el indice que se ingresó
    if 1<= indice<= len(carrito):
            item=carrito[indice-1]
            cantidad_nueva= int(input("Ingrese la cantidad nueva:"))
            if cantidad_nueva>0:
                item["cantidad"]+= cantidad_nueva
                item["Costo total"]= item["precio $"]* item["cantidad"]
                print("Cantidad actualizada correctamente")
            else:
                print("La cantidad debe ser mayor a cero")
    else:
        print("Índice iválido. Por favor ingrese un número válido")

def disminuir_cantidad(carrito):
     #Mostrar productos con sus cantidades
    for i,item in enumerate(carrito):
        print(f"{i+1}.{item['nombre']}- Cantidad: {item['cantidad']}")
    #Solicitar al usuario la cantidad que desea disminuir
    codigo=int(input("Ingrese el código del producto que desea disminuir:"))
     #Verificamos el codigo que se ingresó
    if 1<= codigo < len(carrito):
        item=carrito[codigo-1]
        cantidad_nueva= int(input("Ingrese la cantidad nueva:"))
        if cantidad_nueva>=0 and cantidad_nueva<= item["cantidad"]:
            item["cantidad"]-= cantidad_nueva
            item["Costo total"]= item["precio $"]* item["cantidad"]
            print("Cantidad actualizada correctamente")
        else:
            print("La cantidad debe ser mayor o igual a cero")
    else:
        print("Índice iválido. Por favor ingrese un número válido")

def eliminar_product(carrito):
     #Mostrar productos con sus cantidades
    for i,item in enumerate(carrito):
        print(f"{i+1}.{item['nombre']}- Cantidad: {item['cantidad']}")
    #Solicitar al usuario la cantidad que desea eliminar
    codigo=int(input("Ingrese el código del producto que desea eliminar:"))-1

    #Validamos
    if 0<= codigo < len(carrito):
        producto_eliminado=carrito.pop(codigo)
        print(f"Producto'{producto_eliminado['nombre']}' eliminado correctamente")
    else:
        print("Índice inválido. Por favor ingrese un número válido.")

def confirmar_compra(carrito):
    print("\n"*1)
    print("************************************")
    print("LA COMPRA FUE REALIZADA CON ÉXITO")
    print("************************************")
    print("\n"*1)
    print("Detalle del carrito")
    print("--------------------------------------------------")
    print("\n"*1)
    for item in carrito:
        print("Nombre:", item["nombre"])
        print("Cantidad:", item["cantidad"])
        print("Precio por unidad:", item["precio $"])
        print("Costo total:", item["costo total"])
        print("-----------------------------------------------")
        print("\n"*1)
        print("¡Gracias por su compra!")


def menu():

    while True:
        print("****************************")
        print("BIENVENIDOS A iPHONE KING")
        print("****************************")
        print("\n"*1)
        print("------------------------------------------------------------------------")
        print("Envío Express en CBA hasta 24 horas.")
        print("Verificar zona de cobertura en checkout y preguntas frecuentes.")
        print("Disfrutá 6 cuotas sin interés en toda nuestra Tienda con Visa y Master ")
        print("------------------------------------------------------------------------")
        print("\n"*1)
        print("Elija una de las siguientes opciones:")
        print("\n"*1)
        print("1) Mostrar productos en detalle")
        print("2) Mostrar información breve del producto")
        print("3) Buscar producto por código")
        print("4) Realizar compras")
        print("5) Finalizar compra")
        print("6) Salir")
        print("\n"*1)
        opcion= input_integer("INGRESE UNA OPCIÓN:")
        print("\n"*1)
        if opcion==1:
            print("\n"*1)
            print("PRODUCTOS EN DETALLE:")
            print("------------------------------")
            mostrar_product_detalle (productos)
            
        elif opcion==2:
            print("\n"*1)
            print("INFORMACIÓN BREVE DEL PRODUCTO:")
            print(("---------------------------------"))
            info_breve_product(productos)
            print("\n"*1)
            
        elif opcion==3:
            print("\n"*1)
            print("BUSCAR PRODUCTO POR CÓDIGO:")
            print("-------------------------------------")
            buscar_product_por_codigo()
            print("\n"*1)
        elif opcion==4:
            print("\n"*1)
            print("REALIZAR COMPRAS:")
            print("--------------------------------------")
            realizar_compra(carrito)
            print("\n"*1)
        elif opcion==5:
            print("\n"*1)
            print("FINALIZAR COMPRA:")
            print("--------------------------")
            finalizar_compra()
            print("\n"*1)
            
        elif opcion ==6:
            print("\n"*1)
            confirmacion= input("¿Está segura/o que desea salir? (SI/NO):")
            if confirmacion.upper== "SI":
                break
            print("¡Usted ha salido!. Gracias por visitar nuestra página")
        else:
            print("Opción inválida, por favor seleccione una opción válida del 1 al 6")
            print("\n"*1)
            menu()
            break
    return opcion

def input_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


menu()