init python:
    import logging
    import os

    logpath = config.basedir + "/rhythmbeats.log"

    logging.basicConfig(
                filename=logpath,
                format="[%(asctime)s] %(levelname)s: %(message)s",
                level=logging.DEBUG)

    logging.info("-----------<[Sesión de juego iniciada]>-----------")

    renpy.music.register_channel("ui_01", mixer = "sfx", loop = False)
    renpy.music.register_channel("notify_01", mixer = "sfx", loop = False)
    renpy.music.register_channel("sfx_01", mixer = "voice", loop = False)


init:
    ## ---------------------------------------------------------------------- ##
    ## Audio UI
    define audio.ui_sound_btn01 = "audio/main/ui_sound_button_01.ogg"
    define audio.ui_sound_btn02 = "audio/main/ui_sound_button_02.ogg"
    define audio.ui_sound_btn03 = "audio/main/ui_sound_button_03.ogg"
    define audio.ui_sound_notify = "audio/main/ui_sound_notify.ogg"
    define audio.ui_sound_error = "audio/main/ui_sound_error.ogg"

    define audio.bgm_0001 = "audio/main/bgm_0001.ogg"

    ## ---------------------------------------------------------------------- ##
    ## Imágenes
    image bg_main = Fixed("gui/bg_main.jpg", Transform(Solid("#000"), alpha = 0.4))
    image ui_icon_logo = "gui/window_icon.png"
    image ui_icon_headphones = Transform("gui/ui_icon_headphones.png", zoom = 0.15)


## -------------------------------------------------------------------------- ##
## ATL

transform headphone_blink:
    xalign 0.5

    block:
        alpha 0.0
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        repeat
