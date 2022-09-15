#Elaborado por José Nieves
#carnet: 12-11017
from random import shuffle, random
from time import time, sleep, asctime, gmtime
import json

tiempo_inicial = time()

def registro_jugador(nivel):
    '''Obtenemos los datos del usuario para guardarlo en
    caso de ser necesario en la base de datos'''
    registro = {"Posicion":0, "Nombre":nombre,"Tiempo de juego(seg)":tiempo_de_juego,
                "Dinero Obtenido":total[nivel],"Fecha(UTC)":fecha}
    return(registro)

with open("preguntas.json", encoding = 'utf8') as json_file:    
    preguntas = json.load(json_file)       
    shuffle(preguntas)
    
def preguntas_aleatorias(n, t):
    '''Seleccionamos una pregunta aleatoria del banco de preguntas'''
    return elegir_pregunta[n][t]
    
def menu_inicial():
    while True:
        print(f"\n{nombre} elije una opcion:Escribe(jugar, ranking, salir)")
        print("\na.) Jugar")
        print("\nb.) Ranking")
        print("\nc.) Salir")
        seleccion = input("\nTu eleccion es: ").lower()
        if not seleccion in menu:
            print(f"{nombre} esta opcion no es valida.! Escribe(jugar, ranking o salir")
        elif seleccion == "ranking":
            print(f"{json.dumps(mostrar_ranking(), indent = 4)}")
            sleep(3)
        elif seleccion == "salir":
            sleep(3)
            exit()
        else:
            inicia_el_juego()
            break
        
def inicia_el_juego():
    print(f"\nEmpecemos el juego, {nombre}! tienes un total de 8 preguntas\n\
Cada pregunta tendrá 4 opciones y solo 1 es correcta. Si respondes\n\
correctamente las 8 preguntas ganaras 80Bs!!!. Tienes 3 comodines y solo puedes usarlos una vez\n\
        \t{ayuda_50}\n\
        \t{ayuda_amigo}\n\
        \t{ayuda_audiencia}\n\
Puedes escribir 'ayuda' para ver que comodines tienes disponibles y para retirarte escribe\n\
la palabra 'retirarme', sin mas nada que agregar EMPECEMOS!!!!\n")
    sleep(2)
    print(seleccionar_pregunta(0))
    registro_jugador(0)
    verificar_respuesta(0);

def mostrar_ranking():
    global registro_previo
    '''Función donde cargamos los datos de los mejores 5 puntajes'''
    with open("Registro_jugadores.json", encoding = 'utf8') as registro:
        registro_previo = json.load(registro)
        return registro_previo

