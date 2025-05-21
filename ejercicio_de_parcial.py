contador_m = 0
contador_f = 0 
contador_o = 0                           #Contadores para guardar la informacion ingresada por los usuarios.
mujeres_mayores = 0 
menor_12 = 0
contador_persona = 1 
print("Bienvenido al centro de vacunacion contra la gripe.")
print("--------------------------")
genero = input ("Ingrese su género (M,F,O). Escriba X para finalizar: ") #Pedirle al usuario que ingrese su genero o que escriba X para finalizar.

while genero == "M" or genero == "F" or genero == "O":   #Mientras la respuesta sea F,M,O pedirle nombre y su edad .
    print("Ingreso de persona #", contador_persona) 
    edad = int (input("Ingrese su edad: "))

    if genero == "M":
        contador_m += 1       #Dependiendo el genero y su respuesta, se suma uno al contador.
    elif genero == "F":
        contador_f += 1 
    if edad > 60:                #Dentro del if mujer, sumarle un if de edad para que, si es mayor de 60 y femenino, se sume al contador de mujeres mayores.              
        mujeres_mayores += 1
    elif genero == "O":
        contador_o += 1
    
    if edad <12:             #Si la edad es menor a 12, sumarle al contador.
        menor_12 += 1
    contador_persona += 1   #Cuenta la cantidad ingresada de personas (cuestiones esteticas de separacion).
    print("----------")
    genero = input ("Bienvenido. Ingrese su género (M,F,O). Escriba X para finalizar: ")
    
if contador_m >= contador_f and contador_m >= contador_o:
    mayor_cantidad = "Masculino"
elif contador_f >= contador_m and contador_f >= contador_o:         #Si contador es mayor a los demas, imprimir la mayor cantidad del genero con mas vacunados.                   
    mayor_cantidad = "Femenino"
else:
    mayor_cantidad = "Otro"

print("--Informacion recopilada--")
print("Genero con mayor vacunacion: ", mayor_cantidad)
print("Cantidad de mujeres mayores a 60 vacunadas: ", mujeres_mayores)          #Imprimir los resultados.
print("Cantidad de menores vacunados: ", menor_12)
