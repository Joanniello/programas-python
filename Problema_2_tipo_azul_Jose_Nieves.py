'''Problema 1 Examen Azul
Elaborado por: Jose Nieves
carnet: 12-11017'''
import json
import time
with open("examen_azul.json") as empleados:
    lista_empleados = json.load(empleados)
print("Este programa compara tu edad y salario con los empleados de nuestra compañia \n\
y te muestra quienes son mayores que tu y tienen un menor sueldo y tambien \n\
los que son menores que tu con un mayor sueldo.")
name = input("\nEscribe tu nombre: ")
salary = int(input("Cual es tu salario = "))
empleados_mayor = [] #Para agregar los empleados de mayor edad y menor salario
empleados_menor = [] #Para agregar los empleados de menor edad y mayor salario
while True: #Para asegurarnos de que el salario sea positivo
    if salary >= 0:
        break
    else:
        print("Escribe un salario valido")
        salary = float(input("Cual es tu salario = "))
age = int(input("Escribe tu edad = "))
while True: #Para asegurarnos de que la edad sea positiva
    if age > 0:
        break
    else:
        print("Escribe una edad valida")
        age = int(input("Cual es tu edad = "))
for comparar_mayor in lista_empleados: # Vamos a comparar los usuarios de mayor edad y menor salario
    comparar_mayor["salary"] = int(comparar_mayor["salary"]) #Convertimos el salario en int
    comparar_mayor["age"] = int(comparar_mayor["age"]) #Convertimos la edad en int
    if comparar_mayor["age"] > age and salary > comparar_mayor["salary"]: #Comparamos mayor edad y menor salario
        empleados_mayor.append(comparar_mayor) #Agregamos los de mayor edad y menor salario en nuestra lista
        
for comparar_menor in lista_empleados: # Vamos a comparar los usuarios de menor edad y mayor salario
    comparar_menor["salary"] = int(comparar_menor["salary"]) #Convertimos el salario en int
    comparar_menor["age"] = int(comparar_menor["age"]) #Convertimos la edad en int
    if age > comparar_menor["age"] and comparar_menor["salary"] > salary: #Comparamos menor edad y mayor salario
        empleados_menor.append(comparar_menor) #Agregamos los de menor edad y mayor salario en nuestra lista
print(f"\n{name} a continuacion te mostrare los usuarios de mayor edad y con menor salario que tu")
time.sleep(2)
print(json.dumps(empleados_mayor, indent = 4))
print(f"\n{name} a continuacion te mostrare los usuarios de menor edad y con mayor salario que tu")
time.sleep(2)
print(json.dumps(empleados_menor, indent = 4))
    
