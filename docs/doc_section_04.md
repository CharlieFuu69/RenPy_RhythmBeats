<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/77955772/208582867-fe267999-3f6c-448f-ae78-26b14ced10ac.png">
</p>
<h6 align = "center"> Documentación de "Ren'Py RhythmBeats!" </h6>
<h1 align = "center"> Sección 4: Tutorial de implementación </h1>

En esta sección encontrarás toda la información que necesitas para implementar el sistema de acción rítmica en tu juego, basándonos en la información proporcionada en la **[Sección 3](doc_section_03.md)** de esta documentación.

Se garantiza que el código presente en este tutorial (y el código del módulo) **funcionan en Ren'Py v7.3.x o posterior**. No se garantiza que funcione correctamente en versiones más antiguas ya que no ha sido probado.

> _**Nota:** Se recomienda que primero <ins>**hagas un proyecto vacío de Ren'Py antes de implementar definitivamente.**</ins>_

Antes de que continúes, asegúrate de descargar el **[Módulo de Ren'Py RhythmBeats!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/tag/v1.02.1b_module)** en tu PC, pues de otro modo será imposible implementar esto XD.

Recuerda que los beatmaps **<u>se crean manualmente</u>**. Los tutoriales y recursos para empezar a crear beatmaps están en **[este link](doc_section_05.md)**!

Sin más que decir, ¡vamos a ver cómo debes implementar el sistema rítmico en tu juego!

---

<h3 align="center">1. Cargando el módulo en el juego.</h3>

Para cargar el módulo debes colocar el código compilado `rhythmbeats.rpymc`, dentro de la carpeta `/game` de tu proyecto. Luego, debes hacer uso de la función `renpy.load_module()` de la siguiente forma:

```renpy
init python:
    renpy.load_module("rhythmbeats")
```

Solo debes poner el nombre del archivo, sin la extensión `.rpymc`. En caso de que lo quieras colocar en alguna subcarpeta, la forma correcta sería:
```renpy
init python:
    renpy.load_module("subcarpeta/rhythmbeats")
```

---

<h3 align="center">2. Implementando una UI simple para jugar.</h3>

Ahora, viene la parte donde crearás una UI simple para jugar alguna canción.

En primer lugar, debes tener una imagen para representar las notas en la pantalla, como por ejemplo, la imagen que se usa en el **[juego demostrativo de Ren'Py RhythmBeats!](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/latest)**:

<p align="center"><img src="img/doc_image_05.png"/></p>
<h6 align = "center"> <i>Imagen: Nota musical utilizada en el juego demostrativo (128x128).</i> </h6>

Por otro lado, el renderizador de notas musicales que posee el sistema de acción rítmica, utiliza el mismo modelo mostrado en el juego demostrativo **"Ren'Py RhythmBeats! Game"**, por lo que la siguiente imagen puedes usarla como base para guiar la caída de las notas:

<p align="center"><img width="70%" height="70%" src="https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/src/rhythmbeats-game/game/coregame/ui/ui_coregame_note_lane.png"/></p>
<h6 align = "center"> <i>Imagen: Guía de cascada utilizada en el juego demostrativo de Ren'Py RhythmBeats (1280x720).".</i> </h6>

Para hacer las cosas más fáciles, puedes definir estas dos imágenes en Ren'Py de esta forma:

```renpy
init:
    image note_tap = "gui/note_tap.png"
    image my_note_lane = "gui/my_note_lane"
```

¡Ahora puedes utilizar tu imagen de nota musical con el nombre `note_tap`, y tu guía de notas con el nombre `my_note_lane`!

---

#### 2.1. Crear la Screen que muestra la cascada de notas.

El sistema rítmico tiene la capacidad de renderizar (por defecto) la cascada de notas al estilo de **[Ren'Py RhythmBeats! Game](https://github.com/CharlieFuu69/RenPy_RhythmBeats/releases/latest)**.

Para mostrar la cascada de notas necesitamos de una screen especialmente para esta actividad, ya que así se perturbará en menor medida el rendimiento visual.

Suponiendo que tenemos instanciada la clase `RhythmPlayground()` en una variable llamada `my_instance`, y que tenemos definida una imagen de guía de notas como `my_note_lane`, pues corresponde el siguiente ejemplo:

```renpy
screen note_waterfall():
    zorder 102
    modal True
    
    add "my_note_lane"

    add rhythm.map_mgr ## Ejecución del mapa y cómputo de interacciones
    add rhythm.waterfall_mgr ## Renderización del Waterfall
```

Este método es en esencia el mismo que utiliza el juego demostrativo de **Ren'Py RhythmBeats!** para mostrar las notas en la pantalla.

Podemos desglosar el código anterior de la siguiente manera:

* El primer `add` se utiliza para mostrar la imagen con el diseño de guía de notas (la imagen de más arriba).
* El segundo `add` ejecuta el `SpriteManager()` encargado de ejecutar el beatmap y computar cada interacción del jugador. No muestra ningún displayable en lo absoluto.
* El tercer `add` ejecuta el `SpriteManager()` que renderiza la cascada de notas.

Todos los `SpriteManager()` mencionados anteriormente están dentro del módulo, y estos cumplen la labor fundamental de hacer que el juego de ritmo tenga sentido. Solo necesitas acceder a los atributos `map_mgr` y `waterfall_mgr` para utilizarlos :3

---

#### 2.2. Crear la Screen para mostrar el Combo y otros datos.

Esta screen funciona de una manera distinta a la screen del sub-ítem 2.1, ya que esta debe mostrar las estadísticas de juego y debe actualizarse de forma independiente para estar atento al comportamiento de la partida.

Suponiendo que aún tenemos instanciada la clase `RhythmPlayground()` en una variable llamada `my_instance`, tenemos el siguiente ejemplo:

```renpy
screen stage_hud():
    zorder 102

    ## ¿La partida aún se está ejecutando?
    ## Si se está ejecutando, continúa jugando.
    if my_instance.is_running():

        ## ¿Llevas menos de 15 notas perdidas? Aún puedes seguir.
        if my_instance.miss < 15:
            ## Cuadro vertical de estadísticas
            vbox:
                pos(0.1, 0.1)
                text "Notas acertadas: %s" % my_instance.perfect
                text "Notas fallidas: %s" % my_instance.miss
                text "Combo: %s" % my_instance.combo

        ## Alto ahí capo. Ya has fallado demasiadas notas XD
        else:
            python:
                ui.close()
                renpy.jump("stage_failed")

    ## ¿Terminó la partida sin que fallaras? Nice =D
    else:
        python:
            ui.close()
            renpy.jump("stage_cleared")



## Esto hace de que la screen del HUD se refresque constantemente,
## sin afectar el rendimiento de la screen del waterfall.
init python:
    config.per_frame_screens.append("stage_hud")
```

Básicamente en esta screen puedes acceder a los atributos `perfect`, `miss` y `combo` de la clase `RhythmPlayground()` que se van actualizando a medida que la canción se ejecuta.

Dos condicionales evalúan si la partida puede continuar o se detiene. Dentro de la condicional de `my_instance.is_running()` se comprueba si el jugador ha perdido menos de 15 notas. Si falla más de 15 notas, se va para el lobby xD.

Por supuesto, la cantidad de notas fallidas admitidas queda a tu criterio =D

Lamentablemente las screens no se actualizan constantemente, razón por la que se ha utilizado a `config.per_frame_screens` más abajo. `config.per_frame_screens` es una lista que sirve para actualizar a un grupo específico de screens, sin afectar a otras.

---

<h3 align="center">3. Creando la secuencia de juego.</h3>

Aquí es donde vamos a crear el flujo del código para jugar una canción. Básicamente reuniremos todo lo que hicimos anteriormente y lo ejecutaremos en los `label` para tener control absoluto de la partida.

---

#### 3.1. Instanciando la clase `RhythmPlayground()`.

Parecía que ya nos estábamos olvidando que `RhythmPlayground()` era básicamente el corazón del sistema de acción rítmica, pero no. Aquí es donde la usaremos porque su uso es clave para poder utilizar todo lo que hicimos en el ítem 2.

Teniendo en cuenta que estábamos usando una variable llamada `my_instance` para instanciar la clase, el código debería ser de esta forma:

```renpy
## Aquí comienza el juego
label start:

    python:
        ## Instancia de la clase
        my_instance = rbs.RhythmPlayground(
                        fn = "my_beatmap.beat",
                        displayable = Transform("note_tap", zoom=0.55),
                        song_file = "audio/bgm_my_song_file.ogg",
                        offset_map = 0.5,
                        offset_game = 0)

        ## Carga el beatmap
        my_instance.load()

        ## (Opcional) Un archivo de audio que se reproducirá cuando
        ## el jugador pierda el combo (BRUH)
        my_instance.miss_sound = "audio/sfx_note_miss.ogg"
```

Hasta aquí tenemos todo bien.

La clase es instanciada de forma global con algunos valores. Por ejemplo, hemos agregado un archivo hipotético de beatmap que se llama `my_beatmap.beat`, que  está en la carpeta `/game` del juego. También agregamos un displayable que el sistema rítmico utilizará para mostrar cada una de las notas de nuestra canción, seguido del archivo de audio (`song_file`) de la canción que queremos reproducir al jugar.

Digamos de que ese beatmap hipotético tenía un desfase. Ahí le cambiamos su `offset_map` a `0.5`, haciendo que el mapa se ejecute con 0.5 segundos de retraso respecto de la canción.

Por último mantenemos el `threshold` en su valor por defecto (100 milisegundos), y el juego se ejecutará normalmente ya que el `failsafe` (Modo seguro) es `False`.

---

#### 3.2. Mostrando las screens para empezar a jugar.

Ahora es el turno de mostrar las screens que hicimos en el ítem 2.

Para completar la secuencia de juego, dentro del mismo label `start` pero fuera del bloque `python`, continuamos el código anterior de la siguiente forma:

```renpy
show screen stage_hud ## Muestra el HUD de la partida
call screen note_waterfall ## Muestra la cascada de notas
```

En este caso, primero mostramos la screen `stage_hud` que se encarga de mostrar las estadísticas básicas de juego, y por último mostramos la screen `note_waterfall` que se encarga de mostrar la cascada de notas.

---

#### 3.3. Decidiendo el flujo de la partida.

¿Recuerdas los `renpy.jump()` que pusimos en la screen `stage_hud`? Los `renpy.jump()` son el equivalente pythónico de escribir `jump <label de destino>` en un script RPY, y en nuestro caso, lo usamos para saltar hacia algún label cuando una o más condiciones se cumplan.

Ahora esos labels que llamamos en esos `renpy.jump()` entrarán en acción de la siguiente manera:

```renpy
## ------------------------------------------------------------------- ##
## Labels de partidas finalizadas

label stage_cleared:
    hide screen stage_hud
    hide screen note_waterfall

    "¡Excelente! ¡Terminaste la partida a salvo!"

    ## Elimina la instancia y retorna al menú principal
    $ del my_instance
    return


label stage_failed:
    hide screen stage_hud
    hide screen note_waterfall

    "Oh no. ¡Se te escaparon 15 notas! Has fallado =("

    ## Elimina la instancia y retorna al menú principal
    $ del my_instance
    return
```

El objetivo de estos labels, es de que cuando la partida finaliza, o si el jugador falla muchas notas, el juego necesita continuar su recorrido en algún lugar.

Dicho esto, entonces el label llamado `stage_cleared` se usa cuando el jugador termina la partida sin problemas, independiente de que si falló algunas notas o no. La condicional presente en la screen `stage_hud` apunta a que el jugador puede completar una canción siempre y cuando tenga una cantidad menor a 15 notas fallidas.

Por otro lado tenemos al label llamado `stage_failed`, que este se ejecuta cuando el jugador falló 15 notas durante la partida. En síntesis, cuando el jugador haya fallado 15 notas, la partida se detendrá incluso si aún no terminaba la canción.

Por último al finalizar en estos labels, la instancia actual es eliminada mediante `$ del`, lo que es útil para que el sistema rítmico inicie en limpio nuevamente y puedas usarlo en una nueva canción.

---

<h3 align="center">4. Código completo de este tutorial.</h3>

Para sintetizar la secuencia completa que debes hacer en tu juego, te dejo el código de ejemplo completo aquí abajo para que lo analices con mayor detenimiento.

Para probarlo en un proyecto vacío, reemplaza todo el contenido del archivo `script.rpy` y pega el código a continuación.

```renpy
## Archivo script.rpy

## Cargar el módulo
init python:
    renpy.load_module("rhythmbeats")
    

## ----------------------------------------------------------------- ##
## APARTADO DE DEFINICIONES DE IMÁGENES

## Recuerda que la ruta debe ser un archivo de imagen válido
init:
    image note_tap = "gui/note_tap.png"
    image my_note_lane = "gui/my_note_lane.png"
    

## ----------------------------------------------------------------- ##
## APARTADO DE SCREENS

## Cascada de notas
screen note_waterfall():
    zorder 102
    modal True

    add "my_note_lane"

    add rhythm.map_mgr ## Ejecución del mapa y cómputo de interacciones
    add rhythm.waterfall_mgr ## Renderización del Waterfall


## HUD de la partida
screen stage_hud():
    zorder 102

    ## ¿La partida aún se está ejecutando?
    ## Si se está ejecutando, continúa jugando.
    if my_instance.is_running():

        ## ¿Llevas menos de 15 notas perdidas? Aún puedes seguir.
        if my_instance.miss < 15:
            ## Cuadro vertical de estadísticas
            vbox:
                pos(0.1, 0.1)
                text "Notas acertadas: %s" % my_instance.perfect
                text "Notas fallidas: %s" % my_instance.miss
                text "Combo: %s" % my_instance.combo

        ## Alto ahí capo. Ya has fallado demasiadas notas XD
        else:
            python:
                ui.close()
                renpy.jump("stage_failed")

    ## ¿Terminó la partida sin que fallaras? Nice =D
    else:
        python:
            ui.close()
            renpy.jump("stage_cleared")



## Esto hace de que la screen del HUD se refresque constantemente,
## sin afectar el rendimiento de la screen del waterfall.
init python:
    config.per_frame_screens.append("stage_hud")


## ----------------------------------------------------------------- ##
## FLUJO/SECUENCIA DE JUEGO

## Aquí comienza el juego
label start:

    python:
        ## Instancia de la clase
        my_instance = rbs.RhythmPlayground(
                        fn = "my_beatmap.beat",
                        displayable = Transform("note_tap", zoom=0.55),
                        song_file = "audio/bgm_my_song_file.ogg",
                        offset_map = 0.5,
                        offset_game = 0)

        ## Carga el beatmap
        my_instance.load()

        ## (Opcional) Un archivo de audio que se reproducirá cuando
        ## el jugador pierda el combo (BRUH)
        my_instance.miss_sound = "audio/sfx_note_miss.ogg"

    ## Ejecución del juego
    show screen stage_hud ## Muestra el HUD de la partida
    call screen note_waterfall ## Muestra la cascada de notas

## ------------------------------------------------------------------- ##
## Labels de partidas finalizadas

label stage_cleared:
    hide screen stage_hud
    hide screen note_waterfall

    "¡Excelente! ¡Terminaste la partida a salvo!"

    ## Elimina la instancia y retorna al menú principal
    $ del my_instance
    return

label stage_failed:
    hide screen stage_hud
    hide screen note_waterfall

    "Oh no. ¡Se te escaparon 15 notas! Has fallado =("

    ## Elimina la instancia y retorna al menú principal
    $ del my_instance
    return
```

---

<h4 align = "center"> ¡Navega por la documentación! </h4>
<h5 align = "center"> <a href="doc_section_03.md"> Ir a la Sección 3 </a> | <a href="doc_section_05.md"> Ir a la Sección 5</a> </h5>
