# Mini-proyectos en Python

Este repositorio contiene varios mini-proyectos que usé para practicar Python. Cada carpeta es un proyecto independiente con su propio punto de entrada.

---

## Estructura general (resumen)
- Calculadora/ — aplicación de consola (calculadora con historial)
  - [Calculadora/calculadora_main.py](Calculadora/calculadora_main.py) — punto de entrada
  - [Calculadora/funciones_principales.py](Calculadora/funciones_principales.py) — utilidades como [`operacionDosNumeros`](Calculadora/funciones_principales.py) y [`agregarElementosColaMax10`](Calculadora/funciones_principales.py)
 
  <img width="640" height="264" alt="image" src="https://github.com/user-attachments/assets/d38d6c58-4a45-4cd3-b05e-450955268ced" />

- FastAPI_API/ — API demo con autenticación básica y JWT
  - [FastAPI_API/main.py](FastAPI_API/main.py) — aplicación FastAPI (app)
  - Rutas:
    - [FastAPI_API/routers/users.py](FastAPI_API/routers/users.py) — endpoints de usuarios (p. ej. [`users`](FastAPI_API/routers/users.py))
    - [FastAPI_API/routers/basic_auth_users.py](FastAPI_API/routers/basic_auth_users.py) — auth básica (login endpoint: [`login`](FastAPI_API/routers/basic_auth_users.py))
    - [FastAPI_API/routers/jwt_auth_users.py](FastAPI_API/routers/jwt_auth_users.py) — auth JWT (login endpoint: [`login`](FastAPI_API/routers/jwt_auth_users.py))
    - [FastAPI_API/routers/products.py](FastAPI_API/routers/products.py)
- Gestor_de_Estudiantes_CSV_Pandas/ — gestor CSV con pandas (consola)
  - [Gestor_de_Estudiantes_CSV_Pandas/menu_main.py](Gestor_de_Estudiantes_CSV_Pandas/menu_main.py) — UI de consola
  - [Gestor_de_Estudiantes_CSV_Pandas/logica.py](Gestor_de_Estudiantes_CSV_Pandas/logica.py) — funciones principales como [`ingresarArchivo`](Gestor_de_Estudiantes_CSV_Pandas/logica.py), [`agregarEstudiante`](Gestor_de_Estudiantes_CSV_Pandas/logica.py), [`BuscarFilaPorNombre`](Gestor_de_Estudiantes_CSV_Pandas/logica.py)
  - [Gestor_de_Estudiantes_CSV_Pandas/manejo_de_CSV.py](Gestor_de_Estudiantes_CSV_Pandas/manejo_de_CSV.py) — I/O CSV (ej.: [`leerArchivo`](Gestor_de_Estudiantes_CSV_Pandas/manejo_de_CSV.py))
  - [Gestor_de_Estudiantes_CSV_Pandas/datos.csv](Gestor_de_Estudiantes_CSV_Pandas/datos.csv) — ejemplo de datos
  - [Gestor_de_Estudiantes_CSV_Pandas/instrucciones.txt](Gestor_de_Estudiantes_CSV_Pandas/instrucciones.txt)
  - [Gestor_de_Estudiantes_CSV_Pandas/variables_globales.py](Gestor_de_Estudiantes_CSV_Pandas/variables_globales.py)
 
    <img width="581" height="382" alt="image" src="https://github.com/user-attachments/assets/5c7690e5-3642-4b64-8d3e-e68bed19df0d" />

- Juego_de_Rol_POO_GUI/ — GUI Tkinter para crear personajes (POO)
  - UI:
    - [Juego_de_Rol_POO_GUI/Presentacion/gui_app.py](Juego_de_Rol_POO_GUI/Presentacion/gui_app.py) — app principal
    - [Juego_de_Rol_POO_GUI/Presentacion/frame_personajes.py](Juego_de_Rol_POO_GUI/Presentacion/frame_personajes.py)
    - [Juego_de_Rol_POO_GUI/Presentacion/frame_acciones.py](Juego_de_Rol_POO_GUI/Presentacion/frame_acciones.py)
    - [Juego_de_Rol_POO_GUI/Presentacion/frame_log.py](Juego_de_Rol_POO_GUI/Presentacion/frame_log.py)
  - Lógica:
    - [Juego_de_Rol_POO_GUI/Logica/personaje.py](Juego_de_Rol_POO_GUI/Logica/personaje.py)
    - [Juego_de_Rol_POO_GUI/Logica/mago.py](Juego_de_Rol_POO_GUI/Logica/mago.py) — clase `Mago`
    - [Juego_de_Rol_POO_GUI/Logica/clerigo.py](Juego_de_Rol_POO_GUI/Logica/clerigo.py) — clase `Clerigo`
    - [Juego_de_Rol_POO_GUI/Logica/hechizo.py](Juego_de_Rol_POO_GUI/Logica/hechizo.py) — clase `Hechizo`
    - [Juego_de_Rol_POO_GUI/Logica/raza.py](Juego_de_Rol_POO_GUI/Logica/raza.py) — enum `Raza`
    - [Juego_de_Rol_POO_GUI/Logica/Manejador_de_Exceptions.py](Juego_de_Rol_POO_GUI/Logica/Manejador_de_Exceptions.py) — `PuntosDeVidaException`
   
      <img width="1280" height="751" alt="image" src="https://github.com/user-attachments/assets/6c8c34d2-b214-47ee-9308-ff25d95606df" />


