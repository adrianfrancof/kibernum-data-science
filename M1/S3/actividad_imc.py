'''Calcular indice de masa corporal
IMC = PESO / ESTATURA**2

IMC = BAJO PESO   = < 18.5
IMC = PESO NORMAL = 18.5 <= IMC < 25.0
IMC = SOBREPESO   = 25.0 <= IMC < 30.0

# Individuo
1, 62, 1.65
2, 72, 1.73
3, 65, 1.57
4, 70, 1.68
5, 95, 1.89
'''
class Persona:
    def __init__(self):
        pass

# DATOS TABULADOS O EN DICCIONARIO
lista_personas = [ # [{'individuo 1': 1, 'peso': 62, 'altura': 1.65},{},{},{},{}]
    {'individuo': 1, 'peso': 62, 'altura': 1.65}, # diccionario
    {'individuo': 2, 'peso': 72, 'altura': 1.73}, # diccionario
    {'individuo': 3, 'peso': 65, 'altura': 1.57}, # diccionario
    {'individuo': 4, 'peso': 70, 'altura': 1.68}, # diccionario
    {'individuo': 5, 'peso': 95, 'altura': 1.89}  # diccionario
]

# CALCULAR IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# CLASIFICAR IMC
def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif 18.5 <= imc < 25.0:
        return 'Peso Normal'
    elif 25.0 <= imc < 30.0:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

# CICLO DE EJECUCION
# recorrer lista de personas, para acceder a cada diccionario
def ejecucion():
    resultado = []                                                        # lista para almacenar elementos
    for persona in lista_personas:                                        # se recorren los elementos de la lista_personas
        imc = calcular_imc(persona['peso'], persona['altura'])
        clasificacion = clasificar_imc(imc)
        resultado.append(clasificacion)
                
        print(f'Persona {persona['individuo']} tiene un imc {imc} y una clasificación {clasificacion}')
            
    return resultado    
   
print(ejecucion())







