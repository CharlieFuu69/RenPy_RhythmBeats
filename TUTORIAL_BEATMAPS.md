<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>

<h1 align = "center"> Tutorial: ¿Cómo crear beatmaps para Ren'Py RhythmBeats? </h1>

<img align="left" width="35" height="35" src="https://user-images.githubusercontent.com/77955772/195962734-6a3e86be-c5c5-475f-8980-815819b07dfa.png"></img>
#### ¡Pronto estará disponible la herramienta de conversión!

En este documento podrás encontrar todo lo necesario para empezar a crear secuencias de Beatmaps y utilizarlas con **Ren'Py RhythmBeats!**.

Antes de comenzar el tutorial, debes tener las siguientes consideraciones para crear tus beatmaps:

* Los beatmaps <ins>**deben hacerse manualmente**</ins> (al menos por ahora). Esto quiere decir de que debes utilizar algún software musical que te permita crear secuencias con instrumentos, como **FL Studio (Mobile o Desktop), Abbleton**, etc, y crear a oído los patrones de toques.
* Debes descargar la herramienta de conversión **`beatmap.exe`** para hacer las conversiones de beatmaps.

---

## 1. Creando la secuencia del Beatmap en un DAW de producción musical.

En este ítem usaré de ejemplo al DAW **"FL Studio Mobile"**, disponible para Android, iOS y Windows App (UWP).

<p align="center">
  <img width="80%" height="80%" src="https://user-images.githubusercontent.com/77955772/210670964-080e905e-d656-4310-b8df-ca3221a061a7.png">
</p>

> _**Nota:** Si no puedes pagarlo, muchas webs lo tienen disponible de forma gratuíta, pero no voy a agregar URLs hacia esos sitios para que este repositorio no tenga problemas._

Hice un video tutorial de 3 a 4 minutos, donde te explico cómo usar Drums (tambores) en **FL Studio Mobile** para crear beatmaps con taps.

