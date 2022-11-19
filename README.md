# RenPy_Rhythm_Game
[Sin documentación] Sistema de acción rítimica para juegos Ren'Py

---

Este proyecto no será documentado hasta que sea lo suficientemente estable para su implementación.

> **ADVERTENCIA: NO USAR EN PROYECTOS EN FASE DE PRODUCCIÓN BASADOS EN REN'PY.**

---
### Detalles importantes de desarrollo:
* _**[COMPATIBILIDAD]:** No es compatible con Android. Se utilizan teclas de un teclado de PC para las interacciones._
* _**[COMPATIBILIDAD]:** En un futuro intento de portear para Android, este no será compatible con gestos o multitouch (múltiples dedos en el táctil), por lo tanto, no es posible colocar taps simultáneos._
* _**[RENDIMIENTO]:** Los fotogramas objetivo del proyecto apuntan hacia 60 FPS, pero el juego puede caer a 40 o 30 FPS si se utilizan beatmaps con muchas notas (marcas de tiempo), o si se incluyen 2DMVs._
* _**[RENDIMIENTO]:** El sonido de los taps puede retrasarse o superponerse si se tocan notas muy repetidas._
* _**[BEATMAPS]:** Aún no hay documentación para generar los beatmaps. Los beatmaps se crean usando un DAW de producción musical, se exporta la secuencia a un archivo MIDI y se obtienen las marcas de tiempo de cada tap al procesar el archivo MIDI._

---
### Tasklist:
- [x] Lectura y procesado de archivos `.beat` (Beatmap).
- [x] Adición de umbral de detección (Threshold) y compensación de retraso (Offset).
- [x] Detector de beatmap terminado.
- [x] Adición de capa para 2DMV (basado en video).
- [x] Adición de conteo de Combo.
- [x] Adición de conteo de notas perfectas y fallidas (BRUH).
- [x] Adición de cálculo de precisión promedio.
- [x] Umbral de detección fijado en 100 ms (-100/+100).
- [x] Adición de menú de selección de pistas musicales.
- [x] Adición de pantallas de inicio de pista, pista finalizada (Full Combo/Show Clear/Show Failed), y resultados finales de la partida.
- [ ] Reorganizar metadatos de pistas musicales.
- [ ] Modificar estructura de archivos `.beat`
