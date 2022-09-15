'''Problema 1 Examen Azul
Elaborado por: Jose Nieves
carnet: 12-11017'''
print("Este problema te pide un numero y suma todos los numeros impares hasta ese numero")
numero_ingresado = float(input("Introduce un numero entero: "))
while True: #Para asegurarnos de que el numero introducido sea positivo
    if numero_ingresado > 0:
        break
    else:
        print("Por favor introduce un numero positivo")
        numero_ingresado = float(input("Introduce un numero entero: "))
while True:
    if type(numero_ingresado) == int:
        break
    else:
        print("Ingrese un numero entero")
        numero_ingresado = int(input("Introduce un numero entero: "))
suma_impares = 0
for x in range(0,numero_ingresado+1):
    if not x % 2 == 0: #Filtramos los numeros pares
        suma_impares += x
print(f"La suma de todos los numeros impares hasta {numero_ingresado} es: {suma_impares}")

