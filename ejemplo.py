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