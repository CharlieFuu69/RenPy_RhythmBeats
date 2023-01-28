<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>
<h6 align = "center"> Documentación de "Ren'Py RhythmBeats!" </h1>
<h1 align = "center"> Sección 3: Documentación para programadores/desarrolladores. </h5>

En esta sección encontrarás todo lo necesario para comenzar a escribir código en tu juego, utilizando el sistema de acción rítmica dispuesto en el módulo de **Ren'Py RhythmBeats!**

---

<h3 align="center">1. Clases y métodos del módulo <code>rhythmbeats</code></h3>

Aquí está documentado el cómo está constituido **Ren'Py RhythmBeats!**. Como la lógica más "compleja" del  sistema rítmico es manejada por el módulo, no necesitas hacer demasiadas maniobras para implementarlo.

En fin, vamos a ver las clases y métodos que posee el módulo `rhythmbeats`.

---

#### 1.1. Clase `RhythmPlayground(fn, offset_map = 0.0, offset_game = 0.0, threshold = 0.1, failsafe = False)`.

Esta clase se encarga de gestionar la carga y procesamiento de los beatmaps, seguido de la interpretación de los toques del jugador y los cálculos de precisión al momento de tocar las notas en el juego.

El constructor de esta clase recibe 5 parámetros (1 obligatorio) en el momento que se crea la instancia de la clase.

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

* **offset_map `(float)`:**
  
  Este parámetro sirve para compensar cualquier desfase que exista entre el beatmap y la canción asociada al mapa.
  
  Si no es `0.0`, este parámetro recibe como argumento un número de punto flotante, que representa el tiempo (en segundos) de compensación del beatmap respecto de la reproducción de la pista musical.
  
  Esto debería ser un número individual para cada beatmap creado, ya que no todos los mapas van a tener exactamente la misma compensación de tiempo.

* **offset_game `(float)`:**
  
  Si no es `0.0`, este parámetro recibe como argumento un número de punto flotante que representa el tiempo (en milisegundos) de compensación personalizable por el jugador, cuyo valor se adiciona al `offset_map`.
  
  Esto es útil para que el jugador pueda calibrar manualmente el juego, en caso de que perciba que la cascada de notas no se sincroniza del todo bien con sus toques.
  
  En ese caso, puedes guardar el valor calibrado por el jugador en una variable `persistent`, y pasar ese `persistent` como argumento de este parámetro.

* **threshold `(float)`:**
  
  Si no es `0.1`, este parámetro recibe como argumento un número de punto flotante, que representa el umbral de reacción (en segundos), que sirve para determinar si el jugador ha tocado la nota o no. Por defecto se ha fijado el umbral en 0.1 segundos (100ms) por lo que el jugador tiene un rango total de 200ms para tocar correctamente una nota.

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

#### 1.3. Método `monocycle_beatmap()`.

Este método retorna un objeto iterable `itertools.zip_longest` con el beatmap para la visualización de los taps en una screen. Esto ayuda a iterar el beatmap con solo 1 bucle for en una screen =D

Este método debe ser llamado posterior a instanciar la clase. No recibe ningún argumento en particular.

---

#### 1.4. Método `play()`.

Se encarga del gameplay principal.

Este método reproduce el beatmap cargado y se encarga de realizar todos los cálculos necesarios para determinar si el jugador acierta o falla alguna nota. Las interacciones del jugador se computan en este método respecto de un tiempo de época (Epoch) dado en segundos, que por cierto, es entregada gracias a la clase `DynamicDisplayable()` de Ren'Py.

No retorna ningún valor importante para el desarrollador o el jugador.

---

#### 1.5. Método `accuracy_rate()`.

Este método devuelve una tupla con la precisión media del jugador durante la partida, y la tendencia de reacción (en atraso o en adelanto) con flechas.

> **Formato de retorno:**
> `(Tiempo de reacción media, tendencia de reacción)`

El tiempo de reacción media es expresado en milisegundos, mientras que las flechas de tendencia de reacción son retornadas como cadenas de texto unicode. El texto unicode de la flecha utiliza a la fuente `DejaVuSans.ttf`de Ren'Py automáticamente.

Puedes usar este método para obtener estadísticas durante la partida o al finalizar =D

---

#### 1.6. Método `is_running()`.

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

---

<h3 align="center">3. Atributos de la clase a los que puedes acceder.</h3>

Al instanciar la clase `RhythmPlayground()`, también puedes tener acceso a los valores de algunos atributos que pueden ser útiles para mostrar en el HUD de la partida o para depurar la actividad de juego, ya que se actualizan siempre.

Estos atributos son los siguientes:

---

* **Atributo `perfect` (int):**
  
  Este atributo entrega el conteo actual de notas acertadas por el jugador.

* **Atributo `miss` (int):**
  
  A diferencia de `perfect`, este atributo entrega el conteo actual de notas fallidas del jugador.

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

---

> _**Nota:** Recuerda que puedes acceder a los atributos de la clase, siempre y cuando hayas instanciado a la clase en alguna variable._

Y eso es todo lo que conforma al módulo `rhythmbeats`. Ahora solo te falta ver los ejemplos para implementarlo en tu juego. Sigue navegando para ver un tutorial detallado para integrar **Ren'Py RhythmBeats!** en una novela visual.

---

<h4 align = "center"> ¡Navega por la documentación! </h4>
<h5 align = "center"> <a href="doc_section_02.md"> Ir a la Sección 2 </a> | <a href="doc_section_04.md"> Ir a la Sección 4</a> </h5>
