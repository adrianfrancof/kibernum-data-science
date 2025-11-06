'''Crear un script en Python que emule el comportamiento de una calculadora.
La calculadora debe soportar las 4 operaciones básicas (suma, resta, multiplicación y división).
Debe preguntar los operandos y la operación en la entrada de la consola.'''

import math

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def logaritmo(a):
    if a <= 0:
        return "Error: El logaritmo de números negativos o cero no está definido."
    return math.log(a)

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de números negativos."
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: No se puede calcular el factorial de números negativos."
    if a != int(a):
        return "Error: El factorial solo se calcula para números enteros."
    return math.factorial(int(a))

def calculadora():
    print("Bienvenido a la calculadora científica Python")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Logaritmo natural (ln)")
    print("6. Potencia (^)")
    print("7. Raíz cuadrada (√)")
    print("8. Factorial (!)")

    operacion = input("Seleccione una operación (+, -, *, /, ln, ^, √, !): ")
    if operacion not in ['+', '-', '*', '/', 'ln', '^', '√', '!']:
        print("Operación no válida.")
        return

    try:
        a = float(input("Ingrese el primer operando: "))
        
        # Para operaciones que necesitan dos operandos
        if operacion in ['+', '-', '*', '/', '^']:
            b = float(input("Ingrese el segundo operando: "))
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")
        return

    # Operaciones básicas
    if operacion == '+':
        resultado = suma(a, b)
        print(f"El resultado de {a} + {b} es: {resultado}")
    elif operacion == '-':
        resultado = resta(a, b)
        print(f"El resultado de {a} - {b} es: {resultado}")
    elif operacion == '*':
        resultado = multiplicacion(a, b)
        print(f"El resultado de {a} * {b} es: {resultado}")
    elif operacion == '/':
        resultado = division(a, b)
        print(f"El resultado de {a} / {b} es: {resultado}")
    # Operaciones científicas
    elif operacion == 'ln':
        resultado = logaritmo(a)
        print(f"El logaritmo natural de {a} es: {resultado}")
    elif operacion == '^':
        resultado = potencia(a, b)
        print(f"El resultado de {a} ^ {b} es: {resultado}")
    elif operacion == '√':
        resultado = raiz_cuadrada(a)
        print(f"La raíz cuadrada de {a} es: {resultado}")
    elif operacion == '!':
        resultado = factorial(a)
        print(f"El factorial de {a} es: {resultado}")

# Ejecutar la calculadora
calculadora()
