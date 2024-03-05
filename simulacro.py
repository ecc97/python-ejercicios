def inventario():
    productos = {'nombre_producto': '', 'precio': 0, 'cantidad': 0}
      
    while True:
        opciones = int(input('Para proseguir apreta algunas opciones: 1: crear, 2: actualizar, 3: eliminar, 4: listar'))
        if opciones == 1:
            create_product(productos)
        elif opciones == 2:
            update_product(productos)
        elif opciones == 3:
            eliminar_producto(productos)
        elif opciones == 4:
            listar_productos(productos)
        else:
            print('aprieta la opción correcta')   

    

def create_product(dict): 
    nombre_producto = input('Nombre del producto:')
    precio_unitario = int(input('Precio unitario'))
    cantidad = int(input('Cantidad'))
    
    if nombre_producto in dict.values():
        print('Este producto ya existe en el inventario')
    else:
        dict['nombre_producto'] = nombre_producto
        dict['precio'] = precio_unitario
        dict['cantidad'] = cantidad 
    

def update_product(dict):
    nombre_producto = input('Actualiza nombre del producto:')
    precio_unitario = int(input('Actualiza precio unitario:'))
    cantidad_producto = int(input('Actualiza cantidad:'))
    
    dict['nombre_producto'] = nombre_producto
    dict['precio'] = precio_unitario
    dict['cantidad'] = cantidad_producto
            

def listar_productos(dict):
    for clave, valor in dict.items():
        print(clave, valor)
        
def eliminar_producto(dict):
    nombre_producto = input('Ingresa nombre del producto que desea eliminar:')
    
    if nombre_producto in dict.values():
        dict.pop('nombre_producto', None)
        dict.pop('precio', None)
        dict.pop('cantidad', None)
        print('producto eliminado')
    else:
        print('no existe este producto')

    

inventario()