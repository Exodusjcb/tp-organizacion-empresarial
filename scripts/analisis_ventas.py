
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Convertir fecha
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Crear columna mes
df["mes"] = df["sales_date"].dt.to_period("M")

# Calcular métricas
ventas_totales = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()

ventas_por_mes = df.groupby("mes")["sales_amount"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Promedio de ventas:", promedio_ventas)

# Crear gráfico
ventas_por_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto vendido")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

# Guardar resumen
with open("resultados/resumen.txt", "w") as archivo:
    archivo.write(f"Ventas totales: {ventas_totales}\n")
    archivo.write(f"Promedio ventas: {promedio_ventas}\n")

print("Análisis completado correctamente")