---

## Cómo ejecutar cada mini-proyecto

1. Calculadora (consola)
   - Requisitos: Python 3.x
   - Ejecutar:
     ```sh
     python Calculadora/calculadora_main.py
     ```
   - Entradas/funciones principales: [`operacionDosNumeros`](Calculadora/funciones_principales.py)

2. Gestor de Estudiantes (CSV + pandas)
   - Requisitos: Python 3.x, pandas
   - Instalar:
     ```sh
     pip install pandas
     ```
   - Ejecutar:
     ```sh
     python Gestor_de_Estudiantes_CSV_Pandas/menu_main.py
     ```
   - Funciones clave: [`ingresarArchivo`](Gestor_de_Estudiantes_CSV_Pandas/logica.py), [`agregarEstudiante`](Gestor_de_Estudiantes_CSV_Pandas/logica.py), [`leerArchivo`](Gestor_de_Estudiantes_CSV_Pandas/manejo_de_CSV.py)

3. FastAPI (API demo)
   - Requisitos: Python 3.x, FastAPI, uvicorn, python-multipart, python-jose, passlib
   - Instalar:
     ```sh
     pip install fastapi uvicorn python-multipart python-jose passlib[bcrypt]
     ```
   - Ejecutar (desde la raíz del repo):
     ```sh
     uvicorn FastAPI_API.main:app --reload --port 8000
     ```
   - Punto de entrada: [FastAPI_API/main.py](FastAPI_API/main.py) — función [`read_root`](FastAPI_API/main.py)
   - Rutas y autenticaciones en:
     - [FastAPI_API/routers/users.py](FastAPI_API/routers/users.py)
     - [FastAPI_API/routers/basic_auth_users.py](FastAPI_API/routers/basic_auth_users.py)
     - [FastAPI_API/routers/jwt_auth_users.py](FastAPI_API/routers/jwt_auth_users.py)

4. Juego de Rol (GUI Tkinter)
   - Requisitos: Python 3.x, Pillow
   - Instalar:
     ```sh
     pip install pillow
     ```
   - Ejecutar:
     ```sh
     python Juego_de_Rol_POO_GUI/Presentacion/main.py
     ```
   - Puntos importantes: la UI carga sprites desde la carpeta `Presentacion/assets` (referenciado en [frame_personajes.py](Juego_de_Rol_POO_GUI/Presentacion/frame_personajes.py)). Clases principales: [`Mago`](Juego_de_Rol_POO_GUI/Logica/mago.py), [`Clerigo`](Juego_de_Rol_POO_GUI/Logica/clerigo.py), [`Hechizo`](Juego_de_Rol_POO_GUI/Logica/hechizo.py)

---

## Dependencias sugeridas
- fastapi, uvicorn, python-multipart, python-jose, passlib[bcrypt]
- pandas
- pillow

---

## Notas y recomendaciones
- Algunos scripts usan rutas relativas fijas (por ejemplo la lectura de instrucciones en [Gestor_de_Estudiantes_CSV_Pandas/logica.py](Gestor_de_Estudiantes_CSV_Pandas/logica.py)). Ejecuta desde la raíz del repositorio o ajusta las rutas si es necesario.
- El GUI espera imágenes en `Presentacion/assets` (ver [frame_personajes.py](Juego_de_Rol_POO_GUI/Presentacion/frame_personajes.py)). Añade los sprites si quieres ver las imágenes.
- Los endpoints de la API usan datos en memoria (listas/diccionarios) — son demos, no producción.