def nuevo_registro(nivel):
    global registro_previo
    '''Vamos a comparar el resultado obtenido por el jugador
    con los mejores puntajes
    y lo colocamos en su posicion correspondiente'''
    registro_nuevo = registro_jugador(nivel)
    registro_antiguo = mostrar_ranking()
    posicion_1 = registro_antiguo[0]
    posicion_2 = registro_antiguo[1]
    posicion_3 = registro_antiguo[2]
    posicion_4 = registro_antiguo[3]
    posicion_5 = registro_antiguo[4]
    if (int(registro_nuevo["Dinero Obtenido"]) > int(posicion_1["Dinero Obtenido"])):
        registro_nuevo["Posicion"] = int(registro_nuevo["Posicion"])
        registro_nuevo["Posicion"] = 1
        posicion_1["Posicion"] = 2
        posicion_2["Posicion"] = 3
        posicion_3["Posicion"] = 4
        posicion_4["Posicion"] = 5
        registro_antiguo.clear()
        cambiar_registro = [registro_nuevo, posicion_1, posicion_2, posicion_3, posicion_4]
        for x in cambiar_registro:
            registro_antiguo.append(x)
    elif registro_nuevo["Dinero Obtenido"] > posicion_2["Dinero Obtenido"]:
        registro_nuevo["Posicion"] = int(registro_nuevo["Posicion"])
        registro_nuevo["Posicion"] = 2
        posicion_2["Posicion"] = 3
        posicion_3["Posicion"] = 4
        posicion_4["Posicion"] = 5
        registro_antiguo.clear()
        cambiar_registro = [posicion_1,registro_nuevo, posicion_2, posicion_3, posicion_4]
        for x in cambiar_registro:
            registro_antiguo.append(x)
    elif registro_nuevo["Dinero Obtenido"] > posicion_3["Dinero Obtenido"]:
        registro_nuevo["Posicion"] = int(registro_nuevo["Posicion"])
        registro_nuevo["Posicion"] = 3
        posicion_3["Posicion"] = 4
        posicion_4["Posicion"] = 5
        registro_antiguo.clear()
        cambiar_registro = [posicion_1, posicion_2,registro_nuevo, posicion_3, posicion_4]
        for x in cambiar_registro:
            registro_antiguo.append(x)
    elif registro_nuevo["Dinero Obtenido"] > posicion_4["Dinero Obtenido"]:
        registro_nuevo["Posicion"] = int(registro_nuevo["Posicion"])
        registro_nuevo["Posicion"] = 4
        posicion_4["Posicion"] = 5
        registro_antiguo.clear()
        cambiar_registro = [posicion_1, posicion_2, posicion_3, registro_nuevo,  posicion_4]
        for x in cambiar_registro:
            registro_antiguo.append(x)
    elif registro_nuevo["Dinero Obtenido"] > posicion_5["Dinero Obtenido"]:
        registro_nuevo["Posicion"] = int(registro_nuevo["Posicion"])
        registro_nuevo["Posicion"] = 5
        registro_antiguo.pop()
        registro_antiguo.append(registro_nuevo)
    else:
        pass
    with open("Registro_jugadores.json", "w") as reescribir_registro:
        json.dump(registro_antiguo, reescribir_registro, indent = 4)
    return(registro_nuevo)


def introduccion_pregunta(nivel):
    '''Generando introduccion a las preguntas'''
    nivel += 1
    dinero = total[nivel]
    intro = [0 for i in range(6)]
    intro[0] =f"{nombre} esta es la pregunta #{nivel} por un valor de Bs{dinero}."
    intro[1] =f"{nombre} vamos por la pregunta #{nivel} para que ganes Bs{dinero}."
    intro[2] =f"{nombre}, pregunta #{nivel} por Bs{dinero}."
    intro[3] =f"{nombre} ¿quieres ganar Bs{dinero}? vamos a ver si puedes responder la pregunta #{nivel}."
    intro[4] =f"{nombre} veamos cuánto tiempo te tomará responder la pregunta #{nivel} y ganar Bs{dinero}."
    intro[5] =f"{nombre} para ganar Bs{dinero}, debes responder la pregunta #{nivel}."
    numero = int(random() * 6)
    return intro[numero]

def seleccionar_pregunta(nivel):
    global pregunta
    ''' Seleccionar la pregunta de la funcion preguntas_aleatorias'''
    mostrar = f"\n {introduccion_pregunta(nivel)} \n"
    mostrar += f"{'-'*(len(mostrar))} \n"
    numero_pregunta = 0
    pregunta = preguntas_aleatorias(nivel, numero_pregunta)
    mostrar += pregunta["Pregunta"]
    mostrar += f"\n A.   {pregunta['1']}  \t\t B.   {pregunta['2']}".expandtabs()
    mostrar += f"\n C.   {pregunta['3']}  \t\t D.   {pregunta['4']}".expandtabs() 
    global respuesta_correcta, a, b, c, d
    respuesta_correcta = pregunta['5']
    a = pregunta['1']
    b = pregunta['2']
    c = pregunta['3']
    d = pregunta['4']
    return mostrar

