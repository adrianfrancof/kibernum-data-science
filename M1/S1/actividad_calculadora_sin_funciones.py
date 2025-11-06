# Calculadora sin funciones
'''Crear un script en Python que emule el comportamiento de una calculadora.
La calculadora debe soportar las 4 operaciones básicas (suma, resta, multiplicación y división).
Debe preguntar los operandos y la operación en la entrada de la consola.'''

def calculadora():
    print("Bienvenido a la calculadora Python") # imprimiendo
    print("Operaciones disponibles:")           # imprimiendo
    print("1. Suma (+)")                        # imprimiendo
    print("2. Resta (-)")                       # imprimiendo
    print("3. Multiplicación (*)")              # imprimiendo
    print("4. División (/)")                    # imprimiendo

    operacion = input("Seleccione una operación (+, -, *, /): ")    # estamos ingresando valores
    if operacion not in ['+', '-', '*', '/']:                       # si no esta en el arreglo ['+', '-', '*', '/']
        print("Operación no válida.")                               # imprime a usuario
    else:                                                           # Entonces, esta la operacion en el arreglo
        try:
            a = float(input("Ingrese el primer operando: "))
            b = float(input("Ingrese el segundo operando: "))
        except ValueError:
            print("Entrada no válida. Por favor ingrese números.")
        else:
            if operacion == '+':
                resultado = a + b   # operacion de calculo
            elif operacion == '-': 
                resultado = a - b   # operacion de calculo
            elif operacion == '*':
                resultado = a * b
            elif operacion == '/':
                if b == 0:
                    resultado = "Error: División por cero no permitida."
                else:
                    resultado = a / b
            print(f"El resultado de {a} {operacion} {b} es: {resultado}")
                       