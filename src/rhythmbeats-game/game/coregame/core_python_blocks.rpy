## CharlieFuu69
## Ren'Py RhythmBeats! Demo

## Script: (Coregame) Bloques de código Python para ejecución del juego.

################################################################################

init python:
    import rhythmbeats as rbs

    """NOTAS:
    El contenido de este script no forma parte del módulo de RhythmBeats.
    Es código para ejecución correcta de la implementación de este juego."""


    def finish_playstage(screen_queue = [], dissolving = False):
        """Esta función cierra las screens escritas en 'screen_queue' cuando la partida finaliza"""

        renpy.hide_screen("playground_2dmv")
        if screen_queue:
            for scr in screen_queue:
                renpy.hide_screen(scr)
            if dissolving:
                renpy.with_statement(dissolve)


    def accuracy_color(avg = 0.0, disp = "bar"):
        """Esta función se utiliza para colorizar la barra y el texto que señala la precisión
        media del jugador."""

        avg = abs(avg)

        colors = {
                "bar" : {"perfect" : "#9F9", "great" : "#FF9", "bad" : "#F44"},
                "text" : {"perfect" : "#090", "great" : "#990", "bad" : "#900"}
        }

        if avg < 10.0:
            return colors[disp]["perfect"]
        elif avg >= 10.0 and avg < 20.0:
            return colors[disp]["great"]
        elif avg >= 20.0:
            return colors[disp]["bad"]
        else:
            return "#000"


    def hp_color(hp = 0, disp = "bar"):
        """Esta función se utiliza para colorizar la barra y el texto que señala la precisión
        media del jugador."""

        colors = {
                "bar" : {"normal" : "#9F9", "critical" : "#F44"},
                "text" : {"normal" : "#090", "critical" : "#900"}
        }

        if hp <= 5:
            return colors[disp]["critical"]
        else:
            return colors[disp]["normal"]


    def difficult(level):
        colors = {
                2 : "0AA",
                3 : "0A0",
                4 : "AA0",
                5 : "F00",
                6 : "F0F"
        }

        return u"{outlinecolor=%s}L%s{/outlinecolor}" % (colors[level], level)


    class AlphaControl2DMV(BarValue):

        def __init__(self):
            """Constructor de la clase AlphaControl2DMV().
            Esta clase se utiliza para controlar la atenuación del 2DMV desde los ajustes.
            Hereda la clase BarValue de Ren'Py para ajustar la atenuación con una barra slider."""

            self.step = 0.1

        def set_alpha(self, value):
            persistent.custom_alpha = value
            renpy.restart_interaction()

        def get_adjustment(self):
            return ui.adjustment(
                range = 1.0,
                value = persistent.custom_alpha,
                changed=self.set_alpha,
                step=self.step)

        def get_style(self):
            return "slider", "vslider"


    class MusicData:

        def __init__(self, fn):
            self.fn = fn
            self.entire_data = dict()

        def load(self):
            try:
                logging.info("Cargando metadatos JSON de canciones...")
                content = renpy.file(self.fn)
                self.entire_data = json.loads(content.read().decode("utf-8"))

            except Exception as load_error:
                logging.error("Error al cargar metadatos JSON: %s" % str(load_error))

        def sort(self, now = "all"):
            sort_results = []

            if now == "all":
                for section in sorted(self.entire_data):
                    sort_results.extend(self.entire_data[section])
            else:
                sort_results = self.entire_data[now]

            return sort_results

        def get_category(self, id):
            music_metadata = {
                        "all" : "Todos",
                        "love_live" : "Love Live!",
                        "project_sekai" : "Project SEKAI",
                        "other" : "Otras pistas"
            }

            return music_metadata[id]


    def play_preview(now):
        """Esto reproduce un fragmento de la canción completa al seleccionarla
        desde el menú de pistas."""

        renpy.music.stop(channel="music", fadeout = 0.15)
        renpy.music.play(
                    now["audio_preview"],
                    loop = True,
                    fadeout = 0.15,
                    if_changed = True)


    ## NO IMPLEMENTADO NI TESTEADO
    """
    class WaterfallDisplay(object):

        def __init__(self, beatmap_object):

            self.sm = SpriteManager(update=self.update)
            self.note_image = "coregame/ui/ui_coregame_note_tap.png"

            ## Lista de sprites (las notas)
            self.note_taps = []

            ## Iteración del Beatmap
            for left, right in beatmap_object():
                if isinstance(left, float):
                    self.add(self.note_image, left, "LEFT")
                if isinstance(right, float):
                    self.add(self.note_image, right, "RIGHT")

        def add(self, disp, timestamp, lane):
            if lane == "LEFT":
                sprite = self.sm.create(At(disp, note_fall_opt(x=[0.45, 0.37], timing = timestamp)))
            elif lane == "RIGHT":
                sprite = self.sm.create(At(disp, note_fall_opt(x=[0.55, 0.63], timing = timestamp)))

            self.note_taps.append((sprite, timestamp))

        def update(self, st):
            return 0.1666
    """
