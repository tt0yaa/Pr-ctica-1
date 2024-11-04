print("Sistema para calcular el promedio de horas de sueño")

# Cuestionario inicial para recopilar datos del usuario
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
edad = int(input("¿Cuántos años tienes, " + nombre + "?: "))
estatura = float(input("¿Cuál es tu estatura en metros?: "))
peso = float(input("¿Cuál es tu peso en kilogramos?: "))

# Mensaje para introducir al usuario a la entrada de datos
print("Ahora, vamos a registrar las horas de sueño de la semana.")
print("En caso de no haber tenido horas de siesta, coloca un 0.")

# Creamos variables para los días de la semana
lunes = int(input(nombre + ", ¿Cuántas horas dormiste el lunes?: ")) + int(input("¿Cuántas horas de siesta dormiste el lunes?: "))
martes = int(input( ",¿Cuántas horas dormiste el martes?: ")) + int(input("¿Cuántas horas de siesta dormiste el martes?: "))
miercoles = int(input( " ,¿Cuántas horas dormiste el miércoles?: "))+ int(input("¿Cuántas horas de siesta dormiste el miércoles?: "))
jueves = int(input( " ,¿Cuántas horas dormiste el jueves?: ")) + int(input("¿Cuántas horas de siesta dormiste el jueves?: "))
viernes = int(input("¿Cuántas horas dormiste el viernes?: ")) + int(input("¿Cuántas horas de siesta dormiste el viernes?: "))
sabado = int(input( " ,¿Cuántas horas dormiste el sábado?: ")) + int(input("¿Cuántas horas de siesta dormiste el sábado?: "))
domingo = int(input("¿Cuántas horas dormiste el domingo?: ")) + int(input("¿Cuántas horas de siesta dormiste el domingo?: "))


# Creamos variables para evaluar los promedios de las horas de sueño
promedio = (lunes + martes + miercoles + jueves + viernes + sabado + domingo) / 7

# Determinamos el rango de sueño adecuado según la edad
if edad <= 12:
    sueño_adecuado = 9  # Para niños de 10-12 años
elif 13 <= edad <= 17:
    sueño_adecuado = 8  # Para adolescentes de 13-17 años
elif 18 <= edad <= 64:
    sueño_adecuado = 7.5  # Para adultos jóvenes y adultos de 18-64 años
else:
    sueño_adecuado = 7  # Para adultos mayores de 65 años en adelante

# Evaluamos el promedio de horas de sueño según el rango adecuado
if promedio < sueño_adecuado - 1:
    print("\n¡Ohhh!, " + nombre + ", al parecer tienes muy pocas horas de sueño. Tu promedio es de:", promedio, "horas. Deberías intentar dormir más. El promedio adecuado para tu edad es de:", sueño_adecuado, "horas.")
elif promedio == sueño_adecuado - 1:
    print("\n¡Estás en el límite, " + nombre + "! Tu promedio es de:", promedio, "horas. Sería recomendable aumentar tus horas de sueño. El promedio adecuado para tu edad es de:", sueño_adecuado, "horas.")
elif promedio == sueño_adecuado:
    print("\nMuy bien, " + nombre + ", tu promedio es de:", promedio, "horas. Estás cumpliendo con las horas de sueño adecuadas para tu edad.")
else:
    print("\nExcelente, " + nombre + "! Tu promedio es de:", promedio, "horas.")

# Mensaje de agradecimiento
print("Gracias, " + nombre+ ". Ese fue tu resultado de sueño. ")

# Imprimimos un mensaje de fin
print("Fin")