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

def ValidacionDeNumero(limite_inf,limite_sup,mensaje_pregunta):
    numero = input(f"{mensaje_pregunta}\nIngrese la opcion deseada: ")
    if numero.isdigit() == False:
        es_numero = False
    else:
        numero = int(numero)
        es_numero = True
    
    while es_numero == False or numero < limite_inf or numero > limite_sup:
        system("cls")
        numero = input(f"El numero ingresado no es correcto ha ingresado({numero})\nIntente nuevamente\n{mensaje_pregunta}\nIngrese la opcion deseada: ")
        if numero.isdigit() == False:
            es_numero = False
        else:
            numero = int(numero)
            es_numero = True
    
    return int(numero)

def AgregarNuevoExperimento():
    nombre = input("Ingrese el nombre del experimento: ")
    fecha = input("Ingrese la fecha del experimento: ")
    tipo = ValidacionDeNumero(1,3,"Digite el tipo de experimento correspondiente")
    
    num_resulados = ValidacionDeNumero(1,100,"Ingrese la cantidad de datos del experimento: ")
    resultados = []
    for i in range(num_resulados):
        resultado = input("\nIngrese el resultado obtenido: ")  

        while resultado.isdigit() == False:
            resultado = input("Resultado ingresado incorrecto\nIngrese el resultado obtenido nuevamente: ")  
        resultados.append(resultado)
    return {"nombre":nombre,"fecha":fecha,"tipo":tipo,"resultados":resultados}


def MostrarResultadosExperimento(experimentos:list):
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
    if opcion == 1:#AgregarNuevoExperimento
        Experimentos.append(AgregarNuevoExperimento())
                
    elif opcion == 2:   #MostrarResultadosExperimento        
        print()

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