def verificar_respuesta(nivel):
    '''Verificar Respuesta del usuario'''
    while True:
        respuesta = input("\nTu respuesta es: ").lower()
        if not (respuesta in respuestas_permitidas):
            print(f"\n{nombre} esa opcion no es valida, para ver las opciones disponibles escribe 'ayuda' o 'retirarme' si quieres retirarte del juego.")
        else:
            break
    if (respuesta == "ayuda"):
        ayuda(nivel)   
    elif (respuesta == "amigo"):
        comodin_amigo(nivel)
    elif (respuesta == "50"):
        comodin_50(nivel)     
    elif (respuesta == "audiencia"):
        audiencia(nivel)        
    elif (respuesta == "retirarme"):
        retirada(nivel)    
    elif(respuesta == "a"):
        opcion_a(nivel)      
    elif(respuesta == "b"):
        opcion_b(nivel)
    elif(respuesta == "c"):
        opcion_c(nivel)      
    elif(respuesta == "d"):
        opcion_d(nivel)

def ayuda(nivel):
    global comodin_amigo_disponible, comodin_50_disponible, comodin_audiencia_disponible
    if (comodin_50_disponible): print(f"{' '*5} {ayuda_50}")
    if (comodin_amigo_disponible): print(f"{' '*5} {ayuda_amigo}")
    if (comodin_audiencia_disponible): print(f"{' '*5} {ayuda_audiencia}")
    if not (comodin_50_disponible or comodin_amigo_disponible or comodin_audiencia_disponible):
        print(f"\n {' '*5}{nombre} No tienes comodines disponibles, si quieres retirarte escribe: 'retirarme'")
    verificar_respuesta(nivel)

def comodin_amigo(nivel):
    global respuesta_correcta, pregunta, comodin_amigo_disponible, comodin_50_disponible
    global a, b, c, d, tiempo_final, tiempo_de_juego
    if (comodin_amigo_disponible == True):
        comodin_amigo_disponible = False
        if (random() >= 0.40):
            print("\nHas usado el comodin Llamar a un Amigo, tu amigo tiene un 60% de posibilidad de acertar")
            sleep(1)
            print(f"\n{nombre} estamos llamando a tu amigo")
            sleep(3)
            print(f"\n{nombre} tu amigo cree que la opcion correcta es {respuesta_correcta}")
            verificar_respuesta(nivel)
        else: #En caso de que dos respuestas fueron eliminadas por el comodin 50-50
            while True:
                indice = int(random()*4 +1)
                indice = str(indice)
                if (pregunta[indice] != ""):
                    print("\nHas usado el comodin Llamar a un Amigo")
                    sleep(1)
                    print(f"\n{nombre} estamos llamando a tu amigo")
                    sleep(3)
                    print(f"\n{nombre} tu amigo cree que la opcion correcta es {pregunta[indice]}")
                    verificar_respuesta(nivel)
    else:
        print(f"\n{nombre} Ya usaste este comodin. Escribe 'ayuda' para conocer que otros comodines tienes disponible")
        verificar_respuesta(nivel)

def comodin_50(nivel):
    global respuesta_correcta, pregunta, comodin_50_disponible
    global a, b, c, d, tiempo_final, tiempo_de_juego
    if (comodin_50_disponible == True):
        comodin_50_disponible = False
        print("\nHas usado el comodin: 50-50")
        sleep(1)
        print(f"\n{nombre} Estamos Eliminando 2 respuestas incorrectas")
        sleep(5)
        eliminadas = 0 #Para saber cuantas se han eliminados
        while True:
            if eliminadas == 2:
                break
            indice = int(random()*4 +1)
            indice = str(indice)
            if (respuesta_correcta != pregunta[indice] and pregunta[indice] != ""):
                eliminadas += 1
                pregunta[indice] = ""
        print(f"\n{nombre} Hemos eliminado dos respuestas incorrectas, las dos opciones sobrantes son: ")
        letras = [" A. ", " B. ", " C. ", " D. "]
        for indice in range(1,5):
            indice_string = str(indice)
            if (pregunta[indice_string] != ""):
                print (f'\n{letras[indice-1]} {pregunta[indice_string]}', end = "\t\t"),
        verificar_respuesta(nivel)
    else:
        print(f"\n{nombre} Ya usaste este comodin. Escribe 'ayuda' para conocer que otros comodines tienes disponible")
        verificar_respuesta(nivel)
        
