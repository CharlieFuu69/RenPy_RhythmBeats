## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Coregame) Interfaz de menú principal.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

## -------------------------------------------------------------------------- ##
## Alerta de Performance

screen performance_warning():
    modal True
    zorder 200
    style_prefix "confirm"

    use notify_window("ADVERTENCIA DE RENDIMIENTO", notify_sound = audio.ui_sound_error):
        vbox:
            spacing 15
            text "Las pistas musicales con un número {color=cf0}igual o mayor a 450 notas{/color} podrían experimentar severos problemas de rendimiento, ya que el motor no es lo suficientemente eficiente en móviles =("
            text "Si quieres jugar esta pista con lag, será bajo tu propia responsabilidad."
            text "De verdad quieres jugarla?"

        hbox:
            style_prefix "main_ui"
            xalign 0.5 ypos 0.8 spacing 20

            textbutton "Jugar de todos modos":
                action [SetVariable("data", p.song_selected),
                Hide("performance_warning"),
                Hide("category_switcher"),
                Hide("song_select", transition = dissolve),
                Return(),
                Jump("game_playstage")]
                activate_sound audio.ui_sound_btn03

            textbutton "Cerrar advertencia":
                action Hide("performance_warning")
                activate_sound audio.ui_sound_btn02


## -------------------------------------------------------------------------- ##
## Menú inicial de configuración.

screen config_panel():
    style_prefix "config_panel"
    modal True
    zorder 104

    add "tex_black"

    default current_config = "system"

    if current_config == "system":
        use system_menu
    elif current_config == "audio":
        use audio_control
    elif current_config == "calibrate":
        use calibration_menu
    elif current_config == "alpha":
        use alpha_menu


    ## Selector de categoría en panel de ajustes.
    vbox:
        textbutton "Sistema" action SetLocalVariable("current_config", "system")
        textbutton "Ajustes de Sonido" action SetLocalVariable("current_config", "audio")
        textbutton "Calibración" action SetLocalVariable("current_config", "calibrate")
        textbutton "Atenuación 2DMV" action SetLocalVariable("current_config", "alpha")

    hbox:
        textbutton "Cerrar menú" action Hide("config_panel"):
            activate_sound audio.ui_sound_btn02


## Preferencias de sistema
screen system_menu():
    style_prefix "settings"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label "PREFERENCIAS DE SISTEMA"

        text "Aquí puedes ajustar distintos parámetros de sistema que se verán reflejados durante el juego."

        viewport:
            xysize(650, 320)
            yinitial 0.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            vbox:
                style_prefix "config_toggle"

                if not renpy.android:
                    vbox:
                        text "Modo de visualización:"
                        hbox:
                            spacing 15
                            textbutton "Ventana" action Preference("display", "window")
                            textbutton "Pantalla Completa" action Preference("display", "fullscreen")

                vbox:
                    text "Métricas de operación:"
                    hbox:
                        spacing 15
                        textbutton "Oculto" action SetVariable("persistent.operating_stats", False)
                        textbutton "Visible" action SetVariable("persistent.operating_stats", True)

                if not renpy.android:
                    vbox:
                        text "Presencia en Discord (Discord RPC):"
                        hbox:
                            spacing 15
                            textbutton "Inactivo" action SetVariable("persistent.discord_rpc", False), Notify("Los cambios de Discord RPC se aplicarán en el próximo arranque del juego.")
                            textbutton "Activo" action SetVariable("persistent.discord_rpc", True), Notify("Los cambios de Discord RPC se aplicarán en el próximo arranque del juego.")

                vbox:
                    text "Ejecución de pistas musicales:"
                    hbox:
                        spacing 15
                        textbutton "Modo Juego" action SetVariable("persistent.failsafe", False)

                        if config.developer:
                            textbutton "Modo Seguro" action SetVariable("persistent.failsafe", True)

                vbox:
                    text "Fotogramas objetivo (Reinicio del juego requerido):"
                    hbox:
                        textbutton "Automático" action Preference("gl framerate", None), Notify("Los cambios en los FPS se aplicarán en el próximo arranque del juego.")
                        textbutton "30 FPS" action Preference("gl framerate", 30), Notify("Los cambios en los FPS se aplicarán en el próximo arranque del juego.")
                        textbutton "45 FPS" action Preference("gl framerate", 48), Notify("Los cambios en los FPS se aplicarán en el próximo arranque del juego.")
                        textbutton "60 FPS" action Preference("gl framerate", 60), Notify("Los cambios en los FPS se aplicarán en el próximo arranque del juego.")

                vbox:
                    text "API Gráfica (Reinicio del juego requerido):"

                    hbox:
                        textbutton "Automático" action _SetRenderer("auto"), Notify("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego.")

                        if renpy.windows or renpy.linux:
                            textbutton "OpenGL" action _SetRenderer("gl2" if config.gl2 else "gl"), Notify("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego.")
                            textbutton "ANGLE" action _SetRenderer("angle2" if config.gl2 else "angle"), Notify("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego.")
                        elif renpy.android:
                            textbutton "OpenGL ES (Por defecto)" action _SetRenderer("gles2" if config.gl2 else "gles"), Notify("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego.")

                vbox:
                    text "Tearing (V-Sync):"
                    hbox:
                        textbutton "Inactivo" action Preference("gl tearing", False), Notify("Los cambios de V-Sync se aplicarán en el próximo arranque del juego.")
                        textbutton "Activo" action Preference("gl tearing", True), Notify("Los cambios de V-Sync se aplicarán en el próximo arranque del juego.")


