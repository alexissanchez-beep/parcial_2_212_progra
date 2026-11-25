import random


def obtener_carta() -> str:
    """
    Genera y devuelve una carta aleatoria de un mazo estandar sin palos.

    Parametros:
        Ninguno.

    Retorna:
        str: Cadena que representa la carta ('2'-'10', 'J', 'Q', 'K', 'A').
    """
    cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    indice = random.randint(0, len(cartas) - 1)
    carta_elegida = cartas[indice]
    return carta_elegida


def formatear_mano(mano: list) -> str:
    """
    Convierte una lista de cartas en una cadena legible separada por guiones.

    Parametros:
        mano (list): Lista de strings con las cartas de la mano.

    Retorna:
        str: Representacion formateada de la mano (ej: 'A - 10 - K').
    """
    texto = ""
    i = 0
    while i < len(mano):
        texto = texto + mano[i]
        if i < len(mano) - 1:
            texto = texto + " - "
        i = i + 1
    return texto


def calcular_puntos(mano: list) -> int:
    """
    Calcula el puntaje total de una mano de BlackJack aplicando el valor
    dinamico del As (11 o 1) para evitar superar 21 puntos.

    Parametros:
        mano (list): Lista de strings con las cartas actuales.

    Retorna:
        int: Puntaje total acumulado de la mano.
    """
    total = 0
    ases = 0
    i = 0

    while i < len(mano):
        carta = mano[i]
        if carta == "J" or carta == "Q" or carta == "K":
            total = total + 10
        elif carta == "A":
            total = total + 11
            ases = ases + 1
        else:
            total = total + int(carta)
        i = i + 1

    while total > 21 and ases > 0:
        total = total - 10
        ases = ases - 1

    return total


def es_entero_positivo(cadena: str) -> bool:
    """
    Valida manualmente mediante codigos ASCII si una cadena representa
    un numero entero positivo mayor a cero (sin usar metodos de string).

    Parametros:
        cadena (str): Texto ingresado por el usuario.

    Retorna:
        bool: True si es un entero valido mayor a 0, False en caso contrario.
    """
    valido = True
    if len(cadena) == 0:
        valido = False
    else:
        i = 0
        while i < len(cadena) and valido:
            codigo = ord(cadena[i])
            if codigo < 48 or codigo > 57:
                valido = False
            i = i + 1
        if valido and int(cadena) <= 0:
            valido = False
    return valido


def jugar_tragamonedas(puntaje: int, apuesta: int) -> int:
    """
    Ejecuta una tirada de tragamonedas generando 3 simbolos aleatorios
    mediante random.randint() y actualiza el puntaje segun las reglas.

    Parametros:
        puntaje (int): Puntaje actual disponible del jugador.
        apuesta (int): Valor de la apuesta realizada para la ronda.

    Retorna:
        int: Nuevo puntaje del jugador luego de resolver la tirada.
    """
    nuevo_puntaje = puntaje

    if apuesta > puntaje:
        print("La apuesta actual es mayor al puntaje disponible.")
    else:
        caracteres = ["A", "B", "C", "D", "E", "0", "7"]
        limite = len(caracteres) - 1

        c1 = caracteres[random.randint(0, limite)]
        c2 = caracteres[random.randint(0, limite)]
        c3 = caracteres[random.randint(0, limite)]

        print("Resultado del tiro: [ " + c1 + " | " + c2 + " | " + c3 + " ]")

        if c1 == "0" and c2 == "0" and c3 == "0":
            print("Tres ceros. Perdiste todo el puntaje.")
            nuevo_puntaje = 0
        elif c1 == "7" and c2 == "7" and c3 == "7":
            ganancia = apuesta * 10
            print("Tres sietes. Ganaste " + str(ganancia) + " puntos.")
            nuevo_puntaje = puntaje + ganancia
        elif c1 == c2 and c2 == c3:
            ganancia = apuesta * 5
            print("Tres iguales. Ganaste " + str(ganancia) + " puntos.")
            nuevo_puntaje = puntaje + ganancia
        elif c1 == c2 or c1 == c3 or c2 == c3:
            ganancia = apuesta * 2
            print("Dos iguales. Ganaste " + str(ganancia) + " puntos.")
            nuevo_puntaje = puntaje + ganancia
        else:
            print("Todos distintos. Perdiste " + str(apuesta) + " puntos.")
            nuevo_puntaje = puntaje - apuesta

    return nuevo_puntaje


