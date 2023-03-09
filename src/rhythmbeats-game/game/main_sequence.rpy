## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: Flujo principal.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

## -------------------------------------------------------------------------- ##
## Secuencia de vefiricación de recursos y actualizaciones

label splashscreen:

    play music audio.bgm_0001 fadeout 1.0 fadein 1.0
    call screen main_advice with dissolve
    show bg_main
    call screen startscreen with dissolve

    jump check_updates

    label check_updates:
        $ update = UpdateManager(ext = ".bruh", skip = config.developer)
        $ update.index_url = "https://raw.githubusercontent.com/CharlieFuu69/RenPy_RhythmBeats/main/src/index.json"

        show tex_black with dissolve
        call screen update(inst = update)

        return

label download_sequence:
    $ update.start_batch_download()

    call screen download_complete

    $ renpy.quit(save=False, relaunch=renpy.windows or renpy.linux)


## -------------------------------------------------------------------------- ##
## Evasión del Menú Principal

label main_menu:
    $ del update
    return


## -------------------------------------------------------------------------- ##
## Secuencia de vefiricación de recursos y actualizaciones

label start:
    $ quick_menu = False
    scene bg_main
    show tex_black

    if renpy.has_label("song_selection_menu"):
        stop music fadeout 1.0
        $ renpy.pause(1.0, hard = True)
        jump song_selection_menu
    else:
        $ logging.critical("Error de flujo (song_selection_menu): Label inexistente. Cerrando el juego.")
        $ renpy.quit(relaunch = False, save = False)
