import pandas as pd
import variables_globales as vg

def leerArchivo(nombreArchivo):
    df = pd.read_csv(nombreArchivo)
    return df

def agregarFila(datos_nuevo_estudiante):
    nueva_fila_df = pd.DataFrame(datos_nuevo_estudiante)
    
    nueva_fila_df.to_csv(
    vg.ruta_archivo, 
    mode='a', 
    header=False, 
    index=False
    )

def eliminarFila(indice):
    df_actualizado = vg.informacion_archivo.drop(index=indice)
    df_actualizado.to_csv(vg.ruta_archivo, index = False)

def ordenarDataFrame(param1, param2):
    df_ordenado = vg.informacion_archivo.sort_values(by=[param1, param2], ascending= True)
    return df_ordenado

def ordenarDataFrameUnParam(param):
    df_ordenado = vg.informacion_archivo.sort_values(by=param, ascending= True)
    return df_ordenado

def guardarDataFrame(dataFrame):
    dataFrame.to_csv(vg.ruta_archivo, index=False)