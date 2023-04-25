import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos = pd.read_csv("b_depressed.csv")
datos.groupby(['Age'])['sex'].mean()

datos[['Married','Number_children']].value_counts().plot(kind="bar")
plt.title("Estado civil e Hijos")
plt.show()

datos[['Married','sex']].value_counts().plot(kind="bar")
plt.title("Estado civil y Genero")
plt.show()

datos[['Married','depressed']].value_counts().plot(kind="bar")
plt.title("Estado civil y Depresion")
plt.show()

datos[['Number_children','depressed']].value_counts().plot(kind="bar")
plt.title("Hijos y Depresion")
plt.show()