## Ajustes de Sonido
screen audio_control():
    style_prefix "settings"

    frame at place_atl((0.5, -0.5), (0.5, 0.5), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label "AJUSTES DE SONIDO"

        text "Ajusta el volumen de los canales de audio aquí abajo."

        vbox:
            text "BGM (Música)" size 20
            bar:
                value Preference("music volume")

        vbox:
            text "UI (Interfaz)" size 20
            bar:
                value Preference("sound volume")

        vbox:
            text "SFX (Efectos de sonido)" size 20
            bar:
                value Preference("voice volume")


## Calibración manual
screen calibration_menu():
    style_prefix "settings"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label "CALIBRACIÓN MANUAL"

        text "Por defecto, la compensación de tiempo es de 0 milisegundos.\nEn valores negativos, las notas llegarán {color=cf0}antes de lo esperado{/color}, mientras que con valores positivos se {color=cf0}retrasará la llegada{/color} de las notas."

        vbox:
            style_prefix "offset_setup"
            label "[persistent.custom_offset]{size=20}ms{/size}"

            hbox:
                spacing 15
                textbutton "-10" action If(
                persistent.custom_offset - 10 >= -1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset - 10),
                None)

                textbutton "-1" action If(
                persistent.custom_offset - 1 >= -1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset - 1),
                None)

                null width 40

                textbutton "+1" action If(
                persistent.custom_offset + 1 <= 1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset + 1),
                None)

                textbutton "+10" action If(
                persistent.custom_offset + 10 <= 1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset + 10),
                None)


