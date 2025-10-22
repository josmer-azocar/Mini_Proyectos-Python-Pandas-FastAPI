import manejo_de_CSV as csvHandler
import variables_globales as vg

def ingresarArchivo(nombreArchivo):
    return csvHandler.leerArchivo(nombreArchivo)

def agregarEstudiante(nombre, edad, grado, seccion):
    datos_nuevo_estudiante = {
    'nombre': [nombre],
    'edad': [edad],
    'grado': [grado],
    'seccion': [seccion]
    }
    
    csvHandler.agregarFila(datos_nuevo_estudiante)
    
    return f"datos agregados: {datos_nuevo_estudiante}"

def eliminarFilaPorNombre(name):
    indices_por_condicion = vg.informacion_archivo[vg.informacion_archivo["nombre"] == name].index
    csvHandler.eliminarFila(indices_por_condicion)
    
def eliminarFilaPorIndice(indice):
    csvHandler.eliminarFila(indice)

def mostrarInstrucciones():
    with open(r"Gestor_de_Estudiantes_CSV_Pandas\instrucciones.txt", encoding = "UTF-8") as archivo:
        contenido = archivo.read()
    print(contenido)
    espera = input("ingrese cualquier digito para continuar\n")
    
def dataFrameOrdenadoPor(param1, param2):
    return csvHandler.ordenarDataFrame(param1, param2)

def dataFrameOrdenadoPorUnParam(param):
    return csvHandler.ordenarDataFrameUnParam(param)

def guardarDataFrame(dataFrame):
    csvHandler.guardarDataFrame(dataFrame)
    vg.informacion_archivo = dataFrame

def BuscarFilaPorNombre(name):
    fila = vg.informacion_archivo[vg.informacion_archivo["Nombre"] == name]
    indice = vg.informacion_archivo[vg.informacion_archivo["Nombre"] == name].index
    return fila, indice

def ModificarDatoPorIndice(nuevo_dato, nombre_columna, indice):
    vg.informacion_archivo.loc[indice, nombre_columna] = nuevo_dato
    return vg.informacion_archivo