<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>
<h6 align = "center"> Documentación de "Ren'Py RhythmBeats!" </h1>
<h1 align = "center"> Sección 3: Documentación para programadores/desarrolladores. </h5>

En esta sección encontrarás todo lo necesario para comenzar a escribir código en tu juego, utilizando el sistema de acción rítmica dispuesto en el módulo de **Ren'Py RhythmBeats!**

---

<h3 align="center">1. Clases y métodos del módulo <code>rhythmbeats.rpym</code></h3>

Aquí está documentado el cómo está constituido **Ren'Py RhythmBeats!**. Como la lógica más "compleja" del  sistema rítmico es manejada por el módulo, no necesitas hacer demasiadas maniobras para implementarlo.

> _**[¡NUEVO!]:** Ahora el sistema rítmico posee un apartado para obtener puntajes por tocar una nota. Pon atención a los cambios aplicados en esta sección._

En fin, vamos a ver las clases y métodos que posee el módulo `rhythmbeats.rpym`.

---

#### 1.1. Clase `RhythmPlayground(fn, displayable, song_file, offset_map=0.0, offset_game=0, threshold=100, max_score=1000 failsafe=False)`.

Esta clase se encarga de gestionar la carga y procesamiento de los beatmaps, seguido de la interpretación de los toques del jugador, los cálculos de precisión al momento de tocar las notas en el juego, y la representación gráfica de la partida.

El constructor de esta clase recibe 8 parámetros (3 obligatorios) en el momento que se crea la instancia de la clase.

Estos parámetros son los siguientes:

* **fn `(str)`:**
  
  Este parámetro es obligatorio, y recibe una cadena con la ruta del archivo de beatmap `.beat` relativa a la carpeta `/game` de tu juego. Por ejemplo, si tu archivo de beatmap está en esta ruta:
  
  ```
  /game
  |   /my_beatmap.beat <- [Tu archivo de beatmap]
  ```
  
  Deberías escribirlo como:
  
  ```renpy
  fn = "my_beatmap.beat"
  ```
  
  Este archivo puede ser leído incluso dentro de un paquete RPA.
  
* **displayable `(str o displayable)`:**
  
  Este parámetro es obligatorio, y recibe como argumento un elemento displayable que será utilizado para mostrar cada nota en la pantalla. Puedes pasar como argumento una ruta de una imagen, o algún displayable de Ren'Py como `Image()` o `Transform()`.
  
* **song_file** `(str o list)`:**

  Este parámetro es obligatorio, y recibe como argumento una cadena de texto con la ruta del archivo de audio que contiene la canción a reproducir durante la partida. También puedes pasar una lista para crear una cola de reproducción, por ejemplo, en el caso de que quieras agregar un breve silencio antes de que inicie la canción real de la partida.
  Más detalles en la Documentación de Ren'Py: [https://www.renpy.org/doc/html/audio.html#renpy.music.play](https://www.renpy.org/doc/html/audio.html#renpy.music.play)

* **offset_map `(int o float)`:**
  
  Si no es `0`, este parámetro recibe como argumento un número entero o un número de coma flotante que representa el tiempo (en segundos) que el beatmap debe compensar respecto de la pista musical, en caso de que exista un desfase entre ambas.
  Valores positivos retrasan al beatmap respecto de la pista musical, mientras que valores negativos lo adelantan.

* **offset_game `(float)`:**
  
  Si no es `0`, este parámetro recibe como argumento un número entero que representa el tiempo (en milisegundos) que se agrega como una compensación personalizable por el jugador, cumpliendo un rol similar al calibrador de Timing que tienen algunos juegos de ritmo.
  Tip: Almacena ese número en una variable `persistent` para que el jugador no tenga que calibrar una y otra vez cada vez que inicia el juego. Luego pasa esa variable como argumento de este parámetro.

* **threshold `(float)`:**
  
  Si no es `100`, este parámetro recibe como argumento un número entero que representa el umbral de tiempo base (en milisegundos) para detectar si el jugador ha acertado una nota.
  Por defecto el umbral ha sido fijado en 100ms (0.1 segundos), lo que da un total de 200ms para acertar una nota.
  