def jugar_blackjack(puntaje: int, apuesta: int) -> int:
    """
    Desarrolla una ronda completa de BlackJack simplificado (turno del jugador
    y turno de la banca) y calcula el puntaje resultante.

    Parametros:
        puntaje (int): Puntaje actual disponible del jugador.
        apuesta (int): Valor de la apuesta realizada para la ronda.

    Retorna:
        int: Nuevo puntaje del jugador al finalizar la ronda.
    """
    nuevo_puntaje = puntaje

    if apuesta > puntaje:
        print("La apuesta actual es mayor al puntaje disponible.")
    else:
        mano_jugador = [obtener_carta(), obtener_carta()]
        mano_banca = [obtener_carta(), obtener_carta()]

        print("\n--- INICIO DE RONDA DE BLACKJACK ---")
        print("Tus cartas: " + formatear_mano(mano_jugador) + " (Total: " + str(calcular_puntos(mano_jugador)) + ")")
        print("Carta visible de la banca: " + mano_banca[0])

        turno_jugador = True
        se_paso_jugador = False

        while turno_jugador:
            puntos_jugador = calcular_puntos(mano_jugador)
            if puntos_jugador > 21:
                print("\nTe pasaste de 21. Perdiste la apuesta.")
                se_paso_jugador = True
                turno_jugador = False
            else:
                print("\n1) Pedir carta")
                print("2) Plantarse")
                op = input("Elija una opcion: ")

                if op == "1":
                    nueva_carta = obtener_carta()
                    mano_jugador.append(nueva_carta)
                    print("Recibiste: " + nueva_carta)
                    print("Tus cartas: " + formatear_mano(mano_jugador) + " (Total: " + str(calcular_puntos(mano_jugador)) + ")")
                elif op == "2":
                    turno_jugador = False
                else:
                    print("Opcion invalida.")

        if se_paso_jugador:
            nuevo_puntaje = puntaje - apuesta
        else:
            print("\n--- TURNO DE LA BANCA ---")
            print("Cartas de la banca: " + formatear_mano(mano_banca) + " (Total: " + str(calcular_puntos(mano_banca)) + ")")

            while calcular_puntos(mano_banca) < 17:
                nueva_carta_banca = obtener_carta()
                mano_banca.append(nueva_carta_banca)
                print("La banca pide carta y recibe: " + nueva_carta_banca)
                print("Cartas de la banca: " + formatear_mano(mano_banca) + " (Total: " + str(calcular_puntos(mano_banca)) + ")")

            puntos_jugador = calcular_puntos(mano_jugador)
            puntos_banca = calcular_puntos(mano_banca)

            print("\n--- RESULTADO FINAL ---")
            print("Jugador: " + str(puntos_jugador) + " | Banca: " + str(puntos_banca))

            if puntos_banca > 21:
                print("La banca se paso de 21. Ganaste el doble de tu apuesta.")
                nuevo_puntaje = puntaje + apuesta
            elif puntos_jugador > puntos_banca:
                print("Ganaste la ronda. Ganaste el doble de tu apuesta.")
                nuevo_puntaje = puntaje + apuesta
            elif puntos_jugador < puntos_banca:
                print("La banca tiene mayor puntaje. Perdiste tu apuesta.")
                nuevo_puntaje = puntaje - apuesta
            else:
                print("Empate (Push). Se te devuelve la apuesta.")
                nuevo_puntaje = puntaje

    return nuevo_puntaje


def cambiar_apuesta(puntaje: int, apuesta_actual: int) -> int:
    """
    Solicita un nuevo valor de apuesta por consola, valida que sea un entero
    positivo dentro del rango permitido y devuelve la apuesta resultante.

    Parametros:
        puntaje (int): Puntaje total disponible del jugador.
        apuesta_actual (int): Valor de apuesta vigente antes del cambio.

    Retorna:
        int: Nueva apuesta validada, o la apuesta anterior si el ingreso fue invalido.
    """
    nueva_apuesta = apuesta_actual
    entrada = input("Ingrese nueva apuesta: ")

    if es_entero_positivo(entrada):
        valor = int(entrada)
        if valor >= 1 and valor <= puntaje:
            nueva_apuesta = valor
            print("Apuesta actualizada a: " + str(nueva_apuesta))
        else:
            print("La apuesta debe ser entre 1 y tu puntaje disponible.")
    else:
        print("Debe ingresar un numero entero positivo valido.")

    return nueva_apuesta