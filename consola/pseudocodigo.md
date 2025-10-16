Inicio
Declarar variables y rutas a los archivos de lectura de opciones
Declara variable salir para condicion del bucle
MIENTRAS (no salir)
Mostrar Menu:
1 - Mostrar problema y solucion
2 - Mostrar pseudocodigo
3 -Mostrar datasets utilizados
4 -Mostrar diagrama de flujo
5 - Fin
Leer opción
Si opción == 1..4 imprimir texto asociado
Si opción == 5 romper bucle fin

INICIO FUNCION leer_mostrar_archivo
Prueba abrir el archivo con la ruta pasada por parametro
Lee el archivo y lo carga a memoria
Imprime el contenido del archivo
Captura errores en caso de no poder leer o que no exista archivo con ruta
