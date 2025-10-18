## Declaracion de variables
path_problema = './consola/tema_problema_solucion.md'
path_pseudocodigo = './consola/pseudocodigo.md'
path_datasets = './consola/datasets.md'
path_sugerencias = './consola/sugerencias_mejoras.md'

def leer_mostrar_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {ruta} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta}: {e}")

## Menu principal del proyecto
salir = False
while not salir:
    print("\n" + "=" * 50)
    print("      MENÚ INTERACTIVO DEL PROYECTO AURELION")
    print("=" * 50)
    print("1. Mostrar tema, problema y solucion")
    print("2. Mostrar pseudocodigo")
    print("3. Mostrar info acerca de los datasets")
    print("4. Sugerencias y mejoras con Copilot")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
   
    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            # Abre el archivo problema_solucion.txt y lo muestra por pantalla
            leer_mostrar_archivo(path_problema)
        case "2":
            print("Opcion 2 seleccionada")
            # Abre el archivo pseudocodigo.txt y lo muestra por pantalla
            leer_mostrar_archivo(path_pseudocodigo)
        case "3":
            print("Opcion 3 seleccionada")
            # Abre los archivos datasets y muestra las 5 primeras filas de cada uno
            leer_mostrar_archivo(path_datasets)
        case "4":
            print("Opcion 4 seleccionada")
            # muestra el archivo sugerencias_mejoras.md
            leer_mostrar_archivo(path_sugerencias)
        case "5":
            salir = True
        case _:
            print("Opcion no valida")

