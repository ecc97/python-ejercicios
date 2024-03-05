def main():
    nombre, apellido, documento = registro_nuevo()
    productos = {}
    while True: 
        menu()
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            nombre, apellido, documento=registro_nuevo()
        elif(opcion==2):
            nuevo_producto(productos)
        elif opcion == 3:
            listar_productos(productos)
            input('Presione cualquier tecla para continuar')
        elif opcion == 4:
            mostrar_fact(nombre, apellido, documento, productos)
        elif opcion == 5:
            break
        else:
            print("Ingresaste una opcion invalida")

def menu():
    print("(1) Volver a registrar el documento, nombres y apellidos del cliente \n",
"(2) Registrar un nuevo producto a la factura (nombre producto, valor producto) \n",
"(3) Listar productos actuales de la factura.\n",
"(4)Mostrar factura \n",
"(5)Apagar el programa")

def registro_nuevo():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    documento = int(input("Ingresa tu documento: "))
    return nombre,apellido,documento


def nuevo_producto(diccionario):
    nombre_producto = input("ingrese el producto")
    valor_producto = int(input("ingrese el valor del producto"))
    diccionario[nombre_producto] = valor_producto

def listar_productos(diccionario):
    for producto, valor in diccionario.items():
        print(f"el producto es {producto}, el valor es {valor}") 

def mostrar_fact(nombre,apellido,documento,diccionario):
    print(f'FACTURA \n ')
    print(f'{nombre},{apellido},{documento} \n ')
    listar_productos(diccionario)
    totalFact(diccionario)

def totalFact(diccionario):

    Total1=0
    for valor in diccionario.values():
        Total1 += valor
    total_iva=Total1+Total1*0.19
    
    if len(diccionario)>=3 and len(diccionario)<5:
        totalfactura=total_iva * 0.95
        print(f'total a pagar {totalfactura}')
    
    elif len(diccionario)in range (5,7):
        totalfactura = total_iva * 0.9
        print(f'total a pagar {totalfactura}')
    elif len(diccionario)>=7:
        print(f'total a pagar {total_iva} ganaste 1 bono de 100.000')
    elif len(diccionario)==1 and Total1>500000:
        print(Total1)
    else:
        print(total_iva)

    
main()