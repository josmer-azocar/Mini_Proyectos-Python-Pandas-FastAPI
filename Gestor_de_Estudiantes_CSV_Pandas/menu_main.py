from os import system
import time
import logica as lg
import variables_globales as vg

#Apartado de instrucciones
lg.mostrarInstrucciones()
    
#Menu de opciones
while True:
    system('cls')
    print("Menu de opciones:")
    time.sleep(1)
    print("1) Ingresar archivo CSV")
    print("2) Mostrar información del CSV")
    print("3) Agregar un nuevo alumno")
    print("4) ELiminar una fila")
    print("5) Ordenar por grado y sección")
    print("6) Ordenar por edad")
    print("7) Modificar la información de un alumno")
    print("8) Salir")
    
    opcion = input("\nIngrese una opcion disponible por favor: ")
    
    match opcion:
        case "1":
            vg.ruta_archivo = input("ingrese la direccion completa de su archivo CSV: \n")
            vg.informacion_archivo = lg.ingresarArchivo(vg.ruta_archivo)
            
            if (vg.informacion_archivo.bool):
                print("\nel archivo se ha registrado de manera exitosa")
                
            espera = input("\ningrese cualquier digito para continuar\n")
            
        case "2":
            if (vg.ruta_archivo == ""):
                print("El archivo no ha sido ingresado")
                espera = input("\ningrese cualquier digito para continuar\n")
            else:
                print("Información del CSV: ")
                vg.informacion_archivo = lg.ingresarArchivo(vg.ruta_archivo)
                print(vg.informacion_archivo)
                
                espera = input("\ningrese cualquier digito para continuar\n")
    
        case "3":
            if (vg.ruta_archivo == ""):
                print("El archivo no ha sido ingresado")
                espera = input("\ningrese cualquier digito para continuar\n")
            else:
                nombre = input("ingrese el nombre del alumno: \n")
                edad = int(input("ingrese la edad del alumno (debe ser un dato numerico): \n"))
                grado = int(input("ingrese el grado que esta cursando el alumno (debe ser un dato numerico): \n"))
                seccion = input("ingrese la sección del alumno: \n")
            
                resultado = lg.agregarEstudiante(nombre, edad, grado, seccion)
            
                print(resultado)
            
            espera = input("\ningrese cualquier digito para continuar\n")
            
        case "4":
            if (vg.ruta_archivo == ""):
                print("El archivo no ha sido ingresado")
                espera = input("\ningrese cualquier digito para continuar\n")
            else:
                system('cls')
                manera = input("De que manera desea eliminar la fila \n1) Por nombre del estudiante \n2) Por indice de la fila \n")
                if (manera == "1"):
                    nombre = input("Ingrese el nombre del alumno: \n")
                    lg.eliminarFilaPorNombre(nombre)
                elif (manera == "2"):
                    indice = int(input("Ingrese el indice de la Fila: \n"))
                    lg.eliminarFilaPorIndice(indice)
                else:
                    print("\nOpción Invalida!")
                    time.sleep(2)
                    
                espera = input("\ningrese cualquier digito para continuar\n")
            
        case "5":
            if (vg.ruta_archivo == ""):
                print("El archivo no ha sido ingresado")
                espera = input("\ningrese cualquier digito para continuar\n")
            else:
                df_ordenado = lg.dataFrameOrdenadoPor("Grado", "Seccion")
                print("\nDatos ordenado: \n")
                print(df_ordenado)
                
                eleccion = input("\nDesea modificar el archivo original con este orden? (s/n) \n")
                if (eleccion == "s"):
                    lg.guardarDataFrame(df_ordenado)
                    print("\nSe ha modificado de manera exitosa")
                elif (eleccion == "n"):
                    print("OK!")
                else:
                    print("\nOpción Invalida!")
                    time.sleep(2)
                    
                espera = input("\ningrese cualquier digito para continuar\n")
        
        case "6":
            if (vg.ruta_archivo == ""):
                print("El archivo no ha sido ingresado")
                espera = input("\ningrese cualquier digito para continuar\n")
            else:
                df_ordenado = lg.dataFrameOrdenadoPorUnParam("Edad")
                print("\nDatos ordenado: \n")
                print(df_ordenado)
                
                eleccion = input("\nDesea modificar el archivo original con este orden? (s/n) \n")
                if (eleccion == "s"):
                    lg.guardarDataFrame(df_ordenado)
                    print("\nSe ha modificado de manera exitosa")
                elif (eleccion == "n"):
                    print("OK!")
                else:
                    print("\nOpción Invalida!")
                    time.sleep(2)   
                                                
                espera = input("\ningrese cualquier digito para continuar\n")
            
        case "7":
            if (vg.ruta_archivo == ""):
                print("El archivo no ha sido ingresado")
                espera = input("\ningrese cualquier digito para continuar\n")
            else:
                nombre = input("Ingrese el nombre del alumno a quien desea modificar la Información: \n")
                fila, indice = lg.BuscarFilaPorNombre(nombre)
                print(fila)
                print("\nQue desea modificar?")
                print("Nombre")
                print("Edad")
                print("Grado")
                print("Seccion")
                eleccion = input("\nIngrese lo que desea modificar por favor: (ejem: Edad))\n")
                
                match eleccion:
                    
                    case "Nombre":
                    
                        nuevo_nombre = input("Ingrese el nuevo nombre: (ejem: Maria)\n")
                        nuevo_df = lg.ModificarDatoPorIndice(nuevo_nombre, "Nombre", indice)
                        
                        elect = input("\nDesea modificar el archivo original? (s/n) \n")
                        if (elect == "s"):
                            lg.guardarDataFrame(nuevo_df)
                            print("\nSe ha modificado de manera exitosa")
                        elif (elect == "n"):
                            print("OK!")
                        else:
                            print("\nOpción Invalida!")
                            time.sleep(2)
                            break
                                            
                    case "Edad":
                        nueva_edad = int(input("Ingrese la nueva edad: (ejem: 16)\n"))
                        nuevo_df = lg.ModificarDatoPorIndice(nueva_edad, "Edad", indice)
                        
                        elect = input("\nDesea modificar el archivo original? (s/n) \n")
                        if (elect == "s"):
                            lg.guardarDataFrame(nuevo_df)
                            print("\nSe ha modificado de manera exitosa")
                        elif (elect == "n"):
                            print("OK!")
                        else:
                            print("\nOpción Invalida!")
                            time.sleep(2)
                            break
                                            
                    case "Grado":
                        nuevo_grado = int(input("Ingrese el nuevo grado: (ejem: 5)\n"))
                        nuevo_df = lg.ModificarDatoPorIndice(nuevo_grado, "Grado", indice)
                        
                        elect = input("\nDesea modificar el archivo original? (s/n) \n")
                        if (elect == "s"):
                            lg.guardarDataFrame(nuevo_df)
                            print("\nSe ha modificado de manera exitosa")
                        elif (elect == "n"):
                            print("OK!")
                        else:
                            print("\nOpción Invalida!")
                            time.sleep(2)
                            break                   
                    
                    case "Seccion":
                        nueva_seccion = input("Ingrese el nuevo nombre: (ejem: B)\n")
                        nuevo_df = lg.ModificarDatoPorIndice(nueva_seccion, "Seccion", indice)
                        
                        elect = input("\nDesea modificar el archivo original? (s/n) \n")
                        if (elect == "s"):
                            lg.guardarDataFrame(nuevo_df)
                            print("\nSe ha modificado de manera exitosa")
                        elif (elect == "n"):
                            print("OK!")
                        else:
                            print("\nOpción Invalida!")
                            time.sleep(2)
                            break                        
                        
                    case _:
                        print("\nOpción Invalida!")
                        time.sleep(2)
                        
            espera = input("\ningrese cualquier digito para continuar\n")

        case "8":
            print("\nGracias por usar este Programa")
            break
            
        case _:
            print("\nOpción Invalida!")
            time.sleep(2)