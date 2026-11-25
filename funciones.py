import random


GENEROS_VALIDOS = ("RPG", "Deportes", "Carreras", "Aventura", "Estrategia")


def es_numero_entero(texto):
    """Verifica con codigos ASCII si texto contiene solo digitos del 0 al 9."""
    es_valido = True
    if len(texto) == 0:
        es_valido = False
    else:
        i = 0
        while i < len(texto):
            codigo = ord(texto[i])
            if codigo < 48 or codigo > 57:
                es_valido = False
            i = i + 1
    return es_valido


def es_numero_flotante(texto):
    """Verifica con codigos ASCII si texto es un numero decimal o entero positivo."""
    es_valido = True
    puntos = 0
    if len(texto) == 0:
        es_valido = False
    else:
        i = 0
        while i < len(texto):
            codigo = ord(texto[i])
            if codigo == 46:
                puntos = puntos + 1
                if puntos > 1:
                    es_valido = False
            elif codigo < 48 or codigo > 57:
                es_valido = False
            i = i + 1
        if texto == ".":
            es_valido = False
    return es_valido


def separar_por_coma(linea):
    """Separa una linea de texto por comas recorriendo caracter por caracter."""
    partes = []
    actual = ""
    i = 0
    while i < len(linea):
        caracter = linea[i]
        if caracter == ",":
            partes.append(actual)
            actual = ""
        elif caracter != "\n" and caracter != "\r":
            actual = actual + caracter
        i = i + 1
    partes.append(actual)
    return partes


def pasar_a_minusculas(texto):
    """Convierte letras mayusculas A-Z a minusculas a-z usando ASCII."""
    resultado = ""
    i = 0
    while i < len(texto):
        codigo = ord(texto[i])
        if codigo >= 65 and codigo <= 90:
            resultado = resultado + chr(codigo + 32)
        else:
            resultado = resultado + texto[i]
        i = i + 1
    return resultado


def normalizar_genero(texto):
    """Devuelve el nombre oficial del genero si coincide sin importar mayusculas."""
    minus = pasar_a_minusculas(texto)
    genero_limpio = ""
    if minus == "rpg":
        genero_limpio = "RPG"
    elif minus == "deportes":
        genero_limpio = "Deportes"
    elif minus == "carreras":
        genero_limpio = "Carreras"
    elif minus == "aventura":
        genero_limpio = "Aventura"
    elif minus == "estrategia":
        genero_limpio = "Estrategia"
    return genero_limpio


