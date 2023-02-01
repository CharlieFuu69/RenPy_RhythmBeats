## CharlieFuu69
## Ren'Py RhythmBeats! Demo

## Script: (Coregame) Secuencia de juego.

################################################################################

## -------------------------------------------------------------------------- ##
## Secuencia del menú de pistas musicales.

label song_selection_menu:
    $ music_inst = MusicData(fn = "coregame/music_data.json")
    $ music_inst.load()
    $ stage_aborted = False
    $ data = None
    $ p = persistent ## Reduce el espacio horizontal usado por variables "persistent"

    if not p.song_selected:
        $ p.song_selected = music_inst.sort(p.category)[0]

    $ renpy.notify("Las canciones que muestren la insignia {image=ui_performance_alert} podrían tener problemas de rendimiento.")

    call screen song_select(music_inst) with dissolve

    $ renpy.pause(hard = True)


    ## ---------------------------------------------------------------------- ##
    ## Flujo de escenario en partida

    label game_playstage:

        ## Esto libera un poco de memoria antes de ejecutar una canción
        $ renpy.free_memory()

        ## Instancia de la clase RhythmPlayground para ejecutar una partida.
        python:
            rhythm = rbs.RhythmPlayground(
                        fn = data["beatmap"],
                        offset_map = data["map_offset"],
                        offset_game = p.custom_offset,
                        failsafe = p.failsafe)

            rhythm.load()

            rhythm.miss_sound = audio.sfx_note_miss

        stop music fadeout 1.0
        call screen song_start(data) with dissolve
        hide bg_main
        $ renpy.pause(0.5, hard = True)

        play music data["audio"] noloop
        show screen playground_hud(data["length"])
        show screen playground(mv_data = data["mv"]) with dissolve

        $ renpy.pause(hard = True)


    ## ---------------------------------------------------------------------- ##
    ## Flujo de partidas finalizadas

    ## Show completado
    label show_cleared:
        show screen playground_finish(miss_notes = rhythm.miss, max_allowed = 15)
        $ renpy.pause(6.0 if rhythm.miss == 0 else 4.0, hard = True)
        stop music fadeout 1.0
        jump show_results_sequence


    ## Show fallido
    label show_failed:
        stop music
        $ finish_playstage(["playground_hud", "playground"])
        show screen playground_finish(miss_notes = 15, max_allowed = 15)
        $ renpy.pause(3.0, hard = True)

        ## Si no fue una partida abortada, muestra los resultados de la partida
        if not stage_aborted:
            jump show_results_sequence

        hide screen playground
        hide screen playground_finish with dissolve

        $ del rhythm
        $ renpy.free_memory()

        jump song_selection_menu


    ## Secuencia de resultados de la partida
    label show_results_sequence:
        $ finish_playstage(["playground", "playground_hud"], dissolving = True)
        hide screen playground_finish with dissolve

        $ renpy.pause(1.0, hard = True)

        play music bgm_0047
        call screen show_results(data, rhythm)

        $ del rhythm
        $ renpy.free_memory()

        jump song_selection_menu
