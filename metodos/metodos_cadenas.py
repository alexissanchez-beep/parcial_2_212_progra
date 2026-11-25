cadena1 = "Hola soy alexis"
cadena2 = "Bienvenido maquinola"

#convierte a mayusculas
mayusculas = cadena1.upper()

#convierte a minusculas
minusculas = cadena1.lower()

#Primera letra en mayusculas
primer_letra_mayusculas = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no lo encuentra devulve -1
buscamos_find = cadena1.find("s")

#buscamoos una cadena en otra cadena; si no lo encuentra lanza una excepcion 
busqueda_index = cadena1.index("H")

#si es numerico devolvemos true; sino devuelve false
es_numerico = cadena1.isnumeric()

es_alfanumerico = cadena1.isalpha()
print(es_numerico)