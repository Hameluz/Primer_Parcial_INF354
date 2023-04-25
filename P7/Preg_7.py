import csv
import random

datos = []
with open('b_depressed.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        datos.append(row)
def Entr_Prueba(datos_1):
    #Número total de filas en el CSV
    num_fila = len(datos_1)
    #Conjunto de entrenamiento y prueba
    train_size = int(0.8 * num_fila)
    #lista de índices aleatorios
    indices = random.sample(range(num_fila), num_fila)
    # Separar los índices de las filas de conjunto de entrenamiento y de conjunto de prueba
    train_indices = indices[:train_size]
    test_indices = indices[train_size:]
    # Almacenar los datos del conjunto de entrenamiento y prueba
    datos_train = [datos[i] for i in train_indices]
    datos_test = [datos[i] for i in test_indices]
    return datos_train, datos_test
print("*************************** Primero ***************************")
dato_a, dato_b = Entr_Prueba(datos)
print(dato_b)
print("*************************** Segundo ***************************")
dato_c, dato_d = Entr_Prueba(dato_b)
print(dato_d)