## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: Definiciones principales del juego.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

default persistent.language_choice = False

init -5 python:
    import logging
    import os
    import sys

    PC_ENV = any((renpy.windows, renpy.linux))
    BASEPATH = config.basedir if PC_ENV else os.environ["ANDROID_PUBLIC"]

    logging.basicConfig(
                filename=os.path.join(BASEPATH, "rhythmbeats.log"),
                format="[%(asctime)s] %(levelname)s: %(message)s",
                level=logging.DEBUG,
                filemode = "w")

    if os.path.exists(os.path.join(BASEPATH, "game", "Multilanguage.bruh")):
        os.remove(os.path.join(BASEPATH, "game", "Multilanguage.bruh"))


    def chunkdata(data, chunk_qty):
        data = tuple(data)
        return [data[i:i + chunk_qty] for i in xrange(0, len(data), chunk_qty)]


    def logger(func, content):
        func(content)
        print(content)


    class Alert(Action):

        def __init__(self, content, status=0, icon=None):
            self.content = content
            self.status = status
            self.icon = icon

        def __call__(self):
            renpy.hide_screen("custom_notify")
            renpy.show_screen("custom_notify",
                            content=content,
                            status=status,
                            icon=icon)
            return None


    def rbs_alert(content, status=0, icon=None):
        renpy.hide_screen("custom_notify")
        renpy.show_screen("custom_notify",
                        content=content,
                        status=status,
                        icon=icon)
        renpy.restart_interaction()
        return None


    logger(logging.info, "-----------<[Game session started. Don't close the terminal.]>-----------")
    logger(logging.info, "Initializing audio channels...")

    renpy.music.register_channel("ui_01", mixer = "sfx", loop = False)
    renpy.music.register_channel("ui_02", mixer = "sfx", loop = False)
    renpy.music.register_channel("ui_03", mixer = "sfx", loop = False)
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

    define audio.startscreen_queue = ("audio/main/bgm_0001.ogg",
                                    "audio/main/bgm_0002.ogg",
                                    "audio/main/bgm_0003.ogg")

    ## ---------------------------------------------------------------------- ##
    ## Imágenes
    image bg_main = Fixed("gui/bg_main.jpg", Transform(Solid("#000"), alpha = 0.4))
    image ui_icon_logo = "gui/window_icon.png"
    image ui_icon_headphones = Transform("gui/ui_icon_headphones.png", zoom = 0.15)
    image ui_icon_warning = "gui/ui_icon_warning.png"
    image ui_icon_waiting = "gui/ui_icon_waiting.png"
    image ui_icon_success = "gui/ui_icon_success.png"

    image tex_black = Transform(Solid("#000"), alpha = 0.6)
    image tex_black_solid = Solid("#000")


## -------------------------------------------------------------------------- ##
## ATL

transform headphone_blink:
    xalign 0.5

    block:
        alpha 0.0
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        repeat


transform msgwindow_anim:
    subpixel True
    anchor(0.5, 0.5)

    on show, start:
        zoom 0.0
        ease 0.12 zoom 1.0

    on hide:
        zoom 1.0
        ease 0.12 zoom 0.0


transform notify_small_bg:
    subpixel True
    anchor(0.5, 0.5)

    xzoom 0.0
    easein_quint 0.2 xzoom 1.0
    pause 5.0
    alpha 1.0
    ease 0.5 alpha 0.0


transform notify_small_text(delta=0.0):
    alpha 0.0
    pause 0.001 + delta

    block:
        alpha 1.0
        pause 0.08
        alpha 0.0
        pause 0.08
        alpha 1.0

        repeat 1