* **[Mira el video aquí! (YouTube)](https://youtu.be/18qIeMV9jNM).**

Sintetizando el video, debes hacer lo siguiente:

* **Crear un canal de Drums con solo 2 instrumentos**, ya que "Ren'Py RhythmBeats!" solo admite 2 pistas en la cascada de notas musicales. Se recomienda usar **secuencias de Drums (tambores o instrumentos de percusión)** para crear los taps de tus beatmaps. Se puede percibir mejor las marcas con estos instrumentos, además, por algo los juegos de ritmo tienen SFX de panderos o de claps al tocar las notas, ¿no crees?

* Agregar un archivo de audio en otro canal para reproducirlo en paralelo y así crear tu secuencia de taps.

* Estabilizar los BPM del metrónomo de la app con los BPM de la canción que quieres incluir en tu juego, así la malla de la línea de tiempo es más precisa para colocar los taps.

* Apagar todos los canales, a excepción del canal de **Drums** y el canal **MASTER** (que no se puede desactivar, ya que es el control maestro del proyecto xd).

* Exportar la secuencia como archivo MIDI, y opcional, guardar el proyecto como FLM para acceder a la secuencia más tarde.


**Para usuarios de "FL Studio Mobile" en Android:**
>_para incluir archivos de audio como una canción a un proyecto de FL Studio Mobile, necesitas colocar ese archivo de audio dentro de la ruta `/storage/emulated/0/FLM User Files`, es decir, esa carpeta es donde DL Studio Mobile puede leer y guardar archivos._
> 
> *(FL Studio crea esa carpeta dentro de tu almacenamiento interno cuando es iniciado por primera vez.)*

---

## 2. ¿Cómo usar la herramienta `beatmap.exe` para convertir archivos MIDI en Beatmaps (.beat)?

`beatmap.exe` es un programa CLI (Command Line Interface) que he creado para facilitar el proceso de conversión de archivos `.mid` (MIDI) a un archivo Beatmap `beat` legible para **"Ren'Py RhythmBeats!"**.
Por el momento este programa debe ser ejecutado desde el terminal o CMD de Windows, pero he creado un tutorial abajo que te puede ayudar a usarlo.

---

##### 2.1.1. ¿CÓMO CONVERTIR UN ARCHIVO MIDI A BEATMAP?

* **Paso 1:**

  Abre tu terminal (CMD). Si no sabes donde está, escribe en la búsqueda **"CMD"** y te aparecerá de inmediato.

  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/210672247-9c714c8b-a1e0-45b0-b31b-da0addfdbf1e.png">


* **Paso 2:**

  Navega desde la línea de comandos hasta el directorio donde está ubicado el archivo `beatmap.exe`. Aquí verás que he navegado hasta una carpeta llamada `my_beatmaps`.

  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/210673543-089cbdef-83d6-4e8c-ab81-0cc773d07779.png">


* **Paso 3:**

  Para realizar la conversión de un archivo MIDI a beatmap, debes ejecutar este comando:

  > ```powershell
  > beatmap.exe /convert
  > ```

* **Paso 4:**

  Cuando se haya ejecutado el comando anterior, la herramienta se iniciará en modo conversión. Cuando esto suceda, se abrirá una ventana del explorador solicitando el archivo `.mid` (MIDI) que quieres convertir. Clickea dos veces y se procesará el archivo MIDI.

  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/210673798-979a659c-731b-4b6d-8db6-1c865ab8b782.png">


* **Paso 5:**

  Si todo salió sin errores, verás una lectura de los pitchs detectados en ese archivo MIDI, seguido de que se abrirá una nueva ventana del explorador donde debes seleccionar el lugar en que debe guardarse el archivo convertido. Por supuesto, debes darle un nombre a ese archivo. La misma herramienta le dará la extensión `.beat` al guardar.

  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/210677021-8323239e-2627-435f-a6b8-b99b879f6b07.png">

Cuando el proceso haya finalizado, verás una lectura con las estadísticas de la secuencia que hiciste, es decir, la cantidad de notas en las pistas (L y R), y el Full Combo que corresponde a la suma de ambas cantidades. Una vez terminado el proceso, ya podrás ver el archivo `.beat` en el directorio del ejecutable.

<img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/210677693-d133b834-862b-4c98-94cd-5d721fa681e0.png">

Este archivo es el que se usa para que el juego pueda mostrar la cascada de notas en pantalla. El contenido son solo números que representan el tiempo donde el jugador debe tocar las teclas.

---

##### 2.1.2. ¿CÓMO OBTENER LAS ESTADÍSTICAS DE UN ARCHIVO BEAT/MIDI, SIN CONVERTIRLO?

La herramienta ofrece un comando de trabajo que abre estos archivos en modo de solo lectura, para mostrar sus estadísticas como la cantidad de notas por pista, el Full Combo y las marcas de tiempo completas.

* **Paso 1:**

  En tu terminal, ejecuta el siguiente comando:
  > ```powershell
  > beatmap.exe /read
  > ```

* **Paso 2:**

  Cuando se haya ejecutado el comando anterior, la herramienta se iniciará en modo de lectura. Cuando esto suceda, se abrirá una ventana del explorador solicitando un archivo `.mid` (MIDI) o `.beat` (beatmap) . Clickea dos veces y se procesará el archivo seleccionado. 
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/210678176-54cb27c4-a4b5-4cea-a341-b942a0afb166.png">


* **Paso 3:**

  Si los archivos fueron procesados correctamente, debería visualizarse las estadísticas del Beatmap.
  Si deseas ver la secuencia completa del beatmap en pantalla, escribe `Y` y pulsa `ENTER`.
  
  > <img width="70%" height="70%" src="https://user-images.githubusercontent.com/77955772/210709429-98c8a065-2fb0-4e7f-9875-ae06835c2011.png">


---
## 3. Errores específicos al convertir un archivo.

Por lo general, los errores en la herramienta son notificados de forma clara. Sin embargo, pueden haber errores emitidos por el procesamiento de archivos MIDI durante la conversión o en actividades de solo lectura. Estos errores son los siguientes:

* **Error `IOError('data byte must be in range 0..127')`:**
  Este error se da generalmente cuando el archivo MIDI está corrupto o ha sido creado con errores. Una solución posible es que vuelvas a exportar el archivo MIDI desde el programa que estás creando las secuencias.
  
* **Error `Conversión abortada. Se detectaron más de 2 pitchs en la secuencia MIDI.`:**
  Este error ocurre cuando creas una secuencia con más de 2 instrumentos en el canal de Drums (u otro canal que estés usando). El sistema rítmico de **Ren'Py RhythmBeats** solo admite 2 pistas para la cascada de notas en pantalla, por lo que solo puedes usar 2 instrumentos dentro del canal de Drums.

---

## 4. Librerías de terceros utilizadas en `beatmap.exe`.

* **pretty_midi:**
  
  `pretty_midi` es una librería para manipulación de datos MIDI. [(Código fuente)](https://github.com/craffel/pretty-midi).

* **pyinstaller:**
  
  `pyinstaller` es una utilidad que permite empaquetar scripts Python (y sus librerías importadas) en un ejecutable de Windows. [(Código fuente)](https://github.com/pyinstaller/pyinstaller).

* **python-tabulate**
  
  `tabulate` es una librería que sirve para dar formato de tablas a datos dentro en una interfaz de línea de comandos. [(Código fuente)](https://github.com/astanin/python-tabulate).
