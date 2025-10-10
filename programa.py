import random
stock=[]
def añadirProducto(x,y,w):
    z=random.randint(100000,999999) #Genero el codigo del producto
    repetido=0
    while repetido: #Verifico que el codigo no exista previamente
        repetido=0
        for producto in stock:
            if producto["codigo"] == z:
                repetido=1
                z=random.randint(100000,999999)
    producto={"codigo":z ,"producto":x , "cantidad en stock":y, "Precio Unitario":w}
    stock.append(producto)
    print(f"¡{x} añadido al stock con éxito!")
def buscar_valor_matriz(valor, stock):
    ubicacion = -1
    valor = str(valor).lower()
    for i in range(len(stock)): #recorro cada producto 
        if valor == str(stock[i]["producto"]).lower():
            ubicacion = i + 1  # guardo la posición (1-based)
    return ubicacion


ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
while ifagregar!=1 and ifagregar!=0:
    ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
if ifagregar==1:
    while ifagregar==1:
        aprod=input("Ingrese el producto que quiere agregar al stock:")
        if len(stock)>1:
            if buscar_valor_matriz(aprod, stock)!=-1:
                aprod=input("El producto ya se encuentra en la matriz, ingrese otro producto:")
        valido=False
        while valido==False:
            try:
                acant=int(input("Ingrese la cantidad disponible del producto:"))
                valido=True
            except ValueError:
                print("Entrada invalida. No introdujiste un número entero.")
        valido=False
        while valido==False:
            try:
                aprecio=float(input("Ingrese el precio unitario del producto:"))
                valido=True
            except ValueError:
                print("Entrada invalida. No introdujiste un número.")
        añadirProducto(aprod,acant,aprecio)
        ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
        while ifagregar!=1 and ifagregar!=0:
            ifagregar=int(input("Ingrese un 1 si quiere agregar un producto, 0 en caso contrario:"))
print("------Stock Actual------")
for fila in stock:
    print(fila)

