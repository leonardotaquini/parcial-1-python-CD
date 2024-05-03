import pandas as pd
import random
import matplotlib.pyplot as plt




productos = [
    {"nombre": "Camiseta", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible": 25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible": 150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible": 180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]
# Creo un DataFrame con sus columnas correspondientes
productos_df = pd.DataFrame( productos, columns=["nombre", "precio", "cantidad_disponible"])

# Creo una columna total_por_producto multiplicando la cantidad de cada producto por su precio.
productos_df['total_por_producto'] = productos_df["precio"] * productos_df["cantidad_disponible"]

# Creo una columna valor_total_del_inventario y realizo la suma acumulada.
productos_df['valor_total_del_inventario'] = productos_df["total_por_producto"].cumsum()

# Simulo ventas
productos_df["ventas"] = round( productos_df["cantidad_disponible"] / 2 - random.randint(0,20) )

# Actualizo la cantidad disponible
productos_df["cantidad_disponible"] = productos_df["cantidad_disponible"] - productos_df["ventas"]

# Creo un DataFrame con el nombre y la cantidad disponible
nombres_cantidad_df = pd.DataFrame( productos_df[['nombre', 'cantidad_disponible']] , columns=["nombre", "cantidad_disponible"])

# Visualizo la cantidad disponible de productos.

plt.bar(  nombres_cantidad_df['nombre'], nombres_cantidad_df['cantidad_disponible']  )
plt.title('Ejercicio 4')
plt.xlabel('Productos')
plt.ylabel('Cantidad')
plt.xticks(rotation=50, ha='right')
plt.show()