def audiencia(nivel):
    global respuesta_correcta, pregunta, comodin_50_disponible, comodin_audiencia_disponible
    global a, b, c, d, tiempo_final, tiempo_de_juego
    if (comodin_audiencia_disponible == True):
        comodin_audiencia_disponible = False
        if comodin_50_disponible == True:
            comodin_audiencia(nivel)
        else:
            while True:
                uso_50 = input(f"{nombre}, ¿usaste el comodin 50-50 en esta pregunta?(si/no): ").lower()
                if uso_50 == "no":
                    comodin_audiencia(nivel)
                    break
                elif uso_50 == "si":
                    comodin_audiencia_con_50(nivel)
                    break
                else:
                    print("Esa opcion no es valida, diga 'si' o 'no'")
    else:
        print(f"\n{nombre} ya usaste este comodin. Escribe 'ayuda' para conocer que otros comodines tienes disponible")
        verificar_respuesta(nivel)

def comodin_audiencia(nivel):
    global respuesta_correcta, pregunta, ayuda_amigo_disponible, ayuda_50_disponible, ayuda_audiencia_disponible
    global a, b, c, d, tiempo_final, tiempo_de_juego
    while True: #Aseguramos que una pregunta tenga mas de un 25% de votos
        aleatorio_1 = random()
        aleatorio_2 = random()
        aleatorio_3 = random()
        aleatorio_4 = random()
        if (aleatorio_1 + aleatorio_2 + aleatorio_3 + aleatorio_4) <= 1.00:
            aleatorio_1 = int(aleatorio_1*100)
            aleatorio_2 = int(aleatorio_2*100)
            aleatorio_3 = int(aleatorio_3*100)
            aleatorio_4 = int(aleatorio_4*100)
            break
    if (aleatorio_1 > 50): #Si mas del 50% de la audiencia vota por una respuesta, es la correcta.
        respuesta_audiencia_1 = respuesta_correcta
    else: # Si mas del 50% no esta de acuerdo, elegimos una respuesta al azar
        while True: #En caso de que se haya usado el comodin 50-50
            indice = int(random()*4 +1)
            indice = str(indice)
            if(pregunta[indice] != respuesta_correcta):
                respuesta_audiencia_1 = pregunta[indice]
                break
    if (aleatorio_2 > 50): #Si mas del 50% de la audiencia vota por una respuesta, es la correcta.
        respuesta_audiencia_2 = respuesta_correcta
    else: # Si mas del 50% no esta de acuerdo, elegimos una respuesta al azar
        while True: #En caso de que se haya usado el comodin 50-50
            indice = int(random()*4 +1)
            indice = str(indice)
            if(pregunta[indice] != respuesta_audiencia_1):
                respuesta_audiencia_2 = pregunta[indice]
                break
    if (aleatorio_3 > 50): #Si mas del 50% de la audiencia vota por una respuesta, es la correcta.
        respuesta_audiencia_3 = respuesta_correcta
    else: # Si mas del 50% no esta de acuerdo, elegimos una respuesta al azar
        while True: #En caso de que se haya usado el comodin 50-50
            indice = int(random()*4 +1)
            indice = str(indice)
            if(pregunta[indice] != respuesta_audiencia_1 and pregunta[indice] != respuesta_audiencia_2):
                respuesta_audiencia_3 = pregunta[indice]
                break
    if (aleatorio_4 > 50): #Si mas del 50% de la audiencia vota por una respuesta, es la correcta.
        respuesta_audiencia_4 = respuesta_correcta
    else: # Si mas del 50% no esta de acuerdo, elegimos una respuesta al azar
        while True: #En caso de que se haya usado el comodin 50-50
            indice = int(random()*4 +1)
            indice = str(indice)
            if(pregunta[indice] != respuesta_audiencia_1 and pregunta[indice] != respuesta_audiencia_2
               and pregunta[indice] != respuesta_audiencia_3):
                respuesta_audiencia_4 = pregunta[indice]
                break
    print("\nHas usado el comodin: Consultar a la Audiencia")
    sleep(1)
    print(f"\n{nombre} La audiencia esta votando")
    sleep(3)
    print(f"\n{nombre} La audiencia ha votado: ")
    print(f"Un {aleatorio_1}% vota: {respuesta_audiencia_1}")
    print(f"Un {aleatorio_2}% vota: {respuesta_audiencia_2}")
    print(f"Un {aleatorio_3}% vota: {respuesta_audiencia_3}")
    print(f"Un {aleatorio_4}% vota: {respuesta_audiencia_4}")
    verificar_respuesta(nivel)

