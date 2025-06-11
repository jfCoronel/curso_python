__Curso Python (Iniciación a Python para Ingenieros)__

_© Juan F. Coronel Toro, 2025_

## 4. Desarrollo de aplicaciones web con Python (Streamlit)

Existen muchos paquetes orientados al desarrollo de aplicaciones web usando Python.

El paquete _Streamlit_ es una de las opciones más sencillas para desarrollar aplicaciones web usando exclusivamente código Python.

__Instalación de Streamlit__

Instalamos en nuestro entorno virtual "streamlit"

vamos a crear un archivo llamado "prueba_streamlit.py" con el siguiente código:

```python

import streamlit as st

st.write("Probando Streamlit !!")
```

para poder mostrar el archivo en el explorador debemos abrir un terminal (dentro del propio VS Code) y ejecutar:

```
streamlit run prueba_streamlit.py
```
### 4.1. Principales funciones de Streamlit

La mejor forma de aprender las diferentes funciones que incluye la librería es con la hoja resumen que podemos encontrar en la documentación.

[Streamlit cheat sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)

_Flujo de ejcución:_

Streamlit ejecuta todo el código en el arranque y cada vez que uno de los valores obtenidos por pantalla cambien se vuelve a ejecutar el código entero.

### 4.2. Ejemplo de aplicación a desarrollar

Vamos desarrollar un visor de datos meteorlógicos por día.

La aplicación debe cargar un dataframe con los datos del archivo "sevilla_met.csv", pedir al usuario el mes y el día que debe mostra, filtrar el dataframe y mostrarlo para ese día y mes.

Añadir tambíen una gráfica con líneas que muestre una variable previamente seleccionada para el día elegido.


