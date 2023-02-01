## CharlieFuu69
## Ren'Py RhythmBeats! Demo

## Script: Flujo principal.

################################################################################

## -------------------------------------------------------------------------- ##
## Secuencia de vefiricación de recursos y actualizaciones

label splashscreen:
    call screen main_advice with dissolve
    show bg_main
    play music audio.bgm_0001 fadeout 1.0 fadein 1.0
    call screen startscreen with dissolve

    jump check_updates

    label check_updates:
        if not config.developer:
            $ update = UpdateManager()
            call screen update(inst = update)

        return

label download_sequence:
    $ update.start_batch_download()
    $ renpy.pause(2.0, hard = True)
    $ renpy.utter_restart()

## -------------------------------------------------------------------------- ##
## Evasión del Menú Principal

label main_menu:
    if not config.developer:
        $ del update
    return


## -------------------------------------------------------------------------- ##
## Secuencia de vefiricación de recursos y actualizaciones

label start:
    $ quick_menu = False
    show bg_main

    if renpy.has_label("song_selection_menu"):
        stop music fadeout 1.0
        $ renpy.pause(1.0, hard = True)
        jump song_selection_menu
    else:
        $ logging.critical("Error de flujo (song_selection_menu): Label inexistente. Cerrando el juego.")
        $ renpy.quit(relaunch = False, save = False)
