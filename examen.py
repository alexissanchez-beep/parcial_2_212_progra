from funciones import (
    cargar_juegos,
    alta_videojuego,
    registrar_venta,
    mostrar_estadisticas,
    mostrar_catalogo_ordenado
)

archivo_csv = "juegos.csv"
catalogo = cargar_juegos(archivo_csv)
opcion = ""

while opcion != "5":
    print("\n=== MENU PRINCIPAL ===")
    print("1. Alta de videojuego.")
    print("2. Registrar una venta.")
    print("3. Consultar estadisticas.")
    print("4. Mostrar catalogo ordenado.")
    print("5. Salir.")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        alta_videojuego(catalogo, archivo_csv)
    elif opcion == "2":
        registrar_venta(catalogo, archivo_csv)
    elif opcion == "3":
        mostrar_estadisticas(catalogo)
    elif opcion == "4":
        mostrar_catalogo_ordenado(catalogo)
    elif opcion == "5":
        print("Programa finalizado.")
    else:
        print("Opcion invalida.")