def comodin_audiencia_con_50(nivel):
    global respuesta_correcta, pregunta, comodin_50_disponible, comodin_audiencia_disponible
    global a, b, c, d, tiempo_final, tiempo_de_juego
    while True: #Aseguramos que una pregunta tenga mas de un 25% de votos
        aleatorio_1 = random()
        aleatorio_2 = random()
        if (aleatorio_1 + aleatorio_2) <= 1.00 and 0.50<=(aleatorio_1 + aleatorio_2):
            aleatorio_1 = int(aleatorio_1*100)
            aleatorio_2 = int(aleatorio_2*100)
            break
    if (aleatorio_1 > 50): #Si mas del 50% de la audiencia vota por una respuesta, es la correcta.
        respuesta_audiencia_1 = respuesta_correcta
    else: 
        while True:
            indice = int(random()*4 + 1)
            indice = str(indice)
            if(pregunta[indice] != "" and pregunta[indice] != respuesta_correcta):
                respuesta_audiencia_1 = pregunta[indice]
                pregunta[indice] = ""
                break
    if (aleatorio_2 > 50): #Si mas del 50% de la audiencia vota por una respuesta, es la correcta.
        respuesta_audiencia_2 = respuesta_correcta
    else: # Si mas del 50% no esta de acuerdo, elegimos una respuesta al azar
        while True:
            indice = int(random()*4 +1)
            indice = str(indice)
            if(pregunta[indice] != ""):
                respuesta_audiencia_2 = pregunta[indice]
                pregunta[indice] = ""
                break
    print("\nHas usado el comodin: Consultar a la Audiencia")
    sleep(1)
    print(f"\n{nombre} La audiencia esta votando")
    sleep(3)
    print(f"\n{nombre} La audiencia ha votado: ")
    print(f"Un {aleatorio_1}% vota: {respuesta_audiencia_1}")
    print(f"Un {aleatorio_2}% vota: {respuesta_audiencia_2}")
    verificar_respuesta(nivel)

def retirada(nivel):
    confirmar = input(f"{nombre} estas seguro que quieres retirarte?(si/no): ").lower()
    if confirmar == "no":
        print(f"{nombre} escribe 'ayuda' para ver que comodines tienes disponibles")
        verificar_respuesta(nivel)
    elif confirmar == "si":                 
        tiempo_final = time()
        tiempo_de_juego = int(tiempo_final-tiempo_inicial)
        print(f"\n{nombre} has decidido retirarte, Has ganado {total[nivel]}Bs")
        print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
        print(f"{json.dumps(nuevo_registro(nivel), indent = 4)}")
        quit()
    else:
        print(f"Esa respuesta no es valida, escribe 'ayuda' para ver tus comodines disponibles o 'retirarme' si quieres retirarte")
        verificar_respuesta(nivel)
        
