from os import system       #Se importa la funcion os de la libreria system para usarla para el limpiado de pantalla

#Se crea una variable string (str) que contiene el menu mostrado al usuario
menu =  "Digite la opcion deseada\n"
menu += "1. Ingresar nuevo experimento\n"
menu += "2. Mostrar resultados\n"
menu += "3. Realizar analisis de datos\n"
menu += "4. Eliminar experimento\n"
menu += "5. Modificar experimento\n"
menu += "6. Generar informe de experimento\n"
menu += "7. Comparar experimentos\n"
menu += "8. Salir\n"
menu += "ej: si desea ingresar un nuevo experimento debe digitar 1"

# Se crea una funcion encargada de validar que un dato sea un numero, esta funcion tiene como parametros un limite inferior
# y un limite superior del digito que ingresa el usuario, un parametro de tipo str el cual se le muestra al usuario  
# para realizar la pregunta cuantas veces supere los limites inferior y superior
def ValidacionDeNumero(limite_inf,limite_sup,mensaje_pregunta:str ):
    #limpiado de pantalla
    system("cls") 
    
    # Se le muestra el mensaje pregunta y se le pide al usuario que ingrese la opcion deseada mediante un input
    numero = input(f"{mensaje_pregunta}\nIngrese la opcion deseada: ")
    
    # Si el numero ingresado resulta no ser un digito entero, la variable es_numero se le asigna un False para que el while
    # mas adelante se ejecute el while, caso contrario se le asigna un True y se convierte a variable tipo int
    if numero.isdigit() == False:
        es_numero = False
    else:
        numero = int(numero)
        es_numero = True
    
    # Este while mantiene preguntando al usuario el numero ingresado en caso de superar los limites y no ser un numero
    while es_numero == False or numero < limite_inf or numero > limite_sup:
        #limpiado de pantalla
        system("cls")   
        # Se le muestra el mensaje pregunta y el dato erroneo que ingreso y se le pide al usuario que ingrese 
        # la opcion deseada mediante un input
        numero = input(f"El numero ingresado no es correcto ha ingresado({numero})\nIntente nuevamente\n{mensaje_pregunta}\nIngrese la opcion deseada: ")
        
        #Luego se repite el proceso anterior al while de validacion
        if numero.isdigit() == False:
            es_numero = False
        else:
            numero = int(numero)
            es_numero = True
    # Aqui se retorna el numero ya validado cumpliendo los limites superior e inferior
    return int(numero)

# Se crea una funcion para agregar un experimento, esta funcion retorna un diccionario con todos los datos
def AgregarNuevoExperimento():
    # Se le pregunta al usuario un nombre para el experimento hasta que digite al menos una letra o caracter
    nombre = ""
    while len(nombre) == 0:
        system("cls")
        nombre = input("Ingrese el nombre del experimento: ")
    
    # Se le pide al usuario la fecha del experimento usando la funcion ValidacionDeNumero
    fecha = str(ValidacionDeNumero(1,31,"Ingrese el dia del experimento (numero 1-31): ")) + " / "
    fecha += str(ValidacionDeNumero(1,12,"Ingrese el mes del experimento (numero 1-12): ")) + " / "
    fecha += str(ValidacionDeNumero(1900,2025,"Ingrese el año del experimento (numero 1900-2025): "))
    
    # Se le pide al usuario el tipo del experimento usando la funcion ValidacionDeNumero
    tipo = ValidacionDeNumero(1,3,"Digite el tipo de experimento correspondiente\n1. Quimica\n2. Biologia\n3. Fisica")
    
    # Dependiendo del numero se le asigna un str con el tipo de experimento
    if tipo == 1:
        tipo = "Quimica"
    elif tipo == 2:
        tipo = "Biologia"
    elif tipo == 3:
        tipo = "Fisica"

    # Se crea una lista donde se guardaran los resultados del usuario
    resultados = [] 
    # Se hace una validacion de que el usuario ingrese correctamente los resultados del experimento con ayuda del try-except
    # Si al convertir el str a float falla, se ira al except y una variable llamada correcto hara que inicie el ciclo preguntando
    # de nuevo hasta que ingrese los datos correctos, si no falla se le asigna a la variable resultados los resultados del usuario   
    try: 
        resultados = list(map(float, input("Ingrese los resultados separados por coma: ").split(",")))
        correcto = True
    except ValueError:
        correcto = False
    
    # Se le pide al usuario los ressultados obtenidos hasta que este los ingrese correctamente
    while correcto == False:
        system("cls")
        print("Resultado ingresado incorrecto\nIngrese el resultado obtenido nuevamente\nRecuerde ingresar numeros: ")  
        try:
            resultados = list(map(float, input("Ingrese los resultados separados por coma: ").split(",")))
            correcto = True
        except ValueError:
            correcto = False
    
    # Se retorna un diccionario con el nombre, tipo, fecha y resultados que el usuario ingreso
    return {"nombre":nombre,"fecha":fecha,"tipo":tipo,"resultados":resultados}

