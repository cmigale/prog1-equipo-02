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