def opcion_a(nivel):
    global respuesta_correcta, pregunta
    global a, b, c, d, tiempo_final, tiempo_de_juego
    if(respuesta_correcta == a):
        if nivel == 7:
            tiempo_final = time()
            tiempo_de_juego = int(tiempo_final-tiempo_inicial)
            print(f"****FELICIDADES, {nombre}!****")
            print("********GANASTE 80Bs**********")
            print("Excelente juego, una vez mas Felicidades!")
            print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
            print(f"\n{nombre} Tu registro de partida es: ")
            print(f"{json.dumps(nuevo_registro(nivel+1), indent = 4)}")
            quit()
        else:
            print(f"\n{nombre} Muy bien, Ahora tienes {total[nivel+1]}Bs vamos a la pregunta {nivel +2}")
            print(seleccionar_pregunta(nivel+1))
            verificar_respuesta(nivel+1)
    else:
        tiempo_final = time()
        tiempo_de_juego = int(tiempo_final-tiempo_inicial)
        print(f"\nLo siento {nombre}, has seleccionado la respuesta incorrecta.\n La respuesta correcta es:{respuesta_correcta}")
        print(f"Muchas Gracias por jugar, lograste ganar {total[nivel]}Bs")
        print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
        print(f"\n{nombre} Tu registro de partida es: ")
        print(f"\n{json.dumps(nuevo_registro(nivel), indent = 4)}")                      
        intentar_nuevamente()
    
def opcion_b(nivel):
    global respuesta_correcta, pregunta
    global a, b, c, d, tiempo_final, tiempo_de_juego
    if(respuesta_correcta == b):
        if nivel == 7:
            tiempo_final = time()
            tiempo_de_juego = int(tiempo_final-tiempo_inicial)
            print(f"****FELICIDADES, {nombre}!****")
            print("********GANASTE 80Bs**********")
            print("Excelente juego, una vez mas Felicidades!")
            print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
            print(f"\n{nombre} Tu registro de partida es: ")
            print(f"{json.dumps(nuevo_registro(nivel+1), indent = 4)}")
            quit()
        else:
            print(f"\n{nombre} Muy bien, Ahora tienes {total[nivel+1]}Bs vamos a la pregunta {nivel +2}")
            print(seleccionar_pregunta(nivel+1))
            verificar_respuesta(nivel+1)
    else:
        tiempo_final = time()
        tiempo_de_juego = int(tiempo_final-tiempo_inicial)
        print(f"\nLo siento {nombre}, has seleccionado la respuesta incorrecta.\n La respuesta correcta es:{respuesta_correcta}")
        print(f"Muchas Gracias por jugar, lograste ganar {total[nivel]}Bs")
        print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
        print(f"\n{nombre} Tu registro de partida es: ")
        print(f"\n{json.dumps(nuevo_registro(nivel), indent = 4)}")
        intentar_nuevamente()
    
def opcion_c(nivel):
    global respuesta_correcta, pregunta
    global a, b, c, d, tiempo_final, tiempo_de_juego
    if(respuesta_correcta == c):
        if nivel == 7:
            tiempo_final = time()
            tiempo_de_juego = int(tiempo_final-tiempo_inicial)
            print(f"****FELICIDADES, {nombre}!****")
            print("********GANASTE 80Bs**********")
            print("Excelente juego, una vez mas Felicidades!")
            print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
            print(f"\n{nombre} Tu registro de partida es: ")
            print(f"{json.dumps(nuevo_registro(nivel+1), indent = 4)}")
            quit()
        else:
            print(f"\n{nombre} Muy bien, Ahora tienes {total[nivel+1]}Bs vamos a la pregunta {nivel +2}")
            print(seleccionar_pregunta(nivel+1))
            verificar_respuesta(nivel+1)
    else:
        tiempo_final = time()
        tiempo_de_juego = int(tiempo_final-tiempo_inicial)
        print(f"\nLo siento {nombre}, has seleccionado la respuesta incorrecta.\n La respuesta correcta es:{respuesta_correcta}")
        print(f"Muchas Gracias por jugar, lograste ganar {total[nivel]}Bs")
        print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
        print(f"\n{nombre} Tu registro de partida es: ")
        print(f"\n{json.dumps(nuevo_registro(nivel), indent = 4)}")
        intentar_nuevamente()
    
