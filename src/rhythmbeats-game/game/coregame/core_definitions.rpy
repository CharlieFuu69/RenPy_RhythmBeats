## CharlieFuu69
## Ren'Py RhythmBeats! Demo

## Script: (Coregame) Definiciones elementales del programa.

################################################################################

init offset = -4

init:
    default persistent.operating_stats = False
    default persistent.failsafe = False
    default persistent.category = "all"
    default persistent.song_selected = None

    ## ---------------------------------------------------------------------- ##
    ## Definiciones de audio

    define audio.sfx_stage_failed = "coregame/sound/sfx_coregame_failed.ogg"
    define audio.sfx_stage_cleared = "coregame/sound/sfx_coregame_cleared.ogg"
    define audio.sfx_stage_full_combo = "coregame/sound/sfx_coregame_full_combo.ogg"
    define audio.sfx_note_miss = "coregame/sound/ui_coregame_note_miss.ogg"
    define audio.sfx_results_intro = "coregame/sound/sfx_results_intro.ogg"

    define audio.ui_sound_radiobutton = "coregame/sound/ui_sound_radiobutton.ogg"

    define audio.bgm_0047 = "coregame/sound/bgm_0047.ogg"


    ## ---------------------------------------------------------------------- ##
    ## Capas de video (2DMV)

    image 2dmv_0001 = Movie(play="MV/2dmv_0001.webm", loop = False)
    image 2dmv_0002 = Movie(play="MV/2dmv_0002.webm", loop = False)
    image 2dmv_0003 = Movie(play="MV/2dmv_0003.webm", loop = False)
    image 2dmv_0005 = Movie(play="MV/2dmv_0005.webm", loop = False)
    image 2dmv_0006 = Movie(play="MV/2dmv_0006.webm", loop = False)
    image 2dmv_0007 = Movie(play="MV/2dmv_0007.webm", loop = False)
    image 2dmv_0008 = Movie(play="MV/2dmv_0008.webm", loop = False)
    image 2dmv_0010 = Movie(play="MV/2dmv_0010.webm", loop = False)
    image 2dmv_0011 = Movie(play="MV/2dmv_0011.webm", loop = False)
    image 2dmv_0013 = Movie(play="MV/2dmv_0013.webm", loop = False)
    image 2dmv_0014 = Movie(play="MV/2dmv_0014.webm", loop = False)
    image 2dmv_0015 = Movie(play="MV/2dmv_0015.webm", loop = False)
    image 2dmv_0017 = Movie(play="MV/2dmv_0017.webm", loop = False)

    ## ---------------------------------------------------------------------- ##
    ## Imágenes de UI

    image ui_tex_black:
        Solid("#000")
        alpha 0.0
        ease 1.0 alpha 0.45

    image ui_tex_white = Solid("#FFF")
    image ui_black_solid = Solid("#000")

    image ui_coregame_note_lane = "coregame/ui/ui_coregame_note_lane.png"
    image ui_coregame_note_tap = "coregame/ui/ui_coregame_note_tap.png"
    image ui_coregame_bg_failed = "coregame/ui/ui_coregame_bg_failed.png"

    image ui_performance_alert = Transform("coregame/ui/ui_icon_performance_alert.png", zoom = 0.5)
    image ui_icon_github = Transform("coregame/ui/ui_icon_github.png", zoom = 0.1)

    ## ---------------------------------------------------------------------- ##
    ## Texturas VFX

    image fx_endshow_orange_fps:
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (0, 0, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (32, 0, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (0, 32, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (32, 32, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (32, 32, 32, 32)), xzoom = -1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (0, 32, 32, 32)), xzoom = -1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (32, 0, 32, 32)), xzoom = -1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_orange.png", (0, 0, 32, 32)), xzoom = -1.0)
        pause 0.03
        repeat


    image fx_endshow_green_fps:
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (0, 0, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (32, 0, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (0, 32, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (32, 32, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (32, 32, 32, 32)), xzoom = -1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (0, 32, 32, 32)), xzoom = -1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (32, 0, 32, 32)), xzoom = -1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_green.png", (0, 0, 32, 32)), xzoom = -1.0)
        pause 0.05
        repeat


    image fx_endshow_yellow_fps:
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (0, 0, 32, 32)), xzoom = 1.0)
        pause 0.06
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (32, 0, 32, 32)), xzoom = 1.0)
        pause 0.06
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (0, 32, 32, 32)), xzoom = 1.0)
        pause 0.06
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (32, 32, 32, 32)), xzoom = 1.0)
        pause 0.06
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (32, 32, 32, 32)), xzoom = -1.0)
        pause 0.06
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (0, 32, 32, 32)), xzoom = -1.0)
        pause 0.06
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (32, 0, 32, 32)), xzoom = -1.0)
        pause 0.06
        Transform(im.Crop("coregame/textures/ui_tex_confetti_yellow.png", (0, 0, 32, 32)), xzoom = -1.0)
        pause 0.06
        repeat


    image fx_endshow_blue_fps:
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (0, 0, 32, 32)), xzoom = 1.0)
        pause 0.04
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (32, 0, 32, 32)), xzoom = 1.0)
        pause 0.04
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (0, 32, 32, 32)), xzoom = 1.0)
        pause 0.04
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (32, 32, 32, 32)), xzoom = 1.0)
        pause 0.04
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (32, 32, 32, 32)), xzoom = -1.0)
        pause 0.04
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (0, 32, 32, 32)), xzoom = -1.0)
        pause 0.04
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (32, 0, 32, 32)), xzoom = -1.0)
        pause 0.04
        Transform(im.Crop("coregame/textures/ui_tex_confetti_blue.png", (0, 0, 32, 32)), xzoom = -1.0)
        pause 0.04
        repeat


    image fx_endshow_red_fps:
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (0, 0, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (32, 0, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (0, 32, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (32, 32, 32, 32)), xzoom = 1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (32, 32, 32, 32)), xzoom = -1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (0, 32, 32, 32)), xzoom = -1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (32, 0, 32, 32)), xzoom = -1.0)
        pause 0.03
        Transform(im.Crop("coregame/textures/ui_tex_confetti_red.png", (0, 0, 32, 32)), xzoom = -1.0)
        pause 0.03
        repeat


    image fx_endshow_violet_fps:
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (0, 0, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (32, 0, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (0, 32, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (32, 32, 32, 32)), xzoom = 1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (32, 32, 32, 32)), xzoom = -1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (0, 32, 32, 32)), xzoom = -1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (32, 0, 32, 32)), xzoom = -1.0)
        pause 0.05
        Transform(im.Crop("coregame/textures/ui_tex_confetti_violet.png", (0, 0, 32, 32)), xzoom = -1.0)
        pause 0.05
        repeat


    image fx_tex_confetti:
        Fixed(
        SnowBlossom("fx_endshow_orange_fps", border = 50, yspeed = 150, start = 6.0, count = 7),
        SnowBlossom("fx_endshow_green_fps", border = 50, yspeed = 150, start = 4.0, count = 7),
        SnowBlossom("fx_endshow_yellow_fps", border = 50, yspeed = 150, start = 6.0, count = 7),
        SnowBlossom("fx_endshow_blue_fps", border = 50, yspeed = 150, start = 4.0, count = 7),
        SnowBlossom("fx_endshow_red_fps", border = 50, yspeed = 150, start = 6.0, count = 7),
        SnowBlossom("fx_endshow_violet_fps", border = 50, yspeed = 150, start = 6.0, count = 7))
        alpha 0.0
        pause 2.0
        ease 0.8 alpha 1.0
