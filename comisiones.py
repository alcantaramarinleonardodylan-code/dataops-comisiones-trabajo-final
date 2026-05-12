import pandas as pd

datos = {
    "Empleado": ["Juan", "Ana", "Luis"],
    "Ventas": [1000, 1500, 2000]
}

df = pd.DataFrame(datos)

df["Comision"] = df["Ventas"] * 0.10

df.to_excel("comisiones.xlsx", index=False)

print("Excel generado correctamente")
