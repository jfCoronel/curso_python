__Curso Python (Iniciación a Python para Ingenieros)__

_© Juan F. Coronel Toro, 2026_

## Configuración de python local

Para poder utilizar python en nuestra máquina, podemos hacerlo de múltiples formas diferentes, nosotros vamos a instalar tres componentes:

- uv: Es un gestor de paquetes y proyectos para Python extremadamente rápido, escrito en Rust y desarrollado por [Astral](https://astral.sh/). Actúa como un sustituto moderno y directo de `pip`, `pip-tools`, `virtualenv` y `poetry`, ofreciendo una velocidad 10-100 veces mayor para instalar dependencias, resolver conflictos y gestionar entornos virtuales.
- python: Instalaremos y gestionaremos las diferentes versiones de python a traves de uv.
- IDE (Integrated Development Environment): Es una aplicación de software que combina herramientas esenciales —editor de código, depurador, extensiones, etc.— en una sola interfaz gráfica. Existen muchos IDEs para desarrollar en Python, nosotros usaremos Visual Studio Code (VS Code) de Microsoft.

__Instalación de uv__

Para instalar el programa uv lo instalamos siguiendo las instrucciones de su página web, según cual sea nuestro sistema operativo:

https://docs.astral.sh/uv/

Esto nos instalará la última versión de uv en nuestra máquina, para comprobar que se a instalado correctamente cerramos y volvemos a abrir una terminal y escribimos:

```
uv --version
```

uv nos servirá para gestionar las versiones de python que tenemos instaladas, para ver las lista de versiones de python en nuestro ordenador escribimos en la terminal:

```
uv python list
```

Para instalar la última version estable de python escribimos:

```
uv python install
```

Esto nos instalará una versión de Python "limpia" sin ningún paquete externo. Para mostrar la lista de paquetes externos instalados globalmente en python escribimos:

```
uv pip list
```

Si instalamos los paquetes globalmente podrán usarse desde todas los archivos de python que tengamos pero el muy probable que se generen conflictos entre diferentes proyectos que quieran usar versiones diferentes de paquetes. Por lo tanto recomendamos instalar los paquetes para cada uno de los proyectos que tengamos, utilizando lo que se llama "entornos virtuales" (virtual environments).

Una vez tengamos instalado uv y python ya podemos ejecutar archivos python, a modo de ejemplo vamos a crear un archivo llamado "saludar.py" y con cualquier editor de texto (por ejemplo el block de notas), escribimos dentro:

```python
print("Hola, mundo!")

```

Ahora abrimos una ventana de terminal en la misma carpeta donde está en archivo "saludar.py" y ejecutamos:

```
uv run saludar.py
```



__Instalación de VS Code__

Para instalar VS Code lo descargamos e instalamos desde su página web, para windows instalar la version System, mejor que User:

https://code.visualstudio.com/

Visual Studio Code, al que conocemos también como VSCode, es un editor de código para programadores gratuito, de código abierto y multiplataforma, desarrollado por Microsoft. Este programa puede usarse para programar en multiples lenguajes, para utilizarlo para cada uno de los lenguajes es necesario configurarlo instalandole las extensiones adecuadas.

__Configuración de VS Code para Python__

Para poder usar VS Code con Python y cuadernos de jupyter es necesario instalar algunas extensiones a VS Code. Extensiones a instalar:

- Python (Microsoft)
-  Jupyter (Microsoft)

Si hacemos esto nos pedirá varios permisos para instalar extensiones y finalmente tendremos 8 o 9 extensiones instaladas en VS code.

__Creación de proyectos y entornos virtuales Python__

Es muy recomendable encapsular cada uno de los proyectos que tengamos en una carpeta dedicada a ese proyecto y configurar un entorno virtual dedicado en esa carpeta. Un entorno virtual en Python es un directorio o carpeta aislada donde se puede elegir una versión específica de Python que queremos usar e instalar un conjunto de paquetes que sólo serán válidos para ese directrorio.

Supongamos que hemos creado una carpeta llamada "curso_python_p1", y la abrimos con VSCode, a continuación abrimos un terminal (VSCode incluye un terminal integrado) y ejecutamos lo siguiente:

```
uv init
uv sync
```

La primera orden iniciara un proyecto creando los archivos "README.md", "main.py", "pyproyect.toml" y ".python-version". Y la segunda orden crea la carpeta del directorio virtual ".venv" y un archivo llamado"uv.lock".

Puede que para conseguir que powerhell (Windows) de un error de permisos en la activación de entornos virtuales (.venv), en ese caso podemos ejecutar el siguiente comando en el powershell:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Si abrimos el archivo "main.py" veremos que contiene lo siguiente:

```python
def main():
    print("Hello from curso-python-p1!")

if __name__ == '__main__':
    main()
```

La sentencia `if __name__ == '__main__':` en Python se utiliza para definir qué código se ejecutará cuando un archivo se ejecuta directamente como un programa principal, en lugar de ser importado como un módulo. 

_¿Cómo funciona?:_

`__name__` es una variable especial en Python que indica cómo se está ejecutando el archivo. `"__main__"` es el valor de `__name__` cuando el archivo se ejecuta directamente como el programa principal. Si el módulo fuera importado desde otro archivo la variable `__name__` contendría el nombre del módulo.

Vamos a hacer un ejemplo que incluya otro módulo (archivo de python) que incluimos desde el archivo principal "main.py"

_archivo funciones.py:_

```python
def potencia(base, exponente = 2, imprimir=False):
    valor = base ** exponente
    if (imprimir):
    	print(f"{base}^{exponente}= {valor}")
    return valor
```

Cambiamos también el "main.py" a:

```python
import funciones as fn

if __name__ == "__main__":
    print (fn.potencia(3,5))
    fn.potencia(3,4,True)
  
```

__Ejemplo con importación de paquetes__

Vamos a cambiar el archivo "main.py" por el siguiente código:

```python
import numpy as np
import matplotlib.pyplot as plt

def grafica():
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

if __name__ == '__main__':
    grafica()
```

Para que este código funciones debemos instalar los paquetes numpy y matplotlib, que instalaremos unicamente en nuestro entorno virtual.

Los instalaremos usando la terminal:

```
uv add numpy, matplotlib
```

Ahora ya podemos ejecutar o depurar (debug) el archivo de python con VS Code.
