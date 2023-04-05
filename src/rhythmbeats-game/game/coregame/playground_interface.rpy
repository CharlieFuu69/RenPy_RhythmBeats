## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Coregame) Interfaz de partidas.

## © 2023 CharlieFuu69 - GNU GPL v3.0

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

    ## Accionamiento del sistema rítmico (Detección + Visualización)
    add rhythm.map_mgr
    add rhythm.waterfall_mgr


## -------------------------------------------------------------------------- ##
## HUD del campo de juego (Actúa por separado ya que debe refrescarse con interacciones,
## y las interacciones decrementan los FPS)

screen playground_hud(song_length, score_goal):
    zorder 103
    style_prefix "stats"

    timer song_length + 1.0 action Jump("show_cleared")

    python:
        hp = 15 - rhythm.miss
        average_ms, reaction = rhythm.accuracy_rate()
        sc_color, sc_rank, sc_count, sc_icon = score_color(rhythm.stage_score, score_goal)


    ## ¿Hay menos de 15 notas fallidas? Si hay menos de 15, se puede seguir jugando.
    if rhythm.miss < 15:

        ## Barra de puntuación de la partida
        hbox:
            style_prefix "score_style"

            ## Barra de XP de la partida
            frame:
                background Transform(sc_icon, xsize=103, ysize=79)
                text sc_rank

            vbox:
                label u"{font=DejaVuSans.ttf}♪{/font} %s XP (+%s)" % (sc_count, rhythm.note_score)
                bar:
                    value AnimatedValue(old_value = 0.0,
                                        value = rhythm.stage_score,
                                        range = score_goal,
                                        delay = 0.1)
                    left_bar sc_color

            null width 430

            ## Barra de HP (se calcula restando 15 por la cantidad de notas perdidas.)
            vbox:
                style_prefix "stats"
                null height 10
                text "{font=DejaVuSans.ttf}❤{/font} [hp]/15" color hp_color(hp, "text")
                bar:
                    value AnimatedValue(old_value = 0.0, value = hp, range = 15, delay = 0.1)
                    left_bar hp_color(hp, "bar")


        ## Combo actual
        if rhythm.combo > 0:
            vbox:
                style_prefix "song_combo"
                label "COMBO"
                text str(rhythm.combo)

        ## Barra de progreso de la pista
        bar:
            style "song_progress"
            value AudioPositionValue(channel="music" , update_interval=0.1)

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
            label _("Métricas de operación.")
            text "- Beatmap: %s" % rhythm.fn
            text "- Offset: %s s" % rhythm.offset
            text "- Epoch: %.01f s" % round(rhythm.epoch, 2)
            text __("- Último tap: %.01f ms" % rhythm.last_tap)
            text __("- Progreso del mapa: %s/%s" % rhythm.map_progress)
            text __("- Acertados: %s" % rhythm.perfect)
            text __("- Fallidos: %s" % rhythm.miss)

    ## Muestra el botón para abortar el Show mientras aún quedan notas para tocar.
    if rhythm.is_running():
        hbox:
            xalign 0.5 ypos 0.85
            style_prefix "sort_music"
            textbutton _("Abortar Show") action [
            SetVariable("stage_aborted", True),
            Jump("show_failed")]

## Esto hace de que la screen del HUD se refresque constantemente, sin afectar el rendimiento de la
## screen del waterfall.
init python:
    config.per_frame_screens.append("playground_hud")

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
    style_prefix "finish_style"

    if miss_notes == 0:
        timer 1.8 action Play("sfx_01", audio.sfx_stage_full_combo)
        add "ui_tex_black"
        add "tex_show_cleared"

        add "ui_tex_flashlight" at full_combo_light_effect(2.5)
        text "Full Combo!" at show_clear_text(2.3)

        add "ui_tex_white" at full_combo_line_effect(xymap = [(-0.3, 1.3), 0.42], delta = 2.0)
        add "ui_tex_white" at full_combo_line_effect(xymap = [(-0.3, 1.3), 0.58], delta = 2.15)

    elif miss_notes < max_allowed:
        timer 1.0 action Play("sfx_01", audio.sfx_stage_cleared)
        add "ui_tex_black"
        text "Show Clear!" at show_clear_text(1.0)

    else:
        timer 0.001 action Play("sfx_01", audio.sfx_stage_failed)
        add "ui_coregame_bg_failed"
        text "Show Failed!" at show_clear_text(0.0)