def opcion_d(nivel):
    global respuesta_correcta, pregunta
    global a, b, c, d, tiempo_final, tiempo_de_juego
    if(respuesta_correcta == d):
        if nivel == 7:
            tiempo_final = time()
            tiempo_de_juego = int(tiempo_final-tiempo_inicial)
            print(f"****FELICIDADES, {nombre}!****")
            print("********GANASTE 80Bs**********")
            print("Excelente juego, una vez mas Felicidades!")
            print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
            print(f"\n{nombre} Tu registro de partida es: ")
            print(f"{json.dumps(nuevo_registro(nivel+1), indent = 4)}")
            quit()
        else:
            print(f"\n{nombre} Muy bien, Ahora tienes {total[nivel+1]}Bs vamos a la pregunta {nivel +2}")
            print(seleccionar_pregunta(nivel+1))
            verificar_respuesta(nivel+1)
            registro_jugador(nivel+1)
    else:
        tiempo_final = time()
        tiempo_de_juego = int(tiempo_final-tiempo_inicial)
        print(f"\nLo siento {nombre}, has seleccionado la respuesta incorrecta.\n La respuesta correcta es:{respuesta_correcta}")
        print(f"Muchas Gracias por jugar, lograste ganar {total[nivel]}Bs")
        print(f"\n{nombre} tardaste {tiempo_de_juego}seg jugando")
        print(f"\n{nombre} Tu registro de partida es: ")
        print(f"\n{json.dumps(nuevo_registro(nivel), indent = 4)}")
        intentar_nuevamente()
        
def intentar_nuevamente():
    global respuesta_correcta, pregunta, comodin_amigo_disponible, comodin_50_disponible, comodin_audiencia_disponible
    global a, b, c, d, tiempo_final, tiempo_de_juego
    nuevo_intento = input(f"\n\n{nombre} Te gustaria intentarlo una vez mas?(si/no): ").lower()
    if nuevo_intento == "si":
        comodin_audiencia_disponible = True
        comodin_50_disponible = True
        comodin_amigo_disponible = True
        print(seleccionar_pregunta(0))
        verificar_respuesta(0)
        registro_jugador(0)
    elif nuevo_intento == "no":
        exit()
    else:
        print(f"{nombre} seleccione 'si' o 'no'")
        intentar_nuevamente()

#seleccionamos aleatoriamente las preguntas
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 1:
        pregunta_1 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 1:
        pregunta_2 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 2:
        pregunta_3 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 2:
        pregunta_4 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 3:
        pregunta_5 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 3:
        pregunta_6 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 4:
        pregunta_7 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
for pregunta_turno in preguntas:
    if pregunta_turno["Dificultad"] == 4:
        pregunta_8 = pregunta_turno
        preguntas.remove(pregunta_turno)
        break
elegir_pregunta = [[0] for i in range(8)]

elegir_pregunta[0][0] = pregunta_1
elegir_pregunta[1][0] = pregunta_2

elegir_pregunta[2][0] = pregunta_3
elegir_pregunta[3][0] = pregunta_4

elegir_pregunta[4][0] = pregunta_5
elegir_pregunta[5][0] = pregunta_6

elegir_pregunta[6][0] = pregunta_7
elegir_pregunta[7][0] = pregunta_8

#Definimos las variables iniciales

registro_final =[]
tiempo_final = 0
tiempo_de_juego = 0
fecha = asctime(gmtime())
dinero = 0
total = [0,10, 20, 30, 40, 50, 60, 70, 80]
nivel = 0
respuesta_correcta = ""
pregunta = []
a,b,c,d = "","","",""
menu = ["jugar","ranking","salir"]
respuestas_permitidas = ["ayuda", "amigo", "50","audiencia","retirarme","a","b","c","d"]
ayuda_50 = "Para usar \"50:50\", escribe '50'"
comodin_50_disponible = True
ayuda_amigo = "Para \"Llamar a un amigo\", escribe 'amigo'"
comodin_amigo_disponible = True
ayuda_audiencia = "Para \"preguntar a la audiencia\", escribe 'audiencia'"
comodin_audiencia_disponible = True

#Iniciamos el Juego

print ("               BIENVENIDO A")
print ("             Quien Quiere ser")
print ("                MILLONARIO")

nombre = input("\n¿cual es tu nombre?: ")
nombre.strip()
menu_inicial()
