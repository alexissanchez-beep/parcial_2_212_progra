#creando diccionarios con dict()
diccionario = dict(nombre="Alexis",apellido="Sanchez")

#las listas no pueden ser claves si usamos fozenset para meter conjuntos
diccionario = {("dalto","rancio")}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido"],"no se")

print(diccionario) 