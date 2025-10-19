from pathlib import Path
import sys

BASE_DIR = Path(__file__).parent

# Declaracion de variables (usar Path para compatibilidad de rutas)
path_problema = BASE_DIR / 'consola' / 'tema_problema_solucion.md'
path_pseudocodigo = BASE_DIR / 'consola' / 'pseudocodigo.md'
path_diagrama_flujo = BASE_DIR / 'consola' / 'diagrama_flujo.md'
path_datasets = BASE_DIR / 'consola' / 'datasets.md'
path_sugerencias = BASE_DIR / 'consola' / 'sugerencias_mejoras.md'


def leer_mostrar_archivo(ruta: Path) -> None:
    """Lee y muestra el contenido de `ruta` de forma segura.

    Acepta tanto strings como Path. No lanza excepciones al usuario final,
    imprime mensajes claros en caso de error.
    """
    try:
        ruta = Path(ruta)
        if not ruta.exists():
            print(f"El archivo {ruta} no se encontró.")
            return
        with ruta.open('r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta}: {e}")


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
            print("6. Salir")
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
                    print("\n" + "*" * 5 + " Opcion 5 seleccionada " + "*" * 5 + "\n")
                    leer_mostrar_archivo(path_sugerencias)
                case "6":
                    print("\nGracias por usar el menú interactivo. ¡Adiós!")
                    salir = True
                case _:
                    if opcion == "":
                        # Si el usuario presionó Enter sin ingresar, mostramos el menú de nuevo
                        continue
                    print("\nOpcion no valida. Por favor, ingrese un número del 1 al 6")
    except KeyboardInterrupt:
        print("\nInterrupción por teclado. Saliendo...")
        return 0
    return 0


if __name__ == '__main__':
    sys.exit(main())