# Se crea una funcion para mostrar al usuario un experimento aunque esta funcion retorna un indice correspondiente al experimento
# dentro de la lista ofrecida por el parametro: experimentos 
def MostrarResultadosExperimento(experimentos:list):
    #En caso de que la lista este vacia se le dira al usuario que no hay experimentos y se retorna cero 
    if not experimentos:
        print("Aun no hay experimentos registrados.")
        return 0
    
    # Creo una variable de tipo str donde guardo los nombres de los experimentos contenidos dentro de los diccionarios que estan
    # en experimentos, la llave de los diccionarios es nombre 
    pregunta = "\n0.Volver\n"
    
    for i,exp in enumerate(experimentos,1):
        pregunta += f"{i}. {exp["nombre"]}\n" 
    
    # Uso la funcion para validar que el usuario digite un dato correcto
    indice = ValidacionDeNumero(0,len(experimentos),f"{pregunta}\nDeacuerdo al experimento")

    # Retorno el indice que contiene la ubicacion del experimento
    return indice

# Se crea una funcion para realizar un analisis a los datos de uno de los experimentos
def RealizarAnalisisDeDatos(experimentos:list ):
    #Se obtiene el indice donde se encuentra el experimento al cual se le va a realizar el analisis
    indice = MostrarResultadosExperimento(experimentos) - 1
    if indice == -1:
        return
    # Con una variable datos almaceno los datos contenidos en el diccionario
    datos = experimentos[indice]["resultados"]

    # Con la variable datos calculo el promedio, el maximo y el minimo 
    print(f"Promedio: {sum(datos) / len(datos):.2f}")
    print(f"Máximo: {max(datos)}")
    print(f"Mínimo: {min(datos)}")

# Futura funcion para eliminar un experimento

def EliminarExperimento(experimentos:list):

# Se crea esta condicional para especificar si no tenemos experimentos se saldra a experimentos.
    if not experimentos:
        print("No hay experimentos registrados para eliminar.")
        input("Presione Enter para continuar...")
        return experimentos
    indice = MostrarResultadosExperimento(experimentos) - 1

    system("cls")

#Se crea esta variable para especificar que idice damos a elegir entre S o N adicional se agrego funciones 
#Strip para eliminar espacios y Lower para colocar cualquier letra ingresada en Minuscula
    confirmacion = input(f"¿Esta seguro que desea Eliminar el experimento '{experimentos[indice]['nombre']}'? (s/n): ").strip().lower()
# Si el usuario ingresa S se eliminaria la elegida en el indice    
    if confirmacion == 's':
        del experimentos[indice]
        print("Experimento eliminado correctamente. ")
# De lo contrario imprime un comentario que se cancelo
    else:
        print("Operacion Cancelada.")
    #espera que el usuario ingrese enter
    input("Presione Enter para continuar...")

    return experimentos

