import csv
#Listas para almacenar datos
id_Encuesta = []; id_Ciudad = []; sexo = []; edad = []; casado = []
nro_hijos = []; nivel_educacion = []; miembros_fam_tot = []; activo_ganado = []
activo_duradero = []; ahorro_activos = []; gastos_manutencion = []; otros_gastos = []
salario_entrante = []; granja_propia_entrante = []; negocios_entrantes = []
entrada_sin_negocio = []; entrada_agricola = []; gastos_agricolas = []
mano_de_obra_primaria = []; inversion_duradera = []; sin_inversion_duradera = []
deprimido = []

#Funcion para almacenar las columnas en listas
def listar_datos(nombre_columna):
    columna = []
    with open('b_depressed.csv', 'r') as datos:
        lector_csv = csv.DictReader(datos)
        #Almacenar los datos en las listas
        for fila in lector_csv:
            if fila[nombre_columna] is not None and fila[nombre_columna] != '' and not fila[nombre_columna].isspace():
                columna.append(int(fila[nombre_columna]))
    return columna

#Funcion para hallar la media
def media(columna):
    valor = sum(columna)/len(columna)
    return valor

#Funcion para hallar la MODA
def moda(columna):
    frecuencia = {}
    for fila in columna:
        frecuencia[fila] = frecuencia.get(fila, 0) + 1
    mayor = max(frecuencia.values())
    valor = [key for key, fila in frecuencia.items()
                if fila == mayor]
    return valor

#Funcion para hallar los cuartiles
def cuartiles(columna):
    datos_ordenados = sorted(columna)
    n = len(datos_ordenados)
    if n % 2 == 0:
        q2 = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        q2 = datos_ordenados[n//2]
    if n % 2 == 0:
        mitad_inferior = datos_ordenados[:n//2]
        q1 = (mitad_inferior[len(mitad_inferior)//2 - 1] + mitad_inferior[len(mitad_inferior)//2]) / 2
    else:
        mitad_inferior = datos_ordenados[:n//2 + 1]
        q1 = mitad_inferior[len(mitad_inferior)//2]
    if n % 2 == 0:
        mitad_superior = datos_ordenados[n//2:]
        q3 = (mitad_superior[len(mitad_superior)//2 - 1] + mitad_superior[len(mitad_superior)//2]) / 2
    else:
        mitad_superior = datos_ordenados[n//2 + 1:]
        q3 = mitad_superior[len(mitad_superior)//2]
    # imprimir los resultados
    print("\tPrimer cuartil:", q1)
    print("\tSegundo cuartil:", q2)
    print("\tTercer cuartil:", q3)

#Funcion para hallar los percentiles
def percentiles(columna, n):
    datos_ordenados = sorted(columna)
    percentil_n = int((n/100) * (len(datos_ordenados) - 1))
    percentil_n = datos_ordenados[percentil_n]
    return percentil_n

#Uso de Listas para las columnas
id_Encuesta = listar_datos('Survey_id')
id_Ciudad = listar_datos('Ville_id')
sexo = listar_datos( 'sex')
edad = listar_datos('Age')
casado = listar_datos('Married')
nro_hijos = listar_datos('Number_children')
nivel_educacion = listar_datos('education_level')
miembros_fam_tot = listar_datos('total_members')
activo_ganado = listar_datos('gained_asset')
activo_duradero = listar_datos('durable_asset')
ahorro_activos = listar_datos('save_asset')
gastos_manutencion = listar_datos('living_expenses')
otros_gastos = listar_datos('other_expenses')
salario_entrante = listar_datos('incoming_salary')
granja_propia_entrante = listar_datos('incoming_own_farm')
negocios_entrantes = listar_datos('incoming_business')
entrada_sin_negocio = listar_datos('incoming_no_business')
entrada_agricola = listar_datos('incoming_agricultural')
gastos_agricolas = listar_datos('farm_expenses')
mano_de_obra_primaria = listar_datos('labor_primary')
inversion_duradera = listar_datos('lasting_investment')
sin_inversion_duradera = listar_datos('no_lasting_investmen')
deprimido = listar_datos('depressed')

#Uso de la funcion para la obtencion de MEDIAS
print('************  MEDIAS  ************')
print('Edad: ', media(edad))
print('Numero de Hijos: ', media(nro_hijos))
print('Nivel de Educacion: ', media(nivel_educacion))
print('Miembros de la familia: ', media(miembros_fam_tot))
print('Activo Ganado: ', media(activo_ganado))
print('Actvo Duradero: ', media(activo_duradero))
print('Ahorro de Activos: ', media(ahorro_activos))
print('Gastos de Manutencion: ', media(gastos_manutencion))
print('Otros Gastos: ', media(otros_gastos))
print('Entrada Agricola: ', media(entrada_agricola))
print('Gastos Agricolas: ', media(gastos_agricolas))
print('Inversion Duradera: ', media(inversion_duradera))
print('Sin Inversion Duradera: ', media(sin_inversion_duradera))

#Uso de la funcion para la obtencion de la MODA
print('************  MODA  ************')
print('Ciudad: ', moda(id_Ciudad))
print('Sexo: ', moda(sexo))
print('Edad: ', moda(edad))
print('Casado: ', moda(casado))
print('Numero de Hijos: ', moda(nro_hijos))
print('Nivel de Educacion: ', moda(nivel_educacion))
print('Miembros de la familia: ', moda(miembros_fam_tot))
print('Activo Ganado: ', moda(activo_ganado))
print('Activo Duradero: ', moda(activo_duradero))
print('Ahorro activos: ', moda(ahorro_activos))
print('Gastos de Manutencion: ', moda(gastos_manutencion))
print('Otros Gastos: ', moda(otros_gastos))
print('Salario Entrante: ', moda(salario_entrante))
print('Granja Propia Entrante: ', moda(granja_propia_entrante))
print('Negocios Entrantes: ', moda(negocios_entrantes))
print('Entrada sin Negocio: ', moda(entrada_sin_negocio))
print('Entrada Agricola: ', moda(entrada_agricola))
print('Gastos Agricolas: ', moda(gastos_agricolas))
print('Mano de obra Primaria: ', moda(mano_de_obra_primaria))
print('Inversion Duradera: ', moda(inversion_duradera))
print('Sin Inverion Duradera: ', moda(sin_inversion_duradera))
print('DEPRIMIDO: ', moda(deprimido))

print('************  CUARTILES  ************')
print('Edad: '); cuartiles(edad)
print('Numero de Hijos: '); cuartiles(nro_hijos)
print('Nivel de Educacion: '); cuartiles(nivel_educacion)
print('Miembros de la familia: '); cuartiles(miembros_fam_tot)
print('Activo Ganado: '); cuartiles(activo_ganado)
print('Actvo Duradero: '); cuartiles(activo_duradero)
print('Ahorro de Activos: '); cuartiles(ahorro_activos)
print('Gastos de Manutencion: '); cuartiles(gastos_manutencion)
print('Otros Gastos: '); cuartiles(otros_gastos)
print('Entrada Agricola: '); cuartiles(entrada_agricola)
print('Gastos Agricolas: '); cuartiles(gastos_agricolas)
print('Inversion Duradera: '); cuartiles(inversion_duradera)
print('Sin Inversion Duradera: '); cuartiles(sin_inversion_duradera)

print('************  PERCENTILES  ************')
print('Edad n: ', percentiles(edad, 50))
print('Numero de Hijos: ', percentiles(nro_hijos, 50))
print('Nivel de Educacion: ', percentiles(nivel_educacion, 50))
print('Miembros de la familia: ', percentiles(miembros_fam_tot, 50))