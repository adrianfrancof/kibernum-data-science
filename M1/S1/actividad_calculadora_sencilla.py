'''Crear un script en Python que emule el comportamiento de una calculadora.
La calculadora debe soportar las 4 operaciones básicas (suma, resta, multiplicación y división).
Debe preguntar los operandos y la operación en la entrada de la consola.'''

# paso 1 impresion a usuario
print("Bienvenido a la calculadora Python") # se imprime informacion en la terminal
print("Operaciones disponibles:")           # se imprime informacion en la terminal
print("1. Suma (+)")                        # se imprime informacion en la terminal
print("2. Resta (-)")                       # se imprime informacion en la terminal
print("3. Multiplicación (*)")              # se imprime informacion en la terminal
print("4. División (/)")                    # se imprime informacion en la terminal

# paso 2 impresion ingreso opcion
opcion = input("Ingrese la opción: ")       # se pide la opcion mediante la terminal, entregando un mensaje
a = input("Ingrese el primer operando: ")   # se pide el primer numero mediante la terminal, entregando un mensaje
a = float(a)                                # a = 2.0 castear o convertir a punto flotante o decimal

b = float(input("Ingrese el segundo operando: ")) # b = 3.0

# paso 3 validar y operar
if opcion == '1':    # si opcion es igual a 1
  resultado = a+b       # se realiza la suma
elif opcion == '2':  # si no, si opcion es igual a 2
  resultado = a-b       # se realiza la resta
elif opcion == '3':  # si no, si opcion es igual a 3
  resultado = a*b       # se realiza la multiplicacion
elif opcion == '4':  # si no, si opcion es igual a 4
  resultado = a/b       # se realiza la division

print(resultado)
