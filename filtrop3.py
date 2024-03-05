from datetime import datetime

today = datetime.now()
ano_actual = today.year
ano_nacimiento = int(input('Ingresa fecha de nacimiento'))

edad_actual = ano_actual - ano_nacimiento
print('Tienes', edad_actual, 'años')