# Futura funcion para modificar un experimento, recibe un parametro de tipo lista con los experimentos
def ModificarExperimento(experimentos:list):
    # Obtengo el indice que el usuario quiere modificar 
    if not experimentos:
        print("Aun no hay experimentos registrados.")
        input("presione enter para continuar")
        return experimentos
    
    indice = MostrarResultadosExperimento(experimentos) - 1
    # Con el indice que me da la funcion voy a reemplazar en la lista experimentos ese experimento con ese indice con un nuevo
    # experimento 
    if indice == -1:
        return experimentos
    mini_menu = "\n0.Volver a menu principal" 
    mini_menu += "\n1.Modificar todo el experimento"
    mini_menu += "\n2.Modificar nombre"
    mini_menu += "\n3.Modificar fecha"
    mini_menu += "\n4.Modificar tipo"
    mini_menu += "\n5.Modificar resultados"
    opcion_mini_menu = ValidacionDeNumero(0,5,mini_menu)
    if opcion_mini_menu == 0:
        #retorna el mismo experimento para no reemplazar nada cuando vuelva el usuario
        return experimentos
    elif opcion_mini_menu == 1:
        # Crea un experimento nuevo y retorna el nuevo ecperimento
        experimentos[indice] = AgregarNuevoExperimento()
        return experimentos
    elif opcion_mini_menu == 2:
        # Se le pregunta al usuario un nombre para el experimento hasta que digite al menos una letra o caracter
        nombre = ""
        while len(nombre) == 0:
            system("cls")
            nombre = input("Ingrese el nombre del experimento: ")
        experimentos[indice]["nombre"] = nombre
        return experimentos
    elif opcion_mini_menu == 3:
           # Se le pide al usuario la fecha del experimento usando la funcion ValidacionDeNumero
        fecha = str(ValidacionDeNumero(1,31,"Ingrese el dia del experimento (numero 1-31): ")) + " / "
        fecha += str(ValidacionDeNumero(1,12,"Ingrese el mes del experimento (numero 1-12): ")) + " / "
        fecha += str(ValidacionDeNumero(1900,2025,"Ingrese el año del experimento (numero 1900-2025): "))
        experimentos[indice]["fecha"] = fecha
        return experimentos
    elif opcion_mini_menu == 4:
        # Se le pide al usuario el tipo del experimento usando la funcion ValidacionDeNumero
        tipo = ValidacionDeNumero(1,3,"Digite el tipo de experimento correspondiente\n1. Quimica\n2. Biologia\n3. Fisica")
        # Dependiendo del numero se le asigna un str con el tipo de experimento
        if tipo == 1:
            tipo = "Quimica"
        elif tipo == 2:
            tipo = "Biologia"
        elif tipo == 3:
            tipo = "Fisica"
        experimentos[indice]["tipo"] = tipo
        return experimentos
    elif opcion_mini_menu == 5:
        # Se crea una lista donde se guardaran los resultados del usuario
        resultados = [] 
        # Se hace una validacion de que el usuario ingrese correctamente los resultados del experimento con ayuda del try-except
        # Si al convertir el str a float falla, se ira al except y una variable llamada correcto hara que inicie el ciclo preguntando
        # de nuevo hasta que ingrese los datos correctos, si no falla se le asigna a la variable resultados los resultados del usuario   
        try: 
            resultados = list(map(float, input("Ingrese los resultados separados por coma: ").split(",")))
            correcto = True
        except ValueError:
            correcto = False
        # Se le pide al usuario los ressultados obtenidos hasta que este los ingrese correctamente
        while correcto == False:
            system("cls")
            print("Resultado ingresado incorrecto\nIngrese el resultado obtenido nuevamente\nRecuerde ingresar numeros: ")  
            try:
                resultados = list(map(float, input("Ingrese los resultados separados por coma: ").split(",")))
                correcto = True
            except ValueError:
                correcto = False
        experimentos[indice]["resultados"] = resultados
        return experimentos
    
# Futura funcion para generar el informe de un experimento
def GenerarInforme(experimentos:list):
    #Esta incompleto, solo crea un txt y escribe Primera linea.\nSegunda línea.\n línea.\n
    archi1=open("G:\Mi unidad\phyton\Curso con Dev senior code\Proyectos\datos.txt","w") 
    experimentos_cadena = ""

    archi1.write("Primer línea.\n") 
    archi1.write("Segunda línea.\n") 
    archi1.write(" línea.\n")  
    archi1.close() 
    print()

