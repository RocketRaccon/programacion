"""Gomez de Leon Jose Manuel"""
"""Capitulo 1, Ejercicio 16"""
"""7 de Marzo del 2019"""

numero =int(input("Ingrese el numero de la tabla de multiplicar: \n"))
print ("\n")
print ("Tabla de multiplicar\n")
rango=range(1,13)
for elemento in rango:
    producto=numero*elemento
    print (numero,'x',elemento,'=',producto)
    
    
