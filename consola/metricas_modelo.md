
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
