print("Sistema para calcular el promedio de un alumno")
# Creamos una variable para el nombre
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")
# Creamos variaables para las materias
matemáticas = int(input(nombre + "¿Cuál es tu calificación de matemáticas?: "))
química = int(input(nombre + "¿Cuál es tu calificación de química?: "))  
biología = int(input(nombre + "¿Cuál es tu calificación de biología?: "))
español = int(input(nombre + "¿Cuál es tu calificación de español?: "))
historia = int(input(nombre + "¿Cuál es tu calificación de historia?: "))
inglés = int(input(nombre + "¿Cuál es tu calificación de inglés?: "))
# Creamos variables para evaluar los promedios 
promedio = (matemáticas + química + biología + español + historia + inglés) / 6
# Creamos una condicional para comparar el promedio
if promedio >= 6: 
    print("Felicidades " + nombre + "aprobaste con un promedio de : ", promedio)
# Imprimimos un mensaje de fin
print("Fin")