ListaProductos=[]
#producto={"nombre":nombre, "precio":precio, "cantidad": stock,"codigo": codigo}

opcion="0"

"""
Cambiar las listas para crear el producto por un diccionario[]
Agregar un codigo al diccionario de productos
Agregar una lista para almacenar los diccionarios de un producto
Modificar las funciones para que utilicen la nueva estructura de diccionario
agregar las funciones faltantes:
actualizar: cantidad/precio[]
mostrar inventario completo[]
Eliminar producto[]
"""

def ValidarCodigo(codigo):
     #codigo="Javier"
     contador_mayusculas=0
     contador_numeros=0
     for l in codigo:
          if l.isupper():
               contador_mayusculas+=1
          if l.isnumeric():
               contador_numeros+=1
     if contador_mayusculas<2:
        print("el codigo debe tener al menos 2 mayusculas")
     elif contador_numeros:
        print("el codigo debe tener al menos un numero")
     elif len(codigo) <5:
        print("el codigo debe tener al menos 5 caracteres")
        return False
     else:
         return True     

def solicitarProducto():
        nombre=input("Ingrese el nombre del producto: ")
        while True:
             codigo=input("ingrese el codigo para el producto: ")
             if ValidarCodigo(codigo)==True:
                  print("codigo correcto")
                  break
             else:
                  print("codigo incorrecto. Intentelo de nuevo")
        try:
            stock=int(input("Ingrese el stock del producto: "))
            precio=int(input("Ingrese el precio del producto: "))
            
            if stock<0 or precio <0:
                raise ValueError
                
            else:
                producto=[nombre,precio,stock,codigo]
                return producto

        except ValueError:
            print("Debe ingresar valores enteros positivos")

def guardarProducto(nombre,precio,stock,codigo):
    ProductoBuscado=buscarProducto(codigo)
    if ProductoBuscado!=None:
            print("ese producto ya fue registrado")
            return False
    
    producto={"nombre":nombre,"precio":precio,"stock":stock,"codigo":codigo}
    ListaProductos.append(producto)
    return True
        
def buscarProducto(codigo):
    for Dictproducto in ListaProductos:
        if codigo==Dictproducto["codigo"]:
            return Dictproducto
        
        return None

def mostrarproducto(codigo):
    productoBuscado=buscarProducto(codigo)
    if productoBuscado!=None:
        print("-"*60)
        print(f"cod: {productoBuscado["codigo"]}\tNombre: {productoBuscado["nombre"]}\tPrecio: ${productoBuscado["precio"]}\tStock: {productoBuscado["stock"]}")
        print("-*60")
    else:
            print("No existe un producto con ese codigo")



while opcion!="6":
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion=input("Ingrese la opción que desea(1-6): ")

    
    
    

    
    
    match opcion:

        case "1":
            nuevoProducto=solicitarProducto()
            if nuevoProducto!= None:
                guardarProducto(nuevoProducto[0],nuevoProducto[1],nuevoProducto[2])
        case "2":
            nombreProducto=input("Ingrese el nombre del producto a buscar: ")
            buscarProducto(nombreProducto)

