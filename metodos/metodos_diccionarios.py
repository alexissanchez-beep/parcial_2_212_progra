diccionario = {
    "nombre" : "alexis",
    "apellido" : "sanchez",
    "subs" :  1000000
}

#obteniendo un elemento con .get si no lo encuentra nos devuelve none
claves = diccionario.get("nombre")

#eliminando todo del diccionario
# diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)