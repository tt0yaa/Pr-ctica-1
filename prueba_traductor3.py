nombre = input("Escribe tu nombre: ")
print("**** selecciona una opción ****")
print(nombre + " presiona 1 para traductor de animales: español a inglés")
print(nombre + " presiona 2 para traductor de animales: español a alemán")
print(nombre + " presiona 3 para traductor de animales: español a francés")
print(nombre + " presiona 4 para traductor de animales: español a italiano")
print(nombre + " presiona 5 para traductor de animales: español a irlandés")
print("**********")
opción = int(input("Escribe la opción que deseas usar:"))

# Opción 1 español a inglés
if opción == 1: 
    print("Traductor español - inglés")
    
    opcion_uno = input("Escribe la palabra que deseas traducir : ")
    
    if opcion_uno == "gato":
        print("The word is CAT")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "gato":
            print("The word is CAT")

        elif opcion_uno == "perro":
            print("The word is DOG")
      
        elif opcion_uno == "perro":
            print("The word is DOG")
        elif opcion_uno == "lobo":
            print("The word is WOLF") 
        
        elif opcion_uno == "lobo":
            print("The word is WOLF")    

        elif opcion_uno == "delfín":
            print("The word is DOLPHIN")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "delfín":
            print("The word is DOLPHIN")

        if opcion_uno == "hurón":
            print("The word is FERRET")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "hurón":
            print("The word is FERRET")

        if opcion_uno == "tiburón":
            print("The word is SHARK")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "tiburón":
            print("The word is SHARK")

        if opcion_uno == "tigre":
            print("The word is TIGER")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "tigre":
            print("The word is TIGER")
        
        if opcion_uno == "zorro":
            print("The word is FOX")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "zorro":
            print("The word is FOX")

        if opcion_uno == "búho":
            print("The word is OWL")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "búho":
            print("The word is OWL")

        if opcion_uno == "serpiente":
            print("The word is SNAKE")
        opcion_uno = input("Escribe otra palabra que deseas traducir : ")
        if opcion_uno == "serpiente":
            print("The word is SNAKE")