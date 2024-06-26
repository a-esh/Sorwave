
# Sorwave

Sorwave es un potente clasificador de música basado en Python. Utiliza las bibliotecas `mutagen` y `requests` para gestionar metadatos y realizar otras operaciones relacionadas con archivos de música. Este proyecto está diseñado para ayudar a los usuarios a organizar y gestionar su colección de música de manera eficiente.
https://pypi.org/project/sorwave/

## Tabla de Contenidos

- [Sorwave](#sorwave)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Instalación](#instalación)
  - [Funciones](#funciones)
    - [`get_metadata`](#get_metadata)
      - [Ejemplo de Uso](#ejemplo-de-uso)
    - [`gen_log`](#gen_log)
      - [Ejemplo de Uso](#ejemplo-de-uso-1)
    - [`new_log`](#new_log)
      - [Ejemplo de Uso](#ejemplo-de-uso-2)
    - [`filter_artist`](#filter_artist)
      - [Ejemplo de Uso](#ejemplo-de-uso-3)
    - [`sort_songs`](#sort_songs)
      - [Ejemplo de Uso](#ejemplo-de-uso-4)
  - [Características](#características)
  - [Contribuir](#contribuir)
  - [Roadmap](#roadmap)
  - [Preguntas Frecuentes](#preguntas-frecuentes)
    - [¿Qué formatos de archivos de música son compatibles?](#qué-formatos-de-archivos-de-música-son-compatibles)
    - [¿Cómo puedo reportar un problema o solicitar una nueva característica?](#cómo-puedo-reportar-un-problema-o-solicitar-una-nueva-característica)
  - [Licencia](#licencia)
  - [Contacto](#contacto)
  - [Redes](#redes)
  - [Comunidad](#comunidad)

## Descripción

Sorwave permite a los usuarios organizar su biblioteca de música automáticamente mediante la gestión de metadatos y la clasificación de archivos. Esta herramienta es especialmente útil para quienes desean mantener sus colecciones de música ordenadas sin esfuerzo manual.

## Instalación

Puedes instalar Sorwave desde PyPI usando `pip`:

```bash
pip install sorwave
```

## Funciones

### `get_metadata`

```python
from sorwave import get_metadata
```

Esta función extrae metadatos de una canción cuando se le proporciona la ruta del archivo.

#### Ejemplo de Uso

```python
metadata = get_metadata("ruta/a/tu/cancion.mp3")
print(metadata)
```

### `gen_log`

```python
from sorwave import gen_log
```

Esta función genera un log en el directorio principal de todas las canciones y canciones que hay en los subdirectorios. Guarda un archivo JSON con los metadatos de cada canción organizados por artista, álbumes y canciones en orden.

#### Ejemplo de Uso

```python
gen_log("ruta/a/tu/carpeta/de/musica")
```

### `new_log`

```python
from sorwave import new_log
```

Esta función se puede utilizar para crear un nuevo log de actividades o eventos específicos en el sistema de gestión de música.

#### Ejemplo de Uso

```python
new_log("Descripción del evento o actividad")
```

### `filter_artist`

```python
from sorwave import filter_artist
```

Esta función filtra los nombres de los artistas para que sean compatibles con las rutas de Windows sin que pierdan sentido los nombres.

#### Ejemplo de Uso

```python
artista = "Nombre: del*Artista?"
artista_filtrado = filter_artist(artista)
print(artista_filtrado)  # Salida: Nombre_del_Artista
```

### `sort_songs`

```python
from sorwave import sort_songs
```

Esta función organiza la música en sus respectivas carpetas y subcarpetas (artistas, álbumes y canciones)

#### Ejemplo de Uso

```python
sort_songs("ruta/a/tu/carpeta/de/musica")
```

## Características

- **Gestión de Metadatos:** Usa `mutagen` para leer y escribir metadatos en archivos de música.
- **Clasificación de Canciones:** Clasifica canciones basadas en diferentes criterios.
- **Registro de Actividades:** Mantén un registro de las actividades relacionadas con la gestión de la música.
- **Interfaz de Línea de Comandos:** Ejecuta y gestiona tareas directamente desde la línea de comandos.

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Roadmap

- [ ] Añadir soporte para más formatos de archivos de música.
- [ ] Mejorar la documentación con más ejemplos y tutoriales.
- [ ] Integración con servicios de música en línea para metadatos automáticos.

## Preguntas Frecuentes

### ¿Qué formatos de archivos de música son compatibles?

Actualmente, Sorwave soporta archivos MP3 y FLAC. Estamos trabajando para añadir soporte para más formatos en futuras versiones.

### ¿Cómo puedo reportar un problema o solicitar una nueva característica?

Puedes abrir un [issue en GitHub](https://github.com/A-esh/sorwave/issues) para reportar problemas o solicitar nuevas características.

## Licencia

Este proyecto está bajo la Licencia Apache 2.0. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Autor: a-esh  
Email: [abrahamescalona@live.com](mailto:abrahamescalona@live.com)

## Redes

[![GitHub](https://img.shields.io/badge/GitHub-Mi_perfil-5B47ED?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/A-esh) [![Linkedin](https://img.shields.io/badge/Linkedin-Perfil_Profesional-2867B2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/abraham-esh/)
[![X](https://img.shields.io/badge/Twitter-X-000000?style=for-the-badge&logo=x&logoColor=white&labelColor=101010)](https://twitter.com/abraham_esh)

## Comunidad

[![Discord](https://img.shields.io/badge/Discord-Canal_de_la_comunidad-5865F2?style=for-the-badge&logo=discord&logoColor=white&labelColor=101010)](https://discord.gg/eh7BFDB)
