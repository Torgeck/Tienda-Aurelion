# Tienda Aurelion

## Tema

Tienda Aurelion es una cadena de mercado con varias sedes a lo largo de Cordoba. Dentro de su catalogo ofrece biene de consumo tales como alimentos varios y articulos de limpieza.

## Problema

La Tienda Aurelion no tiene implementado un sistema que permita saber de forma automatica cuales son los productos mas vendidos
y cuales presentan una baja rotacion. Esta falta de informacion dificulta la toma de decisiones respecto a la gestion del stock y
la implementacion de estrategias de descuento/promociones.
Como consecuencia, algunos productos permanecen en inventario durante largos periodos (generando costos de almacenamiento), mientras
que otros se agotan rapidamente sin aprovechar su potencial comercial

## Solucion

## Datos Requeridos

Los datos fueron provistos por los duenios de la tienda Aurelion

### Detalle_venta

- id_venta
  - Tipo cualitativo
  - Ordinal
- id_producto
  - Tipo cualitativo
  - Ordinal
- nombre_producto
  - Tipo cualitativo
  - Nominal
- cantidad
  - Tipo cuantitativo
  - Razon
- precio_unitario
  - Tipo cuantitativo
  - Razon
- importe
  - Tipo cuantitativo
  - Razon

### Clientes

- id_cliente
  - Tipo cualitativo
  - Ordinal
- nombre_cliente
  - Tipo cualitativo
  - Nominal
- email
  - Tipo cualitativo
  - Nominal
- ciudad
  - Tipo cualitativo
  - Nominal
- fecha_alta
  - Tipo cuantitativo
  - Intervalo

### Ventas

- id_venta
  - Tipo cualitativo
  - Nominal
- id_cliente
  - Tipo cualitativo
  - Nominal
- nombre_cliente
  - Tipo cualitativo
  - Nominal
- fecha
  - Tipo cuantitativo
  - Intervalo
- email
  - Tipo cualitativo
  - Nominal
- medio_pago
  - Tipo cualitativo
  - Nominal

### Productos

- id_producto
- nombre_producto
- categoria
- precio_unitario

## Pseudocodigo

## Diagrama
