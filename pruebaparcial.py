# --- PARTE 1: LAS CAJITAS (VARIABLES) DONDE GUARDAMOS INFORMACIÓN ---
# Aquí creamos "cajitas" (variables) y les ponemos un valor inicial de cero.
# Las usamos para contar o sumar cosas que pasan a lo largo del día en el cine.

total_funciones = 0          # Cajita para contar CUÁNTAS funciones se registraron en total.
total_espectadores = 0       # Cajita para SUMAR TODOS los espectadores de todas las funciones.

# Estas cajitas son para contar funciones que cumplen ciertas reglas de cantidad de espectadores:
entre50_y_110 = 0            # Cajita para contar funciones con entre 50 y 110 espectadores.
entre_100_150_200 = 0        # Cajita para contar funciones con exactamente 100, 150 o 200 espectadores.
menos_20 = 0                 # Cajita para contar funciones con MENOS de 20 espectadores.

# Estas cajitas son para SUMAR los espectadores que hubo en cada turno.
# Así podemos saber al final qué turno acumuló más gente.
espectadores_turno_m = 0
espectadores_turno_t = 0
espectadores_turno_n = 0

# Estas cajitas son para contar CUÁNTAS funciones se hicieron en cada sala.
sala1_funciones = 0
sala2_funciones = 0
sala3_funciones = 0
sala4_funciones = 0

# Estas dos cajitas son para recordar cuál fue la función que tuvo MÁS espectadores en UN SOLO pase.
max_espectadores_funcion = 0     # Aquí guardaremos el número más grande de espectadores que vimos.
nombre_pelicula_max_asistencia = "" # Aquí guardaremos el nombre de la película de esa función "récord".


# --- PARTE 2: EL MENSAJE DE BIENVENIDA Y EL BUCLE PARA PEDIR DATOS ---
# Esto es lo primero que se ve al correr el programa.

print("--- Registro de Funciones de Cine ---") # Un título bonito para el usuario.

# Este es el "corazón" del programa. El 'while True:' significa:
# "Haz lo que está aquí adentro una y otra vez, SIN PARAR, a menos que yo te diga 'break'."
while True:
    # 1. PEDIMOS EL NOMBRE DE LA PELÍCULA
    # 'input()' hace una pregunta al usuario y guarda lo que escribe en la cajita 'nombre_pelicula'.
    nombre_pelicula = input("Ingrese el nombre de la película (o 'FIN' para terminar): ")

    # 2. DECIDIMOS SI EL USUARIO QUIERE SALIR O SEGUIR
    # '.upper()' convierte lo que el usuario escribió a MAYÚSCULAS (ej. "fin" se vuelve "FIN").
    # Así, si escribe "fin", "FIN", "Fin", etc., siempre lo detectamos.
    if nombre_pelicula.upper() == "FIN":
        break # Si es "FIN", la palabra mágica 'break' hace que el bucle 'while True' PARE y el programa salte a la "Parte 4".

    # --- PARTE 3: AQUÍ PASA TODO LO IMPORTANTE POR CADA FUNCIÓN REGISTRADA ---
    # Si el usuario NO escribió "FIN", el programa sigue aquí adentro,
    # pidiendo los datos de la función actual y actualizando las cajitas.

    # 3.1. PEDIMOS LOS DEMÁS DATOS DE LA FUNCIÓN ACTUAL
    turno = input("Ingrese el turno al que desea asistir (Mañana, Tarde, Noche): ")
    # '.lower()' convierte el turno a minúsculas (ej. "Mañana" se vuelve "mañana").
    # Esto facilita compararlo después sin preocuparnos por mayúsculas.
    turno_normalizado = turno.lower()

    # Pedimos la sala y la convertimos a un NÚMERO entero con 'int()'.
    # Si el usuario escribe "uno", dará error, debe escribir "1".
    sala = int(input("Ingrese la sala deseada (1-4): "))

    # Pedimos la cantidad de espectadores y la convertimos a NÚMERO entero con 'int()'.
    cantidad = int(input("Ingrese la cantidad de espectadores: "))

    # 3.2. ACTUALIZAMOS NUESTRAS CAJITAS CON LA INFORMACIÓN DE ESTA FUNCIÓN

    # Aumentamos en 1 el contador total de funciones.
    total_funciones += 1 # Es lo mismo que decir: total_funciones = total_funciones + 1

    # Sumamos los espectadores de esta función al total acumulado.
    total_espectadores += cantidad # Es lo mismo que decir: total_espectadores = total_espectadores + cantidad

    # Si la cantidad de espectadores está entre 50 y 110 (incluyendo el 50 y el 110)...
    if cantidad >= 50 and cantidad <= 110:
        entre50_y_110 += 1 # Aumentamos en 1 el contador de este tipo de funciones.

    # Si la cantidad de espectadores es EXACTAMENTE 100, O 150, O 200...
    if cantidad == 100 or cantidad == 150 or cantidad == 200:
        entre_100_150_200 += 1 # Aumentamos en 1 el contador de este tipo de funciones.

    # Si la cantidad de espectadores es MENOR a 20...
    if cantidad < 20:
        menos_20 += 1 # Aumentamos en 1 el contador de funciones con pocos espectadores.

    # Vemos qué turno es y sumamos los espectadores a la cajita de ese turno.
    if turno_normalizado == "mañana":
        espectadores_turno_m += cantidad # Sumamos los espectadores de esta función al total de la mañana.
    elif turno_normalizado == "tarde":
        espectadores_turno_t += cantidad # Sumamos los espectadores de esta función al total de la tarde.
    elif turno_normalizado == "noche":
        espectadores_turno_n += cantidad # Sumamos los espectadores de esta función al total de la noche.
    else:
        # Si el usuario escribe un turno diferente, le avisamos.
        print("Advertencia: Turno ingresado no válido. Se ignorará para el cálculo por turno.")

    # Vemos qué sala es y aumentamos en 1 el contador de funciones de esa sala.
    if sala == 1:
        sala1_funciones += 1
    elif sala == 2:
        sala2_funciones += 1
    elif sala == 3:
        sala3_funciones += 1
    elif sala == 4:
        sala4_funciones += 1
    else:
        # Si el usuario escribe una sala diferente, le avisamos.
        print("Advertencia: Sala ingresada no válida. Se ignorará para el cálculo por sala.")

    # AHORA BUSCAMOS LA PELÍCULA CON MÁS ESPECTADORES EN UNA SOLA FUNCIÓN
    # Si la 'cantidad' de espectadores de esta función es MÁS grande que lo que tenemos guardado
    # como 'max_espectadores_funcion' (el récord actual)...
    if cantidad > max_espectadores_funcion:
        max_espectadores_funcion = cantidad # ¡Actualizamos el récord! Ahora este es el nuevo máximo.
        # Y también guardamos el nombre de la película que logró este récord.
        nombre_pelicula_max_asistencia = nombre_pelicula

