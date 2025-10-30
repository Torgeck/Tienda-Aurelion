## Script for cleaning and format the data of excel sheets
import pandas as pd

path_clientes = "./data/clientes.xlsx"
path_det_ventas = "./data/detalle_ventas.xlsx"
path_productos = "./data/productos.xlsx"
path_ventas = "./data/ventas.xlsx"

## Read excel file and then change types of columns
df_ventas = pd.read_excel(path_ventas)
df_ventas = df_ventas.astype({col: "string" for col in df_ventas.select_dtypes(include=["object"]).columns})
df_ventas = df_ventas.apply(lambda col: col.str.upper() if col.dtype == "string" else col)

## Save in an excel file
df_ventas.to_excel("./clean_data/ventas_clean.xlsx",index=False)

## Repeat for each excel file
df_clientes = pd.read_excel(path_clientes)

df_clientes = df_clientes.astype({col: "string" for col in df_clientes.select_dtypes(include=["object"])})
df_clientes = df_clientes.apply(lambda col: col.str.upper() if col.dtype == "string" else col)

df_clientes.to_excel("./clean_data/clientes.xlsx",index=False)

## Productos
df_productos = pd.read_excel(path_productos)


df_productos = df_productos.drop(df_productos.columns[[4,5]], axis = 1)
df_productos = df_productos.astype({col: "string" for col in df_productos.select_dtypes(include=["object"])})
df_productos = df_productos.apply(lambda col: col.str.upper() if col.dtype == "string" else col)

df_productos.to_excel("./clean_data/productos_clean.xlsx",index=False)

## detalle_ventas
df_detventas = pd.read_excel(path_det_ventas)
df_detventas["nombre_producto"] = df_detventas["nombre_producto"].astype("string").str.upper()

print(df_detventas.describe())

df_detventas.to_excel("./clean_data/detalles_ventas_clean.xlsx", index=False)

