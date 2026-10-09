import os
import pandas as pd
import unicodedata

df = pd.read_excel(os.path.join(os.path.dirname(__file__), "resultado_laboratorio_suelo.xlsx"))


def sin_tildes(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', str(texto).lower())
                   if unicodedata.category(c) != 'Mn')


def mediana(columna, datos):
    numeros = pd.to_numeric(datos[columna].astype(str).str.replace(",", "."), errors="coerce")
    return numeros.median()


def consultar(Departamento, Municipio, Cultivo, num_registros):
    filtered_df = df[(df['Departamento'].map(sin_tildes) == sin_tildes(Departamento)) &
                     (df['Municipio'].map(sin_tildes) == sin_tildes(Municipio)) &
                     (df['Cultivo'].map(sin_tildes) == sin_tildes(Cultivo))]
    result_df = filtered_df.head(int(num_registros))[['Departamento', 'Municipio', 'Cultivo', 'Topografia']].copy()
    result_df['Mediana pH'] = mediana('pH agua:suelo 2,5:1,0', filtered_df)
    result_df['Mediana P'] = mediana('Fósforo (P) Bray II mg/kg', filtered_df)
    result_df['Mediana K'] = mediana('Potasio (K) intercambiable cmol(+)/kg', filtered_df)
    return result_df