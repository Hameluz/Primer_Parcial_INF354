import pandas as pd
import numpy as np
datos = pd.read_csv("b_depressed.csv")

def media(columna):
    media_c = datos[columna].mean()
    return media_c

def moda(columna):
    moda_c = datos[columna].mode()[0]
    return moda_c

def cuartiles(columna):
    cuartiles_c = datos[columna].quantile([0.25,0.5,0.75])
    print("El primer cuartil es:", cuartiles_c[0.25])
    print("El segundo cuartil es:", cuartiles_c[0.5])
    print("El tercer cuartil es:", cuartiles_c[0.75])

def percentiles(columna, n):
    percentil_n = datos[columna].quantile(q=(n/100))
    return percentil_n

print('************  MEDIAS  ************')
print('Edad: ', media("Age"))
print('Numero de Hijos: ', media('Number_children'))
print('Nivel de Educacion: ', media('education_level'))
print('Miembros de la familia: ', media('total_members'))
print('Activo Ganado: ', media('gained_asset'))
print('Actvo Duradero: ', media('durable_asset'))
print('Ahorro de Activos: ', media('save_asset'))
print('Gastos de Manutencion: ', media('living_expenses'))
print('Otros Gastos: ', media('other_expenses'))
print('Entrada Agricola: ', media('incoming_agricultural'))
print('Gastos Agricolas: ', media('farm_expenses'))
print('Inversion Duradera: ', media('lasting_investment'))
print('Sin Inversion Duradera: ', media('no_lasting_investmen'))

print('************  MODA  ************')
print('Ciudad: ', moda("Ville_id"))
print('Sexo: ', moda('sex'))
print('Edad: ', moda('Age'))

print('************  CUARTILES  ************')
print('Edad: '); cuartiles('Age')
print('Numero de Hijos: '); cuartiles('Number_children')
print('Nivel de Educacion: '); cuartiles('education_level')
print('Miembros de la familia: '); cuartiles('total_members')

print('************  PERCENTILES  ************')
print('Edad: ', percentiles('Age', 50))
print('Numero de Hijos: ', percentiles('Number_children', 50))
print('Nivel de Educacion: ', percentiles('education_level', 50))
print('Miembros de la familia: ', percentiles('total_members', 50))