<p align="center">
  <img width="180" height="180" src="https://user-images.githubusercontent.com/77955772/235035814-790e9d30-7aa3-41f5-b5ad-4b112cf89716.png">
</p>
<h6 align = "center"> Documentación de "Ren'Py RhythmBeats!" </h1>
<h1 align = "center"> Sección 2: Rendimiento y requerimientos de tu juego </h5>

Con el uso de este sistema de acción rítmica, es posible que tu juego experimente algunos cambios en los requerimientos mínimos, ya que usualmente no se implementan sistemas como este en una novela visual.

Esta sección te entregará detalles estimados de lo que tu juego podría requerir para operar fluidamente utilizando **Ren'Py RhythmBeats!**

---

<h3 align="center">1. Compatibilidad de Ren'Py RhythmBeats.</h4>

Actualmente el sistema rítmico de **Ren'Py RhythmBeats!** posee compatibilidad para teclados de PC y pantallas táctiles de dispositivos Android. Por el momento, el sistema posee una mejor capacidad de reacción en un teclado físico, ya que aún está en fase de desarrollo la habilidad de detección en pantallas táctiles.

Las interacciones (por defecto) del sistema rítmico se ejecutan con las teclas `C` (pista izquierda) y `M` (pista derecha) en teclados físicos, mientras que para pantallas táctiles, el área izquierda y derecha acierta las notas de cada pista respectivamente.

---

<h3 align="center">2. Requisitos mínimos de Ren'Py RhythmBeats.</h3>

Este sistema de acción rítmica, y el **[Juego demostrativo de Ren'Py RhythmBeats](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/latest)**, han sido desarrollado en una máquina con las siguientes especificaciones técnicas:

|             | Detalles                                                |
| ----------- | ------------------------------------------------------- |
| **Equipo:** | HP Pavilion an1010la.                                   |
| **CPU:**    | Intel Core i5 10° generación (1.1 - 3.6 GHz) Quad-Core. |
| **RAM:**    | 8 GB.                                                   |
| **GPU:**    | Intel UHD Graphics (3.9 de memoria).                    |

Como tal, es un hardware bastante modesto, por lo que no puedo negar que igual experimento caídas de FPS.

Estas especificaciones vendrían siendo el equivalente de los requisitos mínimos para ejecutar el sistema rítmico de forma casi fluida.

---

<h3 align="center">3. Consideraciones de rendimiento de Ren'Py RhythmBeats.</h3>

El apartado que computa las interacciones del jugador funciona de forma fluida, pero la implementación gráfica experimenta caídas de FPS cuando una pista posee demasiadas notas musicales.

Las estadísticas de rendimiento que he obtenido en mi máquina (especificaciones técnicas del ítem 2) sugieren que el decremento de la performance del juego puede empezar a ser notoria cuando se utilizan <ins>**canciones con 500 o más notas**</ins>.

Aquí abajo adjunto un gráfico de líneas que indica la curva de FPS en función de la densidad de notas en un beatmap:

<p align="center"><img width="90%" height = "90%" src="img/doc_image_04.png"/></p>
<h6 align = "center"> <i>Gráfico: Curva de FPS con determinadas cantidades de notas de un beatmap.</i> </h6>

Como ya te has dado cuenta, <ins>**los FPS tienden a caer cuando se cargan beatmaps con muchas notas musicales**</ins>. Esto no es por culpa del sistema de reconocimiento de taps como tal, sino que del algoritmo utilizado para el apartado gráfico en Ren'Py.

En dispositivos Android, el lag puede ser un poco mayor con beatmaps que tienen una alta densidad de notas, pero eso ya se escapa de mis manos. Lamentablemente Ren'Py (el motor) no es tan eficiente si hablamos de rendimiento. Python no es un lenguaje rápido, asi que de todos modos no me sorprende demasiado.

---

<h4 align = "center"> ¡Navega por la documentación! </h4>
<h5 align = "center"> <a href="doc_section_01.md"> Ir a la Sección 1 </a> | <a href="doc_section_03.md"> Ir a la Sección 3</a> </h5>
