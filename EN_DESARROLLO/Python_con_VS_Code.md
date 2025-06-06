__Curso Python (Iniciación a Python para Ingenieros)__

_© Juan F. Coronel Toro, 2025_

## 3. Manejo de Python Visual Studio Code

Visual Studio Code (VS Code) es un editor de código fuente gratuito, de código abierto y multiplataforma desarrollado por Microsoft. Es una herramienta muy popular entre desarrolladores, que se utiliza para escribir, editar y depurar código en diversos lenguajes de programación. 

__Instalación de VS Code__

Para instalar VS Code lo descargamos e instalamos desde su página web:

https://code.visualstudio.com/

__Instalación de Python__

Para instalar un interprete de Python lo descargamos e instalamos desde su página web:

https://python.org/

Esto nos instalará una versión de Python "limpia" sin ningún paquete externo.

__Configuración de VS Code para Python__

Para poder usar VS Code con Python es necesario instlarle una extensión de Python desarrollada por microsoft.

Si queremos usar jupyter notebooks en VS Code, cuando abrimos uno y lo intentamos ejecutar, nos instalará algunas extensiones más para VS Code y algunos paquetes que necesita para poder correr jupyter.

__Ejemplo inicial de archivo Python__

Vamos a crear un primer archivo de pruebas para ver las capacidades de VS Code como entorno de desarrollo en Python. LLamaremos al archivo "pruebas.py" y copiamos en el el siguiente código:

```python

import numpy as np
import matplotlib.pyplot as plt

# Ejemplo de gráfica
x = np.array([1, 2.5, 5, 10])
y = np.random.rand(4)
plt.figure()
plt.plot(x,y, label='y (x)')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Figura de ejemplo')
plt.xlim([0, 11])
plt.ylim([0, 1])
plt.grid()
plt.show()

```

Para que este código funciones debemos instalar a través de la terminal los paquetes numpy y matplotlib. Para ello escribimos en el terminal:

```
pip install numpy
pip install matplotlib
```

Ahora ya podemos ejecutar o depurar (debug) el archivo de python con VS Code.



