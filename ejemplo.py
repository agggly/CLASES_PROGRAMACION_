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

















































    
