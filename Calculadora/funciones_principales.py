#Funcion para agregar elementos al historial, siempre manteniendo un max de 10 elementos
def agregarElementosColaMax10(historial, resultado):
    if len(historial) >= 10:
                historial.popleft()
                historial.append(resultado)
                return historial
    else:
                historial.append(resultado)
                return historial

#Funcion que se encarga de operar los numeros segun sea la operación correspondiente
def operacionDosNumeros(tipo):
    if tipo == "suma":
        print("Suma")
        num1 = int(input("Ingrese el primer numero:"))
        num2 = int(input("Ingrese el segundo numero:"))
        resultado = num1 + num2
    elif tipo == "resta": 
        print("Resta")
        num1 = int(input("Ingrese el primer numero:"))
        num2 = int(input("Ingrese el segundo numero:"))
        resultado = num1 - num2
    elif tipo == "multiplicacion":
        print("Multiplicacion")
        num1 = int(input("Ingrese el primer numero:"))
        num2 = int(input("Ingrese el segundo numero:"))
        resultado = num1 * num2
    elif tipo == "division":
        print("Division")
        num1 = int(input("Ingrese el primer numero:"))
        num2 = int(input("Ingrese el segundo numero:"))
        resultado = num1 / num2
    else:
        return "Operacion invalida"
    
    print("El resultado es:", resultado)
    return resultado