def cargar_juegos(ruta):
    """Lee juegos desde el archivo CSV y devuelve una lista de diccionarios."""
    juegos = []
    archivo = open(ruta, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    i = 0
    while i < len(lineas):
        campos = separar_por_coma(lineas[i])
        if len(campos) == 6 and campos[0] != "codigo_identificador" and campos[0] != "":
            juego = {
                "codigo_identificador": campos[0],
                "nombre": campos[1],
                "genero": campos[2],
                "precio": float(campos[3]),
                "stock": int(campos[4]),
                "unidades_vendidas": int(campos[5])
            }
            juegos.append(juego)
        i = i + 1
    return juegos


def guardar_juegos(ruta, juegos):
    """Guarda la lista completa de videojuegos en el archivo CSV."""
    archivo = open(ruta, "w", encoding="utf-8")
    archivo.write("codigo_identificador,nombre,genero,precio,stock,unidades_vendidas\n")
    i = 0
    while i < len(juegos):
        j = juegos[i]
        fila = (
            j["codigo_identificador"] + ","
            + j["nombre"] + ","
            + j["genero"] + ","
            + str(j["precio"]) + ","
            + str(j["stock"]) + ","
            + str(j["unidades_vendidas"]) + "\n"
        )
        archivo.write(fila)
        i = i + 1
    archivo.close()
    return None


def generar_codigo_unico(juegos):
    """Genera un codigo aleatorio de 7 digitos que no este repetido."""
    minimo = 1000000
    maximo = 9999999
    codigo = ""
    valido = False
    while not valido:
        numero = random.randint(minimo, maximo)
        codigo = str(numero)
        repetido = False
        i = 0
        while i < len(juegos):
            if juegos[i]["codigo_identificador"] == codigo:
                repetido = True
            i = i + 1
        if not repetido:
            valido = True
    return codigo


def alta_videojuego(juegos, ruta):
    """Solicita datos validados por consola, crea el juego y actualiza el CSV."""
    nombre = ""
    nombre_valido = False
    while not nombre_valido:
        nombre = input("Ingrese nombre del juego (3 a 50 caracteres): ")
        if len(nombre) >= 3 and len(nombre) <= 50:
            nombre_valido = True
        else:
            print("Error: el nombre debe tener entre 3 y 50 caracteres.")

    genero = ""
    genero_valido = False
    while not genero_valido:
        entrada_genero = input("Ingrese genero (RPG, Deportes, Carreras, Aventura, Estrategia): ")
        genero = normalizar_genero(entrada_genero)
        if genero != "":
            genero_valido = True
        else:
            print("Error: genero no valido.")

    precio = 0.0
    precio_valido = False
    while not precio_valido:
        entrada_precio = input("Ingrese precio (mayor a 0): ")
        if es_numero_flotante(entrada_precio):
            valor_precio = float(entrada_precio)
            if valor_precio > 0:
                precio = valor_precio
                precio_valido = True
            else:
                print("Error: el precio debe ser mayor a 0.")
        else:
            print("Error: ingrese un numero valido.")

    stock = 0
    stock_valido = False
    while not stock_valido:
        entrada_stock = input("Ingrese stock inicial (0 o mayor): ")
        if es_numero_entero(entrada_stock):
            stock = int(entrada_stock)
            stock_valido = True
        else:
            print("Error: el stock debe ser un numero entero no negativo.")

    codigo = generar_codigo_unico(juegos)
    nuevo_juego = {
        "codigo_identificador": codigo,
        "nombre": nombre,
        "genero": genero,
        "precio": precio,
        "stock": stock,
        "unidades_vendidas": 0
    }
    juegos.append(nuevo_juego)
    guardar_juegos(ruta, juegos)
    print("Videojuego registrado con codigo: " + codigo)
    return None


def registrar_venta(juegos, ruta):
    """Muestra juegos con stock, registra una venta y actualiza el archivo CSV."""
    print("\n--- JUEGOS CON STOCK DISPONIBLE ---")
    hay_stock = False
    i = 0
    while i < len(juegos):
        if juegos[i]["stock"] > 0:
            hay_stock = True
            print(
                "Codigo: " + juegos[i]["codigo_identificador"]
                + " | Nombre: " + juegos[i]["nombre"]
                + " | Genero: " + juegos[i]["genero"]
                + " | Stock: " + str(juegos[i]["stock"])
                + " | Precio: $" + str(juegos[i]["precio"])
            )
        i = i + 1

    if not hay_stock:
        print("No hay videojuegos con stock disponible.")
    else:
        codigo_ingresado = input("Ingrese el codigo identificador del juego: ")
        posicion = -1
        i = 0
        while i < len(juegos):
            if juegos[i]["codigo_identificador"] == codigo_ingresado:
                posicion = i
            i = i + 1

        if posicion == -1:
            print("Error: codigo no encontrado.")
        elif juegos[posicion]["stock"] <= 0:
            print("Error: el juego seleccionado no tiene stock.")
        else:
            entrada_cant = input("Ingrese cantidad de unidades a vender: ")
            if es_numero_entero(entrada_cant):
                cantidad = int(entrada_cant)
                if cantidad <= 0:
                    print("Error: la cantidad debe ser mayor a 0.")
                elif cantidad > juegos[posicion]["stock"]:
                    print("Error: no hay suficiente stock. Disponible: " + str(juegos[posicion]["stock"]))
                else:
                    juegos[posicion]["stock"] = juegos[posicion]["stock"] - cantidad
                    juegos[posicion]["unidades_vendidas"] = juegos[posicion]["unidades_vendidas"] + cantidad
                    guardar_juegos(ruta, juegos)
                    print("Venta registrada. Nuevo stock: " + str(juegos[posicion]["stock"]))
            else:
                print("Error: ingrese una cantidad entera valida.")
    return None


def mostrar_estadisticas(juegos):
    """Muestra las 5 estadisticas requeridas sobre los videojuegos."""
    if len(juegos) == 0:
        print("No hay videojuegos cargados.")
    else:
        mayor_vendido = juegos[0]
        i = 1
        while i < len(juegos):
            if juegos[i]["unidades_vendidas"] > mayor_vendido["unidades_vendidas"]:
                mayor_vendido = juegos[i]
            i = i + 1
        print(
            "\n1) Videojuego mas vendido: "
            + mayor_vendido["nombre"]
            + " | Unidades vendidas: "
            + str(mayor_vendido["unidades_vendidas"])
        )

        ventas_genero = {}
        i = 0
        while i < len(GENEROS_VALIDOS):
            ventas_genero[GENEROS_VALIDOS[i]] = 0
            i = i + 1

        i = 0
        while i < len(juegos):
            g = juegos[i]["genero"]
            ventas_genero[g] = ventas_genero[g] + juegos[i]["unidades_vendidas"]
            i = i + 1

        mejor_genero = GENEROS_VALIDOS[0]
        i = 1
        while i < len(GENEROS_VALIDOS):
            if ventas_genero[GENEROS_VALIDOS[i]] > ventas_genero[mejor_genero]:
                mejor_genero = GENEROS_VALIDOS[i]
            i = i + 1
        print(
            "2) Genero con mas unidades vendidas: "
            + mejor_genero
            + " | Unidades vendidas: "
            + str(ventas_genero[mejor_genero])
        )

        valor_inventario = 0.0
        i = 0
        while i < len(juegos):
            valor_inventario = valor_inventario + (juegos[i]["stock"] * juegos[i]["precio"])
            i = i + 1
        print("3) Valor total del inventario: $" + str(valor_inventario))

        sin_stock = 0
        i = 0
        while i < len(juegos):
            if juegos[i]["stock"] == 0:
                sin_stock = sin_stock + 1
            i = i + 1
        porcentaje_sin_stock = (sin_stock / len(juegos)) * 100
        print("4) Porcentaje de videojuegos sin stock: " + str(porcentaje_sin_stock) + "%")

        print("5) Promedio de precios por genero:")
        i = 0
        while i < len(GENEROS_VALIDOS):
            g = GENEROS_VALIDOS[i]
            suma = 0.0
            cantidad = 0
            k = 0
            while k < len(juegos):
                if juegos[k]["genero"] == g:
                    suma = suma + juegos[k]["precio"]
                    cantidad = cantidad + 1
                k = k + 1
            if cantidad > 0:
                promedio = suma / cantidad
                print("   - " + g + ": $" + str(promedio))
            else:
                print("   - " + g + ": Sin juegos")
            i = i + 1
    return None


def mostrar_catalogo_ordenado(juegos):
    """Ordena una copia de la lista por criterio y sentido y muestra los datos."""
    if len(juegos) == 0:
        print("No hay videojuegos en el catalogo.")
    else:
        criterio = ""
        criterio_valido = False
        while not criterio_valido:
            criterio = pasar_a_minusculas(input("Ordenar por (nombre, genero, precio): "))
            if criterio == "nombre" or criterio == "genero" or criterio == "precio":
                criterio_valido = True
            else:
                print("Error: criterio invalido.")

        sentido = ""
        sentido_valido = False
        while not sentido_valido:
            sentido = pasar_a_minusculas(input("Sentido (asc o desc): "))
            if sentido == "asc" or sentido == "desc":
                sentido_valido = True
            else:
                print("Error: sentido invalido.")

        copia = []
        i = 0
        while i < len(juegos):
            copia.append(juegos[i])
            i = i + 1

        n = len(copia)
        i = 0
        while i < n - 1:
            j = 0
            while j < n - 1 - i:
                a = copia[j][criterio]
                b = copia[j + 1][criterio]
                if criterio == "nombre" or criterio == "genero":
                    a = pasar_a_minusculas(a)
                    b = pasar_a_minusculas(b)

                cambiar = False
                if sentido == "asc" and a > b:
                    cambiar = True
                elif sentido == "desc" and a < b:
                    cambiar = True

                if cambiar:
                    aux = copia[j]
                    copia[j] = copia[j + 1]
                    copia[j + 1] = aux
                j = j + 1
            i = i + 1

        print("\n--- CATALOGO ORDENADO ---")
        i = 0
        while i < len(copia):
            item = copia[i]
            print(
                "Codigo: " + item["codigo_identificador"]
                + " | Nombre: " + item["nombre"]
                + " | Genero: " + item["genero"]
                + " | Precio: $" + str(item["precio"])
                + " | Stock: " + str(item["stock"])
                + " | Vendidos: " + str(item["unidades_vendidas"])
            )
            i = i + 1
    return None