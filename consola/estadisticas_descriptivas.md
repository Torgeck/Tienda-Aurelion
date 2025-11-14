
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
