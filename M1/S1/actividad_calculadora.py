'''Crear un script en Python que emule el comportamiento de una calculadora.
La calculadora debe soportar las 4 operaciones básicas (suma, resta, multiplicación y división).
Debe preguntar los operandos y la operación en la entrada de la consola.'''

def suma(a, b):
    # aqui, todo lo que se declare
    return a + b

# aqui, todo lo que se declare se ejecuta fuera de la funcion suma 
def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def calculadora():
    print("Bienvenido a la calculadora Python")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    operacion = input("Seleccione una operación (+, -, *, /): ")
    if operacion not in ['+', '-', '*', '/']:
        print("Operación no válida.")
        return

    try:
        a = float(input("Ingrese el primer operando: "))
        b = float(input("Ingrese el segundo operando: "))
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")
        return

    if operacion == '+':
        resultado = suma(a, b) # a + b 
    elif operacion == '-':
        resultado = resta(a, b)
    elif operacion == '*':
        resultado = multiplicacion(a, b)
    elif operacion == '/':
        resultado = division(a, b)

    print(f"El resultado de {a} {operacion} {b} es: {resultado}")
