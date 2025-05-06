print("Para saber si aprobo la materia de ingles: ")
nota_ingles1 = int (input ("Ingrese su primer nota: "))
nota_ingles2 = int (input ("Ingrese su segunda nota: "))
nota_ingles3 = int (input ("Ingrese su tercer nota: "))
nota_ingles4 = int (input ("Ingrese su cuarta nota nota: "))

promedio_ingles = (nota_ingles1 + nota_ingles2 + nota_ingles3 + nota_ingles4) / 4
print("Su promedio es ", promedio_ingles)

if promedio_ingles >=60: 
    print("Aprobaste")
else: 
    print("Reprobaste")
    
    
print("Para saber si aprobo la materia de programacion: ")
nota_progra1= int (input ("Ingrese su primer nota: "))
nota_progra2 = int (input ("Ingrese su segunda nota: "))
nota_progra3 = int (input ("Ingrese su tercer nota: "))
nota_progra4 = int (input ("Ingrese su cuarta nota: "))

promedio_progra = (nota_progra1 + nota_progra2 + nota_progra3 + nota_progra4) / 4
print("Su promedio es ", promedio_progra)




if promedio_progra >=60:
    print("Aprobaste")
else:
    print("Reprobaste")


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Clase del 24/04 - Programacion, teorico es esto. 
Estructuras de interaccion. 
1. Que es una interacion?
2. FOR 
3. WHILE
4. DO...WHILE 
5. Contadores
6. Acumuladores 


- Las sentencias de iteracion o ciclos son estructuras de control que repiten la ejecucion de un grupo de instrucciones. 
    - una sentencia de iteracion es una estructura de control codicional, ya que dentro de la misma se repite la ejecucion de una o mas instrucciones
    mientras que una condicion especifica se cumpla. 

- Muchas veces tenemos que repetir un numero definido o indefinido de veces un grupo de instrucciones por los que en estos casos utilizamos este tipo de sentencias. 


La iteracion basicamente, si la condicion se cumple, se realiza el conjunto  de instrucciones, basicamente HACE ALGO.
    Si no se cumple, X. (Sale, F.)

-FOR.
    La sentencia for es util para los casos en donde se conoce de antemano el numero de veces que una o mas sentencias han de repetirse.
                 for(contador; final; incremento)
            {
            codigo a repetir;
            }

EN FOR, LAS LISTAS INICIAN CON 0, EN WHILE, LA LISTA COMIENZA CON 1.
    i = indice. 
        i = 0 / i = 4
                i ++
1. Contador es una variable numerica
2. final es la condicion que se evalua para finalizar el ciclo (puede ser independiente del contador)
3. incremento es el valor que se suma o resta al contador
4. el for evalua la condicion de finalizacion y mientras esta se cumpla continuaran las repeticiones. 


(PILDORAS-INFORMATICAS VIDEITOS DE PYTHON/RECOMENDACION) 
PROGRAMACIOM I ES PROMOCIONAL.

-WHILE.
    La sentencia while es util en aquellos casos en donde no se conoce de antemano el numero de veces que una o mas sentencias se tienen que repetir. 
-DO... WHILE.
    La sentencia do es usada generalmente en cooperacion con while para garantizar que una o mas instruccionnes se ejecuten al menos una vez. 

SENTENCIAS BREAK - CONTINUE
    En la condicion switch, la sentencia break es utilizada con el proposito de forzar un salto dentro del bloque switch haciael final del mismo. La misma sentencia se puede usar
    un conjunto con las distintas operaciones de iteracion. Ademas existe una nueva sentencia que se puede incluir en los ciclos.....

        La sentencia break se usa para forzar un salto hacia el final de un ciclo controlado por for o por while.
            La construccion del cliclo while para el caso de la setnencia break es diferente, esto para garantizar que el  
            ciclo no vaya a caer en una iteracion infinita. 

- CONTINUE
    continue es una sentencia que, cuando se encuentra dentro de un bucle (for o while), hace que la iteración actual se interrumpa y el control pase directamente a la siguiente iteración.
    En otras palabras, continue salta el resto del código dentro del bucle en la iteración actual y vuelve al principio del bucle para la siguiente iteración. 




La ciudad esta dividida en 2 zonas de recoleccion de basura zona norte y zona sur de acuerdo al nombre y segun el tipo de ubicacion centrico o nocentrico.

        La zona norte esta conformada por los algunos barrios centricos cuyo nombre son:
            - Barrio Paykin    
            - Barrio Atlantico Sur
            - Villa Rio negro.
Y la zona sur por los algunos barrios no centricos>
    - Barrios mujeres argentinas
    - Barrio quebracho
    - Barrio Santa Ines.

Debemos hacer un programa que ingresando el nombre del barrio y la ubicacion, nos informe en que zona se encuentra y la cantidad de veces que accedio a las distintas zonas. El 
programa finalizara el ingreso de datos hasta que ingresen "FIN".

(PSEINT !!!!!) 

//Proceso Recoleccion
	Definir barrio, ubicacion Como Cadena 
	Definir zona_norte, zona_sur Como Entero 
	zona_norte <-- 0 
	zona_sur <-- 0 
	Escribir "Ingrese el nombre del barrio o escriba FIN: " 
	Leer barrio
Mientras barrio =! "0" Hacer
    Escriibir

	 Si ubicacion = norte Entonces
		si barrio = Barrio Paykin 
	 FinSi
	 
 FinMientras
 
 
FinProceso

Mi primer condicion del mientras es que el FIN no sea igual a 0. 

 

