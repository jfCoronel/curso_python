__Curso Python (Iniciación a Python para Ingenieros)__

_© Juan F. Coronel Toro, 2026_

## Marimo notebooks

Marimo notebooks son un nuevo tipo de cuaderno que viene a sustituir y mejorar a los cuadernos Jupyter. Se caracterizan por ejecutarse como scripts de Python puro y permiten crear aplicaciones interactivas web. 

Características principales:

- Ejecución reactiva: Al cambiar una variable o celda, marimo actualiza automáticamente todas las celdas dependientes, garantizando la consistencia.
- Archivos Python puros: A diferencia de los archivos .ipynb de Jupyter, los cuadernos marimo son archivos .py estándar.
- Modo App: Permite convertir el cuaderno en una aplicación web interactiva sin necesidad de código adicional.
- Interactividad integrada: Incluye elementos de interfaz de usuario como controles deslizantes (sliders), menús desplegables y tablas interactivas. 

Podemos instalar marimo como un paquete más en cada uno de nuestros proyectos, pero si lo vamos a utilizar mucho podemos instalarlo en un entorno global usando uv.

```
uv tool install marimo
```

Para comprobar que tenemos instalado marimo correctamente podemos escribir en el terminal:

```
marimo --version
```
 
Para editar un archivo (nuevo o existente) usaremos:

```
marimo edit --sandbox --watch prueba_marimo.py
```

Entonces arrancará el editor de marimo usando nuestro explorador preferido.

La opción --sandbox es para que el monte un entorno virtual en memoria y instale los paquetes que sean necesarios.

La opción --watch permite poder modificar el archivo simultaneamente desde VS Code usando una IA y que recargue automaticamente los cambios que hagamos.

Si queremos correr el archivo en forma de página web usaremos:

```
marimo run prueba_marimo.py
```


