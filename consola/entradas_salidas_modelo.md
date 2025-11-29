
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