* **max_score `(int)`:**

  El sistema rítmico de **Ren'Py RhythmBeats!** ahora posee una funcionalidad básica para computar puntajes durante la partida, según la precisión con la que se toquen las notas de una canción.
  Este parámetro recibe como argumento un número entero que representa un máximo 'hipotético' de puntos que se podría recibir por nota. Por defecto, el máximo hipotético está fijado en 1000 puntos.

* **failsafe `(bool)`:**
  
  Si es `True`, la canción de la partida se ejecuta en "Modo Seguro", de lo contrario, las partidas se ejecutan normalmente como en cualquier juego de ritmo.
  
  El modo seguro permite reproducir el beatmap sin perder el combo durante la partida. Es útil en caso de querer ajustar visualmente o sincronizar la cascada de notas respecto de la música (mediante `offset_map`).

---

Ahora, los métodos que puedes ocupar de la clase `RhythmPlayground()` son los siguientes:

#### 1.2. Método `load()`.

Este método carga y procesa las secuencias de un archivo beatmap de una canción en específico. El archivo `.beat` debe ser señalado en el momento en que se crea una instancia de la clase.

Si el archivo ha sido cargado sin problemas, se imprimirán las estadísticas de la pista y la compensación final aplicada en `stdout`. En caso de que ocurra algún error en la carga del archivo, ya sea porque el formato del contenido no es correcto, o porque no se encontró en la ruta especificada, el método generará una excepción de tipo `RhythmBeatsException`.

Este método debe ser llamado posterior a instanciar la clase. No recibe ningún argumento ni tampoco retorna datos.

---

#### 1.3. Método `beatmap_object()`.

Este método retorna un objeto iterable `itertools.zip_longest` con el beatmap para la visualización de los taps en una screen. Esto ayuda a iterar el beatmap con solo 1 bucle for en donde quieras hacerlo. Es muy útil si no quieres usar el renderizador que posee por defecto  posees los conocimientos suficientes para crear tu propio renderizador de notas musicales con `SpriteManager()` u otros displayables `Sprite` de Ren'Py.

Este método debe ser llamado posterior a instanciar la clase. No recibe ningún argumento en particular.

---

#### 1.4. Método `accuracy_rate()`.

Este método devuelve una tupla con la precisión media del jugador durante la partida, y la tendencia de reacción (en atraso o en adelanto) con flechas.

> **Formato de retorno:**
> `(Tiempo de reacción media, tendencia de reacción)`

El tiempo de reacción media es expresado en milisegundos, mientras que las flechas de tendencia de reacción son retornadas como cadenas de texto unicode. El texto unicode de la flecha utiliza a la fuente `DejaVuSans.ttf`de Ren'Py automáticamente.

Puedes usar este método para obtener estadísticas durante la partida o al finalizar =D

---

#### 1.5. Método `is_running()`.

Este método retorna `True` si el mapa aún se está ejecutando. En el caso contrario, retorna `False` si se recorrieron todas las notas del Beatmap.

---

<h3 align="center">2. Atributos de la clase que puedes editar.</h3>

Al instanciar la clase `RhythmPlayground()` puedes editar algunos atributos.

Estos atributos son:

---

* **Atributo `miss_sound` (str):**

Al editar este atributo (que por defecto es `None`), puedes pasarle una cadena con la ruta de un archivo de audio para reproducir cuando el jugador falle una nota. La ruta de ese archivo de audio, es relativo a la carpeta `/game` de tu proyecto.

Si por ejemplo tienes instanciada la clase `RhythmPlayground()` en una variable llamada `my_instance`, puedes editar el atributo de la siguiente forma:

```renpy
my_instance.miss_sound = "audio/sfx_note_miss.ogg"
```

Al igual que con el archivo de Beatmap, se puede acceder a este archivo de audio incluso si está dentro de un archivo RPA.

