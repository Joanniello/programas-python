import json
import time

def data_clients(operaciones):
    with open("clients.json") as clients:
        client = json.load(clients)
        return client
    
def new_or_old_client(operaciones): #Esta funcion sirve para saber si es nuevo o viejo cliente
    global n_o_client
    operaciones = +1
    n_o_client = input("Bienvenido al banco, ¿es cliente frecuente?(si/no): ").lower()
    if n_o_client != "si" and n_o_client != "no": #Si no responde 'si' o 'no' le repetimos la pregunta
        print("\nOpcion incorrecta")
        new_or_old_client(operaciones)
    else: #En caso de responder 'si' o 'no' llamamos a la funcion que verifica el camino a seguir de acuerdo a la respuesta
        verificate_n_o_client(operaciones)

def verificate_n_o_client(operaciones): # Funcion que nos ayuda el camino a seguir de acuerdo a si es nuevo o viejo cliente
    global new_client
    if n_o_client == "no": #Si NO es cliente frecuente, llamamos a la funcion para almacenar los datos del nuevo cliente
        new_client = data_new_client(operaciones)
        save_data_new_client(operaciones)
        more_operation(operaciones)
    elif n_o_client == "si": #Si es cliente frecuente, llamamos a la funcion donde vamos a tomar sus datos
        data_old_client(operaciones)
        
def data_new_client(operaciones): #Para guardar los datos en caso de ser un nuevo cliente
    print("\nComo no es usuario de nuestro banco, vamos a proceder a crear una cuenta")
    time.sleep(2)    
    balance = 0 #Balance inicial de 0
    name = input("¿Cual es su nombre?: ").lower()
    while True: #Aseguramos de que la edad sea un numero entero mayor a 0 y menor a 120.
        age = input("Ingrese su edad: ")
        if not age.isdigit():
            print("Ingrese una edad correcta")
        elif int(age) < 1 or 120 < int(age):
            print("Ingrese una edad correcta")
        else:
            break
    while True: #Para segurarnos que la contraseña que guarde el usuario cumpla los parametros de 4 enteros
        password = input("Ingrese su contraseña, debe tener 4 numeros enteros: ")
        if password.isdigit() and len(password) == 4:
            break
        else:
            print("\nIngrese una contraseña correcta:")
    while True:
        balance = input("¿Cuanto dinero va a depositar? (No se acepta decimales): ")
        if balance.isdigit() and 0 < int(balance):
            break   
        else:
            print("\nNo es posible realizar el deposito, ingrese un monto correcto")
    data = {"name" : name, "age": int(age), "password": password, "balance": int(balance)}
    return data


def save_data_new_client(operaciones): #Funcion para guardar los datos de los nuevos clientes
    old_date = data_clients(operaciones)
    old_date["clients"].append(new_client)
    with open("clients.json","w") as clients:
        json.dump(old_date,clients, indent = 4)

def more_operation(operaciones): #mas operaciones, solo para nuevos usuarios despues de registrarse
    while True:
        continue_operation = input("\nDesea seguir realizando mas operaciones?(si/no): ").lower()
        if continue_operation == "si":
            new_or_old_client(operaciones)
            break
        elif continue_operation == "no":
            print("\nGracias por registrarse en nuestro banco, hasta luego")
            exit()
        else:
            print("\nseleccione entre 'si' o 'no'")


def data_old_client(operaciones): # Funcion para tomar los datos del cliente frecuente
    global oc_name, oc_password
    oc_name = input("\nIngrese su nombre: ").lower()
    while True:
        oc_password = input("Ingrese su Contraseña(4 digitos): ")
        if oc_password.isdigit() and len(oc_password) == 4: #La contraseña debe ser 4 digitos
            break
        else:
            print("\nIngrese una contraseña correcta:")
    verificate_old_client(operaciones) #Llamamos a la funcion encontrar los datos del usuario
    

def verificate_old_client(operaciones): #Funcion para encontrar los datos del usuario en la data de usuarios frecuentes
    global actual_client, old_client
    old_client = data_clients(operaciones)
    for x in old_client["clients"]:
        if x["name"] == oc_name and x["password"] == oc_password:
            actual_client = x
            break
    if not actual_client in old_client["clients"]:
        print("\nUsuario o Clave incorrecta")
        new_or_old_client(operaciones)
    else:
        options_client(operaciones)

def end_day(operaciones):
    actualice_clients_data(operaciones+1)
    end = input("\n¿Se acabo el dia?(si/no): ").lower()
    if end == "si":
        print(json.dumps(client_results_final, indent = 4))
        time.sleep(2)
        exit()
    elif end == "no":
        new_or_old_client(operaciones+1)
    else:
        print("\nOpcion incorrecta, escriba 'si' o 'no'")
        end_day()
    

def options_client(operaciones):
    global options
    print(f"\nBienvenido {oc_name}, cual de las siguientes operaciones deseas realizar(1,2,3,4):")
    print("1. Ingresar dinero en la cuenta.")
    print("2. Retirar dinero de la cuenta.")
    print("3. Mostrar dinero disponible.")
    print("4. Salir.")
    options = input("\nopción seleccionada: ")
    time.sleep(2)
    verificate_options(operaciones)
    
def verificate_options(operaciones):
    global result_withdraw, result_deposit
    if not options.isdigit():
        print("Opcion no valida, intente nuevamente")
        options_client()
    elif int(options) == 1:
        while True:
            deposit = input(f"{oc_name} Ingresa la cantidad a depositar sin decimales: ")
            if deposit.isdigit() and int(deposit) > 0:
                actual_client["balance"] += int(deposit)
                result_deposit = int(deposit)
                break
            else:
                print("El monto ingresado no es valido, intente nuevamente")
                time.sleep(2)
        end_day(operaciones)
    elif int(options) == 2:
        if actual_client["age"] < 18:
            print(f"{oc_name} No tienes permitido retirar dinero de la cuenta por ser menor a 18 años, intenta otra opcion.!")
            end_day(operaciones)
        else:
            while True:
                withdraw = input("Ingresa la cantidad a retirar sin decimales: ")
                if withdraw.isdigit() and int(withdraw) > 0 and actual_client["balance"] >= int(withdraw):
                    actual_client["balance"] -= int(withdraw)
                    result_withdraw = int(withdraw)
                    break
                else:
                    print("El monto ingresado no es valido, intente nuevamente")
                    time.sleep(2)
            end_day(operaciones)
    elif int(options) == 3:
        print(f"Tiene: {actual_client['balance']}")
        time.sleep(2)
        options_client(operaciones)
    elif int(options) == 4:
        print("Hasta Luego, sus movimientos totales fueron:")
        actualice_clients_data(operaciones)
        time.sleep(2)
        exit()
    else:
        print("La opcion seleccionada no es valida, intente nuevamente")
        options_client(operaciones)
            
def actualice_clients_data(operaciones):
    global client_results_final
    with open("clients.json", "w") as client:
        json.dump(old_client, client, indent = 4)
    client_results ={"name": oc_name, "withdraw": result_withdraw, "deposit": result_deposit, "date": date}
    client_results_final.append(client_results)
    with open("clients_result.json") as client:
        data_clients_result = json.load(client)
    data_clients_result["clients"].append(client_results)
    with open("clients_result.json", "w") as client:
        json.dump(data_clients_result, client, indent = 4)

operaciones = 0
date = time.asctime(time.gmtime())
result_withdraw = 0
result_deposit = 0
options = ""
n_o_client = ""
new_client = ""
oc_name = ""
oc_password = ""
old_client = ""
actual_client = {}
client_results_final = []
new_or_old_client(operaciones)




    

            
            
            
    

        
