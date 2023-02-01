## CharlieFuu69
## Ren'Py RhythmBeats! Demo

## Script: (Coregame) Interfaz de partidas.

################################################################################

## -------------------------------------------------------------------------- ##
## Presentación de la pista actual

screen song_start(song_data):
    modal True
    style_prefix "song_start"

    timer 4.0 action [Hide("song_start", transition = dissolve), Return()]

    add Fixed(Transform(im.Blur(song_data["cover"], 2.0), zoom = 2.5), Transform(Solid("#000"), alpha = 0.5)) at alpha_com(1.0, 0.3)

    vbox:
        spacing 30
        add song_data["cover"] align(0.5, 0.4) zoom 0.8

        vbox:
            label song_data["song_title"]
            text song_data["song_artists"]

        text "BPM: %s | Full Combo: %s notas" % (song_data["bpm"], song_data["map_length"]) italic True

style song_start_vbox:
    xsize 1280
    align(0.5, 0.5)

style song_start_label:
    xalign 0.5

style song_start_label_text:
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 27
    italic True

style song_start_text:
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    xalign 0.5
    size 17


## -------------------------------------------------------------------------- ##
## Ejecución de beatmaps y vista del waterfall

screen playground(mv_data):
    zorder 102
    modal True

    ## 2DMV/BG
    if mv_data:
        timer mv_data[1] action Show("playground_2dmv", source = mv_data[0], transition = dissolve)
    else:
        timer 0.01 action Show("playground_2dmv", source = Transform(im.Blur(data["cover"], 2.0), zoom = 2.5))


    add "ui_coregame_note_lane"

    ## Accionamiento de la lectura del beatmap como displayable.
    add DynamicDisplayable(rhythm.play)

    ## Waterfall
    ## Aquí se iteran las listas de notas y muestra la cascada respecto de los timestamps.
    for padL, padR in rhythm.monocycle_beatmap():
        if isinstance(padL, float):
            add "ui_coregame_note_tap" at note_fall(x=[0.45, 0.37], timing = padL)
        if isinstance(padR, float):
            add "ui_coregame_note_tap" at note_fall(x=[0.55, 0.63], timing = padR)


## -------------------------------------------------------------------------- ##
## HUD del campo de juego (Actúa por separado ya que debe refrescarse con interacciones,
## y las interacciones decrementan los FPS)

screen playground_hud(song_length):
    zorder 103
    style_prefix "stats"

    timer song_length + 1.0 action Jump("show_cleared")

    python:
        hp = 15 - rhythm.miss
        accuracy = rhythm.accuracy_rate()[0]
        reaction = rhythm.accuracy_rate()[1]

    ## ¿Hay menos de 15 notas fallidas? Si hay menos de 15, se puede seguir jugando.
    if rhythm.miss < 15:
        ## Barra de HP (se calcula restando 15 por la cantidad de notas perdidas.)
        vbox:
            text "{font=DejaVuSans.ttf}❤{/font} [hp]/15" color hp_color(hp, "text")
            bar:
                value AnimatedValue(old_value = 0.0, value = hp, range = 15, delay = 0.1)
                left_bar hp_color(hp, "bar")

        ## Barra de reacción media.
        vbox:
            xpos 0.7
            text u"%s {font=DejaVuSans.ttf}♪{/font} %.01f ms" % (reaction, abs(accuracy)):
                color accuracy_color(accuracy, "text")
            bar:
                value AnimatedValue(old_value = 0.0, value = 100 - abs(accuracy), range = 100, delay = 0.1)
                left_bar accuracy_color(accuracy, "bar")


        ## Combo actual
        vbox:
            style_prefix "song_combo"
            label "COMBO"
            text str(rhythm.combo)

        ## Barra de progreso de la pista
        bar:
            style "song_progress"
            value AudioPositionValue(channel = 'music' , update_interval = 0.1)

    else:
        ## Esto transferirá el control al label "show_failed" en caso de tener
        ## 15 notas fallidas.
        python:
            ui.close()
            renpy.jump("show_failed")


    ## ¿Está activa la opción "Métricas de operación"?
    if persistent.operating_stats:
        frame:
            style_prefix "debugger"
            ypos 0.3

            has vbox
            label "Métricas de operación."
            text "- Beatmap: %s" % rhythm.fn
            text "- Offset: %ss" % rhythm.offset
            text "- Epoch: %.01fs" % rhythm.epoch
            text "- Umbral de reacción: %sms" % int(rhythm.threshold * 1000.0)
            text "- Progreso del mapa: %s/%s" % rhythm.map_progress
            text "- Acertados: %s" % rhythm.perfect
            text "- Fallidos: %s" % rhythm.miss
            text "- Combo: %s" % rhythm.combo


    ## Muestra el botón para abortar el Show mientras aún quedan notas para tocar.
    if rhythm.is_running():
        hbox:
            xalign 0.5 ypos 0.85
            style_prefix "sort_music"
            textbutton "Abortar Show" action [
            SetVariable("stage_aborted", True),
            Jump("show_failed")]

