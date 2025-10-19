# Proyecto Aurelion — Instrucciones para compartir en Google Drive

Este README explica qué carpetas y archivos debes descargar de Google Drive para que el proyecto funcione correctamente en otra máquina.

## Requisitos mínimos
- Python 3.10 o superior (recomendado 3.11+).

## Estructura mínima necesaria para compartir
Comparte estas carpetas/archivos en Google Drive (si faltan, el script puede fallar):

- `proyecto.py` (archivo principal).
- Carpeta `consola/` con los siguientes archivos (al menos):
	- `tema_problema_solucion.md`
	- `pseudocodigo.md`
	- `datasets.md`
	- `sugerencias_mejoras.md`
	- `diagrama_flujo.md` (diagrama ASCII exportado)
- Carpeta `data/` (si usas datasets locales, incluye los CSV/Excel necesarios). Si no tienes datasets, puedes dejarla vacía pero crear la carpeta.

Opcionales (recomendado incluir):
- Cualquier script adicional o notas en la raíz.

## Cómo organizar los archivos en Google Drive
1. Descargar la carpeta de Google Drive con el nombre de `Tienda_Aurelion`.
2. Dentro de esa carpeta, se contendran todas carpetas listadas arriba manteniendo la estructura.
3. Al descargar el contenido en otra máquina, asegúrate de preservar la jerarquía (la carpeta raíz del proyecto debe contener `proyecto.py`, `consola/`, `data/`).

## Cómo descargar y ejecutar en Windows (PowerShell)
1. Descarga y extrae (si es ZIP) la carpeta desde Google Drive en una ubicación local. Supongamos que la extraes a `D:\Proyectos\Tienda_Aurelion`.

2. Navega al directorio del proyecto:


3. (Opcional) Crea y activa un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Instala las dependencias necesaria (si vas a usar funciones con datasets):

```powershell
pip install ....
```

5. Ejecuta el script principal:

.\proyecto.py

## Notas importantes
- Rutas relativas: `proyecto.py` usa rutas relativas a la carpeta `consola/` y `data/`. Asegúrate de mantener esa estructura.
- Codificación: los archivos `.md` deben estar en UTF-8 para evitar problemas con caracteres españoles.
- Si vas a compartir datasets grandes por Google Drive, considera comprimirlos (ZIP) y añadir instrucciones para descomprimirlos localmente.

