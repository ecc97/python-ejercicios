def main():
    lista_tareas = []

    while True:
        menu()
        opcion = int(input('Selecciona una opción: '))

        if opcion == 1:
            agregar_tarea(lista_tareas)
        elif opcion == 2:
            modificar_tarea(lista_tareas)
        elif opcion == 3:
            mostrar_tareas(lista_tareas)
        elif opcion == 4:
            eliminar_tarea(lista_tareas)
        elif opcion == 5:
            break


def menu():
    print('Listado de menú')
    print('1. Agregar tarea')
    print('2. Modificar tarea')
    print('3. Mostrar tareas')
    print('4. Eliminar tarea')
    print('5. Salir')


def agregar_tarea(lista_tareas):
    nombre_tarea = input('Ingresa nombre de la tarea: ')
    
    if verificar_tarea(nombre_tarea, lista_tareas):
        print('La tarea ya existe.')
        return
    
    tarea = {'tarea': nombre_tarea, 'completada': False}
    lista_tareas.append(tarea)
    
    print('Tarea agregada exitosamente.')


def verificar_tarea(nombre, lista_tareas):
    for tarea in lista_tareas:
        if tarea['tarea'] == nombre:
            return True
    return False


def modificar_tarea(lista_tareas):
    nombre_modificar = input('Ingresa el nombre de la tarea a modificar: ')
    
    if not verificar_tarea(nombre_modificar, lista_tareas):
        print('No se encontró una tarea con ese nombre.')
        return
    
    for tarea in lista_tareas:
        if tarea['tarea'] == nombre_modificar:
            nuevo_nombre = input('Ingresa el nuevo nombre de la tarea: ')
            nueva_completada = input('¿La tarea está completada? (True/False): ') == 'true'
            
            tarea['tarea'] = nuevo_nombre
            tarea['completada'] = nueva_completada
            
            print('Tarea modificada exitosamente.')
            return


def mostrar_tareas(lista_tareas):
    for tarea in lista_tareas:
        print('Tarea:', tarea['tarea'])
        print('Completada:', tarea['completada'])
        print('---')


def eliminar_tarea(lista_tareas):
    nombre_eliminar = input('Ingresa el nombre de la tarea a eliminar: ')
    
    if not verificar_tarea(nombre_eliminar, lista_tareas):
        print('No se encontró una tarea con ese nombre.')
        return
    
    for tarea in lista_tareas:
        if tarea['tarea'] == nombre_eliminar:
            lista_tareas.remove(tarea)
            print('Tarea eliminada exitosamente.')
            return

main()