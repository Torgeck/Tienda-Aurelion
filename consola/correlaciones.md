# Análisis de Correlaciones

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
name_list = ["clientes", "detalle_ventas", "productos", "ventas"]

for i, tabla in enumerate(df_list):
    print(f"\n=========== CORRELACIONES PARA {name_list[i].upper()} ===========")
    
    numericas = tabla.select_dtypes(include=[np.number])
    
    if not numericas.empty:
        corr = numericas.corr()
        print(corr)

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax)
        ax.set_title(f'Matriz de Correlación - {name_list[i]}')
        plt.show()
        
        print("\nCorrelaciones más significativas:")
        corr_unstack = corr.unstack()
        corr_sorted = corr_unstack[abs(corr_unstack) > 0.5]
        corr_sorted = corr_sorted[corr_sorted != 1.0] #elimino autocorrelaciones
        if not corr_sorted.empty:
            print(corr_sorted.sort_values(ascending=False))
        else:
            print("No se encontraron correlaciones significativas (>0.5)")
    else:
        print(f"No hay variables numéricas en {name_list[i]} para calcular correlaciones")
    
    print("\n" + "="*50)
```