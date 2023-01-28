## CharlieFuu69
## Ren'Py RhythmBeats!

## Script: Sistema de acción rítmica

################################################################################

import json
import os
import renpy
import pygame
import itertools

def logger(level, content):
    print("[%s] %s" % (level, content))


class RhythmBeatsException(Exception):
    """Una clase simple para emitir excepciones bajo el nombre de Ren'Py RhythmBeats."""
    pass

class RhythmPlayground:

    def __init__(self, fn, offset_map = 0.0, offset_game = 0.0, threshold = 0.1, failsafe = False):
        """Constructor de la clase RhythmPlayground().
        Recibe 5 parámetros (1 obligatorio) en el momento que se crea la instancia de la clase.
        Estos parámetros son los siguientes:

        fn (str):
            Este parámetro es obligatorio, y recibe una cadena con la ruta del archivo BEAT
            relativa a la carpeta /game de tu juego.
            Este archivo puede ser leído incluso dentro de un paquete RPA.

        offset_map (float):
            Si no es 0.0, este parámetro recibe como argumento un número de punto flotante,
            que representa el tiempo (en segundos) que se desfasa el beatmap respecto de la
            reproducción de la pista musical. Esto debería ser un número individual de cada beatmap.

        offset_game (float):
            Si no es 0.0, este parámetro recibe como argumento un número de punto flotante
            que representa el tiempo (en milisegundos) que se agrega como desfase
            personalizable por el jugador.
            Esto es útil para que el jugador pueda calibrar manualmente en caso de que perciba
            que la cascada de notas no se sincroniza del todo bien con sus toques. En ese caso,
            puedes pasar como argumento una variable persistente con el valor calibrado por el
            jugador.

        threshold (float):
            Si no es 0.1, este parámetro recibe como argumento un número de punto flotante,
            que representa el umbral de tiempo (en segundos) para detectar si el jugador ha
            tocado la nota o no. Por defecto se ha fijado el umbral en 0.1 segundos (100ms) por
            lo que el jugador tiene un rango total de 200ms para tocar correctamente una nota.

        failsafe (bool):
            El modo seguro permite reproducir el beatmap sin necesidad de tocar las notas.
            Es útil en caso de querer ajustar visualmente la cascada de notas respecto
            de la música (mediante offset_map).
            Si es True, ejecutará el beatmap en modo seguro. Si es False, el
            juego se ejecutará normalmente.
        """

        ## ------------------ RUTAS Y AJUSTES PRINCIPALES ------------------- ##

        ## Rutas relativas.
        self.fn = fn
        self.miss_sound = None

        ## Calibración del juego y umbral de reacción por nota.
        self.offset = offset_map + (offset_game / 1000.0)
        self.threshold = threshold

        ## Ejecución en modo seguro
        self.failsafe = failsafe

        ## ------------------- DATOS DE BEATMAPS CARGADOS ------------------- ##

        ## Almacenaje del beatmap cargado.
        self.lane_L = list()
        self.lane_R = list()

        ## Almacenaje de timestamps para calcular la precisión media.
        self.timestamp_log = list()

        ## ---------------------- CÓMPUTO DE LA PARTIDA --------------------- ##

        ## Índices de timestamps y progreso del beatmap
        self.note_index = {"left" : 0, "right" : 0}
        self.note_pass = {"left" : 0, "right" : 0}
        self.key_tap = {"left" : 0.0, "right" : 0.0}
        self.map_progress = (0, 0)

        ## Cómputo de juego
        self.combo = 0
        self.perfect = 0
        self.miss = 0

        ## ¿El beatmap aún está corriendo?
        self.running = {"left" : True, "right" : True}
        self.epoch = 0.0


    def load(self):
        """Este método carga y procesa las secuencias de un archivo beatmap de
        una canción en específico. El archivo `.beat` debe ser señalado en el
        momento en que se crea una instancia de la clase.

        Esto debe ser llamado posterior a instanciar la clase. No recibe ningún
        argumento ni tampoco retorna datos."""

        logger("Process", "Cargando beatmap...")

        try:
            with renpy.exports.file(self.fn) as beatmap:
                logger("Stats", "Ruta relativa: %s." % self.fn)

                bmpdata = beatmap.readlines()

                for keypad in bmpdata[1:]:
                    keypad = keypad.replace("\n", "").replace("\r", "").split("|")

                    left = keypad[0]
                    right = keypad[1]

                    if left != "" or right != "":
                        if not "End" in left:
                            self.lane_L.append(eval(left) + self.offset)

                        if not "End" in right:
                            self.lane_R.append(eval(right) + self.offset)

                ## Casting de listas a tuplas
                self.lane_L = tuple(self.lane_L)
                self.lane_R = tuple(self.lane_R)

                logger("Stats", "Offset final: %sms." % self.offset)
                logger("Stats", "Full Combo: %s notas." % (len(self.lane_L) + len(self.lane_R)))
                logger("OK", "Beatmap listo para ejecutar.\n")

                beatmap.close()

        except Exception as open_error:
            raise RhythmBeatsException("(%s) %s" % (type(open_error), str(open_error)))


    def monocycle_beatmap(self):
        """Este método retorna un objeto iterable `itertools.zip_longest` con el
        beatmap para la visualización de los taps en una screen. Esto ayuda a
        iterar el beatmap con solo 1 bucle for en una screen =D

        Esto debe ser llamado posterior a instanciar la clase. No recibe ningún
        argumento en particular."""

        return itertools.zip_longest(self.lane_L, self.lane_R, fillvalue = "End")


    def play(self, st, at):
        """Se encarga del gameplay principal.
        Este método reproduce el beatmap cargado y se encarga de realizar todos
        los cálculos necesarios para determinar si el jugador acierta o falla
        alguna nota.
        Las interacciones del jugador se computan en este método respecto de un
        tiempo de época (Epoch) dado en segundos, que por cierto, es entregada
        gracias a la clase `DynamicDisplayable()` de Ren'Py.

        No retorna ningún valor importante para el desarrollador o el jugador."""

        ## ------------------------------------------------------------------ ##
        ## Área de interacciones

        if self.running["left"] or self.running["right"]:
            self.epoch = round(st, 2)

        keys = pygame.key.get_pressed()

        ## Detecta los taps y guarda el timestamp del toque
        if keys[pygame.K_c]:
            self.key_tap["left"] = st

        if keys[pygame.K_m]:
            self.key_tap["right"] = st

        ## ------------------------------------------------------------------ ##
        ## Área de análisis de taps

        ## Determina si el índice de cada fila de notas ha llegado a su fin
        self.running["left"] = self.note_pass["left"] < len(self.lane_L)
        self.running["right"] = self.note_pass["right"] < len(self.lane_R)

        ## Obtiene la diferencia entre el timestamp de la tecla con el beatmap
        l_match = self.key_tap["left"] - self.lane_L[self.note_index["left"]]
        r_match = self.key_tap["right"] - self.lane_R[self.note_index["right"]]

        ## Obtiene si la nota tocada está dentro del umbral de detección
        l_phase = all([l_match >= -self.threshold, l_match <= self.threshold])
        r_phase = all([r_match >= -self.threshold, r_match <= self.threshold])

        ## Obtiene si el timestamp actual ha sido ignorado por el jugador
        l_badnote = all([st - self.threshold > self.lane_L[self.note_index["left"]], self.key_tap["left"] < st + self.threshold])
        r_badnote = all([st - self.threshold > self.lane_R[self.note_index["right"]], self.key_tap["right"] < st + self.threshold])

        ## ------------------------------------------------------------------ ##
        ## Área de cómputo

        ## Keypad L
        if l_phase and self.running["left"]:
            self.note_index["left"] += 1 if self.note_index["left"] < len(self.lane_L) -1 else 0
            self.timestamp_log.append(l_match)
            self.note_pass["left"] += 1
            self.combo += 1
            self.perfect += 1

        elif l_badnote and self.running["left"]:
            if not self.failsafe:
                renpy.exports.play(self.miss_sound, channel = "audio")
                self.combo = 0
                self.miss += 1

            self.note_index["left"] += 1 if self.note_index["left"] < len(self.lane_L) -1 else 0
            self.note_pass["left"] += 1


        ## Keypad R
        if r_phase and self.running["right"]:
            self.note_index["right"] += 1 if self.note_index["right"] < len(self.lane_R) -1 else 0
            self.timestamp_log.append(r_match)
            self.note_pass["right"] += 1
            self.combo += 1
            self.perfect += 1

        elif r_badnote and self.running["right"]:
            if not self.failsafe:
                renpy.exports.play(self.miss_sound, channel = "audio")
                self.combo = 0
                self.miss += 1

            self.note_index["right"] += 1 if self.note_index["right"] < len(self.lane_R) -1 else 0
            self.note_pass["right"] += 1


        ## Esto actualiza costantemente una tupla con el progreso del beatmap.
        self.map_progress = (self.note_pass["left"] + self.note_pass["right"], len(self.lane_L + self.lane_R))

        return renpy.text.text.Text(""), 0.01667 ## ~60 Hz


    def accuracy_rate(self):
        """Este método devuelve una tupla con la precisión media del jugador
        durante la partida, y la tendencia de reacción (en atraso o en adelanto)
        con flechas.

        **Formato de retorno:**
        (Tiempo de reacción media, tendencia de reacción)

        Los valores de precisión media son retornados en milisegundos, mientras
        que las flechas de tendencia de reacción son retornadas como cadenas de texto.
        Puedes usar este método para obtener estadísticas durante la partida o
        al finalizar =D"""

        average_ms = 0.0

        ## Esta condicional previene una posible excepción ZeroDivisionError.
        if len(self.timestamp_log) > 0:
            average_ms = round(sum(self.timestamp_log) / len(self.timestamp_log), 4) * 1000.0


        if average_ms == 0.0:
            reaction = u"{font=DejaVuSans.ttf}⇋{/font}"
        elif average_ms < 0.0:
            reaction = u"{font=DejaVuSans.ttf}◂{/font}"
        elif average_ms > 0.0:
            reaction = u"{font=DejaVuSans.ttf}▸{/font}"

        return average_ms, reaction


    def is_running(self):
        """Este método retorna `True` si el mapa aún se está ejecutando. En el
        caso contrario, retorna `False` si se recorrieron todas las notas del
        Beatmap."""

        return self.running["left"] or self.running["right"]


## Bandera de ejecución en el arranque
init_flag = renpy.exports.is_init_phase
