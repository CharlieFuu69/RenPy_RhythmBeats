[release]: https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases
[release-badge]: https://img.shields.io/github/v/release/CharlieFuu69/RenPy_RhythmBeats?style=for-the-badge&logo=github

<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>

<h1 align = "center"> Detalles del juego demostrativo de Ren'Py RhythmBeats! </h1>

[![release-badge]][release]

---
### 1. ¿Cómo se juega el juego demostrativo de Ren'Py RhythmBeats?

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

#### ATENUACIÓN DE 2DMVs:
> Si te molesta el brillo normal del 2DMV de fondo mientras juegas, también puedes atenuar el brillo de los 2DMVs desde los ajustes.

---

### 2. Niveles de dificultad de las canciones.

En la versión `v1.00.1b` del juego demostrativo se clasificaron las pistas musicales en "niveles" de dificultad, valor que se puede visualizar al presionar el botón **"Ver Info"** de la canción.

La escala de dificultad se determina en función de la cantidad de notas necesarias para obtener un Full Combo en el juego, es decir, mientras más notas tenga la canción, el nivel de dificultad será mayor. La siguiente tabla representa los niveles de las canciones:

| Nivel de Dificultad | Color    | Cantidad de notas |
|---|---|---|
| L1                  | -        | (No determinado)  |
| L2                  | Cyan     | 200-250 notas     |
| L3                  | Verde    | 251-350 notas     |
| L4                  | Amarillo | 351-450 notas     |
| L5                  | Rojo     | 451-550 notas     |
| L6                  | Púrpura  | 551-600 notas     |

---
### 3. Lista de pistas musicales utilizadas para testeo.

Aquí abajo se listan las pistas musicales que hasta el momento tienen beatmap creado. La mayoría de las pistas poseen una capa de video de 2DMVs/3DMVs oficiales de sus franquicias o creadores.

* **Project SEKAI: COLORFUL STAGE / Vocaloid:**

| Pistas musicales               | Artistas/Unidad                        | BPM | Dificultad | Full Combo | MV                                       |
|---|---|---|---|---|---|
| Highlight                      | Kira Ft. Hatsune Miku                  | 130 | L3         | 253 notas  | MV: Ekkoberry, riguruma (MIKU EXPO 2021) |
| Gunjou Sanka (SEKAI Ver.)      | Hatsune Miku, Ichika Hoshino... (4 más)| 168 | L3         | 307 notas  | 3DMV: "Project SEKAI: COLORFUL STAGE!"   |
| Hand in Hand                   | Hatsune Miku / Kz                      | 128 | L4         | 381 notas  | No añadido                               |
| Angel's Clover                 | MORE MORE JUMP!                        | 193 | L4         | 437 notas  | 3DMV: "Project SEKAI: COLORFUL STAGE!"   |
| Greenlights Serenade           | Hatsune Miku                           | 200 | L4         | 443 notas  | No añadido                               |
| Happy Synthesizer (SEKAI Ver.) | MORE MORE JUMP!                        | 127 | L6         | 592 notas  | 3DMV: "Project SEKAI: COLORFUL STAGE!"   |
| Sweet Magic                    | Wonderlands × Showtime                 | 123 | L5         | 542 notas  | 3DMV: "Project SEKAI: COLORFUL STAGE!"   |


* **Love Live!:**

| Pistas musicales               | Artistas/Unidad                             | BPM | Dificultad | Full Combo | MV                                 |
|---|---|---|---|---|---|
| Mirai no Bokura wa Shitteru yo | Aqours                                      | 181 | L2         | 229 notas  | MV: Love Live! Sunshine!! S2 OP    |
| MOMENT RING                    | μ's                                         | 196 | L4         | 368 notas  | 3DMV: "Love Live! SIF ALL STARS"   |
| Ryouran! Victory Road          | Love Live! Nijigasaki High School Idol Club | 135 | L6         | 580 notas  | MV Fanmade: Henry L.               |
| Snow Halation                  | μ's                                         | 173 | L3         | 305 notas  | 3DMV: "Love Live! SIF ALL STARS"   |
| NEO SKY, NEO MAP!              | Love Live! Nijigasaki High School Idol Club | 142 | L3         | 276 notas  | 3DMV: "Love Live! SIF ALL STARS"   |
| BANZAI! digital trippers       | Aqours Ft. Hatsune Miku                     | 180 | L4         | 418 notas  | MV/CGI: SUNRISE, Lantis, KADOKAWA. |
| START!! True dreams            | Liella!                                     | 178 | L3         | 268 notas  | MV: "Love Live! Superstar!! S1 OP" |
| No brand girls                 | μ's                                         | 196 | L4         | 391 notas  | 3DMV: "Love Live! SIF ALL STARS"   |
| DREAMY COLOR                   | Aqours                                      | 190 | L5         | 521 notas  | No añadido                         |

* **Otras pistas:**

| Pistas musicales      | Artistas                  | BPM | Dificultad | Full Combo | MV         |
|---|---|---|---|---|---1
| The Anthem (Der Alte) | Dimitri Vegas & Like Mike | 140 | L5         | 535 notas  | No añadido |
