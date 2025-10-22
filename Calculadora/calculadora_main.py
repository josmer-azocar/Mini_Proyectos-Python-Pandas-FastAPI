#Calculadora
from collections import deque
from os import system
import time
import funciones_principales as func

#Estructura tipo cola para el historial de los 10 ultimos resultados
historial = deque()

#Menu de opciones
while True:
    system('cls')
    print("Menu de opciones:")
    time.sleep(1)
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Potenciacion")
    print("6) Historial")
    print("7) Salir")
    
    opcion = input("Ingrese una opcion disponible por favor:")
    
    match opcion:
        case "1":
            resultado = func.operacionDosNumeros("suma")
            historial = func.agregarElementosColaMax10(historial, resultado)
            espera = input("ingrese cualquier digito para continuar")
            
        
        case "2":
            resultado = func.operacionDosNumeros("resta")
            historial = func.agregarElementosColaMax10(historial, resultado)
            espera = input("ingrese cualquier digito para continuar")
    
        case "3":
            resultado = func.operacionDosNumeros("multiplicacion")
            historial = func.agregarElementosColaMax10(historial, resultado)
            espera = input("ingrese cualquier digito para continuar")
            
        case "4":
            resultado = func.operacionDosNumeros("division")
            historial = func.agregarElementosColaMax10(historial, resultado)
            espera = input("ingrese cualquier digito para continuar")
            
        case "5":
            print("Potenciacion")
            num1 = int(input("Ingrese la base:"))
            num2 = int(input("Ingrese el exponente:"))
            resultado = num1**num2
            print("El resultado es:", resultado)
            historial = func.agregarElementosColaMax10(historial, resultado)
            espera = input("ingrese cualquier digito para continuar")
            
        case "6":
            print("Historial de los ultimos 10 resultados")
            for guardado in historial:
                print(guardado)  
            espera = input("ingrese cualquier digito para continuar")

        case "7":
            print("Gracias por usar la calculadora")
            break
            
        case _:
            print("opcion invalida")
            time.sleep(2)