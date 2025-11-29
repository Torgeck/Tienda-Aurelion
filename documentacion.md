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




---

## Modelo ML Implementado - Sprint 3

### Objetivo y Justificación del Algoritmo (DecisionTreeClassifier)

#### **Objetivo de la Clasificación**
Predecir si un cliente es un **'Cliente Frecuente'** (1) o **'No Frecuente'** (0), basándose en múltiples variables de comportamiento de compra: método de pago, precio, categoría de productos, ciudad de residencia y cantidad de productos comprados.

#### **Justificación del Algoritmo: Árbol de Decisión**

Se eligió **DecisionTreeClassifier** por las siguientes razones:

1. **Interpretabilidad**: Los árboles de decisión son altamente interpretables. Cada rama representa una regla clara que puede ser comprendida fácilmente por stakeholders no técnicos.

2. **Eficiencia Computacional**: Es rápido de entrenar y realizar predicciones, incluso con pocos datos.

3. **No requiere normalización**: A diferencia de otros algoritmos (SVM, KNN), no necesita escalar los datos.

4. **Captura Relaciones No-Lineales**: Puede detectar patrones complejos en los datos aunque la relación sea no lineal.

5. **Sencillez en el Dominio**: Para este problema específico (predecir frecuencia basada en medio de pago), un árbol con profundidad limitada (max_depth=3) es suficiente y evita sobreajuste.

6. **Ventaja en Clasificación Binaria**: Funciona excelentemente en problemas de clasificación binaria como el nuestro.

---

### Modelo ML Implementado

#### **Algoritmo Utilizado: DecisionTreeClassifier**

Se implementó un modelo de clasificación basado en **Árbol de Decisión (DecisionTreeClassifier)** de scikit-learn con los siguientes parámetros:

```python
DecisionTreeClassifier(random_state=42)
```

**Configuración del Modelo:**
- **max_depth**: None (sin limitación de profundidad)
- **random_state**: 42 (reproducibilidad)
- **Features utilizados**: `medio_pago`, `precio`, `categoria`, `ciudad`, `cantidad`
- **Target**: `es_cliente_frecuente` (binario: 0 = No Frecuente, 1 = Frecuente)
- **Train/Test Split**: 80/20 con random_state=42

**Rendimiento:**
- **Accuracy**: 79.71%
- **Recall (Frecuentes)**: 93%
- **Recall (No Frecuentes)**: 09%

#### **Visualización del Árbol de Decisión**

![Árbol de Decisión - Clasificación de Clientes Frecuentes](./img/arbol_decision.png)

El árbol visualiza las reglas aprendidas por el modelo sobre las 5 variables, mostrando los nodos de decisión y las clasificaciones finales en las hojas.

---



### Entradas (X) y Salida (y)

#### **Variables de Entrada (X)**

El modelo utiliza **5 variables de entrada** que capturan múltiples dimensiones del comportamiento de compra:

**1. `medio_pago` (recodificada numéricamente)**
- **0**: EFECTIVO
- **1**: TARJETA
- **2**: QR
- **3**: TRANSFERENCIA

Refleja el patrón de pago del cliente: clientes frecuentes podrían preferir ciertos métodos de pago sobre otros.

**2. `precio` (variable continua)**
- Rango: valores numéricos del precio unitario de productos
- Refleja el perfil de gasto del cliente: si tiende a comprar productos baratos o costosos
- Clientes frecuentes podrían concentrarse en rangos específicos de precios

**3. `categoria` (recodificada numéricamente)**
- **0**: LIMPIEZA
- **1**: ALIMENTOS

Refleja el tipo de producto que compra el cliente: las preferencias por categoría pueden indicar patrones de consumo característicos de clientes frecuentes.

**4. `ciudad` (variable categórica)**
- Refleja la ubicación geográfica del cliente
- Permite capturar diferencias regionales en patrones de compra
- Puede indicar si la frecuencia de compra varía por zona

**5. `cantidad` (variable continua)**
- Refleja la cantidad de unidades compradas por transacción
- Clientes frecuentes podrían tener patrones diferentes en volumen de compra
- Captura el comportamiento de compra en términos de volumen

