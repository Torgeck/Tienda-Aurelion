# Tienda Aurelion

## Tema, Problema y Solucion

### Tema
Tienda Aurelion es una cadena de mercado con varias sedes a lo largo de Cordoba. Dentro de su catalogo ofrece biene de consumo tales como alimentos varios y articulos de limpieza.

### Problema
Controlar los productos más y venos vendidos por zonas

### Solución
A partir de los productos menos vendidos se les aplicara descuentos promociones o combos para lograr una mayor venta de los mismo

## Dataset de referencia: fuente, definición, estructura, tipos y escala de medición

### Fuente
Los datos fueron provistos por los dueños de la tienda Aurelion

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

Inicio Cargar textos de documentación mientras 
True: 
Mostrar Menu:
1 - Mostrar problema y solucion
2 - Mostrar pseudocodigo
3 -Mostrar datasets utilizados
4 -Mostrar diagrama de flujo
5 - Fin
Leer opción
Si opción == 1..4 imprimir texto asociado
Si opción == 5 romper bucle fin

### Información
En esta etapa, el programa funciona como un visor interactivo de la documentación, para
que el usuario obtenga rápidamente la información clave del proyecto desde la terminal.

### Contenido accesible desde el menu
Mostrar problema y solucion
Mostrar pseudocodigo
Mostrar datasets utilizados
Mostrar diagrama de flujo

## Sugerencias y mejoras aplicadas con Copilot