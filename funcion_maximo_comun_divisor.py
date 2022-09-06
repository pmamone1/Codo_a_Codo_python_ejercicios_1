from os import system

def gcd():
    system("cls")
    print("*** Calculo del maximo comun divisor ***")
    print("")
    a = int(input("Ingrese un numero >>> "))
    b = int(input("Ingrese un numero distinto de 0 >>> "))
    
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    resultado = (f"El maximo comun divisor de {a} y {b} es = " + str(gcd)) 
    print("****************************************************")
    print(resultado)
    a = input("Pulse Enter para continuar")
    return menu()

def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def mcm():
    system("cls")
    print("*** Calculo del minimo comun multiplo ***")
    print("")
    a = int(input("Ingrese un numero >>> "))
    b = int(input("Ingrese un numero >>> "))
    resultado = (a * b) / mcd(a,b)
    cadena = (f"El minimo comun multiplo entre {a} y {b} es = " + str(resultado)) 
    print("****************************************************")
    print(cadena)
    a = input("Pulse Enter para continuar")
    return menu()

def cadena():
    system("cls")
    print("*** Ingrese una cadena y le devolvere un diccionario de palabras y su frecuencia ***")
    print("")
    frase = input("Ingrese una frase >>>")
    frase = frase.lower()
    palabras = frase.split(" ")
    diccionario ={}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    for palabra in diccionario:
        frecuencia = diccionario[palabra]
        print(f"La palabra << {palabra} >> se repite {frecuencia} veces.")
    print("****************************************************")
    a = input("Pulse Enter para continuar")
    return menu()

def menu():
    system("cls")
    print("****************************************************")
    print("***********   Menu Principal   *********************")
    print("****************************************************")
    print("")
    print("( 1 ) Calculo del Maximo Comun Divisor")
    print("( 2 ) Calculo del Minimo Comun Multiplo")
    print("( 3 ) Ingrese una cadena y le devolvere un diccionario de palabras y su frecuencia")
    print("( Q ) Salir")


    
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("Introduce una opcion >>> ")
 
	if opcionMenu=="1":
		print ("")
		gcd()
        
	elif opcionMenu=="2":
		print ("")
		mcm()
  
	elif opcionMenu=="3":
		print ("")
		cadena()
  
	elif opcionMenu=="Q" or opcionMenu=="q":
            print("Gracias por utilizar el programa!!!")
            print("Hasta la proxima!")
            exit()
    
    