import pandas as pd

data = pd.read_excel('IBEX35_Sept2018.xls')

promedio = data['Promedio'].values
fecha = data['Fecha'].values

print(promedio)
print(fecha)
print('hola buenas')

