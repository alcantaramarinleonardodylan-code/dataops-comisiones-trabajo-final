import pandas as pd

df = pd.read_csv("ComisionEmpleados_V1_202605.csv", sep=";")

df.to_excel("comisiones.xlsx", index=False)

print("Excel generado correctamente")
