numero =int(input("Ingrese el numero de la tabla de multiplicar:"))

rango=range(1,11)
for elemento in rango:
    producto=numero*elemento
    print (numero,'x',elemento,'=',producto)
    print ("Tabla de multiplicar")
