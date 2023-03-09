## CharlieFuu69
## Ren'Py RhythmBeats! Game

## Script: (Coregame) Definiciones elementales del programa.

## © 2023 CharlieFuu69 - GNU GPL v3.0

################################################################################

init offset = -4

init:
    ## ---------------------------------------------------------------------- ##
    ## Variables/objetos utilizados posterior a entrar al juego

    default persistent.highscores = dict()
    default persistent.operating_stats = False
    default persistent.failsafe = False
    default persistent.discord_rpc = False
    default persistent.category = "all"
    default persistent.song_selected = None
    default rpc = None

    ## ---------------------------------------------------------------------- ##
    ## Definiciones de audio

    define audio.sfx_stage_failed = "coregame/sound/sfx_coregame_failed.ogg"
    define audio.sfx_stage_cleared = "coregame/sound/sfx_coregame_cleared.ogg"
    define audio.sfx_stage_full_combo = "coregame/sound/sfx_coregame_full_combo.ogg"
    define audio.sfx_note_miss = "coregame/sound/ui_coregame_note_miss.ogg"
    define audio.sfx_results_intro = "coregame/sound/sfx_results_intro.ogg"
    define audio.sfx_results_scoreframe = "coregame/sound/sfx_results_scoreframe.ogg"

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
    image 2dmv_0010 = Movie(play="<from 5.05>MV/2dmv_0010.webm", loop = False)
    image 2dmv_0011 = Movie(play="MV/2dmv_0011.webm", loop = False)
    image 2dmv_0013 = Movie(play="MV/2dmv_0013.webm", loop = False)
    image 2dmv_0014 = Movie(play="MV/2dmv_0014.webm", loop = False)
    image 2dmv_0015 = Movie(play="MV/2dmv_0015.webm", loop = False)
    image 2dmv_0017 = Movie(play="MV/2dmv_0017.webm", loop = False)
    image 2dmv_0018 = Movie(play="MV/2dmv_0018.webm", loop = False)
    image 2dmv_0020 = Movie(play="<from 6.0>MV/2dmv_0020.webm", loop = False)
    image 2dmv_0021 = Movie(play="<from 6.19>MV/2dmv_0021.webm", loop = False)
    image 2dmv_0022 = Movie(play="MV/2dmv_0022.webm", loop = False)

    ## ---------------------------------------------------------------------- ##
    ## Imágenes de UI

    image ui_tex_black:
        Solid("#000")
        alpha 0.0
        ease 1.0 alpha 0.45

    image ui_tex_white = Solid("#FFF")
    image ui_black_solid = Solid("#000")

    image ui_coregame_note_lane = "coregame/ui/ui_coregame_note_lane.png"
    image ui_coregame_note_tap = Transform("coregame/ui/ui_coregame_note_tap.png", zoom = 1.3)
    image ui_coregame_bg_failed = "coregame/ui/ui_coregame_bg_failed.png"

    image ui_performance_alert = Transform("coregame/ui/ui_icon_performance_alert.png", zoom = 0.5)
    image ui_icon_github = Transform("coregame/ui/ui_icon_github.png", zoom = 0.1)
    image ui_icon_discord = Transform("coregame/ui/icon/ui_icon_discord.png", zoom = 0.15)

    image ui_icon_rank_s = "coregame/ui/icon/ui_icon_rank_s.png"
    image ui_icon_rank_a = "coregame/ui/icon/ui_icon_rank_a.png"
    image ui_icon_rank_b = "coregame/ui/icon/ui_icon_rank_b.png"
    image ui_icon_rank_c = "coregame/ui/icon/ui_icon_rank_c.png"

    image ui_icon_playing:
        zoom 0.05
        "coregame/ui/icon/ui_playing_F01.png"
        pause 0.2
        ease 0.1 alpha 1.0
        "coregame/ui/icon/ui_playing_F02.png"
        pause 0.2
        ease 0.1 alpha 1.0
        "coregame/ui/icon/ui_playing_F03.png"
        pause 0.2
        ease 0.1 alpha 1.0
        "coregame/ui/icon/ui_playing_F04.png"
        pause 0.2
        ease 0.1 alpha 0.0
        pause 0.2
        repeat

    image ui_overlay_results = Frame("coregame/ui/ui_overlay_results.png", 200, 0, 300, 0)

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
