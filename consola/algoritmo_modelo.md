#### **Justificación del Algoritmo: Árbol de Decisión**

Se eligió **DecisionTreeClassifier** por las siguientes razones:

1. **Interpretabilidad**: Los árboles de decisión son altamente interpretables. Cada rama representa una regla clara que puede ser comprendida fácilmente por stakeholders no técnicos.

2. **Eficiencia Computacional**: Es rápido de entrenar y realizar predicciones, incluso con pocos datos.

3. **No requiere normalización**: A diferencia de otros algoritmos (SVM, KNN), no necesita escalar los datos.

4. **Captura Relaciones No-Lineales**: Puede detectar patrones complejos en los datos aunque la relación sea no lineal.

5. **Sencillez en el Dominio**: Para este problema específico (predecir frecuencia basada en medio de pago), un árbol con profundidad limitada (max_depth=3) es suficiente y evita sobreajuste.

6. **Ventaja en Clasificación Binaria**: Funciona excelentemente en problemas de clasificación binaria como el nuestro.