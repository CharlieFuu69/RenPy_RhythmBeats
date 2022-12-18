<h1 align = "center"> Ren'Py RhythmBeats! </h1>

<h5 align = "center">
    <i>[Sin documentación disponible]</i>
    
    Sistema de acción rítmica simple para juegos basados en el motor Ren'Py.
</h5>

---

Este proyecto no será documentado hasta que sea lo suficientemente estable para su implementación.

> **ADVERTENCIA: NO USAR EN PROYECTOS EN FASE DE PRODUCCIÓN.**

---
### Detalles importantes de desarrollo:
* _**[COMPATIBILIDAD]:** No es compatible con Android. Se utilizan teclas de un teclado de PC para las interacciones._
* _**[COMPATIBILIDAD]:** En un futuro intento de portear para Android, este no será compatible con gestos o multitouch (múltiples dedos en el táctil), por lo tanto, no es posible colocar taps simultáneos._
* _**[RENDIMIENTO]:** Los fotogramas objetivo del proyecto apuntan hacia 60 FPS, pero el juego puede caer a 40 o 30 FPS si se utilizan beatmaps con muchas notas (marcas de tiempo), o si se incluyen 2DMVs._
* _**[BEATMAPS]:** Aún no hay documentación para generar los beatmaps. Los beatmaps se crean usando un DAW de producción musical, se exporta la secuencia a un archivo MIDI y se obtienen las marcas de tiempo de cada tap al procesar el archivo MIDI._


---
### Jugabilidad:

Las teclas asignadas para jugar son la `C` para la cascada izquierda, y `M` para la cascada derecha.

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

---
### Tasklist:
* **Módulo de Python `RhythmBeats.py`:**

- [x] Adición de umbral de detección (Threshold) y compensación de timing (Offset).
- [x] Detector de beatmap terminado.
- [x] Adición de conteo de Combo.
- [x] Adición de conteo de notas perfectas y fallidas (BRUH XD).
- [x] Adición de cálculo de precisión promedio.
- [x] Umbral de detección fijado en 100 ms (-100/+100).

* **Juego de demostración "Ren'Py RhythmBeats!":**

- [x] Lectura y procesado de archivos `.beat` (Beatmap).
- [x] Adición de capa para 2DMV (basado en video).
- [x] Adición de menú de selección de pistas musicales.
- [x] Adición de pantallas de inicio de pista, pista finalizada (Full Combo/Show Clear/Show Failed), y resultados finales de la partida.
- [ ] Reorganizar metadatos de pistas musicales.
- [ ] Modificar estructura de archivos `.beat`
- [ ] [DEMO] Agregar sistema de descarga de pistas musicales
- [ ] [DEMO] Agregar panel de calibración manual.
- [x] [DEMO] Agregar control de Alpha para atenuar manualmente el fondo de 2DMVs.

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
```

---
### Lanzamientos:

> **NOTA:** _Descomprimir el paquete `beatmaps.zip` dentro de la carpeta `Rhythm_Game-1.0-win/game`._

|Versión|Detalles|URL|
|---|---|---|
|`v0.1.19`|Lanzamiento inicial para fines de pruebas. Puede contener errores de funcionamiento.| [Juego principal](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/download/v0.1.19/Rhythm_Game-1.0-win.zip) - [Beatmaps](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/download/v0.1.19/beatmaps.zip)|
