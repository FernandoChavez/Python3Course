import sys
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 1:
        print("Error, debes introducir un numero positivo")
        print("Ejemplo Tema5-ejercicio1.py 34")
    else:
        cadena = str(numero)
        longitud = len(cadena)
        
        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud-1-i]) * 10 ** i))
        
    
elif len(sys.argv) ==1:
    print("Error, no introduciste ningun argumento")
    print("Ejemplo Tema5-ejercicio1.py [numero]")
