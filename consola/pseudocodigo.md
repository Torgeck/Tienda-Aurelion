INICIO
    Definir rutas:
        path_problema, path_pseudocodigo, path_datasets, path_sugerencias

    Definir funcion:
        leer_mostrar_archivo(ruta):
            intentar abrir archivo en 'ruta' con UTF-8
            SI existe
                leer y mostrar contenido
            SI no existe: informar archivo no encontrado
                capturar e informar otros errores
        FIN leer_mostrar_archivo

    salir = False
    MIENTRAS salir == False
        mostrar menu por consola:
            1 - Mostrar tema, problema y solución
            2 - Mostrar pseudocódigo
            3 - Mostrar datasets utilizados (5 primeras filas)
            4 - Sugerencias y mejoras con Copilot
            5 - Salir
        leer opción 
        
        validar opción:
            SI opción == "1":
                leer_mostrar_archivo(path_problema)
        
            SI opción == "2":
                leer_mostrar_archivo(path_pseudocodigo)
        
            SI opción == "3":
                leer_mostrar_archivo(path_datasets)
        
            SI opción == "4":
                leer_mostrar_archivo(path_sugerencias)
        
            SI opción == "5":
                salir = True
            SINO
                mostrar "Opción no válida"
        FIN MIENTRAS
FIN