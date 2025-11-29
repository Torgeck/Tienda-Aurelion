## Script para limpiar, crear y exportar un dataframe con todos los datos de 
## las tablas a un .cvs
import pandas as pd
import numpy as np
import os
pd.set_option("future.no_silent_downcasting", True)


def limpia_y_exporta():
    """Limpia los datos de los archivos excel y los exporta a un .csv"""
    ## Declaracion de Paths
    path_clientes = "./data/clientes.xlsx"
    path_det_ventas = "./data/detalle_ventas.xlsx"
    path_productos = "./data/productos.xlsx"
    path_ventas = "./data/ventas.xlsx"
    path_salida = "./clean_data/dataset_final.csv"

    ## Carga los data frames desde los excels
    df_ventas = pd.read_excel(path_ventas)
    df_productos = pd.read_excel(path_productos)
    df_clientes = pd.read_excel(path_clientes)
    df_detventas = pd.read_excel(path_det_ventas)

    ## Hace limpieza de los mismos
    # Ventas
    df_ventas = df_ventas.astype({col: "string" for col in df_ventas.select_dtypes(include=["object"]).columns})
    df_ventas = df_ventas.apply(lambda col: col.str.upper() if col.dtype == "string" else col)

    # Clientes
    df_clientes = df_clientes.astype({col: "string" for col in df_clientes.select_dtypes(include=["object"])})
    df_clientes = df_clientes.apply(lambda col: col.str.upper() if col.dtype == "string" else col)

    ## Productos
    df_productos = df_productos.drop(df_productos.columns[[4,5]], axis = 1)
    df_productos = df_productos.astype({col: "string" for col in df_productos.select_dtypes(include=["object"])})
    df_productos = df_productos.apply(lambda col: col.str.upper() if col.dtype == "string" else col)

    ## Detalles_ventas
    df_detventas["nombre_producto"] = df_detventas["nombre_producto"].astype("string").str.upper()


    ## Guardo los df en excels para el notebook
    df_ventas.to_excel("./clean_data/ventas_clean.xlsx",index=False)
    df_clientes.to_excel("./clean_data/clientes.xlsx",index=False)
    df_productos.to_excel("./clean_data/productos_clean.xlsx",index=False)
    df_detventas.to_excel("./clean_data/detalles_ventas_clean.xlsx", index=False)

    # Recategorizo productos (ya que estaban mal categorizados)

    # Setea la columna categoria a ALIMENTOS
    df_productos['categoria'] = 'ALIMENTOS'
    KEYWORDS_LIMPIEZA = ['DETERGENTE', 'LAVANDINA', 'JABÓN', 'ESPONJA', 'DESINFECTANTE', 'SUAVIZANTE','DESODORANTE','CEPILLO','TOALLA','DENTAL','PAPEL','LIMPIA','CAPILAR','PISO','SHAMPOO','SERVILLETA','DESENGRASANTE']

    def clasificar_producto(nombre_producto):
        """Clasifica el producto basado en palabras clave en su nombre."""
        
        for keyword in KEYWORDS_LIMPIEZA:
            if keyword in nombre_producto:
                return 'LIMPIEZA'
                
        return 'ALIMENTOS'

    df_productos['categoria_correcta'] = df_productos['nombre_producto'].apply(clasificar_producto)
    df_productos['categoria'] = df_productos['categoria_correcta']
    df_productos.drop(columns=['categoria_correcta'], inplace=True)

    # Union (merge) de los dataframes
    df_venta_detalle = df_detventas.merge(df_ventas, on='id_venta', how='left').merge(df_productos, on='id_producto', how='left')
    df_todos = df_venta_detalle.merge(df_clientes, on='id_cliente' , how='left')

    # Transformacion de datos - Aplicar una sola vez a df_todos
    medios = {"EFECTIVO": 0 , "TARJETA": 1, "QR":2, "TRANSFERENCIA": 3}
    df_todos["medio_pago"] = df_todos["medio_pago"].replace(medios).infer_objects(copy=False)
    
    categorias = {'LIMPIEZA':0, 'ALIMENTOS':1}
    df_todos["categoria"] = df_todos["categoria"].replace(categorias).infer_objects(copy=False)

    ciudades = {'CARLOS PAZ':0, 'RIO CUARTO':1, 'MENDIOLAZA':2, 'ALTA GRACIA':3, 'VILLA MARIA': 4,'CORDOBA': 5}
    df_todos["ciudad"] = df_todos["ciudad"].replace(ciudades).infer_objects(copy=False)

    # Crear dataset_train.csv ANTES de eliminar columnas
    # Seleccionar columnas necesarias para training
    df_train = df_todos.copy()
    df_train = df_train.drop(columns=['nombre_producto_x','precio_unitario_x','email_x','nombre_cliente_y'])
    df_train.rename(columns={'nombre_producto_y':'producto','precio_unitario_y':'precio','importe':'total','fecha':'fecha_venta','fecha_alta':'fecha_alta_cli','nombre_cliente_x':'nombre_cliente','email_y':'email'}, inplace=True)
    
    # Exportar dataset_train.csv
    path_train = "./clean_data/dataset_train.csv"
    df_train.to_csv(path_train, sep='|', index=False)

    # Limpieza de columnas con datos irrelevantes
    df = df_todos
    df = df.drop(columns=['id_venta','id_producto','nombre_producto_x','precio_unitario_x','nombre_cliente_x','email_x','nombre_cliente_y','email_y','id_cliente'])
    df.rename(columns={'nombre_producto_y':'producto','precio_unitario_y':'precio','importe':'total','fecha':'fecha_venta','fecha_alta':'fecha_alta_cli'}, inplace=True)

    # Reorganizacion de columnas
    df = df[['producto','categoria','cantidad','precio','total','medio_pago','fecha_venta','ciudad','fecha_alta_cli']]

    # Procesamiento de fechas
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
    df['mes'] = df['fecha_venta'].dt.to_period('M')
    df["cuatrimestre"] = ((df["fecha_venta"].dt.month - 1) // 4 + 1).astype(int)
    df["anio_cuatrimestre"] = df["fecha_venta"].dt.year.astype(str) + "-C" + df["cuatrimestre"].astype(str)

    # Eliminacion de Outliers a traves de cuantiles
    Q1 = np.percentile(df["total"], 25)
    Q3 = np.percentile(df["total"], 75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    df = df[(df["total"] >= limite_inferior) & (df["total"] <= limite_superior)].copy()

    # Exportacion del dataframe como .csv
    df.to_csv(path_salida, sep='|', index=False)

    if os.path.exists(path_salida) and os.path.exists(path_train):
        print("|================| Archivo dataset_final.csv creado con exito |===================|")
        print("|================| Archivo dataset_train.csv creado con exito |===================|")
        return True
    else:
        print("Error al crear los archivos CSV")
        return False