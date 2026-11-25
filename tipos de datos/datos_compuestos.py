#creando una lista (se pueden modificar)
lista = ["alexis sanchez", "soy alexis", True, 1.87]

#creando una tupla (no se pueden modificar)
tupla = ("alexis sanchez", "soy alexis", True, 1.87)

#esto es valido 
#lista[3]

#creando un conjunto (set) (no se puede llamar a los elemenos por su indice, no almacena datos duplicados)
conjunto = {"alexis sanchez", "soy alexis", True, 1.87}


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    "nombre" : "alexis sanchez",
    "canal" : "soy alexis",
    "estas_emocionado" : True,
    "altura" : 1.87,
    "datos_duplicados" : "soy alexis"
}

print(diccionario["nombre"])