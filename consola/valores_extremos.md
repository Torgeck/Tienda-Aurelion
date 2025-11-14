# Análisis de Valores Extremos

## Descripción
Este análisis identifica y examina los valores atípicos o extremos en nuestros conjuntos de datos, lo que nos ayuda a detectar patrones inusuales o posibles anomalías en las transacciones.

## Variables Analizadas
1. **Cantidades**
   - Valores mínimos y máximos de unidades vendidas
   - Identificación de ventas inusualmente grandes o pequeñas

2. **Precios Unitarios**
   - Productos con precios extremadamente altos o bajos
   - Variación de precios en el catálogo

3. **Importes Totales**
   - Transacciones con montos extremos
   - Patrones en ventas de alto valor

## Interpretación de Resultados
- Los valores mínimos indican el piso de cada variable
- Los valores máximos muestran los límites superiores
- Los percentiles ayudan a entender la distribución
- Los outliers pueden indicar oportunidades o errores

## Visualizaciones
==================== Valores extremos para CANTIDAD ====================

Estadísticas básicas:
Media: 2.96
Desviación estándar: 1.37

Valores mínimos:
producto	cantidad
0	TOALLAS HÚMEDAS X50	1
4	MEDIALUNAS DE MANTECA	1
8	JUGO EN POLVO NARANJA	1
14	QUESO UNTABLE 190G	1
24	STEVIA 100 SOBRES	1

Valores máximos:
producto	cantidad
1	ACEITUNAS NEGRAS 200G	5
2	HELADO VAINILLA 1L	5
10	BIZCOCHOS SALADOS	5
17	LAVANDINA 1L	5
19	VINO BLANCO 750ML	5

==================== Valores extremos para PRECIO ====================

Estadísticas básicas:
Media: 2654.50
Desviación estándar: 1308.69

Valores mínimos:
producto	precio
128	PAN LACTAL INTEGRAL	272
135	PAN LACTAL INTEGRAL	272
169	PAN LACTAL INTEGRAL	272
314	PAN LACTAL INTEGRAL	272
2	HELADO VAINILLA 1L	469

Valores máximos:
producto	precio
272	MIEL PURA 250G	4982
335	MIEL PURA 250G	4982
7	PEPSI 1.5L	4973
176	PEPSI 1.5L	4973
208	PEPSI 1.5L	4973

==================== Valores extremos para TOTAL ====================

Estadísticas básicas:
Media: 7730.08
Desviación estándar: 5265.54

Valores mínimos:
producto	total
128	PAN LACTAL INTEGRAL	272
286	TURRÓN 50G	503
169	PAN LACTAL INTEGRAL	544
263	TÉ NEGRO 20 SAQUITOS	570
214	ACEITE DE GIRASOL 1L	860

Valores máximos:
producto	total
208	PEPSI 1.5L	24865
141	CARAMELOS MASTICABLES	23760
41	BARRITA DE CEREAL 30G	22150
54	PIZZA CONGELADA MUZZARELLA	21430
175	ENERGÉTICA NITRO 500ML	21090

Outliers detectados: 22 registros
producto	total
22	TRAPO DE PISO	19416
37	RON 700ML	19380
41	BARRITA DE CEREAL 30G	22150
54	PIZZA CONGELADA MUZZARELLA	21430
87	RON 700ML	19380
103	STEVIA 100 SOBRES	19240
109	CARAMELOS MASTICABLES	19008
141	CARAMELOS MASTICABLES	23760
143	DESODORANTE AEROSOL	18760
158	YERBA MATE SUAVE 1KG	19390
170	DESODORANTE AEROSOL	18760
175	ENERGÉTICA NITRO 500ML	21090
181	EMPANADAS CONGELADAS	19112
196	TRAPO DE PISO	19416
207	SPRITE 1.5L	19856
208	PEPSI 1.5L	24865
260	JUGO EN POLVO LIMÓN	20450
262	RON 700ML	19380
300	AGUA MINERAL 500ML	19108
308	JUGO DE NARANJA 1L	20850
325	QUESO CREMOSO 500G	19336
334	VINO TINTO MALBEC 750ML	18876



## Código Implementado
```python
def analizar_valores_extremos(df, columna):
    """Analiza los valores extremos de una columna específica."""
    print(f"\n{'='*20} Valores extremos para {columna.upper()} {'='*20}")
    
    # estadistico
    media = df[columna].mean()
    std = df[columna].std()
    
    print(f"\nEstadísticas básicas:")
    print(f"Media: {media:.2f}")
    print(f"Desviación estándar: {std:.2f}")
    
    print("\nValores mínimos:")
    display(df.nsmallest(5, columna)[['producto', columna]])
    
    print("\nValores máximos:")
    display(df.nlargest(5, columna)[['producto', columna]])
    
    # outliers
    lower_bound = media - 2 * std
    upper_bound = media + 2 * std
    outliers = df[(df[columna] < lower_bound) | (df[columna] > upper_bound)]
    
    if not outliers.empty:
        print(f"\nOutliers detectados: {len(outliers)} registros")
        display(outliers[['producto', columna]])

#valores extremos para las variables que son  numéricas
for columna in ['cantidad', 'precio', 'total']:
    analizar_valores_extremos(df, columna)
```