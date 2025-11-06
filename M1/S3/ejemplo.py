def calcular_imc():
    print("=== ¿Que tan Cerdo te cientes Hoy? (IMC) ===")
   
    try:
        peso = float(input("Ingrese wataje (kg): "))
        estatura = float(input("Ingrese su prestancia (m): "))
       
        if peso <= 0 or estatura <= 0:
            print("Error: No mienta!!! El peso y la estatura deben ser mayores que cero.")
            return
 
        imc = peso / (estatura ** 2)
        print(f"\nSu IMC es: {imc:.2f}")
 
        # Clasificación según el valor del IMC
        if imc < 18.5:
            categoria = "Esqueleto"
        elif imc < 25:
            categoria = "Normal"
        elif imc < 30:
            categoria = "Un poco Pasado"
        elif imc < 35:
            categoria = "Chanchito Bebe"
        elif imc < 40:
            categoria = "Chanchito Madurando "
        elif imc < 50:
            categoria = "Chancho Maduro"
        else:
            categoria = "Chancho Man"
 
        print(f"Categoría: {categoria}")
 
    except ValueError:
        print("Error: Ingrese solo valores que sean Cierto!!!!.")
 
# Ejecutar la calculadora
calcular_imc()