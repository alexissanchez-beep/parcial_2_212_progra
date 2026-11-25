#forma optima de sumar valores
def suma_total (numeros):
    return sum([*numeros])
resultado = suma_total([5,3,9,10,20,3])
print(resultado)

#lo mismo que arriba pero utilizando el operador * como parametro (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
resultado2 = suma("Alexis",5,3,9,10,20,3)
print(resultado2)

