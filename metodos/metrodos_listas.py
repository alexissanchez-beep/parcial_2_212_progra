lista = list(["hola","alexis",21,22,23,True])

#devuelve la cantidad de elemento de la lista
cadena_elementos = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJAJA")

#agregando un elemento a la lista con un indice especifico
lista.insert(2,"TOMA MAMA")

#agregamos varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento de la lista por su indice
lista.pop(1)#-1 para eliminar el ultimo 

#remueve un elemento de la lista por su valor
lista.remove("TOMA MAMA")

#ordena la lista de menor a mayor(si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invierte los elementos de una lista
#lista.reverse()

#elimina todos los elementos de la lista
# lista.clear()
print(lista)