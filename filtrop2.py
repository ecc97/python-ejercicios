def ingreso_gastos():
  salario_mensual = int(input('Ingresar el salario mensual'))
  categorias = {'alimentos': 0, 'transporte': 0, 'vivienda': 0, 'entretenimiento': 0}

  gasto_categorias(categorias)
  saldo_restante = saldo_restante_categorias(salario_mensual, categorias)


def gasto_categorias(dicts):
  for categoria in dicts.keys():
    gastos_val = int(input(f'cuanto gastaste en {categoria}?'))
    dicts[categoria] = gastos_val


def saldo_restante_categorias(salario, dicts):
  total_gastos = sum(dicts.values())
  saldo_restante = salario - total_gastos

  if saldo_restante < 0:
    print('Estás gastando más de lo que ganas')
  else:
    preguntar_mas_gastos = input('desear hacer más gastos? selecciona 1 para si y 0 para no')
    if preguntar_mas_gastos == '1':
      gastos_adicionales(salario, dicts)
    else:
      print(mostrar_total_gastos(total_gastos))
      print('El saldo restante:', saldo_restante)
  mostrar_total_gastos_categoria(dicts)


def gastos_adicionales(salario, dicts):
  for c in dicts.keys():
    monto = int(input('Ingresa un monto adicional'))
    if monto != 0:
      monto_cat  = input('Ingresa la categoría del monto')
      if monto_cat in dicts.keys():
        dicts[monto_cat] += monto
        saldo_restante_categorias(salario, dicts)
      else:
        print('Categoría no disponible')
        break
    else:
        break

def mostrar_total_gastos(total):
  return f'total de gastos: {total}'

def mostrar_total_gastos_categoria(dicts):
  for categoria, gasto in dicts.items():
    print(f'La categoría {categoria} tiene un gasto total de {gasto}')



ingreso_gastos()