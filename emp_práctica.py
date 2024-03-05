def main():
    lista_empleados = []
    
    while True:
        menu()
        opcion = int(input('Selecciona una opción'))
        
        if opcion == 1:
            agregar_empleado(lista_empleados)
        elif opcion == 2:
            modificar_empleado(lista_empleados)
        elif opcion == 3:
            mostrar_empleado(lista_empleados)
        elif opcion == 4:
            eliminar_empleado(lista_empleados)
        elif opcion == 5:
            break
                 
def menu():
    print('Listado de menú')
    print('1. Agregar')
    print('2. Modificar')
    print('3. Mostrar')
    print('4. Eliminar')
    print('5. salir')

def agregar_empleado(lista_empleados):
    nombre_empleado = input('Ingresa nombre de empleado')
    edad = int(input('Ingresa edad del empleado'))
    empresa = input('Ingresa nombre de la empresa')
    
    if verificar_empleado(nombre_empleado, lista_empleados):
      print('El empleado ya existe.')
      return
    
    empleado = {'nombre': nombre_empleado, 'edad': edad, 'empresa': empresa}
    lista_empleados.append(empleado)
    print(lista_empleados)
    print('empleado agregado')
    
def modificar_empleado(lista_empleados):
  empleado_act = input('Ingresa el nombre del empleado a actualizar')
  if not verificar_empleado(empleado_act, lista_empleados):
      print('El empleado no existe')
      return
  for empleado in lista_empleados:
    if empleado_act == empleado['nombre']:
      nombre_empleado_act = input('Actualiza nombre de empleado')
      edad_act = int(input('Actualiza edad del empleado'))
      empresa_act = input('Actualiza nombre de la empresa')
      empleado['nombre'] = nombre_empleado_act
      empleado['edad'] = edad_act
      empleado['empresa'] = empresa_act
      print('empleado actualizado')
      print(empleado)
  print(lista_empleados)

def mostrar_empleado(lista_empleados):
    contador = 0
    print('Lista de los empleados')
    for dict in lista_empleados:
        contador += 1
        print(contador, 'nombre:', dict['nombre'], 'edad:', dict['edad'], 'empresa:', dict['empresa'])

def eliminar_empleado(lista_empleados):
  empleado_del = input('Ingresa el nombre del empleado a eliminar')
  if not verificar_empleado(empleado_del, lista_empleados):
      print('El empleado no existe')
      return
  for empleado in lista_empleados:
    if empleado_del == empleado['nombre']:
      lista_empleados.remove(empleado)
      print('empleado eliminado')

def verificar_empleado(nombre, lista_empleados):
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre:
            return True
    return False


main()