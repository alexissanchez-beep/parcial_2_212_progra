diccionario = {
    "nombre": "Alexis",
    "apellido": "Sanchez",
    "club": "Lanus"
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print(f"la clave es; {key}")

#recorriendo el diccionario con items() paras obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
