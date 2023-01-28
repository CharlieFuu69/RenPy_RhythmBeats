<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>
<h6 align = "center"> Documentación de "Ren'Py RhythmBeats!" </h1>
<h1 align = "center"> Sección 2: Rendimiento y requerimientos de tu juego </h5>

Con el uso de este sistema de acción rítmica, es posible que tu juego experimente algunos cambios en los requerimientos mínimos, ya que usualmente no se implementan sistemas como este en una novela visual.

Esta sección te entregará detalles estimados de lo que tu juego podría requerir para operar fluidamente utilizando **Ren'Py RhythmBeats!**

---

<h3 align="center">1. Compatibilidad de Ren'Py RhythmBeats.</h4>

Por el momento, las capacidades de este sistema de acción rítmica se reducen a **<u>juegos hecho solo para PC</u>**, ya que el medio para interactuar con las canciones es un teclado físico. La compatibilidad con pantallas táctiles (móvil) puede ser un poco engorroso de implementar, pero hay una pequeña posibilidad de hacer esto realidad en el futuro.

Por el momento, el módulo trabaja con las teclas `C` y `M` para interactuar con las notas que caen por la pantalla. La disposición de las teclas es equivalente a la posición de los carriles de notas: la `C` es para acertar notas del carril izquierdo, mientras que la `M` es para acertar las notas del carril derecho.

---

<h3 align="center">2. Requisitos mínimos de Ren'Py RhythmBeats.</h3>

Este sistema de acción rítmica, y el **[Juego demostrativo de Ren'Py RhythmBeats](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v0.3.01a)**, han sido desarrollado en una máquina con las siguientes especificaciones técnicas:

|             | Detalles                                                |
| ----------- | ------------------------------------------------------- |
| **Equipo:** | HP Pavilion an1010la.                                   |
| **CPU:**    | Intel Core i5 10° generación (1.1 - 3.6 GHz) Quad-Core. |
| **RAM:**    | 8 GB.                                                   |
| **GPU:**    | Intel UHD Graphics (3.9 de memoria).                    |

Como tal, es un hardware bastante modesto, por lo que no puedo negar que igual experimento caídas de FPS.

Estas especificaciones vendrían siendo el equivalente de los requisitos mínimos para ejecutar el sistema rítmico de forma casi fluida.

---

<h3 align="center">3. Notas de rendimiento de Ren'Py RhythmBeats.</h3>

El apartado que computa las interacciones del jugador funciona de forma fluida, pero la implementación gráfica experimenta caídas de FPS cuando una pista posee demasiadas notas musicales.

Las estadísticas de rendimiento que he obtenido en mi máquina (especificaciones técnicas del ítem 2) sugieren que el decremento de la performance del juego puede empezar a ser notoria cuando se utilizan <ins>**canciones con 500 o más notas**</ins>.

Aquí abajo adjunto un gráfico de líneas que indica la curva de FPS en función de la densidad de notas en un beatmap:

<p align="center"><img width="90%" height = "90%" src="img/doc_image_04.png"/></p>
<h6 align = "center"> <i>Gráfico: Curva de FPS con determinadas cantidades de notas de un beatmap.</i> </h6>

Como ya te has dado cuenta, <ins>**los FPS tienden a caer cuando se cargan beatmaps con muchas notas musicales**</ins>. Esto no es por culpa del sistema de reconocimiento de taps como tal, sino que del algoritmo utilizado para el apartado gráfico en Ren'Py.

La cantidad mínima de FPS registrada en los testeos del [Juego demostrativo de Ren'Py RhythmBeats!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v0.3.01a) ha sido de 24 FPS con canciones de 620 notas + capa de video (2DMV), registrando también un leve aumento en el uso de CPU, por lo que recomendaría no emocionarte creando beatmaps complejos =(

---

<h4 align = "center"> ¡Navega por la documentación! </h4>
<h5 align = "center"> <a href="doc_section_01.md"> Ir a la Sección 1 </a> | <a href="doc_section_03.md"> Ir a la Sección 3</a> </h5>
