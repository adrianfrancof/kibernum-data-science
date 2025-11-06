# 1. Crear una lista de productos con al menos cinco nombres

productos = ["Laptop", "Teléfono", "Tablet", "Monitor", "Teclado"] # 5 elementos
  # indice  [0       ,          1,        2,         3,         4]

# 2. Agregar dos productos más y rescatar los primeros tres en una nueva lista
productos.append("Mouse")               # ["Laptop", "Teléfono", "Tablet", "Monitor", "Teclado", "Mouse"]
productos.append("Impresora")           # ["Laptop", "Teléfono", "Tablet", "Monitor", "Teclado", "Mouse", "Impresora"]
productos_destacados = productos[:3]    # sublista ['Laptop', 'Teléfono', 'Tablet']
print(productos)                        # ['Laptop', 'Teléfono', 'Tablet', 'Monitor', 'Teclado', 'Mouse', 'Impresora']
print(productos_destacados)             # ['Laptop', 'Teléfono', 'Tablet']
print(productos[0])                     # Laptop

# 3. Crear un diccionario inventario con cantidades en stock
inventario = { # diccionario es una estructura de clave = valor
    "Laptop": 10,
    "Teléfono": 15,
    "Tablet": 8,
    "Monitor": 12,
    "Teclado": 20
}

# 4. Agregar un nuevo producto y mostrar la cantidad en stock de "Tablet"
inventario["Mouse"] = 25                # agregar nuevo valor, diccionario['nueva_clave'] = valor_asignado
cantidad_tablet = inventario["Tablet"]  # acceder al valor, diccionario['clave_a_acceder']

# 5. Crear una tupla de categorías y mostrar la segunda categoría
categorias = ("Electrónica", "Ropa", "Alimentos")
segunda_categoria = categorias[1]

# 6. Desempaquetar la tupla en variables individuales
categoria1, categoria2, categoria3 = categorias

# 7. Crear un set de productos únicos y verificar duplicados
productos_unicos = set(productos)

# 8. Usar comprensión de listas para convertir los nombres de productos en mayúsculas
productos_mayusculas = [producto.upper() for producto in productos]

# Imprimir resultados
print("Lista de productos:", productos)
print("Productos destacados:", productos_destacados)
print("Inventario:", inventario)
print(f"Cantidad de Tablets en stock: {cantidad_tablet}")
print("Lista de categorías:", categorias)
print(f"Segunda categoría: {segunda_categoria}")
print(f"Categorías desempaquetadas: {categoria1}, {categoria2}, {categoria3}")
print("Set de productos únicos:", productos_unicos)
print("Productos en mayúsculas:", productos_mayusculas)