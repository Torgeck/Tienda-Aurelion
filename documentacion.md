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


### Estadisticas descriptivas 

Estadísticas descriptivas para clientes:

Información general:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   id_cliente      100 non-null    int64         
 1   nombre_cliente  100 non-null    object        
 2   email           100 non-null    object        
 3   ciudad          100 non-null    object        
 4   fecha_alta      100 non-null    datetime64[ns]
dtypes: datetime64[ns](1), int64(1), object(3)
memory usage: 4.0+ KB
None

Estadísticas numéricas:
       id_cliente           fecha_alta
count  100.000000                  100
mean    50.500000  2023-02-19 12:00:00
min      1.000000  2023-01-01 00:00:00
25%     25.750000  2023-01-25 18:00:00
50%     50.500000  2023-02-19 12:00:00
75%     75.250000  2023-03-16 06:00:00
max    100.000000  2023-04-10 00:00:00
std     29.011492                  NaN

Valores nulos por columna:
id_cliente        0
nombre_cliente    0
email             0
ciudad            0
fecha_alta        0
dtype: int64

Primeras filas del dataset:
   id_cliente   nombre_cliente                     email      ciudad  \
0           1    MARIANA LOPEZ    MARIANA.LOPEZ@MAIL.COM  CARLOS PAZ   
1           2    NICOLAS ROJAS    NICOLAS.ROJAS@MAIL.COM  CARLOS PAZ   
2           3  HERNAN MARTINEZ  HERNAN.MARTINEZ@MAIL.COM  RIO CUARTO   
3           4     UMA MARTINEZ     UMA.MARTINEZ@MAIL.COM  CARLOS PAZ   
4           5  AGUSTINA FLORES  AGUSTINA.FLORES@MAIL.COM     CORDOBA   

  fecha_alta  
0 2023-01-01  
1 2023-01-02  
2 2023-01-03  
3 2023-01-04  
4 2023-01-05  

==================================================

Estadísticas descriptivas para detalle_ventas:

Información general:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 343 entries, 0 to 342
Data columns (total 6 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   id_venta         343 non-null    int64 
 1   id_producto      343 non-null    int64 
 2   nombre_producto  343 non-null    object
 3   cantidad         343 non-null    int64 
 4   precio_unitario  343 non-null    int64 
 5   importe          343 non-null    int64 
dtypes: int64(5), object(1)
memory usage: 16.2+ KB
None

Estadísticas numéricas:
         id_venta  id_producto    cantidad  precio_unitario       importe
count  343.000000   343.000000  343.000000       343.000000    343.000000
mean    61.492711    49.139942    2.962099      2654.495627   7730.078717
std     34.835525    29.135461    1.366375      1308.694720   5265.543077
min      1.000000     1.000000    1.000000       272.000000    272.000000
25%     31.000000    23.000000    2.000000      1618.500000   3489.000000
50%     61.000000    47.000000    3.000000      2512.000000   6702.000000
75%     93.000000    76.000000    4.000000      3876.000000  10231.500000
max    120.000000   100.000000    5.000000      4982.000000  24865.000000

Valores nulos por columna:
id_venta           0
id_producto        0
nombre_producto    0
cantidad           0
precio_unitario    0
importe            0
dtype: int64

Primeras filas del dataset:
   id_venta  id_producto        nombre_producto  cantidad  precio_unitario  \
0         1           90    TOALLAS HÚMEDAS X50         1             2902   
1         2           82  ACEITUNAS NEGRAS 200G         5             2394   
2         2           39     HELADO VAINILLA 1L         5              469   
3         2           70           FERNET 750ML         2             4061   
4         2           22  MEDIALUNAS DE MANTECA         1             2069   

   importe  
0     2902  
1    11970  
2     2345  
3     8122  
4     2069  

==================================================

Estadísticas descriptivas para productos:

Información general:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 4 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   id_producto      100 non-null    int64 
 1   nombre_producto  100 non-null    object
 2   categoria        100 non-null    object
 3   precio_unitario  100 non-null    int64 
dtypes: int64(2), object(2)
memory usage: 3.3+ KB
None

Estadísticas numéricas:
       id_producto  precio_unitario
count   100.000000       100.000000
mean     50.500000      2718.550000
std      29.011492      1381.635324
min       1.000000       272.000000
25%      25.750000      1590.000000
50%      50.500000      2516.000000
75%      75.250000      4026.500000
max     100.000000      4982.000000

Valores nulos por columna:
id_producto        0
nombre_producto    0
categoria          0
precio_unitario    0
dtype: int64

Primeras filas del dataset:
   id_producto     nombre_producto  categoria  precio_unitario
0            1      COCA COLA 1.5L  ALIMENTOS             2347
1            2          PEPSI 1.5L  ALIMENTOS             4973
2            3         SPRITE 1.5L  ALIMENTOS             4964
3            4  FANTA NARANJA 1.5L  ALIMENTOS             2033
4            5  AGUA MINERAL 500ML  ALIMENTOS             4777

==================================================

Estadísticas descriptivas para ventas:

Información general:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 120 entries, 0 to 119
Data columns (total 6 columns):
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   id_venta        120 non-null    int64         
 1   fecha           120 non-null    datetime64[ns]
 2   id_cliente      120 non-null    int64         
 3   nombre_cliente  120 non-null    object        
 4   email           120 non-null    object        
 5   medio_pago      120 non-null    object        
dtypes: datetime64[ns](1), int64(2), object(3)
memory usage: 5.8+ KB
None

Estadísticas numéricas:
         id_venta                fecha  id_cliente
count  120.000000                  120  120.000000
mean    60.500000  2024-03-29 17:36:00   47.291667
min      1.000000  2024-01-02 00:00:00    1.000000
25%     30.750000  2024-02-11 06:00:00   24.500000
50%     60.500000  2024-03-25 00:00:00   48.500000
75%     90.250000  2024-05-19 06:00:00   67.500000
max    120.000000  2024-06-28 00:00:00  100.000000
std     34.785054                  NaN   27.854181

Valores nulos por columna:
id_venta          0
fecha             0
id_cliente        0
nombre_cliente    0
email             0
medio_pago        0
dtype: int64

Primeras filas del dataset:
   id_venta      fecha  id_cliente    nombre_cliente  \
0         1 2024-06-19          62  GUADALUPE ROMERO   
1         2 2024-03-17          49      OLIVIA GOMEZ   
2         3 2024-01-13          20      TOMAS ACOSTA   
3         4 2024-02-27          36    MARTINA MOLINA   
4         5 2024-06-11          56        BRUNO DIAZ   

                       email     medio_pago  
0  GUADALUPE.ROMERO@MAIL.COM        TARJETA  
1      OLIVIA.GOMEZ@MAIL.COM             QR  
2      TOMAS.ACOSTA@MAIL.COM        TARJETA  
3    MARTINA.MOLINA@MAIL.COM  TRANSFERENCIA  
4        BRUNO.DIAZ@MAIL.COM        TARJETA  

==================================================


## Codigo Utilizado 
```python
name_list = ["clientes", "detalle_ventas", "productos", "ventas"]

for i, tabla in enumerate(df_list):
    print(f"\nEstadísticas descriptivas para {name_list[i]}:")
    print("\nInformación general:")
    print(tabla.info())

    print("\nEstadísticas numéricas:")
    print(tabla.describe())
    
    print("\nValores nulos por columna:")
    print(tabla.isnull().sum())

    # Mostrar primeras filas
    print("\nPrimeras filas del dataset:")
    print(tabla.head())

    print("\n" + "="*50)
```




### Análisis de Correlaciones

## Descripción
Este análisis examina las relaciones entre diferentes variables numéricas en nuestro conjunto de datos, ayudando a identificar patrones y dependencias importantes.

## Variables Analizadas
1. **Ventas y Cantidades**
   - Correlación entre precio unitario y cantidad vendida
   - Impacto del precio en el volumen de ventas

2. **Patrones Temporales**
   - Correlaciones con fechas y estacionalidad
   - Tendencias de ventas por período

3. **Categorías y Precios**
   - Relación entre categorías y precios unitarios
   - Variación de precios por tipo de producto

## Interpretación de Resultados
- Coeficientes positivos indican relaciones directas
- Coeficientes negativos indican relaciones inversas
- Valores cercanos a 0 indican baja correlación
- Valores cercanos a 1 o -1 indican correlación fuerte

## Visualizaciones
El análisis incluye:
- Matrices de correlación con mapa de calor



## Código Implementado
```python

```