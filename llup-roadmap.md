<p align="center">
  <img width="180" height="180" src="https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/icons/llup_icon.png">
</p>

<h2 align="center"> LoveLive! UNOFFICIAL PROJECT </h2>
<h5 align="center"> Roadmap (Progreso de desarrollo) </h5>

> <p align="left">
>    <img align="left" src="https://user-images.githubusercontent.com/77955772/143798585-2a612721-a193-4ec0-af5f-811c6bef6c4c.png"/>
>    <h4>Importante:</h4>
> </p>
>
> _Este Roadmap puede estar sujeto a cambios debido a retrasos, creación de nuevas características y otros elementos no señalados._

---

### Resumen:

| Última actualización de status | Tickets completados | Tickets pendientes | Progreso total |
|---|---|---|---|
| `2024-03-19 23:54 (GMT -3)`| 127 | 15 | 43.75% (7/16) |

---

### Checklist de características:

- [x] **[COMPLETADO] REACONDICIONAMIENTO DEL NÚCLEO DE "REN'PY RHYTHMBEATS!"**

- [x] **[COMPLETADO] INTEGRACIÓN DEL SERVICIO DE DISCORD RICH PRESENCE.**

- [x] **[COMPLETADO] ALMACENAMIENTO DE DATOS PRINCIPALES DEL JUGADOR.**

- [x] **[COMPLETADO] SELECTOR DE CANCIONES (MODO "UN SOLO JUGADOR").**

- [x] **[COMPLETADO] SISTEMA DE CACHING DE DISPLAYABLES (IMÁGENES/MVs).**

- [x] **[COMPLETADO] SISTEMA DE PROGRESO DE JUGADOR (NIVEL DE JUGADOR).**

- [x] **[COMPLETADO] PANEL DE COLECCIÓN DEL JUGADOR.**

- [ ] **[EN CURSO] MENÚ DE RECLUTAMIENTO (Gacha).**
> - [x] Diseño del menú de reclutamiento.
>   > - [x] Mostrar un selector de banners disponibles.
>   > - [x] Mostrar banner seleccionado (imagen).
>   > - [x] Adjuntar botón prara abrir la vista de probabilidad generalizada y probabilidad por carta.
>   > - [x] Adjuntar botones para elegir entre **Reclutar (x1)** o **Reclutar (x9)**.
>   > - [x] Mostrar tiempo disponible del banner (`DD, HH:MM:SS`).    
>    
> - [ ] Crear clase que administre todas las actividades del Gacha (`RecruitmentHandler()`).
>   > - [x] Organizar banners, cartas y detalles de cartas en un archivo JSON de control.
>   > - [ ] Crear método de solicitudes HTTP para adquirir los datos de control JSON del Gacha.
>   > - [x] Comprobar si hay bloques de datos sin actualizar, antes de abrir el menú de reclutamiento.
>   > - [x] Calcular tiempo de disponibilidad del banner seleccionado (cuenta regresiva).
>   > - [x] Crear un mapa de probabilidad (lista) con proporción de R/SR/UR.
>   > - [x] Barajar el mapa de probabilidad para minimizar la lineabilidad del sistema pseudo aleatorio.
>
> - [x] Crear secuencia de reclutamiento.
>   > - [x] Animaciones.
>   > - [x] Adjuntar nombres de personajes y nombre de la carta (SIFAS) al mostrar la carta obtenida.
>   > - [x] Mostrar miniaturas de todas las cartas obtenidas en el reclutamiento.

- [ ] **[EN ESPERA] MENÚ DE INICIO.**
> - [x] Agregar reloj de sistema (Fecha y Hora).
>   > - [x] Crear `DynamicDisplayable()` para actualizar constantemente el reloj.
>   > - [x] Mostrar hora UTC (mundial) por defecto.
>   > - [x] Añadir opción en los ajustes para escoger entre hora UTC (mundial) y GMT (hora local, zona horaria autodetectada).
>
> - [ ] Sprite de la School Idol favorita seleccionada.
>   > - [ ] Crear un selector de School Idols.
>   > - [ ] Crear animación esencial para pestañeos.
>   > - [ ] Crear displayables adaptativos para soportar multiples expresiones por sprite.
>   > - [ ] Crear un selector de atuendo para la School Idol visible en el Menú de Inicio.


