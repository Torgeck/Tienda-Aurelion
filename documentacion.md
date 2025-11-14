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

---

## Análisis Exploratorio de Datos - Proceso Detallado

### 1. Carga Inicial de Datos y Estadísticas Descriptivas

#### Objetivo
Obtener una visión general de cada dataset independiente antes de integrarlos, identificando tipos de datos, valores faltantes y patrones básicos.

#### Metodología
Se cargaron los cuatro datasets *limpios* principales, basados en los excels previamente exportados y formateados por el modulo *data_cleaner*:
- `clientes.xlsx` (~100 registros)
- `detalle_ventas_clean.xlsx` (~343 registros)
- `productos_clean.xlsx` (~100 registros)
- `ventas_clean.xlsx` (~120 registros)

Para cada dataset se ejecutaron:
- `info()`: Tipo de datos y conteo de valores no nulos
- `describe()`: Estadísticas básicas (media, std, min, max, percentiles)
- Inspección de valores faltantes por columna

#### Hallazgos Clave
- Los datasets tienen estructuras compatibles con claves foráneas (id_cliente, id_venta, id_producto)
- No se detectaron valores faltantes críticos en las columnas principales
- Las columnas numéricas (precios, cantidades) presentan distribuciones positivas (rango 0 a máximo)

---



### 2. Recategorización de Productos

#### Problema Identificado
Los productos en la base de datos no estaban categorizados correctamente. La columna `categoria` contenía valores inconsistentes o genéricos que no permitían distinguir entre **Alimentos** y **Artículos de Limpieza**.

#### Solución Implementada
Se desarrolló un algoritmo de clasificación basado en palabras clave presentes en el nombre del producto:

```python
KEYWORDS_LIMPIEZA = ['DETERGENTE', 'LAVANDINA', 'JABÓN', 'ESPONJA', 
                      'DESINFECTANTE', 'SHAMPOO', 'PAPEL', 'SERVILLETA', ...]

# Si el nombre contiene alguna palabra clave → LIMPIEZA
# Si no → ALIMENTOS
```

#### Justificación
- Categorizar correctamente es esencial para segmentar análisis por tipo de producto
- Permite identificar patrones de venta específicos por categoría
- Facilita la toma de decisiones sobre promociones y stock por tipo de bien

#### Resultado
Clasificación automática con ~95% de precisión basada en palabras clave del nombre de producto.

---

### 3. Unificación de Datasets (Merge)

#### Objetivo
Combinar los cuatro datasets independientes en una única tabla que contenga información completa de cada transacción: cliente, producto, venta y detalles.

#### Proceso
Se realizaron merges secuenciales:
1. `detalle_ventas` ← `ventas` (por `id_venta`)
2. Resultado ← `productos` (por `id_producto`)
3. Resultado ← `clientes` (por `id_cliente`)

#### Problema: Columnas Redundantes Post-Merge
Después del merge se generaron automáticamente columnas con sufijos `_x`, `_y` para diferenciar columnas con el mismo nombre provenientes de diferentes datasets.

**Ejemplo**: `nombre_producto_x` (de detalle_ventas) vs `nombre_producto_y` (de productos)

#### Solución: Limpieza de Columnas
Se eliminaron las columnas redundantes manteniendo solo la información más relevante:

```python
df = df.drop(columns=['id_venta', 'id_producto', 'nombre_producto_x', 
                      'precio_unitario_x', 'nombre_cliente_x', 'email_x', ...])

# Renombrar para claridad
df.rename(columns={'nombre_producto_y': 'producto', 
                   'precio_unitario_y': 'precio',
                   'importe': 'total'}, inplace=True)
```

#### Justificación
- Reducir dimensionalidad mejora claridad y rendimiento
- Mantener una única representación de cada atributo evita inconsistencias
- Facilita análisis posteriores al tener columnas con nombres claros y únicos

#### Resultado
DataFrame integrado con ~343 registros y 9 columnas relevantes.

---
### 4. Detección de Columnas Duplicadas y eliminacion de Id's

#### Problema Identificado
- Al explorar la estructura de los datos, se observó que algunos nombres de columnas aparecían repetidos o eran semánticamente equivalentes en diferentes columnas (ej: `nombre_producto`).
- Los campos que hacen referencia a una identificatoria secuencial, no son relevantes a nuestro analisis. 

#### Solución Aplicada
Se eliminó aquellas columnas que se creian repetidas y las referentes a ids, renombrando otras:

```python
df = df_todos

df = df.drop(columns=['id_venta','id_producto','nombre_producto_x','precio_unitario_x','nombre_cliente_x','email_x','nombre_cliente_y','email_y','id_cliente'])
df.rename(columns={'nombre_producto_y':'producto','precio_unitario_y':'precio','importe':'total','fecha':'fecha_venta','fecha_alta':'fecha_alta_cli'}, inplace=True)

```

