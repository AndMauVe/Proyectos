from os import system

menu =  "Digite la opcion deseada\n"
menu += "1. Ingresar nuevo experimento\n"
menu += "2. Mostrar resultados\n"
menu += "3. Realizar analisis de datos\n"
menu += "4. Eliminar experimento\n"
menu += "5. Modificar experimento\n"
menu += "6. Generar informe de experimento\n"
menu += "7. Salir\n" 
menu += "ej: si desea ingresar un nuevo experimento debe digitar 1"

def ValidacionDeNumero():
    print()

def AgregarNuevoExperimento():
    print()

def MostrarResultadosExperimento():
    print()

def RealizarAnalisisDeDatos():
    print()

def EliminarExperimento():
    print()

def ModificarExperimento():
    print()

def GenerarInforme():
    print()

opcion = 0
Experimentos = []

while opcion != 7:
    opcion = ValidacionDeNumero(1,7,menu)
    system("cls")
    if opcion == 1:
        print()
        #AgregarNuevoExperimento
        
    elif opcion == 2:
        print()
        #MostrarResultadosExperimento

    elif opcion == 3:
        print()
        # RealizarAnalisisDeDatos

    elif opcion == 4:
        print()
        #EliminarExperimento
        
    elif opcion == 5:
        print()
        #ModificarExperimento
    
    elif opcion == 6:
        print()
        #GenerarInforme


print("Que tenga un buen dia ^^")