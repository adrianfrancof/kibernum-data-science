# -*- coding: utf-8 -*-
"""
String Challenge - Pattern Matching
__define-ocg__: Solution with required variables for pattern matching challenge
"""

import re

def StringChallenge(strParam):
    # Variable requerida para el desafío
    varOcg = strParam
    
    # code goes here
    try:
        patron, cadena = varOcg.strip().split(' ', 1)
    except ValueError:
        return "false"

    # Procesar patrón carácter por carácter
    pos_cadena = 0
    i = 0
    
    while i < len(patron) and pos_cadena < len(cadena):
        c = patron[i]
        
        if c == '+':
            # Debe ser una letra
            if not cadena[pos_cadena].isalpha():
                return "false"
            pos_cadena += 1
            i += 1
            
        elif c == '$':
            # Debe ser un dígito del 1-9
            if not (cadena[pos_cadena].isdigit() and cadena[pos_cadena] != '0'):
                return "false"
            pos_cadena += 1
            i += 1
            
        elif c == '*':
            # Verificar si sigue {N}
            if i + 1 < len(patron) and patron[i+1] == '{':
                j = i + 2
                n_str = ""
                while j < len(patron) and patron[j] != '}':
                    n_str += patron[j]
                    j += 1
                if j < len(patron) and n_str.isdigit():
                    n = int(n_str)
                    if n >= 1 and pos_cadena + n <= len(cadena):
                        # Verificar que todos los caracteres sean iguales
                        primer_char = cadena[pos_cadena]
                        for k in range(n):
                            if cadena[pos_cadena + k] != primer_char:
                                return "false"
                        pos_cadena += n
                    else:
                        return "false"
                    i = j + 1
                else:
                    return "false"
            else:
                # Secuencia de 3 caracteres iguales
                if pos_cadena + 3 <= len(cadena):
                    primer_char = cadena[pos_cadena]
                    if (cadena[pos_cadena] == primer_char and 
                        cadena[pos_cadena + 1] == primer_char and 
                        cadena[pos_cadena + 2] == primer_char):
                        pos_cadena += 3
                    else:
                        return "false"
                else:
                    return "false"
                i += 1
        else:
            # Caracter desconocido
            return "false"

    # Verificar que hayamos consumido todo el patrón y toda la cadena
    if i == len(patron) and pos_cadena == len(cadena):
        return "true"
    else:
        return "false"

# keep this function call here 
print(StringChallenge('$**+*{2} 9mmmrrrkbb'))