import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
datos = pd.read_csv('b_depressed.csv')
datos = datos.fillna(datos.mean())

datos = pd.get_dummies(data=datos, drop_first=True)
#explicativas = datos.drop(columns='depressed')
explicativas = datos[['Married', 'sex', 'Number_children']].copy()

objetivo = datos.depressed
model = DecisionTreeClassifier()
model.fit(X=explicativas, y=objetivo)
DecisionTreeClassifier(max_depth=4)

plt.figure(figsize=(14,8))
plot_tree(decision_tree=model, feature_names=explicativas.columns, filled=True)
plt.show()

a = explicativas.sample()
print(a)
print(model.predict_proba(a))