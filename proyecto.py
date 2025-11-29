from pathlib import Path
from clean_data.data_cleaner import limpia_y_exporta
import sys
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image  # Para mostrar imágenes en ventanas emergentes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

BASE_DIR = Path(__file__).parent

# Declaracion de variables (usar Path para compatibilidad de rutas)
path_problema = BASE_DIR / 'consola' / 'tema_problema_solucion.md'
path_pseudocodigo = BASE_DIR / 'consola' / 'pseudocodigo.md'
path_diagrama_flujo = BASE_DIR / 'consola' / 'diagrama_flujo.md'
path_datasets = BASE_DIR / 'consola' / 'datasets.md'
path_sugerencias = BASE_DIR / 'consola' / 'sugerencias_mejoras.md'
path_estadisticas = BASE_DIR / 'consola' / 'estadisticas_descriptivas.md'
path_correlaciones = BASE_DIR / 'consola' / 'correlaciones.md'
path_valores_extremos = BASE_DIR / 'consola' / 'valores_extremos.md'
path_graficos = BASE_DIR / 'consola' / 'graficos.md'
path_interpretacion = BASE_DIR / 'consola' / 'interpretacion_resultados.md'
path_limpieza = BASE_DIR / 'clean_data' / 'data_cleaner.py'
path_objetivo =  BASE_DIR / 'consola' / 'objetivo_modelo.md'
path_algoritmo =  BASE_DIR / 'consola' / 'algoritmo_modelo.md'
path_entradas_salidas = BASE_DIR / 'consola' / 'entradas_salidas_modelo.md'
path_metricas =  BASE_DIR / 'consola' / 'metricas_calculadas_modelo.md'
path_modelo_implementado = BASE_DIR / 'consola' / 'modelo_utilizado.md'
path_train_test = BASE_DIR / 'consola' / 'train_test_modelo.md'
path_metricas_calculadas = BASE_DIR / 'consola' / 'metricas_calculadas_modelo.md'
path_resultados = BASE_DIR / 'consola' / 'resultados_modelo.md'

def mostrar_imagen(ruta_imagen: Path) -> None:
    """Muestra una imagen en una ventana emergente."""
    try:
        img = Image.open(ruta_imagen)
        img.show()
    except Exception as e:
        print(f"No se pudo abrir la imagen {ruta_imagen}: {e}")

def leer_mostrar_archivo(ruta: Path) -> None:
    """Lee y muestra el contenido de `ruta` de forma segura.
    
    Si el archivo es un markdown y contiene referencias a imágenes,
    las muestra en ventanas emergentes.
    """
    try:
        ruta = Path(ruta)
        if not ruta.exists():
            print(f"El archivo {ruta} no se encontró.")
            return
            
        with ruta.open('r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
            
            # Si es un archivo markdown, buscar y mostrar imágenes
            if ruta.suffix.lower() == '.md':
                # Buscar referencias a imágenes en el markdown
                imagenes = re.findall(r'!\[.*?\]\((.*?)\)', contenido)
                for img_path in imagenes:
                    # Convertir path relativo a absoluto
                    if img_path.startswith('./'):
                        img_path = ruta.parent / Path(img_path[2:])
                    else:
                        img_path = ruta.parent / img_path
                        
                    if img_path.exists():
                        print(f"\nAbriendo imagen: {img_path.name}")
                        mostrar_imagen(img_path)
                    else:
                        print(f"\nNo se encontró la imagen: {img_path}")
                        
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta}: {e}")