## Esto hace de que la screen del HUD se refresque constantemente, sin afectar el rendimiento de la
## screen del waterfall.
init python:
    config.per_frame_screens.append("playground_hud")


style stats_bar:
    left_bar Solid("#9F9")
    right_bar Solid("#777")
    xysize(300, 7)

style stats_text:
    color "#090"
    outlines [(2, "#FFF", 0, 0)]
    size 22

style stats_vbox:
    pos(0.05, 0.05)

style song_progress:
    xysize(800, 24)
    xalign 0.5 ypos 0.02

    left_bar Frame("coregame/ui/bar/ui_bar_progress_fill.png", 50, 12, 50, 12)
    right_bar Frame("coregame/ui/bar/ui_bar_progress_base.png", 50, 12, 50, 12)
    thumb "coregame/ui/bar/ui_bar_progress_thumb.png"
    thumb_offset 12


style song_combo_vbox:
    xsize 200
    spacing 0
    pos(0.75, 0.38)

style song_combo_label:
    xalign 0.5

style song_combo_label_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 22

style song_combo_text:
    color "#FFF"
    outlines [(3, "#000", 0, 0)]
    size 70
    xalign 0.5


style debugger_frame:
    background Frame(Transform(Solid("#242424"), alpha = 0.7), 24, 24, 24, 24)
    padding(30, 30, 30, 30)
    xminimum 200

style debugger_vbox:
    spacing 10

style debugger_label_text:
    color "#CF0"
    size 20

style debugger_text:
    color "#FFF"
    size 18



## -------------------------------------------------------------------------- ##
## Screen de reproducción 2DMV (o de la carátula si la canción no posee video)

screen playground_2dmv(source):
    zorder 101
    add source
    add Solid("#000") alpha persistent.custom_alpha


## -------------------------------------------------------------------------- ##
## Transición de partida finalizada

screen playground_finish(miss_notes, max_allowed):
    zorder 104
    modal True

    if miss_notes == 0:
        timer 1.8 action Play("sfx_01", audio.sfx_stage_full_combo)
        add "ui_tex_black"
        add "fx_tex_confetti"

        text "Full Combo!" at show_clear_text(2.3) size 70

        add "ui_tex_white" at full_combo_line_effect(xymap = [(-0.3, 1.3), 0.42], delta = 2.0)
        add "ui_tex_white" at full_combo_line_effect(xymap = [(-0.3, 1.3), 0.58], delta = 2.15)

    elif miss_notes < max_allowed:
        timer 1.0 action Play("sfx_01", audio.sfx_stage_cleared)
        add "ui_tex_black"
        text "Show Clear!" at show_clear_text(1.0) size 70

    else:
        timer 0.001 action Play("sfx_01", audio.sfx_stage_failed)
        add "ui_coregame_bg_failed"
        text "Show Failed!" at show_clear_text(0.0) size 70


