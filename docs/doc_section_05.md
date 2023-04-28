<p align="center">
  <img width="180" height="180" src="https://user-images.githubusercontent.com/77955772/235035814-790e9d30-7aa3-41f5-b5ad-4b112cf89716.png">
</p>
<h6 align = "center"> Documentación de "Ren'Py RhythmBeats!" </h1>
<h1 align = "center"> Sección 5: ¿Cómo crear beatmaps para Ren'Py RhythmBeats?</h5>

---

<p align="center">
  <img align="left" width="30" height="30" src="https://user-images.githubusercontent.com/77955772/195962734-6a3e86be-c5c5-475f-8980-815819b07dfa.png"/>
  <h4>
    ¡Descargas disponibles! Obtén el  <i>Kit de desarrollo de Ren'Py RhythmBeats!</i> desde <a href="https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.02.1b_module">este lanzamiento</a>
  </h4>
</p>

---

En este documento podrás encontrar un tutorial para que puedas crear secuencias de Beatmaps y utilizarlas con **Ren'Py RhythmBeats!**

Antes de comenzar el tutorial, debes tener las siguientes consideraciones para crear tus beatmaps:

* Los beatmaps <ins>**deben hacerse manualmente**</ins> (al menos por ahora). Esto quiere decir de que debes utilizar algún software musical que te permita crear secuencias con instrumentos, como **FL Studio (Mobile o Desktop), Abbleton**, etc, y crear a oído los patrones de toques.

* Debes descargar la herramienta de conversión **`beatmap.exe`** para hacer las conversiones de beatmaps. Arriba está el link de descarga.

---

<h3 align="center">1. Creando la secuencia del Beatmap en un DAW de producción musical.</h3>

En este ítem usaré de ejemplo al DAW **"FL Studio Mobile"**, disponible para Android, iOS y Windows App (UWP).

<p align="center">
  <img width="80%" height="80%" src="https://user-images.githubusercontent.com/77955772/210670964-080e905e-d656-4310-b8df-ca3221a061a7.png">
</p>

> _**Nota:** Si no puedes pagarlo, he incluido el APK + OBB de FL Studio Mobile en el kit de creación de beatmaps. Shhhh... es un secreto XD._

Hice un video tutorial de 3 a 4 minutos, donde te explico cómo usar Drums (tambores) en **FL Studio Mobile** para crear beatmaps.

<p align="center">
  <a href="https://youtu.be/18qIeMV9jNM">
    <img width="50%" height="50%" src="https://i.ytimg.com/vi/18qIeMV9jNM/maxresdefault.jpg" title="Tutorial RhythmBeats!: Crear beatmaps para tus canciones con FL Studio Mobile!"/>
  </a>
</p>
<h6 align="center">
  <i>
  <a href="https://youtu.be/18qIeMV9jNM">[Toca aquí o en la miniatura para ver el video]</a>
  </i>
</h6>

Sintetizando el video, debes hacer lo siguiente:

* **Crear un canal de Drums con solo 2 instrumentos**, ya que "Ren'Py RhythmBeats!" solo admite 2 pistas en la cascada de notas musicales. Se recomienda usar **secuencias de Drums (tambores o instrumentos de percusión)** para crear los taps de tus beatmaps. Se puede percibir mejor las marcas con estos instrumentos, además, por algo los juegos de ritmo tienen SFX de panderos o de claps al tocar las notas, ¿no crees?

* Agregar un archivo de audio en otro canal para reproducirlo en paralelo y así crear tu secuencia de taps.

* Sincronizar los BPM del metrónomo con los BPM de la canción que quieres incluir en tu juego. De esa forma la malla de la línea de tiempo queda más alineado para colocar los taps.

* Apagar todos los canales, a excepción del canal de **Drums** y el canal **MASTER** (que no se puede desactivar, ya que es el control maestro del proyecto xd).

* Exportar la secuencia como archivo MIDI, y opcional, guardar el proyecto como FLM para acceder a la secuencia más tarde.

**Para usuarios de "FL Studio Mobile" en Android:**

> _para incluir archivos de audio como una canción a un proyecto de FL Studio Mobile, necesitas colocar ese archivo de audio dentro de la ruta `/storage/emulated/0/FLM User Files`, pues esa carpeta es donde FL Studio Mobile puede leer y guardar archivos._
> 
> *(FL Studio crea esa carpeta dentro de tu almacenamiento interno cuando es iniciado por primera vez.)*

---

<h3 align="center">2. ¿Cómo usar la herramienta `beatmap.exe` para convertir archivos MIDI en Beatmaps (.beat)?</h3>

`beatmap.exe` es un programa CLI (Command Line Interface) que he creado para facilitar el proceso de conversión de archivos `.mid` (MIDI) hacia un archivo `.beat` (Beatmap) legible para **"Ren'Py RhythmBeats!"**. Este programa está incluido en el último lanzamiento del módulo de **Ren'Py RhythmBeats!**

Aquí abajo he creado un tutorial que te puede ayudar a usarlo.

---

#### 2.1. ¿Cómo convertir un archivo MIDI a Beatmap?

* **Paso 1:**
  
  Descarga el Kit de desarrollo de Ren'Py RhythmBeats! desde el **[Pre-Lanzamiento v1.02.1b](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.02.1b_module)**.

