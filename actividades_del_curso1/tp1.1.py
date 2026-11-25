#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5


#diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el pocentaje de tiempo vacio promedio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#mostrando las diferencias de duracion
print("-----------------")
print(f"el curso de dalto dura: ")
print(f" -  un {diferencia_con_min}% menos que el mas rapido")
print(f" -  un {diferencia_con_max}% menos que el mas lento")
print(f" -  un {diferencia_con_promedio}% menos que el mas promedio")
print("-----------------")

#mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f"un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")
print("-----------------")

#mostrando diferencias si los otros cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso /10} horas de otros cursos")
print(f"ver 10 horas de otros curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio /10} horas de este curso")
print("-----------------")

##########################optimizado###########
# Duraciones en horas
otros_cursos = [2.5, 4, 7]
otros_cursos_min = min(otros_cursos)
otros_cursos_max = max(otros_cursos)
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencias de duración (%)
diferencia_con_min = round(100 - (dalto_curso / otros_cursos_min * 100), 1)
diferencia_con_max = round(100 - (dalto_curso / otros_cursos_max * 100), 1)
diferencia_con_promedio = round(100 - (dalto_curso / otros_cursos_promedio * 100), 1)

# Porcentaje de tiempo vacío eliminado (%)
tiempo_vacio_promedio = round(100 - (otros_cursos_promedio / crudo_promedio * 100), 1)
tiempo_vacio_dalto = round(100 - (dalto_curso / crudo_dalto * 100), 1)

# Equivalencias cada 10 horas
equivalencia_dalto_a_otros = round(otros_cursos_promedio / dalto_curso * 10, 1)
equivalencia_otros_a_dalto = round(dalto_curso / otros_cursos_promedio * 10, 1)

# Mostrando las diferencias de duración
print("-----------------")
print("El curso de Dalto dura:")
print(f" - Un {diferencia_con_min}% menos que el más rápido")
print(f" - Un {diferencia_con_max}% menos que el más lento")
print(f" - Un {diferencia_con_promedio}% menos que el promedio")
print("-----------------")

# Mostrando la cantidad de espacios vacíos que se remueven
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío")
print(f"Este curso eliminó el {tiempo_vacio_dalto}% de tiempo vacío")
print("-----------------")

# Mostrando diferencias si los otros cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {equivalencia_dalto_a_otros} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {equivalencia_otros_a_dalto} horas de este curso")
print("-----------------")