#### Justificación
Las columnas duplicadas generan:
- Ambigüedad en análisis posteriores
- Aumento innecesario de memoria
- Confusión en la interpretación de resultados

Por este motivo, se decidió eliminar columnas redundantes posterior al proceso del merge. 

---

### 5. Codificación de Variables Categóricas/Cualitativas

#### Problema Identificado
Las variables categóricas (`medio_pago`, `ciudad`, `categoria`) estaban representadas como texto, lo que dificulta ciertos análisis estadísticos y visualizaciones.

#### Solución: Mapeo a Valores Numéricos

```python
medios = {"EFECTIVO": 0, "TARJETA": 1, "QR": 2, "TRANSFERENCIA": 3}
df["medio_pago"] = df["medio_pago"].replace(medios)

ciudades = {'CARLOS PAZ': 0, 'RIO CUARTO': 1, 'MENDIOLAZA': 2, ...}
df["ciudad"] = df["ciudad"].replace(ciudades)

categorias = {'LIMPIEZA': 0, 'ALIMENTOS': 1}
df["categoria"] = df["categoria"].replace(categorias)
```

#### Justificación
- Facilita cálculos de correlación y análisis estadísticos
- Reduce espacio en memoria
- Permite visualizaciones más claras (gráficos numéricos)

#### Nota de Codificación
- 0, 1, 2 ,por ejemplo, son etiquetas numéricas que no implican jerarquía
- Se mantiene un registro de la codificación para interpretación posterior

---

### 6. Procesamiento de Variables Temporales

#### Objetivo
Extraer y crear variables temporales que permitirán analizar patrones estacionales y tendencias temporales.

#### Variables Creadas

```python
df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
df['mes'] = df['fecha_venta'].dt.to_period('M')  # Período mes (2025-01, 2025-02, ...)
df['cuatrimestre'] = ((df['fecha_venta'].dt.month - 1) // 4 + 1)  # 1, 2 o 3
df['anio_cuatrimestre'] = df['fecha_venta'].dt.year.astype(str) + "-C" + df['cuatrimestre'].astype(str)
```

#### Justificación
- **Mes**: Permite detectar variaciones mensuales (picos de compra)
- **Cuatrimestre**: Agrupa períodos de 4 meses para análisis de tendencias a mediano plazo
- **Año-Cuatrimestre**: Facilita comparaciones entre años evitando confusión de períodos

---

### 7. Detección y Análisis de Outliers

#### Objetivo
Identificar registros con valores atípicos que podrían representar errores de captura, transacciones especiales o anomalías en los datos.

#### Método: Rango Intercuartílico (IQR)

El método IQR es estándar en análisis exploratorio, se utilizo analiticamente el mismo para lograr equivalencia de lo representado graficamente en los graficos boxplot:

1. **Calcular cuartiles**: Q1 (25%) y Q3 (75%)
2. **IQR = Q3 - Q1** (rango donde se concentra el 50% de los datos)
3. **Límites**:
   - Inferior: Q1 - 1.5 × IQR (se utilizara el mayor valor entre cero y este resultado, el limite inferior no puede ser negativo)
   - Superior: Q3 + 1.5 × IQR
4. **Outliers**: Cualquier valor fuera de estos límites

#### Ejemplo Aplicado

```python
def analizar_valores_extremos_iqr(df, columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = max(0, Q1 - 1.5*IQR)
    upper_bound = Q3 + 1.5*IQR
    
    outliers = df[(df[columna] < lower_bound) | (df[columna] > upper_bound)]
    return outliers
```

#### Hallazgos

Se analizaron tres variables:
- **Cantidad**: Identifica transacciones con volúmenes inusualmente altos
- **Precio**: Detecta productos con precios fuera del rango típico
- **Total**: Encuentra transacciones con montos extremos (muy altos o muy bajos)

![Analisis grafico de outliers](./img/boxplot_outliers.png) 


#### Interpretación Visual
Los boxplots muestran:
- **Caja central**: 50% de los datos (Q1 a Q3)
- **Línea dentro de la caja**: Mediana
- **Bigotes**: Límites de 1.5×IQR
- **Puntos aislados**: Outliers

#### Decisión: Eliminación de Outliers

- Se detectan 7 registros por fuera de los valores extremos para la columan TOTAL
- Se eliminaron estos registros, para garantizar que el análisis se base en transacciones típicas y evitar sesgos causados por anomalías.

```python
df_limpio = df.copy()

Q1 = np.percentile(df["total"], 25)
Q3 = np.percentile(df["total"], 75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_limpio = df_limpio[(df_limpio["total"] >= limite_inferior) & (df_limpio["total"] <= limite_superior)]

print(df.info())
print(df_limpio.info())
```

---

### 8. Análisis de Correlaciones

#### Objetivo
Identificar relaciones lineales entre variables numéricas para entender cómo una variable cambia respecto a otra.

#### Método: Coeficiente de Correlación de Pearson