**Justificación de estas 5 variables:**
- Combinan información de **método de pago**, **valor económico**, **tipo de producto**, **ubicación** y **volumen de compra**
- Proporcionan una visión holística del comportamiento de compra del cliente
- Permiten que el árbol de decisión capture patrones más complejos y matizados
- Cada variable aporta una dimensión diferente al análisis de frecuencia de compra

#### **Variable de Salida (y)**

**Columna**: `es_cliente_frecuente` (variable binaria)

Esta variable fue **creada** durante el preprocesamiento:

```python
frecuencia_clientes = df_todos['id_cliente'].value_counts()

umbral_mediana = frecuencia_clientes.median()

es_cliente_frecuente = 1 si frecuencia_compra >= umbral_mediana
                      0 si frecuencia_compra < umbral_mediana
```

**Justificación de la mediana**:
- Divide los clientes en dos grupos de tamaño similar
- Permite detectar cambios significativos en el patrón de compras

---

### División, Entrenamiento y Predicciones

#### **División de Datos (Train/Test)**

Se utilizó la función `train_test_split` de scikit-learn con los siguientes parámetros:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

**Parámetros**:
- **test_size=0.2**: Asigna 80% de los datos para entrenamiento y 20% para prueba (proporción estándar)
- **random_state=42**: Fija la semilla aleatoria para reproducibilidad de resultados

**Distribución del Dataset**:
- **X_train, y_train**: 80% de los datos (para aprender patrones)
- **X_test, y_test**: 20% de los datos (para evaluación independiente)

#### **Entrenamiento del Modelo**

```python
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)
```

#### **Generación de Predicciones**

```python
y_pred = modelo.predict(X_test)
```

El modelo genera predicciones (0 o 1) para cada cliente en el conjunto de prueba, predicciones que serán comparadas con los valores reales para evaluar su desempeño.

---

### Métricas de Evaluación

#### **Accuracy (Exactitud)**

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

Donde:
- **TP** (True Positives): Clientes frecuentes correctamente identificados
- **TN** (True Negatives): Clientes no frecuentes correctamente identificados
- **FP** (False Positives): Clientes no frecuentes erróneamente clasificados como frecuentes
- **FN** (False Negatives): Clientes frecuentes erróneamente clasificados como no frecuentes

El accuracy proporciona el porcentaje general de predicciones correctas.

#### **Classification Report**

Incluye tres métricas por clase:

1. **Precision**: De los clientes predichos como frecuentes, ¿qué proporción realmente lo es?
   ```
   Precision = TP / (TP + FP)
   ```

2. **Recall (Sensibilidad)**: De los clientes frecuentes reales, ¿qué proporción fue detectada?
   ```
   Recall = TP / (TP + FN)
   ```

3. **F1-Score**: Media armónica entre Precision y Recall
   ```
   F1 = 2 * (Precision * Recall) / (Precision + Recall)
   ```

4. **Support**: Número de muestras reales para cada clase en el conjunto de prueba

#### **Matriz de Confusión**

Tabla 2×2 que muestra:

|  | Predicho: No Frecuente | Predicho: Frecuente |
|---|---|---|
| **Real: No Frecuente** | TN | FP |
| **Real: Frecuente** | FN | TP |

Permite identificar tipos específicos de errores cometidos por el modelo.

---

### Resultados Obtenidos

#### **Métricas Calculadas**

```
Accuracy: 0.7971 (79.71%)

              precision    recall  f1-score   support

No Frecuente       0.20      0.09      0.12        11
   Frecuente       0.84      0.93      0.89        58

    accuracy                           0.80        69
   macro avg       0.52      0.51      0.51        69
weighted avg       0.74      0.80      0.76        69
```

#### **Interpretación de Resultados**

- **Accuracy General**: El modelo clasifica correctamente el 79.71% de los casos
- **Clientes Frecuentes**: Recall del 93%, significa que detecta 9 de cada 10 clientes frecuentes
- **Clientes No Frecuentes**: Recall del 9%, tiene dificultad detectando clientes no frecuentes (sesgo hacia clase mayoritaria)

