print("Hola, este es un cajero")
print("Inserte su tarjeta")
#Variable nombre
nombre = input("¿Cuál es tu nombre?")
ahorro = int(input("¿Cuál es tu ahorro?"))
print("Muy bien " + nombre + "¿qué operación deseas realizar? tu saldo es de ", ahorro, "mxn" )
#Opciones
ejecutar = True
while ejecutar: 
    print(" **** selecciona una opción **** ")
    print(nombre + "selecciona 1 para consultar tu saldo")
    print(nombre  + "selecciona 2 para realizar un retiro")
    print(nombre + "selecciona 3 para realizar un pago")
    print(nombre + "selecciona 4 para solicitar préstamos")
    opcion = int(input("Escribe la opción que deseas utilizar"))
    #Opción 1 Consultar tu saldo
    if opcion == 1:
        print("Tu saldo es de", ahorro , " mxn ")
        opcion_uno = input("¿Deseas realizar otra operación?")
        if opcion_uno == "si":
           ejecutar = True
        elif opcion_uno == "no":
            print = input("Regresando al menú principal, espere unos segundos y oprima enter")
            print = input("Gracias, que tengas un excelente día")
            ejecutar = False
    #Opcion 2 Realizar un retiro
    if opcion == 2:
        print = int(input("¿Cuánto es el monto que deseas retirar? "))
        opcion_dos = input("¿Deseas realizar otra operación?")
        if opcion_dos == "si":
            ejecutar = True
        elif opcion_dos == "no":
            print = input("Regresando al menú principal, espere unos segundos y oprima enter")
            print = input("Gracias, que tengas un excelente día")
            ejecutar = False 
    #Opcion 3 Realizar un pago
    if opcion == 3:
        print = int(input("¿Cuánto es el monto que deseas pagar? "))
        donacion = input("Deseas realizar alguna donación?")
        if donacion == "si":
                int(input("Que cantidad deseas donar? "))
                print = input("Gracias por su donación")
        elif donacion == "no":
            opcion_dos = input("¿Deseas realizar otra operación?")
            if opcion_dos == "si":
                ejecutar = True
            elif opcion_dos == "no":
                print = input("Regresando al menú principal, espere unos segundos y oprima enter")
                print = input("Gracias, que tengas un excelente día")
                ejecutar = False    
    #Opcion 4 Para solicitar préstamos
    if opcion == 4:
        print = int(input("Ingresa la cantidad a solicitar "))
        opcion_dos = input("¿Deseas realizar otra operación?")
        if opcion_dos == "si":
            ejecutar = True
        elif opcion_dos == "no":
         print = input("Regresando al menú principal, espere unos segundos y oprima enter")
         print = input("Gracias, que tengas un excelente día")
        ejecutar = False