## -------------------------------------------------------------------------- ##
## Resultados de la partida

screen show_results(song_selected, party):
    zorder 104
    style_prefix "show_results"

    on "show" action Play("sfx_01", audio.sfx_results_intro)

    default delta_header = 1.8
    default delta_cover = 1.5
    default delta_stats = 2.3

    default accuracy_pct = 100.0 - abs(rhythm.accuracy_rate()[0])

    ## BG
    add Fixed(Transform(im.Blur(song_selected["cover"], 2.0), zoom = 2.5), Transform(Solid("#000"), alpha = 0.5)) at alpha_com(1.0, 2.0)

    ## Resultados (Header)
    text "RESULTADOS"  size 60 at crossline_text(xran = (-0.3, 1.3), y = 0.45, offset = 0.2, delta = 0.6)
    text "FINALES" size 60 at crossline_text(xran = (1.3, -0.3), y = 0.55, offset = 0.2, delta = 0.6)

    ## Metadata de pista musical
    vbox at place_atl((1.1, 0.07), (0.07, 0.07), delta = delta_header):
        label song_selected["song_title"]
        text song_selected["song_artists"]
        null height 15
        text "BPM: %s | Full Combo: %s notas" % (song_selected["bpm"], song_selected["map_length"])

    add song_selected["cover"] at place_atl((-0.3, 0.3), (0.07, 0.3), delta = delta_cover) zoom 0.65

    ## Cuadro de resultados de la partida
    frame at place_atl((1.1, 0.26), (0.4, 0.26), delta = delta_stats):
        has vbox spacing 20

        frame:
            style "msg_success"
            text "RESULTADOS DE LA PARTIDA" style "update_label_text" xalign 0.5

        hbox:
            style_prefix "combo_results"
            vbox:
                xsize 250
                text "COMBO FINAL" xalign 0.5
                label str(party.combo) xalign 0.5

            vbox:
                text u"\u2022 Perfecto       : [party.perfect]" italic True
                text u"\u2022 BRUH            : [party.miss]" italic True ## XD

        vbox:
            style_prefix "perfbar"
            text "PRECISIÓN MEDIA: %.02f%%" % (accuracy_pct) xalign 0.5

            bar:
                value AnimatedValue(old_value = 0.0, value = 100 - abs(rhythm.accuracy_rate()[0]), range = 100, delay = 4.0)

            null height 20

            text u"\u2022 Tiempo de reacción promedio: %s ms." % (abs(rhythm.accuracy_rate()[0]))
            text u"\u2022 Tendencia de reacción: %s" % rhythm.accuracy_rate()[1]


    hbox at place_atl((0.5, 1.1), (0.5, 0.85), (0.5, 0.0), delta = delta_stats):
        style_prefix "sort_music"
        textbutton "Regresar a la lista" action Jump("song_selection_menu")


style show_results_frame:
    background Frame(Solid("#242424"), 24, 24, 24, 24)
    padding(30, 30, 30, 30)
    xminimum 600

style show_results_hbox:
    spacing 40

style show_results_label_text:
    size 38
    color "#CF0"
    outlines [(2, "#000", 1, 1)]
style show_results_text is song_btn_text:
    outlines [(2, "#000", 1, 1)]


## perfbar
style perfbar_bar:
    left_bar Solid("#CF0")
    right_bar Solid("#777")
    xysize(550, 7)
    yalign 0.5

style perfbar_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 19

style perfbar_hbox:
    spacing 20


## combo_results
style combo_results_label_text:
    color "#FFF"
    outlines [(3, "#000", 0, 0)]
    size 85

style combo_results_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 19

style combo_results_hbox:
    spacing 40

style combo_results_vbox:
    yalign 0.5
