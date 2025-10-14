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

### Definición
Base que representa una Tienda, con catálogo de productos, registro de clientes, detalles de ventas y ventas.

### Productos — ~100 filas
| Campo           | Tipo  | Escala |
|-----------------|-------|--------|
| id_producto     | int   | Nominal|
| nombre_producto | str   | Nominal|
| precio_unitario | str   | Razón  |

### Clientes — ~100 filas
| Campo           | Tipo  | Escala   |
|-----------------|-------|----------|
| id_cliente      | int   | Nominal  |
| nombre_cliente  | str   | Nominal  |
| email           | str   | Nominal  |
| ciudad          | str   | Nominal  |
| fecha_alta      | date  | Intervalo|

### Ventas — ~120 filas
| Campo           | Tipo  | Escala   |
|-----------------|-------|----------|
| id_venta        | int   | Nominal  |
| fecha           | date  | Intervalo|
| id_cliente      | int   | Nominal  |
| nombre_cliente  | str   | Nominal  |
| email           | str   | Nominal  |
| medio_pago      | str   | Nominal  |

### Detalles de Ventas — ~350 filas
| Campo           | Tipo  | Escala   |
|-----------------|-------|----------|
| id_venta        | int   | Nominal  |
| id_producto     | int   | Nominal  |
| nombre_producto | str   | Nominal  |
| cantidad        | int   | Razón    |
| precio_unitario | int   | Razón    |
| importe         | int   | Razón    |

## Información, pasos, pseudocodigo y diagrama del programa (Sprint 1)

### Información
En esta etapa, el programa funciona como un visor interactivo de la documentación, para
que el usuario obtenga rápidamente la información clave del proyecto desde la terminal.

### Contenido accesible desde el menu
Mostrar problema y solucion
Mostrar pseudocodigo
Mostrar datasets utilizados
Mostrar diagrama de flujo

## Sugerencias y mejoras aplicadas con Copilot