## Atenuación de 2DMVs
screen alpha_menu():
    style_prefix "settings"

    add Transform(im.Blur(p.song_selected["cover"], 2.0), zoom = 2.5)
    add Solid("#000") alpha persistent.custom_alpha

    frame at place_atl((0.5, -0.5), (0.5, 0.5), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label "ATENUACIÓN DE 2DMVs"

        text "Si el brillo normal del fondo (2DMV) te incomoda a la vista, ajusta la atenuación del fondo."

        vbox:
            text "%.02f%%" % round(persistent.custom_alpha * 100, 2):
                size 24
                xalign 0.5

            bar:
                value AlphaControl2DMV()


## -------------------------------------------------------------------------- ##
## Lista de pistas musicales

screen category_switcher():
    style_prefix "switcher"
    on "update" action Hide("category_switcher")

    frame at switcher_animation:
        vbox:
            textbutton "Todos" action SetVariable("p.category", "all")
            textbutton "Love Live!" action SetVariable("p.category", "love_live")
            textbutton "Project SEKAI" action SetVariable("p.category", "project_sekai")
            textbutton "Otras Pistas" action SetVariable("p.category", "other")


screen song_select(data):
    style_prefix "songlist"
    on "show" action Function(play_preview, now = p.song_selected)

    add Transform(im.Blur(p.song_selected["cover"], 2.0), zoom = 2.5) at cover_change_animation
    add "tex_black"

    ## Botones del área superior.
    hbox:
        style_prefix "sort_music"

        textbutton "{font=DejavuSans.ttf}{size=25}⚙{/size}{/font}":
            style_prefix "offset_setup"
            activate_sound audio.ui_sound_btn01
            action Show("config_panel")

        textbutton "Filtro: %s" % data.get_category(p.category):
            action Show("category_switcher")

        null width 160

        fixed:
            fit_first True
            textbutton "Sobre RhythmBeats":
                style_prefix "game_credits"
                action Show("credits_window")
            add "ui_icon_logo" zoom 0.1 xpos 0.05 yalign 0.5

        fixed:
            fit_first True
            textbutton "GitHub":
                style_prefix "game_credits"
                action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats")
            add "ui_icon_github" xpos 0.1 yalign 0.5

        textbutton "{font=DejavuSans.ttf}{size=25}✖{/size}{/font}":
            style_prefix "offset_setup"
            action Quit(confirm = True)


    ## Lista de canciones
    viewport at place_atl((-0.7, 0.2), (0.05, 0.2), delta = 1.0):
        yinitial 0.0
        xysize(625, 500)
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has vbox spacing 15

        ## Esto genera una lista de botones para seleccionar la pista musical a jugar.
        ## (Que pelotudo soy. Recién me doy cuenta que no he utilizado el "song_id".
        ## Tal vez debería cambiar esto xd)
        for song_id, song in enumerate(data.sort(p.category), start = 1):
            button:
                hbox:
                    style_prefix "song_level"
                    ysize 70 spacing 15

                    add Solid(level_color(song["level"])) xysize(7, 64) yalign 0.5

                    vbox:
                        label "Lvl"
                        text str(song["level"]):
                            outlines [(2, level_color(song["level"]), 0, 0)]

                    vbox:
                        style_prefix "song_btn"
                        yalign 0.5

                        hbox:
                            spacing 7
                            if song["map_length"] >= 500:
                                add "ui_performance_alert"
                            label song["song_title"]

                        text trim_text(song["song_artists"], 55)

                action [SetVariable("p.song_selected", song),
                Function(play_preview, now=song)]


    ## Esto muestra la carátula de la pista musical seleccionada.
    frame at place_atl((1.1, 0.2), (0.55, 0.2), delta = 1.0):
        style_prefix "now_showing"

        textbutton "Ver Info" action Show("song_details", metadata = p.song_selected)

        vbox:
            label p.song_selected["song_title"] ## Título de la pista

            ## Artistas/Unidad de esta pista
            text trim_text(p.song_selected["song_artists"], 45)

            ## Información del 2DMV (En caso que la pista disponga de MVs)
            frame:
                style_prefix "mv_info"
                if "2dmv_info" in p.song_selected:
                    text p.song_selected["2dmv_info"]
                else:
                    background Solid("#F44")
                    text "MV NO DISPONIBLE."

            text u"{color=cf0}Récord actual:{/color} %s XP" % dotfmt(p.highscores[p.song_selected["id"]]):
                size 18

            null height 15
            add p.song_selected["cover"] xalign 0.5 zoom 0.5 ## Carátula

    hbox:
        style_prefix "main_ui"
        pos(0.67, 0.85)

        textbutton "Jugar ahora!":
            if p.song_selected["map_length"] > 450 and renpy.android:
                action Show("performance_warning")

            else:
                action [
                SetVariable("data", p.song_selected),
                Hide("category_switcher"),
                Hide("song_select", transition = dissolve),
                Return(),
                Jump("game_playstage")]

            activate_sound audio.ui_sound_btn03


## -------------------------------------------------------------------------- ##
## Ventana de detalles de la pista

screen song_details(metadata = None):
    style_prefix "settings"
    modal True
    zorder 104

    add "tex_black"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label "INFORMACIÓN DE LA PISTA"

        viewport:
            yinitial 0.0
            xysize(700, 430)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            has vbox

            hbox:
                spacing 20
                add metadata["cover"] zoom 0.3

                vbox:
                    spacing 4
                    text "{color=cf0}Título:{/color} %s" % metadata["song_title"]
                    text "{color=cf0}Artistas/Unidad:{/color} %s" % metadata["song_artists"] text_align 0.0
                    text "{color=cf0}BPM:{/color} %s" % metadata["bpm"]

                    if "song_info" in metadata:
                        text "{color=cf0}Detalles:{/color} %s" % metadata["song_info"] text_align 0.0

            add Solid("#FFF") xysize(600, 3)

            frame:
                style_prefix "window_title"
                background Frame(Solid("#900"), 5, 5, 5, 5)
                text "ADVERTENCIA: LA PARTIDA FINALIZARÁ SI TU HP LLEGA A CERO." size 17

            frame:
                style_prefix "score_goal"
                has vbox
                label "XP necesaria para obtener Rank S:"
                text "%s XP" % dotfmt(metadata["score_goal"])

            text "{color=cf0}Nivel de dificultad:{/color} %s" % level_color(metadata["level"], "text")
            text "{color=cf0}Notas totales (Full Combo):{/color} %s notas" % metadata["map_length"]
            text "{color=cf0}Duración estimada:{/color} %s segundos" % int(metadata["length"])

            if metadata["map_length"] >= 500:
                hbox:
                    spacing 5
                    add "ui_performance_alert" yalign 0.5
                    text "Esta pista puede tener rendimiento deficiente en PC de bajos recursos o en Android." text_align 0.0

    hbox:
        xalign 0.5 ypos 0.85
        style_prefix "main_ui"
        textbutton "Cerrar ventana" action Hide("song_details"):
            activate_sound audio.ui_sound_btn02


## -------------------------------------------------------------------------- ##
## Screen de créditos del juego

screen credits_window():
    modal True
    style_prefix "credits_window"

    add "tex_black"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox xsize 900 spacing 20

        frame:
            style_prefix "window_title"
            label "SOBRE REN'PY RHYTHMBEATS! GAME"

        viewport:
            yinitial 0.0
            xysize(900, 450)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            has vbox xsize 900 spacing 20

            vbox:
                xalign 0.5
                add "ui_icon_logo" zoom 0.4 xalign 0.5
                label config.name
                text "[config.version] | Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]"
                text "[game_license]"

            vbox xalign 0.5:
                text "Este juego es una demostración de lo que se puede hacer con el módulo de Acción Rítmica de {color=cf0}Ren'Py RhythmBeats!{/color}."
                text "El proyecto completo ha sido creado sin intenciones de recibir ingresos, por lo que todo el contenido se ofrece de forma gratuita."

            hbox:
                style_prefix "game_credits"
                xalign 0.5 spacing 20

                fixed:
                    fit_first True
                    textbutton "Ir al repositorio de GitHub":
                        style_prefix "game_credits"
                        action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats")
                        activate_sound audio.ui_sound_btn03
                    add "ui_icon_github" xpos 0.08 yalign 0.5

                fixed:
                    fit_first True
                    textbutton "Wiki: ¿Cómo se juega RhythmBeats?":
                        style_prefix "game_credits"
                        action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/DETALLES_DEMO.md")
                        activate_sound audio.ui_sound_btn03
                    add "ui_icon_github" xpos 0.05 yalign 0.5

            add Solid("#FFF") xysize(870, 2) xalign 0.5

            vbox:
                style_prefix "about"

                vbox spacing 0:
                    label "Programación, desarrollo y diseño de UI:"
                    text "CharlieFuu69"

                vbox spacing 0:
                    label "2DMVs:"
                    text "\"Project SEKAI: COLORFUL STAGE!\""
                    text "\"Love Live! School Idol Festival ALL STARS\""

                vbox spacing 0:
                    label "Traductores de RhythmBeats!:"
                    text "Andredron"

                vbox spacing 10:
                    label "Música del juego:"

                    fixed:
                        fit_first True
                        textbutton "Ver tabla de canciones del juego":
                            style_prefix "game_credits"
                            action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/DETALLES_DEMO.md#4-lista-de-pistas-musicales-disponibles-en-el-juego")
                            activate_sound audio.ui_sound_btn03
                        add "ui_icon_github" xpos 0.08 yalign 0.5


            if renpy.windows or renpy.linux:
                add Solid("#FFF") xysize(870, 2) xalign 0.5

                text "¿Encontraste un bug crítico? Aquí están los registros del juego:"

                vbox xalign 0.5:
                    text "Ruta de Instalación: {color=CF0}[config.basedir]{/color}"
                    text "Registro de Ren'Py: {color=CF0}[config.basedir]/log.txt{/color}"
                    text "Registro de RhythmBeats: {color=CF0}[config.basedir]/rhythmbeats.log{/color}"

                if renpy.windows:
                    hbox:
                        style_prefix "main_ui"
                        xalign 0.5 spacing 20

                        textbutton "Abrir carpeta en el Explorador":
                            action Function(os.startfile, config.basedir)
                            activate_sound audio.ui_sound_btn03


    hbox:
        xalign 0.5 ypos 0.85
        style_prefix "main_ui"
        textbutton "Cerrar ventana":
            activate_sound audio.ui_sound_btn02
            action Hide("credits_window")