* **Paso 2:**
  
  Después de descargar el archivo `RhythmBeats_Kit_v1.02.1b.zip`, extrae su contenido en una carpeta que te sea accesible.
  
  Dentro de la carpeta `RhythmBeats Kit v1.02.1b` encontrarás las herramientas para crear beatmaps, y el módulo de acción rítmica:

  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224456505-510c52ea-183d-4f0d-9965-8afe7d4dc1d8.png">
  >
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224456535-8fcf5c30-9c71-4af5-be68-0d6d6428c209.png">

* **Paso 3:**
  
  Busca el ejecutable `beatmap.exe` dentro de la carpeta `Beatmapping Tools` y haz doble click sobre el. Debería aparecerte una ventana de terminal similar a esta:
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224456707-82ab2c4e-9f5f-4260-ace7-f31a3426c772.png">

* **Paso 4:**

  Para convertir una secuencia MIDI a BEATMAP, escribe el comando `convert`. Se desplegará una ventana del explorador para cargar el archivo MIDI en el programa. Selecciona el archivo haciendo doble click sobre el:
  
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224457017-24446196-ccae-4cdf-8218-d2ed3ce2b1de.png">

* **Paso 5:**
  
  Si todo salió sin errores, verás una lectura de los pitchs detectados en ese archivo MIDI seguido de que se abrirá una nueva ventana del explorador, donde debes seleccionar el lugar en que debe guardarse el archivo convertido. Por supuesto, debes darle un nombre a ese archivo. La misma herramienta le dará la extensión `.beat` al guardar.
  
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224457110-84f9f5b6-9288-44f8-9bc1-31ee7cac3af7.png">

Cuando el proceso haya finalizado verás una lectura con las estadísticas de la secuencia que hiciste, es decir, la **cantidad de notas en las pistas (L y R)**, y el **Full Combo** que corresponde a la suma de ambas cantidades. Una vez terminado el proceso, ya podrás ver el archivo `.beat` en el directorio donde lo guardaste.

<img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224457212-66f5f2cd-5698-47f2-be60-f2451bf0417c.png">

Este archivo `.beat` es el que se usa para que el juego pueda mostrar la cascada de notas en pantalla. El contenido son solo números que representan el tiempo donde el jugador debe tocar las teclas.

---

#### 2.2. ¿Cómo obtener las estadísticas de un archivo `.beat` o `.midi` sin convertirlo?

La herramienta ofrece un comando de trabajo que abre estos archivos en modo de solo lectura, para mostrar sus estadísticas como la cantidad de notas por pista, el Full Combo y las marcas de tiempo completas.

* **Paso 1:**
  
  Ejecuta el programa `beatmap.exe` y escribe el comando `read`. Se abrirá una ventana del explorador solicitando un archivo `.beat` o `.midi`. Cuando se abra esta ventana, selecciona el archivo que debe cargarse al programa:
  
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224457563-2007bd09-74f6-405d-a50d-062520ebfde0.png">

* **Paso 2:**
  
  Si los archivos fueron procesados correctamente, debería visualizarse las estadísticas del Beatmap.
  Para ver una tabla con el índice y la secuencia completa del beatmap en pantalla, escribe `Y` y pulsa `ENTER`.
  
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/224457663-1d531612-eac6-4bc5-93a9-a170e4bc1105.png">

---

<h3 align="center">3. Errores específicos al convertir un archivo.</h3>

Por lo general, los errores en la herramienta son notificados de forma clara. Sin embargo, pueden haber errores emitidos por el procesamiento de archivos MIDI durante la conversión o en actividades de solo lectura. Estos errores son los siguientes:

* **Error "`IOError('data byte must be in range 0..127')`":**
  Este error se da generalmente cuando el archivo MIDI está corrupto o ha sido creado con errores. Una solución posible es que vuelvas a exportar el archivo MIDI desde el programa que estás creando las secuencias.

* **Error "`Conversión abortada. Se detectaron más de 2 pitchs en la secuencia MIDI.`":**
  Este error ocurre cuando creas una secuencia con más de 2 instrumentos en el canal de Drums (u otro canal que estés usando). El sistema rítmico de **Ren'Py RhythmBeats** solo admite 2 pistas para la cascada de notas en pantalla, por lo que solo puedes usar 2 instrumentos dentro del canal de Drums.

---

<h3 align="center">4. Librerías de terceros utilizadas en "beatmap.exe".</h3>

* **[pretty_midi](https://github.com/craffel/pretty-midi):**
  
  `pretty_midi` es una librería para manipulación de datos MIDI.

* **[python-tabulate](https://github.com/astanin/python-tabulate):**
  
  `tabulate` es una librería que sirve para dar formato de tablas a datos dentro en una interfaz de línea de comandos.

* **[pyinstaller:](https://github.com/pyinstaller/pyinstaller):**
  
  `pyinstaller` es una utilidad que permite empaquetar scripts Python (y sus librerías importadas) en un ejecutable de Windows.

---

Hasta aquí llega la documentación de **Ren'Py RhythmBeats!**

Si tienes dudas acerca de cómo utilizar el módulo, o encontraste un error fatal en el funcionamiento, puedes abrir un post en la sección **"Issues"** del repositorio :3

---

<h5 align = "center"> ¡Ya has recorrido toda la documentación! ¿Qué quieres hacer ahora? </h5>

* **Ir al [Inicio del repositorio.](https://github.com/CharlieFuu69/RenPy_RhythmBeats)**
* **Descargar el [Juego demostrativo de Ren'Py RhythmBeats! (Beta).](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/latest)**
* **Descargar el [Kit de desarrollo de Ren'Py RhythmBeats!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.02.1b_module)**


