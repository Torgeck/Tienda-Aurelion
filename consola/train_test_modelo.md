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