- [ ] **[EN ESPERA] GESTOR DE ASSETS Y DESCARGAS DESDE EL CDN.**
> - [x] Comprobar actualizaciones examinando los paquetes de assets.
>   > - [x] Remover sistema antiguo de almacenamiento de hashes.
>   > - [x] Escanear archivos locales para comparar diferencias de hashes del CDN con el cliente.
>   > - [x] Apilar archivos faltantes o que requieren actualizaciones.
>   > - [x] Eliminar archivos de descargas fallidas (temporales).  
>
> - [x] Modificaciones a la visualización de descargas.
>   > - [x] Convertir automáticamente Bytes a kB, MB y GB.
>   > - [x] Crear un medidor de ancho de banda para las descargas (MB/s).
>   > - [x] Preformatear datos de descarga (MB descargados, totales, ancho de banda, bloques descargados y porcentaje).
>   >   > - [x] Formatear MB descargados.
>   >   > - [x] Formatear tamaño total de descarga (MB).
>   >   > - [x] Formatear medidor de ancho de banda.
>   >   > - [x] Formatear contador de bloques descargados.
>   >   > - [x] Formatear porcentaje de descarga total.
>   >
>   > - [x] Predecir las imágenes (carga en la RAM) de sprites en la pantalla de descargas.
>
> - [ ] Crear un modo de descarga Light (solo canciones) y modo Full (canciones + MVs)


- [ ] **[EN ESPERA] APARTADO DE JUEGO: LIVE SHOWS.**
> - [x] Secuencia de los Live Shows.
>   > - [x] Mostrar portada, título, Full Combo y BPM de la canción a jugar.
>   > - [x] Instanciar la partida como objeto del núcleo de Ren'Py RhythmBeats! (`RhythmPlayground()`).
>   > - [x] Mostrar juicio del Live Show al finalizar la partida (Live Cleared!, Full Combo!, All Perfect!).
>   > - [x] Mostrar XP obtenida por performance del Live Show.
>   >   > - [x] XP por juicio del Live Show.
>   >   > - [x] XP por tiempo de reacción promedio.
>   >   > - [x] XP por nuevo récord alcanzado.
>   >
>   > - [ ] Mostrar resultados (estadísticas) del Live Show.
>   >   > - [x] Cantidad de notas Perfect!.
>   >   > - [x] Cantidad de notas Great!.
>   >   > - [x] Cantidad de notas Miss.
>   >   > - [x] Mostrar bandera de Full Combo/All Perfect.
>   >   > - [x] Mostrar bandera de nuevo récord.
>   >   > - [x] Mostrar PP obtenidos en el Live Show.
>   >   > - [x] Mostrar el Rank del Live Show (CBAS).
>   >   > - [ ] Mostrar carta más dominante (MVP) del Live Show.
>   >   > - [ ] Escoger y mostrar los ítems de recompensa del Live Show.


- [ ] **[PENDIENTE] PANEL DE FORMACIÓN DE LIVE SHOW.**

- [ ] **[PENDIENTE] PANEL DE AFINIDAD CON SCHOOL IDOL FAVORITA.**

- [ ] **[PENDIENTE] PANEL DE MISIONES CON RECOMPENSAS.**

- [ ] **[PENDIENTE] PANEL DE PERFIL DEL JUGADOR.**

- [ ] **[PENDIENTE] SISTEMA DE CUENTAS DE JUGADOR (LoveLive Fan ID, Database).**

- [ ] **[PENDIENTE] EVENTOS ONLINE ASÍNCRONOS (MODOS DE JUEGO Y BACKEND DEL SERVIDOR).**

- [ ] **[PENDIENTE] MAPEAR UN TOTAL DE 30 CANCIONES PARA EL LANZAMIENTO.**

- [ ] **[PENDIENTE] PROCEDIMIENTO DE LIBERACIÓN DE "LOVELIVE! UNOFFICIAL PROJECT".**

- [ ] **[PENDIENTE] PROCEDIMIENTO DE LIBERACIÓN DEL CÓDIGO FUENTE DEL JUEGO (GitHub).**