def sprint_3_modelo_ml():
    salir = False
    while not salir:
        print("\n" + "=" * 50)
        print("|       MENU INTERACTIVO SPRINT 3      |")
        print("=" * 50)
        print("1. Mostrar objetivo")
        print("2. Mostrar algoritmo elegido y justificacion")
        print("3. Mostrar entradas y salidas")
        print("4. Mostrar metricas de evaluacion")
        print("5. Mostrar modelo de ML implementado")
        print("6. Mostrar division train/test y entrenamiento")
        print("7. Mostrar predicciones y metricas calculadas")
        print("8. Mostrar resultados obtenidos")
        print("9. Regresar al menu principal")
        
        print("=" * 50)
        opcion = input("\nSeleccione una opcion: ").strip()

        match opcion:
            case "1":
                print("\n" + "*" * 5 + " Opcion 1 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_objetivo)
            case "2":
                print("\n" + "*" * 5 + " Opcion 2 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_algoritmo)
            case "3":
                print("\n" + "*" * 5 + " Opcion 3 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_entradas_salidas)
            case "4":
                print("\n" + "*" * 5 + " Opcion 4 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_metricas)
            case "5":
                print("\n" + "*" * 5 + " Opcion 5 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_modelo_implementado)
            case "6":
                print("\n" + "*" * 5 + " Opcion 6 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_train_test)
            case "7":
                print("\n" + "*" * 5 + " Opcion 7 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_metricas_calculadas)
            case "8":
                print("\n" + "*" * 5 + " Opcion 8 seleccionada " + "*" * 5 + "\n")
                leer_mostrar_archivo(path_resultados)
            case "9":
                print("\nRegresando al menú principal...")
                salir = True
            case _:
                if opcion == "":
                    continue
                print("\nOpcion no valida. Por favor, ingrese 1 o 2")

def main() -> int:
    """Menú interactivo principal."""
    salir = False
    try:
        while not salir:
            print("\n" + "=" * 50)
            print("|     MENÚ INTERACTIVO DEL PROYECTO AURELION     |")
            print("=" * 50)
            print("1. Mostrar tema, problema y solucion")
            print("2. Mostrar pseudocodigo")
            print("3. Mostrar diagrama de flujo")
            print("4. Mostrar info acerca de los datasets")
            print("5. Sugerencias y mejoras con Copilot")
            print("6. Estadísticas descriptivas")
            print("7. Valores extremos")
            print("8. Gráficos")
            print("9. Correlaciones")
            print("10. Interpretación de resultados")
            print("11. Limpieza y preparación de la base de datos")
            print("12. Modelo de ML")
            print("13. Salir")
            print("=" * 50)
            opcion = input("\nSeleccione una opcion: ").strip()

            match opcion:
                case "1":
                    print("\n" + "*" * 5 + " Opcion 1 seleccionada " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_problema)
                case "2":
                    print("\n" + "*" * 5 + " Opcion 2 seleccionada " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_pseudocodigo)
                case "3":
                    print("\n" + "*" * 5 + " Opcion 3 seleccionada " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_diagrama_flujo)
                case "4":
                    print("\n" + "*" * 5 + " Opcion 4 seleccionada " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_datasets)
                case "5":
                    print("\n" + "*" * 5 + " Sugerencias y mejoras con Copilot " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_sugerencias)
                case "6":
                    print("\n" + "*" * 5 + " Estadísticas descriptivas y limpieza" + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_estadisticas)
                case "7":
                    print("\n" + "*" * 5 + " Valores extremos " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_valores_extremos)
                case "8":
                    print("\n" + "*" * 5 + " Gráficos " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_graficos)
                case "9":
                    print("\n" + "*" * 5 + " Correlaciones " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_correlaciones)
                case "10":
                    print("\n" + "*" * 5 + " Interpretación de resultados " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_interpretacion)
                case "11":
                    print("\n" + "*" * 5 + " Limpieza y exportacion de .csv " + "*" * 5 + "\n")
                    limpia_y_exporta()
                case "12":
                    sprint_3_modelo_ml()
                case "13":
                    print("\nGracias por usar el menú interactivo. ¡Adiós!")
                    salir = True
                case _:
                    if opcion == "":
                        # Si el usuario presionó Enter sin ingresar, mostramos el menú de nuevo
                        continue
                    print("\nOpcion no valida. Por favor, ingrese un número del 1 al 13")
    except KeyboardInterrupt:
        print("\nInterrupción por teclado. Saliendo...")
        return 0
    return 0


if __name__ == '__main__':
    sys.exit(main())

