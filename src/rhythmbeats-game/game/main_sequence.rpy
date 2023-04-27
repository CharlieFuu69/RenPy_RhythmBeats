## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: Flujo principal.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

init python:
    renpy.load_module("radc-alpha2/radc_module")


## -------------------------------------------------------------------------- ##
## Secuencia de vefiricación de recursos y actualizaciones

label splashscreen:

    hide bg_main
    stop music

    if not persistent.language_choice:
        call screen lang_first_run
        $ rbs_alert(__("Idioma configurado correctamente."), icon="ui_icon_success")

    play music startscreen_queue fadeout 1.0 fadein 1.0 loop

    call screen main_advice with dissolve
    show bg_main
    call screen startscreen with dissolve

    jump check_updates


    label check_updates:
        $ update = UpdateManager(index_url="https://raw.githubusercontent.com/CharlieFuu69/RenPy_RhythmBeats/main/src/index.json",
                                package_ext=".bruh",
                                skip_process=config.developer)
                                #skip_process=False)

        show tex_black with dissolve
        call screen update(inst=update)

        return


label download_sequence:
    #$ update.start_batch_download("download")

    call screen download

    call screen download_complete

    $ renpy.quit(save=False, relaunch=renpy.windows or renpy.linux)


## -------------------------------------------------------------------------- ##
## Evasión del Menú Principal

label main_menu:
    return


## -------------------------------------------------------------------------- ##
## Secuencia de vefiricación de recursos y actualizaciones

label start:
    $ quick_menu = False

    scene bg_main
    show tex_black with dissolve

    if renpy.has_label("song_selection_menu"):
        jump game_post_loading

    else:
        $ logging.critical("Missing label: game_post_loading. Closing the game")
        $ renpy.quit(relaunch = False, save = False)
