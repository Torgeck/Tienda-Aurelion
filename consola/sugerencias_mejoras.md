### Sugerencias y mejoras de Copilot

#### Aceptadas
- Modularicé el script envolviendo el menú en una función main() y añadiendo el guard if __name__ == '__main__'.
- Reemplacé rutas string por pathlib.Path para mayor portabilidad.
- Mejoré la función leer_mostrar_archivo para aceptar Path, comprobar existencia y capturar excepciones de forma clara.
- Normalicé la lectura de la entrada con .strip() y capturé KeyboardInterrupt para salida limpia.

#### Mejoras priorizadas no aplicadas
- Añadir manejo y visualización de datasets reales (pandas).
- Manejo detallado de errores y logs en vez de prints.
- Internacionalización y codificación de mensajes (si se espera usar distintos locales).
- Validación de entradas y menú más tolerante
- Implementar tests de integración para lectura de archivos largos (performance)
- Convertir rutas a partir de BASE_DIR = Path(__file__).parent para robustez cuando se ejecuta desde otro directorio.
- Añadir tests con pytest (crear tests/test_proyecto.py) y correrlos.
