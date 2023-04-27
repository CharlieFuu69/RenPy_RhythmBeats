## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Coregame) Secuencia de juego.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

## -------------------------------------------------------------------------- ##
## Secuencia del menú de pistas musicales.

label quit:
    if "rpc" in globals():
        if rpc:
            $ rpc.stop()

    return

label game_post_loading:
    $ p = persistent ## Reduce el espacio horizontal usado por variables "persistent"

    ## Discord RPC
    $ rpc = DiscordRichPresence()

    if p.discord_rpc:
        $ rpc.set_status(details = __("En menú principal."))
        $ rpc.rpc_start()

    jump main_panel


label main_panel:
    show bg_main
    show tex_black

    if not renpy.music.get_playing(channel="music") in audio.startscreen_queue:
        play music startscreen_queue fadeout 0.8 fadein 0.8

    call screen gamemode_selector


label song_selection_menu:
    $ mdata = MusicData(relative_path = "coregame/metadata/music_metadata.json")
    $ record_scores(init_mode = mdata.get_song_count())
    $ stage_aborted = False
    $ data = None

    if not p.song_selected:
        $ p.song_selected = mdata.sort(p.category)[0]

    $ fix_metadata_diffs(mdata.sort("all"))

    $ rpc.set_status(details = __("Seleccionando pista musical..."))

    call screen song_select with dissolve

    $ renpy.pause(hard = True)


    ## ---------------------------------------------------------------------- ##
    ## Flujo de escenario en partida

    label game_playstage:

        scene tex_black_solid

        $ rpc.set_status(state = __("Artistas: %s") % data["song_artists"],
                        details = __("Jugando: \"%s\"") % data["song_title"],
                        image_text = __("Partida en curso..."))

        ## Esto libera un poco de memoria antes de ejecutar una canción
        $ renpy.free_memory()

        ## Instancia de la clase RhythmPlayground para ejecutar una partida.
        python:
            rhythm = RhythmPlayground(
                        fn = data["beatmap"],
                        displayable = Transform("ui_coregame_note_tap", zoom = 0.55),
                        song_file = data["audio"],
                        offset_map = data["map_offset"],
                        offset_game = p.custom_offset,
                        perfect_threshold = 70,
                        max_score = 25000,
                        failsafe = p.failsafe)

            rhythm.miss_sound = audio.sfx_note_miss

        stop music fadeout 1.0
        call screen song_start(data) with dissolve
        hide bg_main
        $ renpy.pause(0.5, hard = True)

        show screen playground_hud(data["length"], data["score_goal"])
        show screen playground(mv_data = data["mv"]) with dissolve

        $ renpy.pause(hard = True)


    ## ---------------------------------------------------------------------- ##
    ## Flujo de partidas finalizadas

    ## Show completado
    label show_cleared:
        show screen playground_finish(status=rhythm.is_full_combo())
        $ renpy.pause(6.0 if rhythm.miss == 0 else 4.0, hard = True)
        stop music fadeout 1.0
        jump show_results_sequence


    ## Show fallido
    label show_failed:
        stop music
        $ finish_playstage(["playground_hud", "playground"])
        show screen playground_finish(status="FAILED")
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
        $ get_record_flag = record_scores(id = data["id"], score = rhythm.stage_score)
        $ finish_playstage(["playground", "playground_hud"], dissolving = True)
        hide screen playground_hud
        hide screen playground_finish with dissolve

        $ rpc.set_status(state = __("Artistas: %s") % data["song_artists"],
                        details = __("Jugando: \"%s\"") % data["song_title"],
                        image_text = __("En pantalla de resultados..."))

        $ renpy.pause(1.0, hard = True)

        $ bgcover_image = Fixed(Transform(im.Blur(data["cover"], 2.0), zoom = 2.5), Transform(Solid("#000"), alpha = 0.5))

        show expression bgcover_image at alpha_com(1.0, 2.0) as coverimage

        play music bgm_0047
        call screen results_start
        call screen score_frame
        call screen show_results(data, rhythm)
        hide coverimage with dissolve

        $ del rhythm
        $ del get_record_flag
        $ renpy.free_memory()

        jump song_selection_menu