CLASE DE 30/04 PRACTICA PROFESIONALIZANTE 
CLASE DE 30/04 PRACTICA PROFESIONALIZANTE 
lo de abajo i mean

CONSIGNA: 

Un centro de donaciones de sangre necesita registrar a las personas que se presentan para donar en un dia. Para ello,
se ingresa la informacion de cada donante como ser nombre, edad
y tipo de sangre. El registro de donantes continua mientras el operador no ingrese el nombre "FIN".

Desarrolle un algoritmo que:
Cuente la cantidad de donantes registrados
Contar cuantas donaciones se hiciero para cada tipo de sangre
Para cada registro, solo se debe aceptar la donacion si el donante es mayor de 18 años. Si no cumple, se debe informar que no puede donar 

    
# Contadores
total_donantes = 0
tipo_sangre_A = 0
tipo_sangre_B = 0
tipo_sangre_AB = 0
tipo_sangre_O = 0

# Iniciar el ciclo while
nombre_donante = input("Ingrese el nombre del donante (o FIN para terminar): ")
while nombre_donante != "FIN":  # El ciclo continuará mientras el nombre no sea "FIN"
    
    edad = int(input("Ingrese la edad del donante: "))
    
    # Condición para verificar si el donante tiene 18 años o más
    if edad < 18:
        print("No puede donar. Debe ser mayor de 18 años.")
        nombre_donante = input("Ingrese el nombre del donante (o FIN para terminar): ")
        continue  # Si no cumple la edad, vuelve a pedir el nombre sin registrar al donante

    tipo_sangre = input("Ingrese el tipo de sangre (A, B, AB, O): ")
    
    # Condicional para contar las donaciones por tipo de sangre
    if tipo_sangre == "A":
        tipo_sangre_A += 1
    elif tipo_sangre == "B":
        tipo_sangre_B += 1
    elif tipo_sangre == "AB":
        tipo_sangre_AB += 1
    elif tipo_sangre == "O":
        tipo_sangre_O += 1
    else:
        print("Tipo de sangre no válido, donación no registrada.")
        nombre_donante = input("Ingrese el nombre del donante (o FIN para terminar): ")
        continue  # Si el tipo de sangre no es válido, vuelve a pedir el nombre y no registra la donación

    # Incrementa el contador de donantes válidos
    total_donantes += 1
    print("Donación registrada correctamente.")

    # Pedir el siguiente donante
    nombre_donante = input("Ingrese el nombre del donante (o FIN para terminar): ")

# Mostrar los resultados al final
print("\nResumen del día:")
print(f"Total de donantes: {total_donantes}")
print(f"Donaciones tipo A: {tipo_sangre_A}")
print(f"Donaciones tipo B: {tipo_sangre_B}")
print(f"Donaciones tipo AB: {tipo_sangre_AB}")
print(f"Donaciones tipo O: {tipo_sangre_O}")

(TODO LO DE ARRIBA ES CHAT GPT LMAO) 
////////////////////////////////////////////////////////////////////
# fin = (input("Para terminar ingrese FIN: "))

total_donantes = 0
tiposangre_a = 0
tiposangre_b = 0
tiposangre_ab = 0
tiposangre_o = 0
 
nombre_donante = (input("Ingrese su nombre o FIN para terminar: "))
# while nombre_donante != "FIN":
edad_donante = int (input("Ingrese su edad: "))
tiposangre_donante = (input ("Ingrese su tipo de sangre: "))
if edad_donante < 18:
    print("No puede donar por ser menor de edad")

if tiposangre_donante == "A":
    tiposangre_a += 1 
 elif tiposangre_donante = "B":
    tiposangre_b += 1 

(este es mi humilde codigo) 








////////////////////////////////////////////////////////////////7
total_donantes = 0 
ta_positivo = 0 
ta_negativo = 0 
tb_positivo = 0 
tb_negativo = 0
tab_positivo = 0 
tab_negativo = 0 
to_positivo = 0
to_negativo = 0 

nombre_donante = input("Ingrese su nombre o escriba FIN para terminar: ")

while nombre_donante != "FIN":
    edad = int(input("Ingrese su edad: "))
    
    if edad < 18:
        print("Usted no puede donar, debe ser mayor de 18 años.")
    else:
        tiposangre = (input("Ingrese su TIPO de sangre (A+- B+-, AB+-, O+-): "))
        total_donantes += 1

        if tiposangre == "A+":
            ta_positivo += 1
        elif tiposangre == "A-":
            ta_negativo += 1
        elif tiposangre == "B+":
            tb_positivo += 1
        elif tiposangre == "B-":
            tb_negativo += 1
        elif tiposangre == "AB+":
            tab_positivo += 1
        elif tiposangre == "AB-":
            tab_negativo += 1
        elif tiposangre == "O+":
            to_positivo += 1
        elif tiposangre == "O-":
            to_negativo += 1
        else:
            print("Tipo de sangre inválido.")

    nombre_donante = input("Ingrese su nombre o escriba FIN para terminar: ")

print("DONANTES REGISTRADOS:", total_donantes)
print("TIPO DE SANGRE A+: ", ta_positivo)
print("TIPO DE SANGRE A-: ", ta_negativo)
print("TIPO DE SANGRE B+: ", tb_positivo)
print("TIPO DE SANGRE B-: ", tb_negativo)
print("TIPO DE SANGRE AB+: ", tab_positivo)
print("TIPO DE SANGRE AB-: ", tab_negativo)
print("TIPO DE SANGRE O+: ", to_positivo)
print("TIPO DE SANGRE O-: ", to_negativo)
























    