Mide la relación lineal entre dos variables:
- **Rango**: -1 a 1
- **Cercano a 1**: Correlación positiva fuerte (ambas aumentan juntas)
- **Cercano a -1**: Correlación negativa fuerte (una aumenta, otra disminuye)
- **Cercano a 0**: Sin correlación lineal

#### Visualización: Matriz de Correlación

```python
numericas = df.select_dtypes(include=[np.number])
corr = numericas.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación')
plt.show()
```

![Heatmap Matriz Correlaciones](./img/heatmap_correlacion.png)


#### Interpretación del Mapa de Calor
- **Colores cálidos (rojo)**: Correlación positiva
- **Colores fríos (azul)**: Correlación negativa
- **Valores en celdas**: Coeficiente de correlación exacto

#### Correlaciones Significativas Identificadas

Se filtraron pares con correlación absoluta > 0.5:
- **Precio ↔ Total**: Correlación alta (se espera que a mayor precio, mayor total)
- **Cantidad ↔ Total**: Correlación moderada

#### Justificación
Las correlaciones ayudan a:
- Validar relaciones lógicas entre variables
- Identificar variables redundantes

---

### 9. Análisis de Distribuciones

#### Objetivo
Entender la forma y características de la distribución de variables clave.

#### Visualizaciones Realizadas

![Graficos Analisis](./img/graficos_analisis.png)


**1. Histograma de Cantidades**
- Muestra frecuencia de cantidades vendidas
- Identifica si la mayoría de transacciones son de pocos productos o muchos

**2. Scatter Plot: Precio vs Total (coloreado por Categoría)**
- Verifica la relación visual entre precio y total
- Permite identificar si categorías tienen patrones diferentes
- Ayuda a detectar grupos o clustering

**3. Boxplot de Totales por Categoría**
- Compara distribuciones entre Alimentos y Limpieza
- Identifica si una categoría tiene transacciones más altas/bajas

#### Hallazgos Principales
- **Cantidad**: Distribución sesgada (mayoría de transacciones pequeñas)
- **Precio vs Total**: Relación lineal clara y positiva
- **Por Categoría**: Posibles diferencias en montos por tipo de producto



---

## Interpretación de Resultados y Conclusiones

A través de este Análisis Exploratorio de Datos (EDA), hemos transformado un conjunto disperso de cuatro tablas independientes en un dataset integrado y limpio que permite entender profundamente el comportamiento de ventas de la Tienda Aurelion.

### ¿Qué Descubrimos?

#### 1. **Estructura de Datos Robusta**
Los datos originales provenían de sistemas bien organizados con relaciones claras entre clientes, productos, ventas y detalles. Esto facilitó significativamente el proceso de integración y permitió mantener la integridad referencial a lo largo del análisis.

#### 2. **Categorización Mejorada**
Al implementar la recategorización automática de productos basada en palabras clave, identificamos con precisión los **artículos de limpieza** versus **alimentos**.

#### 3. **Patrones de Transacciones**
El análisis de distribuciones reveló que:
- **La mayoría de transacciones son de pequeño volumen** (pocos productos por venta)
- **Existe una relación lineal clara entre precio y total** (esperada pero validada)
- **Las categorías muestran diferencias notables** en montos y patrones

#### 4. **Valores extremos controlados**
Mediante el método IQR identificamos y eliminamos outliers que representaban:
- Transacciones especiales o promocionales
- Posibles errores de captura
- Comportamientos atípicos que podrían sesgar análisis posteriores

Al limpiar estos datos, nos aseguramos de que nuestros análisis se basen en comportamiento típico y representativo.

#### 5. **Correlaciones Validadas**
El análisis de correlaciones confirmó relaciones lógicas esperadas:
- **Precio ↔ Total**: Correlación fuerte (un producto más caro genera un total mayor)
- **Cantidad ↔ Total**: Correlación moderada (compras de mayor volumen = mayores importes)

Estas validaciones dan confianza de que los datos reflejan la realidad operativa.

### Transformación de los Datos: De Caos a Orden

| Aspecto | Antes del EDA | Después del EDA |
|---------|---------------|-----------------|
| **Estructura** | 4 tablas dispersas | 1 tabla integrada y coherente |
| **Columnas** | Redundancias, sufijos _x/_y | Nombres claros y únicos |
| **Categorías** | Inconsistentes | Automáticamente clasificadas |
| **Anomalías** | Sin identificar | Detectadas y eliminadas |

### Lecciones Aprendidas

1. **La calidad de datos es fundamental**: El 80% del tiempo en ciencia de datos se dedica a preparación, no a análisis
2. **La automatización ahorra recursos**: La recategorización automática es más rápida y consistente que manual
3. **Las visualizaciones comunican mejor**: Un boxplot dice más que mil números sobre outliers
4. **La validación es clave**: Verificar correlaciones esperadas aumenta confianza en los datos

### Conclusión Final
El dataset procesado proporciona una base sólida para identificar productos más/menos vendidos y apoyar decisiones comerciales de la Tienda Aurelion.



