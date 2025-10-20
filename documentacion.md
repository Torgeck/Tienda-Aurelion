# Tienda Aurelion

## Tema

Tienda Aurelion es una cadena de mercado con varias sedes a lo largo de Córdoba. Dentro de su catalogo ofrece bienes de consumo tales como alimentos varios y artículos de limpieza.

## Problema

La Tienda Aurelion no tiene implementado un sistema que permita saber de forma automática cuales son los productos mas vendidos
y cuales presentan una baja rotación. Esta falta de información dificulta la toma de decisiones respecto a la gestión del stock y
la implementación de estrategias de descuento/promociones.
Como consecuencia, algunos productos permanecen en inventario durante largos periodos (generando costos de almacenamiento), mientras
que otros se agotan rápidamente sin aprovechar su potencial comercial. Todo esto se traduce como perdida para la tienda.

## Solución

Se propone desarrollar una herramienta de análisis en **Python**, usando librerías como **pandas, numpy y matplotlib,** que permitirá determinar
los **productos mas y menos vendidos** a partir de los registros de las bases de datos **productos.xlsx, ventas.xls, y detalles_ventas.xlsx**.

Con esta información, el sistema sugerirá aplicar un descuento (determinado por el usuario) sobre el grupo de productos de baja rotación para
incentivar la venta de los mismos.

Este análisis permitirá a la Tienda Aurelion:

- Optimizar la gestión del stock de productos
- Aumentar las ventas de productos con bajo movimiento
- Mejorar la rentabilidad mediante estrategias de precios basados en datos reales

Ademas, los resultados podrán visualizarse en gráficos comparativos que faciliten la interpretación de las tendencias de ventas y promuevan
una toma de decisiones comerciales mas informada.

## Dataset de referencia: fuente, definición, estructura, tipos y escala de medición

## Datos Requeridos

Los datos fueron provistos por los dueños de la tienda Aurelion

### Definición

Base que representa una Tienda, con catálogo de productos, registro de clientes, detalles de ventas y ventas.

### Productos — ~100 filas

| Campo           | Tipo | Escala  |
| --------------- | ---- | ------- |
| id_producto     | int  | Nominal |
| nombre_producto | str  | Nominal |
| precio_unitario | str  | Razón   |

### Clientes — ~100 filas

| Campo          | Tipo | Escala    |
| -------------- | ---- | --------- |
| id_cliente     | int  | Nominal   |
| nombre_cliente | str  | Nominal   |
| email          | str  | Nominal   |
| ciudad         | str  | Nominal   |
| fecha_alta     | date | Intervalo |

### Ventas — ~120 filas

| Campo          | Tipo | Escala    |
| -------------- | ---- | --------- |
| id_venta       | int  | Nominal   |
| fecha          | date | Intervalo |
| id_cliente     | int  | Nominal   |
| nombre_cliente | str  | Nominal   |
| email          | str  | Nominal   |
| medio_pago     | str  | Nominal   |

### Detalles de Ventas — ~350 filas

| Campo           | Tipo | Escala  |
| --------------- | ---- | ------- |
| id_venta        | int  | Nominal |
| id_producto     | int  | Nominal |
| nombre_producto | str  | Nominal |
| cantidad        | int  | Razón   |
| precio_unitario | int  | Razón   |
| importe         | int  | Razón   |

## Información, pasos, pseudocodigo y diagrama del programa (Sprint 1)

### Información

En esta etapa, el programa funciona como un visor interactivo de la documentación, para
que el usuario obtenga rápidamente la información clave del proyecto desde la terminal.

### Contenido accesible desde el menú

Mostrar tema, problema y solución
Mostrar pseudocodigo
Mostrar información de los datasets
Mostrar sugerencia de copilot

### Pasos

    1. Definir rutas de archivos para mostrar por consola
    2. Definir función parar leer y mostrar por pantalla los archivos según una ruta pasada por parámetro
    3. Iniciar bucle de menú
       1. Mostrar diferentes opciones
       2. Leer opción ingresada por el usuario y ejecutar la acción correspondiente

### Pseudocodigo

INICIO
Definir rutas:
path_problema, path_pseudocodigo, path_datasets, path_sugerencias

    Definir funcion:
        leer_mostrar_archivo(ruta):
            intentar abrir archivo en 'ruta' con UTF-8
            SI existe
                leer y mostrar contenido
            SI no existe: informar archivo no encontrado
                capturar e informar otros errores
        FIN leer_mostrar_archivo

    salir = False
    MIENTRAS salir == False
        mostrar menu por consola:
            1 - Mostrar tema, problema y solución
            2 - Mostrar pseudocódigo
            3 - Mostrar datasets utilizados (5 primeras filas)
            4 - Sugerencias y mejoras con Copilot
            5 - Salir
        leer opción

        validar opción:
            SI opción == "1":
                leer_mostrar_archivo(path_problema)

            SI opción == "2":
                leer_mostrar_archivo(path_pseudocodigo)

            SI opción == "3":
                leer_mostrar_archivo(path_datasets)

            SI opción == "4":
                leer_mostrar_archivo(path_sugerencias)

            SI opción == "5":
                salir = True
            SINO
                mostrar "Opción no válida"
        FIN MIENTRAS

FIN

### Sugerencias y mejoras de Copilot

#### Aceptadas
- Modularicé el script envolviendo el menú en una función main() y añadiendo el guard if __name__ == '__main__'.
- Reemplacé rutas string por pathlib.Path para mayor portabilidad.
- Mejoré la función leer_mostrar_archivo para aceptar Path, comprobar existencia y capturar excepciones de forma clara.
- Normalicé la lectura de la entrada con .strip() y capturé KeyboardInterrupt para salida limpia.

#### Mejoras priorizadas no aplicadas
- Añadir manejo y visualización de datasets reales (pandas).
- Manejo detallado de errores y logs en vez de prints.
- Internacionalización y codificación de mensajes (si se espera usar distintos locales).
- Validación de entradas y menú más tolerante
- Implementar tests de integración para lectura de archivos largos (performance)
- Convertir rutas a partir de BASE_DIR = Path(__file__).parent para robustez cuando se ejecuta desde otro directorio.
- Añadir tests con pytest (crear tests/test_proyecto.py) y correrlos.