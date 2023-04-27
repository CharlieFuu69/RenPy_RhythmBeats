## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Ren'Py) configuración del proyecto y definiciones.

## © 2023 CharlieFuu69 - GNU GPL v3.0

#############################################################

## Metadatos y Compilación
define config.name = "Ren'Py RhythmBeats! Game"
define config.version = "v1.05.0b"
define game_license = "© 2023 CharlieFuu69 - GNU GPL v3.0"
define gui.show_name = False

define build.name = "RhythmBeats"
define build.directory_name = build.name
define config.save_directory = config.savedir

define config.window_icon = "gui/window_icon.png"

## -------------------------------------------------------------------------- ##
## Configuraciones por defecto

## Audio
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.default_music_volume = 0.65 if renpy.android else 0.3
define config.default_sfx_volume = 0.9 if renpy.android else 0.4
define config.default_voice_volume = 0.65 if renpy.android else 0.3
define config.play_channel = "ui_01"
define config.emphasize_audio_channels = []
define config.main_menu_music = "audio/main/bgm_0001.ogg"
define config.sound_sample_rate = 41000

## Comportamiento de UI
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 0
default preferences.afm_time = 15

## Gráficos
default preferences.gl_powersave = False
default preferences.gl_framerate = 60
default preferences.fullscreen = True
define config.image_cache_size = 800

default persistent.custom_offset = 0
default persistent.custom_alpha = 0.0

## Comportamiento del juego
define config.autosave_on_quit = False
define config.autosave_frequency = None
define config.autoreload = False
define config.has_autosave = False
define config.auto_load = None
define config.save_on_mobile_background = False
define config.rollback_enabled = False
define config.skipping = False
define _game_menu_screen = None
define config.help = False
define config.end_splash_transition = dissolve
define config.has_quicksave = False
define config.auto_voice = None
define config.allow_skipping = False

## -------------------------------------------------------------------------- ##
## Ajustes de compilación

init python:
    CURRENT_SONG_COUNT = 27

    ## Archivos o rutas excluidas de la compilación.
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify("**.log", None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("game/**.rpy", None)
    build.classify("game/**.rpym", None)
    build.classify("other/**.**", None)
    build.classify("exe_compile/**.**", None)
    build.classify("Scripts php/**.**", None)
    build.classify("Screenshots/**.**", None)


    ## Main
    build.archive("Main", "all")
    build.classify("game/gui/**.png", "Main")
    build.classify("game/gui/**.jpg", "Main")
    build.classify("game/gui/**.ttf", "Main")
    build.classify("game/audio/main/**.ogg", "Main")
    build.classify("game/radc-alpha2/*.rpymc", "Main")
    build.classify("game/*.rpyc", "Main")
    build.classify("game/tl/**.rpymc", "Main")
    build.classify("game/tl/**.rpyc", "Main")

    ## Coregame
    build.archive("Coregame", "windows")
    build.classify("game/python-packages/discord_rpc/**.**", "Coregame")
    build.classify("game/audio/coregame/**.ogg", "Coregame")
    build.classify("game/coregame/*.rpyc", "Coregame")
    build.classify("game/coregame/*.rpymc", "Coregame")
    build.classify("game/coregame/**.json", "Coregame")
    build.classify("game/coregame/**.png", "Coregame")
    build.classify("game/coregame/**.ttf", "Coregame")
    build.classify("game/ingame-translate/**.rpyc", "Coregame")

    ## Song packages
    for song_id in range(1, CURRENT_SONG_COUNT+1):
        build.archive("Song_%04d" % song_id, "windows")
        build.classify("game/MV/2dmv_%04d.webm" % song_id, "Song_%04d" % song_id)
        build.classify("game/audio/bgm_%04d.ogg" % song_id, "Song_%04d" % song_id)
        build.classify("game/beatmaps/bmp_%04d.beat" % song_id, "Song_%04d" % song_id)
        build.classify("game/covers/ui_cover_%04d.png" % song_id, "Song_%04d" % song_id)
