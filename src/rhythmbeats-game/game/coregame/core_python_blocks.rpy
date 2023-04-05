## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Coregame) Bloques de código Python para ejecución del juego.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

init python:
    """NOTAS:
    El contenido de este script no forma parte del módulo de RhythmBeats.
    Es código para ejecución correcta de la implementación de este juego.
    """

    import discord_rpc, time

    ## Importación del módulo de "Ren'Py RhythmBeats!"
    renpy.load_module("coregame/rhythmbeats")


    def record_scores(init_mode = False, id = None, score = None):
        """Esta función actualiza claves del diccionario que contiene los récords
        del jugador, o bien, actualiza el récord en caso de que el jugador haya
        superado su propia marca."""

        if init_mode:
            for id in range(1, init_mode+1):
                _id = "Song_%04d" %(id)
                if _id in p.highscores:
                    continue
                else:
                    p.highscores.update({_id : 0})

        else:
            if score > p.highscores[id]:
                p.highscores.update({id : score})
                return True
            else:
                return False


    def fix_previews(all_metadata):
        """Esta función corrige cualquier diferencia de datos entre la canción
        seleccionada y el archivo de metadatos de música."""

        for song in all_metadata:
            if p.song_selected["audio_preview"] == song["audio_preview"]:
                p.song_selected = song
                return None


    def finish_playstage(screen_queue = [], dissolving = False):
        """Esta función cierra las screens escritas en 'screen_queue' cuando la
        partida finaliza"""

        renpy.hide_screen("playground_2dmv")
        if screen_queue:
            for scr in screen_queue:
                renpy.hide_screen(scr)
            if dissolving:
                renpy.with_statement(dissolve)


    def dotfmt(value):
        return format(value, ",d").replace(",", ".")


    def score_color(score, goal):
        """Esta función se encarga de entregar a la UI de la partida, el color
        del Rank alcanzado actualmente, el Rank actual, el puntaje formateado
        con puntos y la medalla correspondiente al Rank actual."""

        b = goal * 0.3
        a = goal * 0.5
        s = goal * 1.0

        colors = {"#CCCCCC" : {"rank" : "C", "icon" : "ui_icon_rank_c", "range" : all((score >= 0, score < b))},
                "#00CCFF" : {"rank" : "B", "icon" : "ui_icon_rank_b", "range" : all((score >= b, score < a))},
                "#EEEE37" : {"rank" : "A", "icon" : "ui_icon_rank_a", "range" : all((score >= a, score < s))},
                "#FF32CD" : {"rank" : "S", "icon" : "ui_icon_rank_s", "range" : score >= s}}

        for k in colors:
            if colors[k]["range"]:
                return (k, colors[k]["rank"], dotfmt(score), colors[k]["icon"])


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


    def level_color(level, mode = "color"):
        colors = {
                2 : "0AA",
                3 : "0A0",
                4 : "AA0",
                5 : "F00",
                6 : "F0F"
        }

        if mode == "color":
            return colors[level]
        elif mode == "text":
            return u"{outlinecolor=%s}L%s{/outlinecolor}" % (colors[level], level)


    def trim_text(_text, limit):
        """Esto recorta un texto si alzanca un límite determinado de caracteres
        de longitud, agregando puntos suspensivos al final del recorte."""

        if len(_text) > limit:
            return _text[:limit] + "..."
        return _text


    def play_preview(now):
        """Esto reproduce un fragmento de la canción completa al seleccionarla
        desde el menú de pistas."""

        if not renpy.music.get_playing(channel = "music") == now["audio_preview"]:
            renpy.music.stop(channel="music", fadeout = 0.15)
            renpy.music.play(
                        now["audio_preview"],
                        loop = True,
                        fadeout = 0.15,
                        if_changed = True)


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

        def __init__(self, _dir):
            self.dir = _dir
            self.entire_data = dict()

        def load(self):
            try:
                logger(logging.info, "Loading music metadata from JSON...")
                content = renpy.file(self.dir)
                self.entire_data = json.loads(content.read().decode("utf-8"))

            except Exception as load_error:
                logger(logging.error, "JSON loading failed: %s" % str(load_error))

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

        def get_song_count(self):
            sort_all_songs = list()

            for section in sorted(self.entire_data):
                sort_all_songs.extend(self.entire_data[section])

            return len(sort_all_songs)


    class DiscordRichPresence:
        """Esta clase permite hacer visible al juego en Discord mediante
        Discord Rich Presence (RPC).
        Esto solo funciona en PC, y para que la actividad sea visible, el jugador
        debe tener instalado el cliente de Discord en su PC.
        No se asegura que el juego sea visible si se usa Discord desde un navegador."""

        def __init__(self):
            self.client = "1072433463833133116"
            self.is_running = True
            self.runtime_epoch = time.time()

            self.cb_methods = {
                            "ready" : self.rpc_ready,
                            "disconnected" : self.rpc_disconnect,
                            "error" : self.rpc_error}

            discord_rpc.initialize(self.client, callbacks=self.cb_methods, log=False)

        ## ---------------------------------------------------------------------- ##
        ## Métodos callback para reportar actividad de Discord RPC

        def rpc_ready(self, userdict):
            logger(logging.info, "Discord RPC running on user \"%(username)s\"..." % userdict)

            rbs_alert(__("¡Ren'Py RhythmBeats ya es visible en Discord!"), 0, "ui_icon_discord")


        def rpc_disconnect(self, code, msg):
            logger(logging.warning, "Discord RPC disconnected.")
            logger(logging.warning, "Error code: %s" % code)
            logger(logging.warning, "Details: %s" % msg)

            rbs_alert(content="(%s) %s" %(code, msg), status=1, icon="ui_icon_warning")


        def rpc_error(self, code, msg):
            logger(logging.error, "Error in Discord RPC runtime.")
            logger(logging.warning, "Error code: %s" % code)
            logger(logging.warning, "Details: %s" % msg)

            rbs_alert("(%s) %s" %(code, msg), status=1, icon="ui_icon_warning")

        ## ---------------------------------------------------------------------- ##
        ## Métodos de ejecución y de actividad de Discord RPC

        def set_status(self, state = None, details = "", image_text = "Jugando a Ren'Py RhythmBeats!"):

            discord_rpc.update_presence(
                **{
                    "state" : state,
                    "details" : details,
                    "start_timestamp": self.runtime_epoch,
                    "large_image_key": "largeimage",
                    "large_image_text" : image_text
                }
            )

            renpy.restart_interaction()


        def stop(self):
            logger(logging.info, "Discord RPC service stopped.")
            self.is_running = False
            discord_rpc.shutdown()


        def rpc_updater(self):
            while True:
                try:
                    discord_rpc.update_connection()
                    discord_rpc.run_callbacks()

                except Exception as rpc_upd_error:
                    logger(logging.info, "Discord RPC Error: %s" % repr(rpc_upd_error))
                finally:
                    if self.is_running:
                        time.sleep(3)
                    else:
                        break


        def rpc_start(self):
            logger(logging.info, "Starting Discord RPC service...")
            rbs_alert(__("Ren'Py RhythmBeats se está conectando con Discord..."), icon="ui_icon_discord")
            renpy.invoke_in_thread(fn=self.rpc_updater)
