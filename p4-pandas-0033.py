# KEYLA PAOLA NC = 0033Z
import pandas as pd
import numpy as np

n_fila = 5
n_columnas = 5
tag_columnas = tuple("ABCDE") # etiquetas para las columnas de una tupla
print(tag_columnas)

# Genera números entre 1 y 10 (se cambia 6 por 11 para incluir el 10)
matriz = np.random.randint(1, 11, size=(n_fila, n_columnas))

print("\nGenera matriz de 5 filas por 5 columnas")
print("\nCon números aleatorios comprendidos entre 1 y 10")
print(matriz)

# Corrección: DataFrame con 'F' mayúscula
df = pd.DataFrame(matriz, columns=tag_columnas)
# la variable df es DataFrame
print("\n---LA TABLA O DATAFRAME NC= 0033---- NC= 0033")
print(df)
print("\n--- KEYLA PAOLA CIAGRROA NC = 0033---")