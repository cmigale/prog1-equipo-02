import random
stock=[["Producto:","Codigo:","Cantidad en stock:","Precio Unitario:",]]
def añadirProducto(x,y,w):
    z=random.randint(100000,999999) #Genero el codigo del producto
    repetido=0
    while repetido: #Verifico que el codigo no exista previamente
        repetido=0
        for fila in stock:
            if z==fila[3]:
                repetido=1
                z=random.randint(100000,999999)
    producto=[x,z,y,w]
    stock.append(producto)
    print(x,"añadido al stock con exito!")
def buscar_valor_matriz(valor, stock):
    print(stock)
    ubicacion = -1
    valor = str(valor).lower()
    for i in range(len(stock[0])):  # recorro por columnas
        if valor == str(stock[0][i]).lower() or valor == str(stock[1][i]).lower():
            ubicacion = i + 1  # guardo la posición (1-based)
    return ubicacion


print(stock)
ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
while ifagregar!=1 and ifagregar!=0:
    ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
if ifagregar==1:
    while ifagregar==1:
        aprod=input("Ingrese el producto que quiere agregar al stock:")
        if len(stock)>1:
            if buscar_valor_matriz(aprod, stock)!=-1:
                aprod=input("El producto ya se encuentra en la matriz, ingrese otro producto:")
        acant=int(input("Ingrese la cantidad disponible del producto:"))
        aprecio=int(input("Ingrese el precio unitario del producto:"))
        añadirProducto(aprod,acant,aprecio)
        ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
        while ifagregar!=1 and ifagregar!=0:
            ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
print("------Stock Actual------")
for fila in stock:
    print(fila)

# Modificar productos
 
 
def buscar_producto(valor, stock):
    valor = str(valor).lower()
    for producto in stock:
        if str(producto["codigo"]) == valor or producto["producto"].lower() == valor:
            return producto
    return None
 
def generador_menu(opciones):
    contador = 0
    entradas_validas = []
    while contador <= len(opciones) - 1:
        print(opciones[contador], "(", contador + 1, ")")
        entradas_validas.append(str(contador + 1))
        contador += 1
    return entradas_validas
 
def borrar_listas(opciones, entradas_validas):
    opciones, entradas_validas = [], []
    return opciones, entradas_validas
 
def verificacion(valor, lista):
    contador = len(lista) - 1
    encontrado = False
    while not encontrado:
        while contador >= 0 and not encontrado:
            if lista[contador] == valor:
                encontrado = True
            else:
                contador -= 1
        if not encontrado:
            valor = input("Valor inválido, ingrese de nuevo: ")
            contador = len(lista) - 1
    return contador
 
 
# ----- MENÚ PRINCIPAL -----
opciones = []
modificar_productos_pantalla = True
 
while modificar_productos_pantalla:
    print("\n------------- MENÚ -------------")
    opciones.append("Buscar producto")
    opciones.append("Salir")
 
    entradas_validas = generador_menu(opciones)
    decision = input("Ingrese decisión: ")
    conector = verificacion(decision, entradas_validas)
    opciones, entradas_validas = borrar_listas(opciones, entradas_validas)
 
    if decision == "1":  # Buscar producto y modificarlo
        valor = input("Ingrese código o nombre del producto: ")
        producto = buscar_producto(valor, stock)
 
        if producto:
            print("")
            print("Producto encontrado: ",producto)
            print("¿Qué desea hacer con este producto?")
            opciones = ["Modificar nombre", "Modificar precio", "Modificar cantidad", "Eliminar producto", "Cancelar"]
            entradas_validas = generador_menu(opciones)
            decision_mod = input("Ingrese decisión: ")
            conector = verificacion(decision_mod, entradas_validas)
 
            if decision_mod == "1":
                nuevo_nombre = input("Nuevo nombre: ")
                producto["producto"] = nuevo_nombre
                print("")
                print("Nombre actualizado correctamente.")
 
            elif decision_mod == "2":
                nuevo_precio = float(input("Nuevo precio: "))
                producto["precio"] = nuevo_precio
                print("")
                print("Precio actualizado correctamente.")
 
            elif decision_mod == "3":
                nueva_cantidad = int(input("Nueva cantidad: "))
                producto["cantidad"] = nueva_cantidad
                print("")
                print("Cantidad actualizada correctamente.")
 
            elif decision_mod == "4":  # Eliminar producto
                confirm = input(f"¿Está seguro que desea eliminar '{producto['producto']}'? (s/n): ").lower()
 
                if confirm == "s":
                    stock.remove(producto)
                    print("")
                    print("Producto ",{producto['producto']}," eliminado correctamente.")
                else:
                    print("")
                    print("Operación cancelada. El producto no fue eliminado.")
 
            elif decision_mod == "5":
                print("Operación cancelada.")
 
            # Mostrar stock actualizado
            print("")
            print("Stock actual:")
            for p in stock:
                print(p)
 
            opciones, entradas_validas = borrar_listas(opciones, entradas_validas)
 
        else:
            print("")
            print("Producto no encontrado.")
 
    elif decision == "2":  # Salir
        modificar_productos_pantalla = False
print("")
print("Programa finalizado.")
