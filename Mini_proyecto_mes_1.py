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
    system("cls")
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
    nombre = ""
    while len(nombre) == 0:
        system("cls")
        nombre = input("Ingrese el nombre del experimento: ")
    
    fecha = ValidacionDeNumero(1,31,"Ingrese el dia del experimento (numero 1-31): ")
    fecha += ValidacionDeNumero(1,12,"Ingrese el mes del experimento (numero 1-12): ")
    fecha += ValidacionDeNumero(1900,2025,"Ingrese el año del experimento (numero 1900-2025): ")
    
    tipo = ValidacionDeNumero(1,3,"Digite el tipo de experimento correspondiente\n1. Quimica\n2. Biologia\n3. Fisica")
    if tipo == 1:
        tipo = "Quimica"
    elif tipo == 2:
        tipo = "Biologia"
    elif tipo == 3:
        tipo = "Fisica"

    #num_resulados = ValidacionDeNumero(1,100,"Ingrese la cantidad de datos del experimento: ")
    resultados = []
    #for i in range(num_resulados):
    #resultado = input("\nIngrese el resultado obtenido (numero): ")  
    try:
        resultados = list(map(float, input("Ingrese los resultados separados por coma: ").split(",")))
        correcto = True
    except ValueError:
        correcto = False
    while correcto == False:
        system("cls")
        print("Resultado ingresado incorrecto\nIngrese el resultado obtenido nuevamente\nRecuerde ingresar numeros: ")  
        try:
            resultados = list(map(float, input("Ingrese los resultados separados por coma: ").split(",")))
            correcto = True
        except ValueError:
            correcto = False
    
    return {"nombre":nombre,"fecha":fecha,"tipo":tipo,"resultados":resultados}


def MostrarResultadosExperimento(experimentos:list):
    if not experimentos:
        print("Aun no hay experimentos registrados.")
        return 0
    
    pregunta = ""
    for i,exp in enumerate(experimentos,1):
        pregunta += f"{i}. {exp["nombre"]}\n" 
    
    indice = ValidacionDeNumero(1,len(experimentos),f"{pregunta}\nDeacuerdo al experimento que desea ver")

    return indice

def RealizarAnalisisDeDatos(experimentos:list ):
    indice = MostrarResultadosExperimento(experimentos)
    indice -= 1

    datos = experimentos[indice]["resultados"]
    print(f"Promedio: {sum(datos) / len(datos):.2f}")
    print(f"Máximo: {max(datos)}")
    print(f"Mínimo: {min(datos)}")


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
        indice = MostrarResultadosExperimento(Experimentos)
        if indice != 0:
            for ex in Experimentos[indice-1]:
                print(f"{ex}: {Experimentos[indice-1][ex]}")
            input("presione enter para continuar")
        else:
            input("presione enter para continuar")

    elif opcion == 3:
        if not Experimentos:
            print("No hay experimentos registrados.")
        else:
            RealizarAnalisisDeDatos(Experimentos)
            
        input("presione enter para continuar")

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