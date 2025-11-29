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