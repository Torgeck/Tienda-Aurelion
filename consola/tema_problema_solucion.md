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
