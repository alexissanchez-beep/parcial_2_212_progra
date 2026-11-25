#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"
frase_resultante = frase(adjetivo = "capo",nombre = "Alexis", apellido = "Sanchez")
print(frase_resultante)
