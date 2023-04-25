from kanren import run, eq, var, Relation, facts
# Definimos las relaciones lógicas y agregamos hechos

#Abuelos
abuelos_nietos = Relation()
facts(abuelos_nietos, ("Abraham", "Bart"), ("Abraham", "Lisa"),("Abraham", "Maggie"), 
              ("Clancy", "Bart"), ("Clancy", "Lisa"),("Clancy", "Maggie"),("Clancy", "Lin"),
              ("Mona", "Bart"), ("Mona", "Lisa"), ("Mona", "Maggie"),
              ("Jaqueline", "Bart"), ("Jaqueline", "Lisa"), ("Jaqueline", "Maggie"), ("Jaqueline", "Lin"))
#Padres
padres_hijos = Relation()
facts(padres_hijos, ("Abraham", "Herbert"), ("Abraham", "Homero"),
              ("Clancy", "Selma"), ("Clancy", "Patty"), ("Clancy", "Marge"),
              ("Homero", "Bart"), ("Homero", "Lisa"), ("Homero", "Maggie"),
              ("Mona", "Herbert"), ("Mona", "Homero"),
              ("Jaqueline", "Selma"), ("Jaqueline", "Patty"), ("Jaqueline", "Marge"),
              ("Marge", "Bart"), ("Marge", "Lisa"), ("Marge", "Maggie"),
              ("Selma", "Lin"))

#Tios
tios_sobrinos = Relation()
facts(tios_sobrinos, ("Homero", "Lin"),
            ("Herbert", "Bart"),("Herbert", "Lisa"), ("Herbert", "Maggie"),
            ("Marge", "Lin"), 
            ("Patty", "Bart"),("Patty", "Lisa"), ("Patty", "Maggie"),("Patty", "Lin"),
            ("Selma", "Bart"),("Selma", "Lisa"), ("Selma", "Maggie"))


#Primos
primo = Relation()
facts(primo, ("Bart", "Lin"),
      ("Lisa", "Lin"), ("Lin", "Bart"), ("Lin", "Lisa"))

# Definimos la variable lógica
var1=var()
var2=var()
# Nietos de Jaqueline Bouvier
#print("Jaqueline es abuela de:")
#run(5,var1,abuelos_nietos("Jaqueline",var1))

def print_nietos(abuela):
    nietos = run(5, var1, abuelos_nietos(abuela, var1))
    print(f"{abuela} es abuela/abuelo de:")
    for nieto in nietos:
        print(f"- {nieto}")

def print_hijos(madre):
    hijos = run(5, var1, padres_hijos(madre, var1))
    print(f"{madre} es madre/padre de:")
    for hijos in hijos:
        print(f"- {hijos}")
def print_padres(hijo):
    padres = run(5, var1, padres_hijos(var1, hijo))
    print(f"{hijo} es hijo/hija de:")
    for padres in padres:
        print(f"- {padres}")
      
def print_sobrinos(tio):
    sobrinos = run(5, var1, tios_sobrinos(tio, var1))
    print(f"{tio} es tia/tio de:")
    for sobrinos in sobrinos:
        print(f"- {sobrinos}")

def print_primos(primo_x):
    primos = run(5, var1, primo(primo_x, var1))
    print(f"{primo_x} es primo/prima de:")
    for primos in primos:
        print(f"- {primos}")
print_nietos("Jaqueline")
print_hijos("Mona")
print_padres("Herbert")
print_sobrinos("Patty")
print_primos("Lin")