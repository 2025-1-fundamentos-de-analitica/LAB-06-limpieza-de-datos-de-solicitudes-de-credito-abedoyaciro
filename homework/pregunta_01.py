"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
Versión alternativa con estilo minimalista.
"""
import os
import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """

    # Leer el archivo CSV de entrada
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", index_col=0, sep=";")
    df = df.copy()

    # Eliminar filas con datos faltantes
    df = df.dropna()

    # Limpiar y convertir la columna 'monto_del_credito' a tipo float
    df["monto_del_credito"] = df["monto_del_credito"].str.removeprefix("$ ").str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)

    # Limpiar columnas de texto con un bucle for
    text_columns = ["tipo_de_emprendimiento", "idea_negocio", "línea_credito", "barrio"]
    for col in text_columns:
        df[col] = df[col].str.lower()
        df[col] = df[col].str.replace(" ", "_")
        df[col] = df[col].str.replace(".", "_")
        df[col] = df[col].str.replace("-", "_")
        if col != "barrio":
            df[col] = df[col].str.strip()
        df[col] = df[col].astype("category")

    # Convertir otras columnas
    df["sexo"] = df["sexo"].str.lower().astype("category")
    df["estrato"] = df["estrato"].astype("category")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int).astype("category")
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")

    # Eliminar registros duplicados
    df.drop_duplicates(inplace=True)

    # Crear el directorio de salida si no existe
    outdir = "files/output"
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Guardar el archivo limpio
    df.to_csv(os.path.join(outdir, "solicitudes_de_credito.csv"), sep=";")

