[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[renpy]: https://renpy.org/

[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/Licencia-CC--BY--SA%204.0-brightgreen
[renpy-shield]: https://img.shields.io/badge/Motor%20Gráfico-Ren'Py-red
[development_status]: https://img.shields.io/badge/Fase%20de%20desarrollo-Alpha-blue

<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>

<h1 align = "center"> Ren'Py RhythmBeats! </h1>

[![cc-by-sa-shield]][cc-by-sa] [![renpy-shield]][renpy] ![development_status]

<h5 align = "center">
    <i>[Sin documentación disponible - Alpha en desarrollo]</i>
</h5>

<img align="left" width="35" height="35" src="https://user-images.githubusercontent.com/77955772/195962734-6a3e86be-c5c5-475f-8980-815819b07dfa.png"></img>
#### ¡Descargas disponibles!: Obtén la más reciente versión de demostración Alpha [Presionando Aquí!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v0.2.01a)

---
### 1. ¿Cómo se juega la versión de demostración de Ren'Py RhythmBeats?

<img align="center" src="https://user-images.githubusercontent.com/77955772/209073140-0bbd0583-4c06-47c4-a768-b42c4b7e660a.png"></img>
<h4 align = "center"> [Interfaz de juego - 2DMV: Highlight] </h4>

Las teclas asignadas para jugar son la `C` para la pista izquierda, y `M` para la pista derecha.

#### INDICADOR DE HP:
> En la esquina superior izquierda se indica tu <ins>**"HP"**</ins> durante la partida, que básicamente señala cuántas notas puedes fallar como máximo.

#### INDICADOR DE PRECISIÓN:
> En la esquina superior derecha hay un indicador de precisión en tiempo real, que señala la diferencia media (en milisegundos) a la que aciertas las notas respecto del beatmap. Mientras más cerca estés de `0ms`, significará que tocas las notas con una precisión casi perfecta.
> Una flecha **"◂"** indicará que tienes tendencia a tocar un poco antes de lo esperado, mientras que la flecha **"▸"** indicará que tienes tendencia a tocar un poco más tarde.

#### CALIBRACIÓN MANUAL:
> En caso de que tengas problemas de sincronización con la caída de las notas, puedes calibrar manualmente cualquier desfase desde el botón **"⚙"** en el menú de pistas musicales.

---
### Lista de pistas musicales utilizadas para testeo:

Aquí abajo se listarán las pistas musicales que hasta el momento tienen beatmap creado y 2DMV añadido.

* **Project SEKAI: COLORFUL STAGE / Vocaloid:**

|Pistas musicales|Artistas|BPM|Full Combo|2DMV|
|---|---|---|---|---|
|Highlight|Kira Ft. Hatsune Miku|130|253 notas|Si (Clip original)|
|Gunjou Sanka (SEKAI Ver.)|Hatsune Miku, Ichika Hoshino... (4 más)|168|307 notas|Si (3DMV Project Sekai)|
|Hand in Hand|Hatsune Miku / Kz|128|381 notas|No|


* **Love Live!:**

|Pistas musicales|Artistas/Unidad|BPM|Full Combo|2DMV|
|---|---|---|---|---|
|Mirai Bokura wa Shitteru yo|Aqours|181|229 notas|Si (Love Live! Sunshine!! S2 OP)|
|MOMENT RING|μ's|196|368 notas|Si (3DMV Love Live! SIFAS)|
|Ryouran! Victory Road|Love Live! Nijigasaki High School Idol Club|135|580 notas|Si (Fanmade: Henry L.)|
|Snow Halation|μ's|173|305 notas|Si (3DMV Love Live! SIFAS)|
|NEO SKY, NEO MAP!|Love Live! Nijigasaki High School Idol Club|142|276 notas|Si (3DMV Love Live! SIFAS)|

* **Otras pistas:**

|Pistas musicales|Artistas|BPM|Full Combo|2DMV|
|---|---|---|---|---|
|The Anthem (Der Alte)|Dimitri Vegas & Like Mike|140|535 notas|No|

---
### Detalles importantes de desarrollo:
* _**[COMPATIBILIDAD]:** No es compatible con Android. Se utilizan teclas de un teclado de PC para las interacciones._
* _**[COMPATIBILIDAD]:** En un futuro intento de portear para Android, este no será compatible con gestos o multitouch (múltiples dedos en el táctil), por lo tanto, no es posible colocar taps simultáneos._
* _**[RENDIMIENTO]:** Los fotogramas objetivo del proyecto apuntan hacia 60 FPS, pero el juego puede caer a 40 o 30 FPS si se utilizan beatmaps con muchas notas (marcas de tiempo), o si se incluyen 2DMVs._
* _**[REQUERIMIENTOS DE HARDWARE]:** El juego de demostración está siendo probada en una máquina con **8 GB** de RAM, procesador de **1.1 GHz** x8 núcleos y **2 GB** de VRAM._

---
### Tasklist:
* **Módulo de Python `rhythmbeats.py`:**

- [x] Adición de umbral de detección (Threshold) y compensación de timing (Offset).
- [x] Detector de beatmap terminado.
- [x] Adición de conteo de Combo.
- [x] Adición de conteo de notas perfectas y fallidas (BRUH XD).
- [x] Adición de cálculo de precisión promedio.
- [x] Umbral de detección fijado en 100 ms (-100/+100).
- [ ] Adaptar código núcleo a módulo de Python importable.
- [ ] Crear documentación del módulo.

* **Juego de demostración "Ren'Py RhythmBeats!":**

- [x] Lectura y procesado de archivos `.beat` (Beatmap).
- [x] Adición de capa para 2DMV (basado en video).
- [x] Adición de menú de selección de pistas musicales.
- [x] Adición de pantallas de inicio de pista, pista finalizada (Full Combo/Show Clear/Show Failed), y resultados finales de la partida.
- [x] Reorganizar metadatos de pistas musicales.
- [x] Modificar estructura de archivos `.beat`
- [x] Agregar sistema de descarga de pistas musicales
- [x] Agregar panel de calibración manual.
- [x] Agregar control de Alpha para atenuar manualmente el fondo de 2DMVs.
- [ ] Publicar el código fuente y los Assets del juego DEMO.

---
### Registro de desarrollo:
```
[19/Nov/2022 23:52 GMT -3]:
    - Calibración de todos los beatmaps para alinear desfase a 0ms.
    
[20/Nov/2022 01:09 GMT -3]:
    - Adición de panel de calibración para ajustar la diferencia de milisegundos de retraso o adelanto.
    
[20/Nov/2022 02:15 GMT -3]:
    - Eliminación del sonido para los taps, pues su retraso resulta ser extremadamente molesto.
    
[20/Nov/2022 18:10 GMT -3]:
    - Adición de control de atenuación para 2DMVs.
    
[04/Dic/2022 20:05 GMT -3]:
    - Fallo encontrado: El panel de calibración manual no sirve de nada.
    
[04/Dic/2022 20:38 GMT -3]:
    - El sistema de calibración fue corregido y está operando correctamente.
    
[16/Dic/2022 14:33 GMT -3]:
    - Agregando 2 nuevas pistas de demostración. Serán reveladas cuando se publique una nueva release del juego de demostración.
    
[18/Dic/2022 02:35 GMT -3]:
    - Clasificando los archivos de cada pista musical en paquetes RPA individuales.
    - Integrando sistema de descarga/actualización por lotes de pistas musicales jugables.
    
[22/Dic/2022 04:04 GMT -3]:
    - Se ha terminado de calibrar los mapas y las canciones.
    - Versión v0.2.01a publicada en GitHub.
    
[27/Dic/2022 19:41 GMT -3]:
    - Actualización completa del README.md.
```

---
### Todos los lanzamientos:

|Versión|Detalles|URL|
|---|---|---|
|`v0.2.01a`|Lanzamiento #2 de demostración (Recomendado)|[Descarga completa](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v0.2.01a)|
|`v0.1.19a`|Lanzamiento inicial para fines de pruebas| [Juego principal](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/download/v0.1.19/Rhythm_Game-1.0-win.zip) - [Beatmaps](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/download/v0.1.19/beatmaps.zip)|

---
### Licencias:
## 3. Licencias:
[![cc-by-sa-image]][cc-by-sa]

Este módulo se distribuye bajo la licencia **Creative Commons CC BY-SA v4.0**.

Si quieres usar o modificar este proyecto, te agradecería que me dieras crédito adjuntando la URL de este repositorio :3

