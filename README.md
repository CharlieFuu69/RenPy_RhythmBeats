[license]: http://creativecommons.org/licenses/by-sa/4.0/
[renpy]: https://renpy.org/
[release]: https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases

[renpy-badge]: https://img.shields.io/badge/Ren'Py-v7.4.11-red?style=for-the-badge&logo=python
[license-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[license-badge]: https://img.shields.io/badge/Licencia-CC--BY--SA%204.0-brightgreen?style=for-the-badge
[status-badge]: https://img.shields.io/badge/Status-Beta-000077?style=for-the-badge
[release-badge]: https://img.shields.io/github/v/release/CharlieFuu69/RenPy_RhythmBeats?style=for-the-badge&logo=github


<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>

<h1 align = "center"> Ren'Py RhythmBeats! </h1>

[![license-badge]][license] [![renpy-badge]][renpy] [![release-badge]][release] ![status-badge]

<h5 align = "center">
    <i>[El módulo ha sido liberado y documentado - ¡Fase beta iniciada!]</i>
</h5>

### ¡Bienvenido(a) al repositorio!

Te contaré un poco acerca de qué trata todo esto.

**Ren'Py RhythmBeats!** es un sistema de Acción Rítmica de 2 pistas que permite integrar la mecánica básica de un juego de ritmo en una novela visual hecha en Ren'Py. Es raro ver novelas visuales con minijuegos de ritmo, pero es una idea loca que tuve a raíz de mi fanatismo por los juegos de ritmo.

En fin, este sistema de Acción Rítmica es un módulo de Python que provee a tu juego la lógica de los juegos de ritmo, en cuanto al reconocimiento de toques de un jugador y la lectura de un mapa de notas.

---

<img align="left" width="35" height="35" src="https://user-images.githubusercontent.com/77955772/195962734-6a3e86be-c5c5-475f-8980-815819b07dfa.png"/>
<h3> Descargas y más: </h3>

* **LANZAMIENTO DEL MÓDULO DE REN'PY RHYTHMBEATS (BETA):**

  ¿Quieres empezar a implementar este sistema rítmico en tu proyecto? ¡Revisa estas URLs!
  * **Descarga la última versión de [Ren'Py RhythmBeats! v1.00.1b](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.00.1b_module).**
  * **Entérate de cómo implementar el sistema en la [documentación de Ren'Py RhythmBeats!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/docs/doc_mainpage.md).**
  
* **JUEGO DEMOSTRATIVO DE REN'PY RHYTHMBEATS!:**
  ¿Quieres pasar el rato jugando la demostración de Ren'Py RhythmBeats? ¡Hay más de 10 canciones con 2DMV!
  * **¡Descarga el juego DEMO de Ren'Py RhythmBeats [en este link](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.00.1b_global01)!**
  * **¿No sabes cómo jugar la DEMO? Mira los detalles [presionando aquí](DETALLES_DEMO.md)!**

---
### Tasklist:
* **Módulo de Python `rhythmbeats.py`:**

- [x] Agregar ejecución de beatmaps en modo seguro (sin notas fallidas).
- [x] Adaptar código núcleo a módulo de Python importable.
- [x] Realizar pruebas del módulo de Python.
- [x] Agregar método para depuración de actividad.
- [x] Crear documentación del módulo.

* **Juego de demostración "Ren'Py RhythmBeats!":**

- [x] Agregar ajustes de sistema en el panel de configuración del juego.
- [ ] Publicar el código fuente y los Assets del juego DEMO (En proceso).

---
### Registro de actividad reciente:
```     
[12/01/2023 04:26 GMT -3]:
    - OOOOH MIERDA! Logré incrementar los fotogramas desde 25 a 45 FPS gracias al SpriteManager(),
      pero aún hay un problema... LAS NOTAS SE ME SIGUEN ALINEANDO EN LA ESQUINA SUPERIOR IZQUIERDA
      PUTA MADREEEEE!!!
      
[13/01/2023 05:44 GMT -3]:
    - Se emitió la actualización global v0.3.01a, junto con la adición de 3 nuevas pistas musicales.
      Tamaño de actualización de recursos: 96.75 MB.
      Tamaño total de recursos: 671.88 MB.
      
[27/01/2023 04:48 GMT -3]:
    - Me rindo con los SpriteManager(). Solucionó el tema de los FPS pero me causa otros problemas.
    - He terminado de escribir la documentación!!!
      Ahora solo me falta preparar la liberación del módulo y del código fuente del juego
      demostrativo, que siendo sincero, lo hice en tiempo récord XD.
      
[28/01/2022 03:48 GMT -3]:
    - Finalmente se ha liberado la primera versión del módulo de Ren'Py RhythmBeats!
      Este lanzamiento marca la transición de Fase Alpha a Fase Beta.
```

---
### Todos los lanzamientos del módulo (Beta):

|Versión|Detalles|URL|
|---|---|---|
|`v1.00.1b`|Módulo de Ren'Py RhythmBeats - Lanzamiento #1! (Recomendado)|[Descarga completa](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.00.1b_module)|

---
### Todos los lanzamientos del juego demostrativo (Beta):

|Versión|Detalles|URL de descarga|
|---|---|---|
|`v1.00.1b`|Ren'Py RhythmBeats! Game - Beta #1|[Descargar aquí](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.00.1b_global01)|
|`v0.3.01a`|Ren'Py RhythmBeats! Game - Lanzamiento Alpha|[Descontinuado]|

---
### Licencias:
[![license-image]][license]

Este juego demostrativo/módulo, se distribuye bajo la licencia **Creative Commons CC BY-SA v4.0**.

Si quieres usar o modificar este proyecto, te agradecería que me dieras crédito adjuntando la URL de este repositorio :3