* **Atributo `left_key` / `right_key` (pygame):**

  Estos dos atributos reciben una constante de Pygame que señala la tecla física del teclado para tocar las notas de la pista izquierda derecha.
  Por defecto al utilizar las teclas `C` y `M`, el valor de estos atributos es `pygame.K_c` y `pygame.K_m`. Si deseas asignar otras teclas al sistema rítmico, mira el siguiente ejemplo:

  ```renpy
  my_instance.left_key = pygame.K_f
  my_instance.right_key = pygame.K_l
  ```
  Puedes asignar cualquier tecla, siempre y cuando no entren en conflicto con el keymap por defecto de Ren'Py.
  Si quieres ver todas las constantes de teclas soportadas por Pygame, visita este link: [https://www.pygame.org/docs/ref/key.html](https://www.pygame.org/docs/ref/key.html)


---

<h3 align="center">3. Atributos de la clase a los que puedes acceder.</h3>

Al instanciar la clase `RhythmPlayground()`, también puedes tener acceso a los valores de algunos atributos que pueden ser útiles para mostrar en el HUD de la partida o para depurar la actividad de juego, ya que se actualizan siempre.

Estos atributos son los siguientes:

---

* **Atributo `perfect` (int):**
  
  Este atributo entrega el conteo actual de notas acertadas por el jugador.

* **Atributo `miss` (int):**
  
  A diferencia de `perfect`, este atributo entrega el conteo actual de notas fallidas del jugador.
  
* **[¡Nuevo!] Atributo `stage_score` (int):**

  Durante la partida el jugador irá acumulando puntaje según su precisión. Este atributo entrega la cantidad total de puntos generado en la partida.
  
* **[¡Nuevo!] Atributo `note_score` (int):**

  Este atributo entrega la cantidad de puntos obtenida en la última nota tocada. Esto se calcula en función de la precisión del jugador por cada nota.

* **Atributo `combo` (int):**
  
  Este atributo entrega el conteo de combo de la partida, es decir, las notas que el jugador ha acertado consecutivamente sin fallar. Si el jugador falla una nota, este conteo regresa a cero.

* **Atributo `epoch` (float):**
  
  Si es que lo necesitas, este atributo entrega el tiempo Epoch actual de la partida, en segundos.

* **Atributo `map_progress` (tuple):**
  
  Este atributo entrega una tupla con el progreso del mapa actual, en el orden:
  
  `(Nota actual, Notas totales)`.

* **Atributo `offset` (float):**
  
  Si lo necesitas, este atributo entrega el offset final aplicado al beatmap de la partida actual. El offset final corresponde a la suma de los parámetros `offset_map` y `offset_game` de la clase.

* **Atributo `threshold` (float):**
  
  Este atributo entrega el tiempo ajustado para el umbral de reacción del jugador.
  
* **[¡Nuevo!] Atributo `map_mgr` (SpriteManager):**
  
  Este atributo entrega un objeto `SpriteManager()` que se encarga de ejecutar el sistema de cómputo de interacciones del jugador. Debe ser llamado en una screen con `add`.
  
* **[¡Nuevo!] Atributo `waterfall_mgr` (SpriteManager):**

  Este atributo entrega un objeto `SpriteManager()` que se encarga de renderizar la cascada de notas en la pantalla. Si has decidido crear tu propio renderizador gráfico de notas musicales, puedes omitir el uso de este atributo. Al utilizar el renderizador por defecto de RhythmBeats, debes llamar a este atributo desde una screen con `add`.

---

> _**Nota:** Recuerda que puedes acceder a los atributos de la clase, siempre y cuando hayas instanciado a la clase en alguna variable._

Y eso es todo lo que conforma al módulo `rhythmbeats.rpym`. Ahora solo te falta ver los ejemplos para implementarlo en tu juego. Sigue navegando para ver un tutorial detallado para integrar **Ren'Py RhythmBeats!** en una novela visual.

---

<h4 align = "center"> ¡Navega por la documentación! </h4>
<h5 align = "center"> <a href="doc_section_02.md"> Ir a la Sección 2 </a> | <a href="doc_section_04.md"> Ir a la Sección 4</a> </h5>