def comparar_resultados(experimentos: list):
    """
    Función para comparar los resultados de al menos dos experimentos y determinar cuál tiene el mejor y el peor promedio.

    Parámetros:
    - experimentos (list): Lista de diccionarios que contienen los experimentos registrados.

    Retorno:
    - None. Muestra los resultados de la comparación en la consola.
    """

    # Verifica si hay al menos dos experimentos para comparar
    if len(experimentos) < 2:
        print("Debe haber al menos dos experimentos registrados para comparar.")
        input("Presione Enter para continuar...")
        return

    print("\nSeleccione los experimentos que desea comparar (ingrese los números separados por coma):")

    # Muestra la lista de experimentos disponibles con sus índices
    for i, exp in enumerate(experimentos, 1):
        print(f"{i}. {exp['nombre']}")

    # Captura la selección de experimentos del usuario
    seleccion = input("\nIngrese los números de los experimentos a comparar: ")

    try:
        # Convierte la selección en una lista de índices válidos
        indices = [int(x) - 1 for x in seleccion.split(",") 
                   if x.strip().isdigit() and 0 < int(x) <= len(experimentos)]
    except ValueError:
        # Maneja errores en la entrada del usuario
        print("Entrada inválida. Asegúrese de ingresar números separados por coma.")
        input("Presione Enter para continuar...")
        return

    # Verifica si el usuario ha seleccionado al menos dos experimentos
    if len(indices) < 2:
        print("Debe seleccionar al menos dos experimentos.")
        input("Presione Enter para continuar...")
        return

    # Diccionario para almacenar los promedios de los experimentos seleccionados
    promedios = {}

    # Calcula el promedio de los resultados de cada experimento seleccionado
    for i in indices:
        datos = experimentos[i]["resultados"]
        promedio = sum(datos) / len(datos)
        promedios[experimentos[i]["nombre"]] = promedio

    # Identifica el experimento con el mejor y el peor promedio
    mejor_experimento = max(promedios, key=promedios.get)
    peor_experimento = min(promedios, key=promedios.get)

    # Muestra los resultados de la comparación
    print("\nResultados de la comparación:")
    for nombre, promedio in promedios.items():
        print(f"{nombre}: Promedio {promedio:.2f}")

    print(f"\n🔹 El mejor experimento es: {mejor_experimento} con un promedio de {promedios[mejor_experimento]:.2f}")
    print(f"🔻 El peor experimento es: {peor_experimento} con un promedio de {promedios[peor_experimento]:.2f}")

    input("\nPresione Enter para continuar...")

# Creo una variable donde guardo la opcion de menu del usuario, tambien un diccionario para guardar los diccionarios con la
# informacion de los experimentos 
opcion = 0
Experimentos = []

# While para preguntarle al usuario que desea realizar
while opcion != 8:

    # Uso la funcion de validacion para el numero ingresado de el menu
    opcion = ValidacionDeNumero(1,8,menu)

    # Limpio pantalla
    system("cls")

    # En caso de que el usuario digite la opcion 1, llamo a la funcion AgregarNuevoExperimento para que me retorne un diccionario
    # que contenga toda la informacion del experimento y agregarlo a la lista Experimentos 
    if opcion == 1:#AgregarNuevoExperimento
        Experimentos.append(AgregarNuevoExperimento())
    
    # En caso de que la opcion sea 2 se usara la funcion MostrarResultadosExperimento para obtener el indice y luego mostrar
    elif opcion == 2:       

        # Se guarda el indice del experimento que el usuario quiere ver
        indice = MostrarResultadosExperimento(Experimentos)
        if indice == -1:
            continue
        # Si el indice retorna 0, significa que la lista esta vacia y volvera al menu cuando el usuario presione enter
        # Si la lista contiene algun elemento no retornara cero si no el indice, el cual es usado para mostrar el experimento deseado 
        if indice != 0:
            print()
            # Con el for recorro todo el diccionario y luego muestro sus llaves y datos del diccionario
            for ex in Experimentos[indice-1]:
                print(f"{ex}: {Experimentos[indice-1][ex]}")
            input("\npresione enter para continuar")
        else:
            input("presione enter para continuar")

    # En caso de que la opcion sea 3 se usara la funcion RealizarAnalisisDeDatos para mostrar promedio, maximo y minimo
    elif opcion == 3:
        # Si la lista Experimentos esta vacia muestra No hay experimentos registrados. caso contrario hace el llamado a funcion 
        if not Experimentos:
            print("No hay experimentos registrados.")
        else:
            RealizarAnalisisDeDatos(Experimentos)
        
        # espera a que el usuario presione enter
        input("presione enter para continuar")

    elif opcion == 4:

        Experimentos = EliminarExperimento(Experimentos)
        #EliminarExperiento

    elif opcion == 5:
        Experimentos = ModificarExperimento(Experimentos)
        #ModificarExperimento
    
    elif opcion == 6:
        GenerarInforme(Experimentos)
        #GenerarInforme

    elif opcion == 7:
        comparar_resultados(Experimentos)
        #CompararExperimentos
    


print("Que tenga un buen dia ^^")