# --- PARTE 4: ¡FIN DEL BUCLE! AHORA MOSTRAMOS TODOS LOS RESULTADOS ---
# El programa llega aquí solo cuando el usuario escribió "FIN" y se rompió el bucle.
# Aquí usamos los valores finales de todas nuestras cajitas.

print("\n--- Resumen del Día del Cine ---") # Título para los resultados.

# Mostramos el total de funciones.
print(f"Cantidad total de funciones registradas: {total_funciones}")
# Mostramos el total de espectadores.
print(f"Total de espectadores: {total_espectadores}")
# Mostramos funciones con espectadores entre 50 y 110.
print(f"Funciones con entre 50 y 110 espectadores: {entre50_y_110}")
# Mostramos funciones con espectadores exactos (100, 150, 200).
print(f"Funciones con exactamente 100, 150 o 200 espectadores: {entre_100_150_200}")

# Para saber si hubo funciones con menos de 20 espectadores,
# preguntamos si nuestra cajita 'menos_20' tiene un número mayor a cero.
if menos_20 > 0:
    print(f"Sí, hubo {menos_20} funciones con menos de 20 espectadores.")
else:
    print("No hubo funciones con menos de 20 espectadores.")


# --- VEMOS CUÁL FUE EL TURNO CON MÁS ESPECTADORES ACUMULADOS ---
# Necesitamos comparar las cajitas de espectadores por turno (espectadores_turno_m, _t, _n).
# Primero, asumimos que no hay ninguno (para el caso de que no se registre nada).
max_espectadores_acumulados_turno = 0
turno_con_mas_espectadores = ""

# Si los espectadores de la mañana son más que el récord actual...
if espectadores_turno_m > max_espectadores_acumulados_turno:
    max_espectadores_acumulados_turno = espectadores_turno_m # Actualizamos el récord de espectadores acumulados.
    turno_con_mas_espectadores = "Mañana" # Guardamos que el turno fue "Mañana".

# Si los espectadores de la tarde son más que el récord actual...
if espectadores_turno_t > max_espectadores_acumulados_turno:
    max_espectadores_acumulados_turno = espectadores_turno_t # Actualizamos el récord.
    turno_con_mas_espectadores = "Tarde" # Guardamos que el turno fue "Tarde".

# Si los espectadores de la noche son más que el récord actual...
if espectadores_turno_n > max_espectadores_acumulados_turno:
    max_espectadores_acumulados_turno = espectadores_turno_n # Actualizamos el récord.
    turno_con_mas_espectadores = "Noche" # Guardamos que el turno fue "Noche".

# Ahora, si encontramos un turno con más espectadores (es decir, la cajita no está vacía)...
if turno_con_mas_espectadores:
    print(f"\nEl turno con mayor cantidad de espectadores acumulados fue: {turno_con_mas_espectadores} ({max_espectadores_acumulados_turno} espectadores).")
else:
    print("\nNo se registraron funciones para determinar el turno con más espectadores acumulados.")


# --- CUÁNTAS FUNCIONES SE HICIERON EN CADA SALA ---
print("\n--- Cantidad de Funciones por Sala ---")
print(f"Funciones en Sala 1: {sala1_funciones}")
print(f"Funciones en Sala 2: {sala2_funciones}")
print(f"Funciones en Sala 3: {sala3_funciones}")
print(f"Funciones en Sala 4: {sala4_funciones}")


# --- LA PELÍCULA CON MÁS ESPECTADORES EN UNA SOLA FUNCIÓN (EL RÉCORD) ---
# Si la cajita con el nombre de la película récord no está vacía (significa que se registró al menos 1 función)...
if nombre_pelicula_max_asistencia:
    print(f"\nLa película con mayor asistencia en una sola función fue: '{nombre_pelicula_max_asistencia}' con {max_espectadores_funcion} espectadores.")
else:
    print("\nNo se registraron funciones para determinar la película con mayor asistencia en una sola función.")

print("\n¡Programa finalizado! Gracias por usar el sistema del cine.")
