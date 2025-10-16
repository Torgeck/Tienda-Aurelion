## Tema

Tienda Aurelion es una cadena de mercado con varias sedes a lo largo de Cordoba. Dentro de su catalogo ofrece biene de consumo tales como alimentos varios y articulos de limpieza.

## Problema

La Tienda Aurelion no tiene implementado un sistema que permita saber de forma automatica cuales son los productos mas vendidos
y cuales presentan una baja rotacion. Esta falta de informacion dificulta la toma de decisiones respecto a la gestion del stock y
la implementacion de estrategias de descuento/promociones.
Como consecuencia, algunos productos permanecen en inventario durante largos periodos (generando costos de almacenamiento), mientras
que otros se agotan rapidamente sin aprovechar su potencial comercial

## Solucion

Se propone desarrollar una herramienta de analisis en **Python**, usando librerias como **pandas, numpy y matplotlib,** que permitira determinar
los **productos mas y menos vendidos** a partir de los registros de las bases de datos **productos.xlsx, ventas.xls, y detalles_ventas.xlsx**.

Con esta informacion, el sistema sugerira aplicar un descuento (determinado por el usuario) sobre el grupo de productos de baja rotacion para
incentivar la venta de los mismos.

Este analisis permitira a la Tienda Aurelion:

- Optimizar la gestion del stock de productos
- Aumentar las ventas de productos con bajo movimiento
- Mejorar la rentabilidad mediante estrategias de precios basados en datos reales

Ademas, los resultados podran visualizarse en graficos comparativos que faciliten la interpretacion de las tendencias de ventas y promuevan
una toma de decisiones comerciales mas informada.