## -------------------------------------------------------------------------- ##
## Resultados de la partida

screen results_start():
    style_prefix "show_results"
    on "show" action Play("sfx_01", audio.sfx_results_intro)
    timer 1.6 action [Hide("results_start"), Return()]

    text _("RESULTADOS FINALES") at crossline_text(xran = (-0.3, 1.3), y = 0.5, offset = 0.2, delta = 0.6):
        size 60


screen score_frame():
    on "show" action If(rhythm.stage_score > 0, Play("ui_02", audio.sfx_results_scoreframe), None)

    default score_target = data["score_goal"]
    default score_int = rhythm.stage_score
    default score_fmt = score_color(score_int, score_target)

    add "ui_overlay_results" at header_showup((0.5, 0.5), scale = 1.0, _offset = 0.01, px = 1150)

    hbox at results_score_anim(0.8):
        style_prefix "scorebar"

        frame:
            background Transform(score_fmt[3], xsize=215, ysize=165)
            label score_fmt[1]

        vbox:
            text _("PUNTUACIÓN OBTENIDA") size 40
            null height 30
            text "%s XP / %s XP" % (score_fmt[2], dotfmt(score_target))
            bar:
                value AnimatedValue(old_value = 0.0,
                                    value = score_int,
                                    range = score_target,
                                    delay = 3.1)
                left_bar Solid(score_fmt[0])


    hbox at place_atl((0.5, 1.1), (0.5, 0.85), (0.5, 0.0), delta = 2.5):
        style_prefix "sort_music"
        textbutton _("Siguiente") action [Hide("score_frame"), Return()]


screen show_results(song_selected, party):
    zorder 104
    style_prefix "show_results"

    default score_target = data["score_goal"]
    default score_int = rhythm.stage_score
    default score_fmt = score_color(score_int, score_target)
    default accuracy = rhythm.accuracy_rate()

    ## Metadata de pista musical
    vbox at place_atl((1.1, 0.07), (0.07, 0.07), delta = 0.8):
        label song_selected["song_title"]
        text song_selected["song_artists"]
        null height 15
        text "BPM: %s | Full Combo: %s notas" % (song_selected["bpm"], song_selected["map_length"])

    add song_selected["cover"] at place_atl((-0.3, 0.3), (0.07, 0.3), delta = 1.1) zoom 0.65

    ## Cuadro de resultados de la partida
    frame at place_atl((1.1, 0.5), (0.43, 0.5), (0.0, 0.5), delta = 1.4):
        has vbox xsize 550 first_spacing 10

        frame:
            style_prefix "msg_success"
            text _("RESULTADOS DE LA PARTIDA") style "update_label_text" xalign 0.5

        hbox:
            style_prefix "combo_results"
            vbox:
                xsize 250
                text _("COMBO FINAL") xalign 0.5
                label str(party.combo) xalign 0.5

            vbox:
                text _(u"\u2022 Perfecto : [party.perfect]") italic True
                text _(u"\u2022 BRUH : [party.miss]") italic True ## XD

        fixed:
            maximum(550, 48)
            add Solid("#FFF") ysize 3 yalign 0.5

            frame at new_record_signal(1.6):
                style_prefix "new_record"
                text _("¡NUEVO RECORD ALCANZADO!")


        hbox:
            style_prefix "score_results"

            frame:
                background Transform(score_fmt[3], xsize=103, ysize=79)
                label score_fmt[1]

            vbox:
                text _("PUNTUACIÓN OBTENIDA") color "#CF0"
                text "%s XP / %s XP" % (score_fmt[2], dotfmt(score_target))
                bar:
                    value AnimatedValue(old_value = 0.0,
                                        value = score_int,
                                        range = score_target,
                                        delay = 2.8)
                    left_bar Solid(score_fmt[0])

        null height 15

        vbox:
            text __(u"\u2022 {color=CF0}Tiempo de reacción promedio:{/color} %s ms.") % (accuracy[0]) size 19
            text __(u"\u2022 {color=CF0}Tendencia de reacción:{/color} %s") % (accuracy[1]) size 19


    hbox at place_atl((0.5, 1.1), (0.5, 0.85), (0.5, 0.0), delta = 1.6):
        style_prefix "sort_music"
        textbutton _("Regresar a la lista") action Jump("song_selection_menu")