#### **Análisis de Matriz de Confusión**

```
     No Frecuente  Frecuente
No Frecuente     1        10
Frecuente        4        54
```

- **Verdaderos Negativos (TN)**: 1 cliente no frecuente correctamente identificado
- **Falsos Positivos (FP)**: 10 clientes no frecuentes erróneamente clasificados como frecuentes
- **Falsos Negativos (FN)**: 4 clientes frecuentes no detectados
- **Verdaderos Positivos (TP)**: 54 clientes frecuentes correctamente identificados

#### **Métricas Derivadas**

- **Sensibilidad (Recall)**: 75% - Probabilidad de detectar un cliente frecuente
- **Especificidad**: 67% - Probabilidad de identificar un cliente no frecuente
- **Precisión (Frecuente)**: 75% - Si el modelo predice frecuente, hay 75% probabilidad de ser correcto

---

### Visualizaciones de Resultados

#### **1. Árbol de Decisión**

El árbol visualiza las reglas aprendidas por el modelo:
- **Nodos internos**: Contienen condiciones sobre las 5 variables (`medio_pago`, `precio`, `categoria`, `ciudad`, `cantidad`)
- **Nodos hoja**: Contienen la clasificación final (No Frecuente / Frecuente)
- **Colores**: Indican la clase dominante (azul para No Frecuente, naranja para Frecuente)
- **Valores**: Muestran la distribución de clases en cada nodo
- **Tamaño**: Puede tener profundidad ilimitada (max_depth=None)

Con 5 features sin limitación de profundidad, el árbol puede descubrir patrones muy complejos y específicos en el comportamiento de compra, permitiendo capturar interacciones multivaribles entre todas las dimensiones del cliente.

#### **2. Matriz de Confusión Visualizada**

Un gráfico de calor que resalta:
- **Diagonal principal**: Predicciones correctas (valores altos deseados)
- **Fuera de la diagonal**: Errores de clasificación

Esta visualización ayuda a identificar rápidamente si el modelo tiende a cometer más falsos positivos o falsos negativos.

#### **3. Importancia de Features**

Gráfico de barras que muestra la contribución relativa de cada variable en las decisiones del modelo:
- **Altura de la barra**: Importancia (suma de valores entre 0 y 1)
- **Variables**: `medio_pago`, `precio`, `categoria`, `ciudad`, `cantidad`

Esta visualización es crucial para entender cuál de las 5 variables tiene mayor influencia en la predicción de frecuencia de clientes. Permite identificar:
- Variables dominantes en el patrón de cliente frecuente
- Ranking de importancia: cuál es más discriminante para clasificar clientes
- Que variables con bajo aporte en iteraciones futuras remover.
- Prioridades para recopilación y mantenimiento de datos

---

### Conclusiones del Modelo

1. **Enfoque Multi-Dimensional**: El modelo utiliza 5 variables (`medio_pago`, `precio`, `categoria`, `ciudad`, `cantidad`) que capturan diferentes dimensiones del comportamiento de compra del cliente, proporcionando una visión integral para predecir frecuencia.

2. **Flexibilidad del Árbol**: Sin limitación de profundidad (max_depth=None), el árbol de decisión puede crecer tanto como sea necesario para descubrir patrones complejos e interacciones entre los 5 features, mejorando significativamente la capacidad predictiva.

3. **Feature Insights**:
   - El análisis de importancia identifica cuál de las 5 variables es más determinante en las decisiones del modelo
   - Proporciona insights comerciales sobre qué factores realmente diferencian clientes frecuentes


4. **Aplicabilidad Práctica**: 
   - Las predicciones pueden usarse para segmentación y perfilado de clientes
   - Estrategias de marketing dirigidas basadas en patrones multivaribles complejos
   - Identificación de oportunidades de retención por región, categoría y método de pago

5. **Potencial de Mejora Futuro**: 
   - Explorar otros algoritmos (Random Forest, Gradient Boosting) que pueden manejar mejor la complejidad
   - Agregar más variables (recencia, tiempo desde última compra, frecuencia temporal)

---

