import pandas as pd
from sklearn.preprocessing import MinMaxScaler

print("**************** IMPUTACION CON PANDAS  ***********************")
# Cargar los datos
datos = pd.read_csv('b_depressed.csv')

# Imputar valores faltantes con la media de la columna
datos = datos.fillna(datos.mean())

print(datos)

print("**************** NORMALIZACION CON PANDAS ***********************")
# Cargar los datos
datos_1 = pd.read_csv('b_depressed.csv')

#Normalizar los datos
X_normalized = (datos_1 - datos_1.mean()) / datos_1.std()
print(X_normalized)

print("**************** ESCALACION CON PANDAS ***********************")
# Cargar los datos
datos_2 = pd.read_csv('b_depressed.csv')
# Escalar los datos
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(datos_2), columns=datos_2.columns)
print(df_scaled)
