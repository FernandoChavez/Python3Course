import sys
if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    
    if filas<1 or filas>9 or columnas<1 or columnas>9:
        print("Error: Filas o/o columnas con formato incorrecto")
        print("Ejemplo: Tema2-ejercicio1.py [1-9] [1-9]")
    else:
        for r in range(filas):
            print("")
            for n in range(columnas):
                print(" * ", end='')
else:
    print("Error, introduce los argumentos correctamente")
    print("Ejemplo Tema2-ejercicio1.py 3 5")