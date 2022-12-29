[license]: http://creativecommons.org/licenses/by-sa/4.0/
[renpy]: https://renpy.org/
[release]: https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases

[renpy-badge]: https://img.shields.io/badge/Motor%20Gráfico-Ren'Py-red?style=for-the-badge
[license-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[license-badge]: https://img.shields.io/badge/Licencia-CC--BY--SA%204.0-brightgreen?style=for-the-badge
[status-badge]: https://img.shields.io/badge/Status-Alpha-blue?style=for-the-badge
[release-badge]: https://img.shields.io/github/v/release/CharlieFuu69/RenPy_RhythmBeats?style=for-the-badge&logo=github


<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>

<h1 align = "center"> Ren'Py RhythmBeats! </h1>

[![license-badge]][license] [![renpy-badge]][renpy] [![release-badge]][release] ![status-badge]

<h5 align = "center">
    <i>[Sin documentación disponible - Alpha en desarrollo]</i>
</h5>

<img align="left" width="35" height="35" src="https://user-images.githubusercontent.com/77955772/195962734-6a3e86be-c5c5-475f-8980-815819b07dfa.png"></img>
#### ¡Descarga de la DEMO!: Obtén la más reciente versión del juego demostrativo Alpha [Presionando Aquí!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases)

* **ÚLTIMA ACTUALIZACIÓN INTERNA: 28/12/2022**

* **Mira los detalles del juego demostrativo [Presionando Aquí!](DETALLES_DEMO.md)**

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
    
[28/Dic/2022 21:45 GMT -3]:
    - Se está preparando una actualización para añadir una nueva pista jugable en la DEMO.
    
[29/Dic/2022 02:10 GMT -3]:
    - Actualización interna emitida. (Actualización: 67 MB | Total: 512 MB)
    - Construcción experimental del módulo de Python en curso.
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

