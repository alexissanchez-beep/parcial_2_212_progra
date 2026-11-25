# #creando una funcion simple
# def saludar():
#     print("Hola alexis, mi maestro ¿como andas?")

# #ejecutando la funcion simple
# saludar()

#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "rey"
    
    print(f"Hola {nombre} mi {adjetivo} como andas?")
saludar("alexis","hombre")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num 
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funcion
password,primer_numero = crear_contraseña_random(405067)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")
 
 