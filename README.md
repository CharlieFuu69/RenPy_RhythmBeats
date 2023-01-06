[license]: http://creativecommons.org/licenses/by-sa/4.0/
[renpy]: https://renpy.org/
[release]: https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases

[renpy-badge]: https://img.shields.io/badge/Ren'Py-v7.4.11-red?style=for-the-badge&logo=python
[license-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[license-badge]: https://img.shields.io/badge/Licencia-CC--BY--SA%204.0-brightgreen?style=for-the-badge
[status-badge]: https://img.shields.io/badge/Status-Alpha-ff0000?style=for-the-badge
[release-badge]: https://img.shields.io/github/v/release/CharlieFuu69/RenPy_RhythmBeats?style=for-the-badge&logo=github


<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>

<h1 align = "center"> Ren'Py RhythmBeats! </h1>

[![license-badge]][license] [![renpy-badge]][renpy] [![release-badge]][release] ![status-badge]

<h5 align = "center">
    <i>[Sin documentación disponible - ¡Fase Beta en camino!]</i>
</h5>

<img align="left" width="35" height="35" src="https://user-images.githubusercontent.com/77955772/195962734-6a3e86be-c5c5-475f-8980-815819b07dfa.png"/>
<h3> Descargas y más: </h3>

* **¡Descarga el juego DEMO!: Obtén la última Alpha [en este link!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases)**

* **¿No sabes cómo jugar la DEMO? Mira los detalles [presionando Aquí!](DETALLES_DEMO.md)**

* **¿Necesitas un tutorial para crear tus propios Beatmaps en "Ren'Py RhythmBeats!"? [Entra al tutorial aquí!](docs/beatmapping/TUTORIAL_BEATMAPS.md) y descarga la herramienta de conversión [en este link!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v0.2.01a_tool01)**

---

* **ÚLTIMA ACTUALIZACIÓN DE RECURSOS: 31/12/2022**

---
### Detalles importantes de desarrollo:
* **[COMPATIBILIDAD]:**

  No es compatible con Android. Se utilizan teclas de un teclado de PC para las interacciones.
  
  En un futuro intento de portear para Android, este no será compatible con gestos o multitouch (múltiples dedos en el táctil), por lo tanto, no es posible colocar taps simultáneos.
  
* **[RENDIMIENTO]:**

  Los fotogramas objetivo del proyecto apuntan hacia 60 FPS, pero el juego puede caer a 40 o 30 FPS si se utilizan beatmaps con muchas notas visibles en pantalla (500 a 600 Notas cae a 25-30 FPS).
  
* **[REQUERIMIENTOS DE HARDWARE]:**

  El juego de demostración está siendo probada en una máquina con **8 GB** de RAM, procesador de **1.1 GHz** x8 núcleos y **2 GB** de VRAM.

---
### Tasklist:
* **Módulo de Python `rhythmbeats.py`:**

- [x] Agregar ejecución de beatmaps en modo seguro (sin notas fallidas).
- [x] Adaptar código núcleo a módulo de Python importable.
- [x] Realizar pruebas del módulo de Python.
- [x] Agregar método para depuración de actividad.
- [ ] Crear documentación del módulo (En proceso).

* **Juego de demostración "Ren'Py RhythmBeats!":**

- [x] Agregar ajustes de sistema en el panel de configuración del juego.
- [ ] Publicar el código fuente y los Assets del juego DEMO (En proceso).

---
### Registro de actividad reciente:
``` 
[31/Dic/2022 00:42 GMT -3]:
    - Intenté hacer el beatmap de una canción, y la verdad es que 630 notas bastaron para hacer
      caer la tasa de fotogramas a 27 FPS.
      Algo que aprendí de mi juego: Muchas notas = sentencia de muerte XD.
      
[31/Dic/2022 22:02 GMT -3]:
    - Actualización interna emitida (#04) (Actualización: 90 MB | Total: 588 MB).
      Los detalles completos de la actualización se encuentran en la etiqueta "v0.2.01a_upd04".
    - Pruebas piloto del módulo de Python en curso a partir de "v0.2.01a_upd04".
    
[05/01/2023 03:24 GMT -3]:
    ¡Primera actualización de progreso de este año!
    - El código fuente del juego demostrativo está en proceso de subirse.
    - Dentro de poco, Ren'Py RhythmBeats pasará a la etapa de desarrollo Beta. Esto significa que la documentación está en proceso de ser escrita y el módulo podrá ser utilizado por todos.
    - Se tiene prevista una nueva actualización In-Game, donde se agregará una nueva canción al juego (Probablemente... del Project SEKAI).
    
[06/01/2023 16:58 GMT -3]:
    - Terminé mi análisis del juego demostrativo. Cuando los FPS caen, noto una subida en el porcentaje de uso de la CPU.
      ¿Cómo decremento el uso de CPU? ¿Debería intentar hacer paginación a las tuplas del beatmap?...
      
[06/01/2023 19:49 GMT -3]:
    - Se liberó la herramienta de conversión de MIDI a Beatmap, y se liberó el tutorial definitivo para crear beatmaps.
    - Se reorganizarán las documentaciones y tutoriales en carpetas separadas dentro del repositorio.
```

---
### Todos los lanzamientos (DEMO):

|Versión|Detalles|URL|
|---|---|---|
|`v0.2.01a`|Lanzamiento #2 de demostración (Recomendado)|[Descarga completa](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v0.2.01a)|
|`v0.1.19a`|Lanzamiento inicial para fines de pruebas| Descontinuado |

---
### Licencias:
[![license-image]][license]

Este módulo se distribuye bajo la licencia **Creative Commons CC BY-SA v4.0**.

Si quieres usar o modificar este proyecto, te agradecería que me dieras crédito adjuntando la URL de este repositorio :3

